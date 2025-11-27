# OpeHarmonyAssistant

OpeHarmonyAssistant 是一个类似于 Gemini-3-pro 的高级智能助手，专注于为 OpenHarmony 生态系统生成**富交互式、视觉化**的用户界面。

与传统仅返回文本的 AI 助手不同，OpeHarmonyAssistant 的核心目标是直接构建**完整的、可交互的 HTML 应用程序**来解决用户的查询。

## 🌟 核心特性

*   **交互式 UI 生成 (Generative UI):** 将用户的自然语言请求转化为功能完备的 Web 应用（如动态时钟、交互式地图、数据仪表盘等）。
*   **实时数据集成:** 强制对实体和事实进行实时搜索验证，确保生成内容的准确性和时效性。
*   **多媒体融合:**
    *   **图片生成 (`/gen`):** 自动为抽象概念或插图生成 AI 图像。
    *   **图片检索 (`/image`):** 自动搜索并展示特定人物、地点或实物的真实照片。
*   **现代设计:** 默认集成 Tailwind CSS，确保生成的界面美观、响应式且符合现代设计规范。

## 💡 设计理念

本项目遵循以下核心设计原则（参考自 System Prompt）：

1.  **Build Interactive Apps First:** 即使是简单的问题（如“现在几点？”），也应返回一个动态的时钟应用，而非静态文本。
2.  **No Walls of Text:** 避免长篇大论的文字，尽可能使用视觉元素和交互组件来传达信息。
3.  **Fact Verification (Mandatory):** 所有涉及实体、数据或新闻的内容必须经过搜索验证，严禁幻觉（Hallucination）。
4.  **No Placeholders:** 拒绝使用 Lorem Ipsum 或占位符图片，所有内容必须是真实的或通过 AI 生成的。

## 🚀 使用示例

OpeHarmonyAssistant 能够处理各种复杂的生成任务：

| 用户请求 | 助手生成的应用 |
| :--- | :--- |
| "什么是OpenHarmony?" | 一个**交互式技术百科页**，包含可视化的分层技术架构图（内核/系统服务/框架/应用层）、支持折叠/展开的子系统详情、以及轻量/小型/标准系统的特性对比卡片。 |
| "现在几点了？" | 一个带有动态指针、支持多时区切换的**时钟应用**。 |
| "我要去新加坡旅游，住在洲际酒店，想要一条慢跑路线。" | 一个集成 Google Maps 的**交互式地图**，标注了酒店、景点并绘制了推荐的慢跑路径。 |
| "介绍一下巴拉克·奥巴马的家庭。" | 一个动态的**家谱树**或**时间轴应用**，包含家庭成员的真实照片和生平简介。 |
| "模拟一个蚁群。" | 一个基于 HTML5 Canvas 的 **2D 模拟器**，用户可以调整蚂蚁数量和食物源。 |
| "生成一个关于外星人交朋友的儿童绘本。" | 一个图文并茂的**数字故事书**，包含一致的角色设计和 AI 生成的插图。 |

## 🛠️ 技术细节

助手通过特定的 System Instructions (详见 [`reference.md`](./reference.md)) 运作，输出格式严格遵循以下标准：

*   **输出格式:** 纯 HTML 代码，包裹在 ` ```html ... ``` ` 标记中。
*   **样式框架:** Tailwind CSS (CDN 引入)。
*   **脚本能力:** 支持原生 JavaScript，用于实现逻辑、动画和数据处理。
*   **API 接口:**
    *   图片生成: `src="/gen?prompt=..."`
    *   图片搜索: `src="/image?query=..."`

## 📖 参考文献

[Generative UI Paper](https://generativeui.github.io/static/pdfs/paper.pdf)

### 2 Method

Our Generative UI implementation outputs a single fully-generated web page and a set of accompanying assets, such as images. The page is rendered as-is on the user’s browser. See Figure 2 for a high level overview of the system.

As depicted in Figure 2, we employ 3 main components:

1. A server exposes several endpoints enabling access to key tools, such as image generation and search. The results can be made accessible to the model (increasing quality) or sent directly to the user’s browser (increasing efficiency).
2. Carefully crafted system instructions. These in turn include: (1) the goal (2) planning and thinking guidelines, (3) examples, and (4) a large set of technical instructions including formatting guidelines, tool endpoints manual, and tips for avoiding common errors. These contribute to the quality of the generated results (see Appendix A.5 for an illustrative prompt from an early research prototype).
3. A set of post-processors. These lightweight components address a set of remaining common issues. Additional post processors deal with error reporting and page analysis. See Appendix A.6.

#### 2.1 Consistent Styling

If desired, our setup allows producing results using a specific style and increased visual consistency across generations. This is done via small changes to the system instructions. Specifically, we experimented with replacing the short “Style” section in our prompt with more detailed variants (which we call “Classic” and “Wizard Green”), specifying colors, fonts, etc. We observe that indeed the generated results follow these styles. Interestingly, the model automatically adapts all elements, including e.g. the generated images and icons to the desired styles. See Figures 3 and 4.


### A.5 The System Instructions

A key component of our Generative UI implementation is a carefully crafted system prompt. Here we include an illustrative example of such instructions from an early research prototype. This example includes around 3K words, in 5 categories:

1. Core philosophy
2. Examples
3. Planning instructions
4. Technical details and endpoint use (most of the system instructions).
5. Dynamically populated information, including the date and the user’s location (if shared).

...

### 中文版系统提示词

完整的中文版系统提示词可参考：[中文版系统提示词](./gemini/system_prompt_zh.md)

### English Version System Prompt

For the complete English version of the system prompt, please refer to: [English Version System Prompt](./gemini/system_prompt.md)


---
*本项目灵感来源于 Generative UI 研究及 OpenHarmony 交互体验的探索。*

