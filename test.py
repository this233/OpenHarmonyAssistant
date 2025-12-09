import asyncio
import os
import sys
import httpx
import json
import loguru

# 配置 Logger
logger = loguru.logger

# API 配置
API_URL = "https://api.modelarts-maas.com/v2/chat/completions"
API_KEY = "BQm_Gkd1EoTcHkJfVf31dTWfMIOsW3_mKIDfM5j-MvvwNM5jNl9XnLOjvNjEOuDiIWoKb-DIphdRWt2gOoNwBw"
MODEL_NAME = "qwen3-coder-480b-a35b-instruct"


async def get_system_prompt():
    """读取自定义的 OpenHarmony System Prompt"""
    prompt_path = os.path.join(os.path.dirname(__file__), 'ours/step2_system_prompt_zh.md')
    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read()


async def call_llm(messages):
    """调用 LLM API"""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    
    data = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 32000,
    }
    
    try:
        logger.info(f"Sending request to {MODEL_NAME}...")
        async with httpx.AsyncClient(verify=False, timeout=600.0) as client:
            response = await client.post(API_URL, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
    except Exception as e:
        logger.error(f"LLM call failed: {e}")
        return None


def extract_html(content):
    """从 Markdown 代码块中提取 HTML"""
    if "```html" in content:
        return content.split("```html")[1].split("```")[0].strip()
    return content


async def run_test(user_prompt_file: str, output_filename: str = None):
    """运行测试：读取用户 prompt 文件并调用 LLM"""
    
    # 读取用户 prompt 文件
    if not os.path.exists(user_prompt_file):
        logger.error(f"User prompt file not found: {user_prompt_file}")
        return
    
    with open(user_prompt_file, 'r', encoding='utf-8') as f:
        user_content = f.read()
    
    # 读取 system prompt
    system_prompt = await get_system_prompt()
    
    # 注入日期占位符
    import datetime
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    system_prompt = system_prompt.replace("%%%DATE%%%", current_date)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_content}
    ]

    logger.info(f"Testing with prompt file: {user_prompt_file}")
    response_content = await call_llm(messages)
    
    if response_content:
        html_content = extract_html(response_content)
        
        # 确保输出目录存在
        os.makedirs("output", exist_ok=True)
        
        # 生成输出文件名
        if output_filename is None:
            base_name = os.path.splitext(os.path.basename(user_prompt_file))[0]
            output_filename = f"{base_name}_output.html"
        
        output_path = os.path.join("output", output_filename)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        logger.info(f"Result saved to {output_path}")
        
        # 同时保存原始响应
        raw_output_path = os.path.join("output", output_filename.replace('.html', '_raw.md'))
        with open(raw_output_path, "w", encoding="utf-8") as f:
            f.write(response_content)
        logger.info(f"Raw response saved to {raw_output_path}")
    else:
        logger.error("No response received.")


async def main():
    if len(sys.argv) < 2:
        logger.error("Usage: python test.py <user_prompt_file> [output_filename]")
        logger.info("Example: python test.py prompts/dev_model.md openharmony_dev_model.html")
        return
    
    user_prompt_file = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) > 2 else None
    
    await run_test(user_prompt_file, output_filename)


if __name__ == "__main__":
    asyncio.run(main())
