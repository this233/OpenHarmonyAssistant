# 用户问题
What is OpenHarmony's development language? 详细介绍！

# 核心回答
OpenHarmony的官方应用开发语言是ArkTS。ArkTS是基于TypeScript生态的扩展语言，保持了TS的基本风格，同时通过规范定义强化了开发期的静态检查和分析，提升了程序执行的稳定性和性能。ArkTS是OpenHarmony应用的默认开发语言，支持与TS/JavaScript高效互操作，并提供了增强的并发编程能力和基础类库。

# 详细内容

## 1. ArkTS：OpenHarmony的官方开发语言

ArkTS是OpenHarmony应用开发的官方高级语言，也是OpenHarmony应用的默认开发语言。ArkTS在TypeScript生态基础上做了进一步扩展，保持了TS的基本风格，同时通过规范定义强化开发期静态检查和分析，提升代码健壮性，并实现更好的程序执行稳定性和性能。

**核心特性：**
- **基于TypeScript生态**：ArkTS在TS生态基础上扩展，支持与TS/JavaScript高效互操作
- **强化静态检查**：通过规范定义强化开发期的静态检查和分析
- **性能优化**：提升程序执行稳定性和性能
- **扩展能力**：提供了增强的基础类库、容器类库和并发编程能力

ArkTS基础类库和容器类库增强了语言的基础功能，提供包括高精度浮点运算、二进制Buffer、XML生成解析转换和多种容器库等能力，协助开发者简化开发工作，提升开发效率。

**来源：**
- 文件: `https://gitee.com/openharmony/docs/raw/master/zh-cn/application-dev/arkts-utils/arkts-overview.md`
  定位: 1 ArkTS简介
- 文件: `https://gitee.com/openharmony/docs/raw/master/zh-cn/application-dev/quick-start/arkts-get-started.md`
  定位: 1 初识ArkTS语言

## 2. ArkTS的技术特点与优势

**主要技术特点：**

1. **强制使用静态类型**：静态类型是ArkTS最重要的特性之一。使用静态类型后，程序中变量的类型就是确定的，编译器可以验证代码的正确性，从而减少运行时的类型检查，有助于性能提升。

2. **禁止在运行时改变对象布局**：为实现最优性能，ArkTS禁止在程序执行期间更改对象布局。

3. **限制运算符语义**：为获得更好的性能并鼓励编写清晰的代码，ArkTS限制了部分运算符的语义。

4. **并发能力增强**：针对TS/JS并发能力支持有限的问题，ArkTS对并发编程API和能力进行了增强，提供了TaskPool和Worker两种并发API供开发者选择。

5. **Sendable概念**：ArkTS进一步提出了Sendable的概念来支持对象在并发实例间的引用传递，提升ArkTS对象在并发实例间的通信性能。

**编译与运行：**
方舟编译运行时（ArkCompiler）支持ArkTS、TS和JS的编译运行，目前主要分为ArkTS编译工具链和ArkTS运行时两部分。ArkTS编译工具链负责将高级语言编译为方舟字节码文件（*.abc），ArkTS运行时则负责在设备侧运行字节码文件，执行程序逻辑。

**来源：**
- 文件: `https://gitee.com/openharmony/docs/raw/master/zh-cn/application-dev/arkts-utils/arkts-overview.md`
  定位: 1 ArkTS简介
- 文件: `https://gitee.com/openharmony/docs/raw/master/zh-cn/application-dev/quick-start/arkts-get-started.md`
  定位: 1 初识ArkTS语言

## 3. ArkTS与TypeScript/JavaScript的兼容性

ArkTS兼容TS/JavaScript生态，开发者可以使用TS/JS进行开发或复用已有代码。OpenHarmony系统对TS/JS支持的详细情况见兼容TS/JS的约束。

**兼容性特点：**
- 支持ECMA2017及更高版本的语法进行TS/JS开发
- 支持与TS/JS高效互操作
- 允许在OpenHarmony ohpm模块中通过export导出ts/js方法，在其他模块中通过import引入使用

**应用环境限制：**
- 强制使用严格模式（use strict）
- 禁止使用`eval()`
- 禁止使用`with() {}`
- 禁止以字符串为代码创建函数
- 禁止循环依赖

这种兼容性设计使得现有TypeScript和JavaScript开发者能够平滑过渡到ArkTS开发，同时充分利用OpenHarmony平台的特性。

**来源：**
- 文件: `https://gitee.com/openharmony/docs/raw/master/zh-cn/application-dev/quick-start/arkts-get-started.md`
  定位: 1 初识ArkTS语言
- 文件: `https://gitee.com/openharmony/docs/raw/master/zh-cn/application-dev/quick-start/arkts-migration-background.md`
  定位: 1 ArkTS语法适配背景 > 1.5 方舟运行时兼容TS/JS

# 相关图片

## 图片 1
![这张图片展示了ArkTS在不同API版本中的特性和优势，体现了ArkTS作为OpenHarmony官方开发语言的技术演进路线](https://gitee.com/openharmony/docs/raw/master/zh-cn/application-dev/quick-start/figures/arkts.png)

**说明：** 这张图片展示了ArkTS在不同API版本中的特性和优势，体现了ArkTS作为OpenHarmony官方开发语言的技术演进路线

**来源文件：** `/root/code/docs/zh-cn/application-dev/quick-start/arkts-get-started.md`
**定位：** 1 初识ArkTS语言
