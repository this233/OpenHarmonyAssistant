# 用户问题
What is OpenHarmony's architecture?

# 核心回答
OpenHarmony采用分层架构设计，从下到上依次为内核层、系统服务层、框架层和应用层。内核层采用多内核设计，支持Linux内核和LiteOS内核，通过内核抽象层（KAL）屏蔽内核差异，为上层提供统一的内核能力。系统服务层是OpenHarmony的核心能力集合，包含系统基本能力、基础软件服务、增强软件服务和硬件服务四个子系统集。框架层为应用开发提供多语言框架和API支持。应用层包括系统应用和第三方应用，基于FA/PA能力模型开发。整个架构支持'系统>子系统>组件'的逐级展开，可根据不同设备形态进行灵活裁剪，支持从128KiB到xGiB内存资源的设备部署，实现一次开发、多设备部署的目标。

## 关键要点
- 四层架构：内核层、系统服务层、框架层、应用层
- 多内核设计：支持Linux和LiteOS内核
- 组件化架构：支持按需裁剪
- 分布式能力：支持跨设备协同
- 多系统类型支持：轻量系统、小型系统、标准系统

# 详细内容

## 1. 整体架构概述

OpenHarmony整体采用分层架构设计，从下向上依次为内核层、系统服务层、框架层和应用层。系统功能按照'系统>子系统>组件'的层级结构逐级展开，这种设计使得在多设备部署场景下，可以根据实际需求裁剪某些非必要的组件。内核层位于最底层，负责提供基础的系统能力；系统服务层是OpenHarmony的核心能力集合；框架层为应用开发提供编程接口；应用层则包含各类应用程序。这种分层架构支持在128KiB到xGiB RAM资源的设备上运行系统组件，设备开发者可以基于目标硬件能力自由选择系统组件进行集成。架构设计充分考虑了不同设备类型的资源差异，从资源受限的嵌入式设备到功能丰富的智能设备都能得到良好支持。整个架构体现了模块化、组件化的设计理念，为开发者提供了灵活的系统定制能力。

**本节要点：**
- 四层架构设计
- 系统>子系统>组件层级结构
- 支持组件裁剪
- 适应不同资源设备

**来源：**
- 文件: `https://gitee.com/openharmony/docs/raw/master/zh-cn/OpenHarmony-Overview_zh.md`
  定位: 1 OpenHarmony开源项目 > 1.2 技术架构
  相关性: 详细描述了OpenHarmony的整体架构层次和各层功能

## 2. 内核层详细架构

内核层是OpenHarmony架构的基础层，采用多内核设计，支持Linux内核和LiteOS内核。内核抽象层（KAL，Kernel Abstract Layer）通过屏蔽多内核差异，对上层提供基础的内核能力，包括进程/线程管理、内存管理、文件系统、网络管理和外设管理等。内核子系统支持针对不同资源受限设备选用适合的OS内核，LiteOS主要包含LiteOS-M和LiteOS-A两类内核。LiteOS-M主要应用于轻量系统，面向MCU类处理器，支持MPU隔离；LiteOS-A主要应用于小型系统，面向设备一般是M级内存，支持MMU隔离。驱动子系统采用统一驱动框架HDF（Hardware Driver Foundation），这是系统硬件生态开放的基础，提供统一外设访问能力和驱动开发、管理框架。多内核架构通过KAL模块向上提供统一的标准接口，使得上层应用无需关心底层具体使用哪种内核。这种设计使得OpenHarmony能够适应从百K级别到百兆级容量的终端产品形态部署。

**本节要点：**
- 多内核设计：Linux和LiteOS
- 内核抽象层（KAL）统一接口
- 驱动框架HDF
- 支持不同资源等级设备

**来源：**
- 文件: `https://gitee.com/openharmony/docs/raw/master/zh-cn/OpenHarmony-Overview_zh.md`
  定位: 1 OpenHarmony开源项目 > 1.2 技术架构
  相关性: 详细说明内核层的多内核设计和驱动子系统
- 文件: `https://gitee.com/openharmony/docs/raw/master/zh-cn/device-dev/kernel/kernel-overview.md`
  定位: 1 内核概述 > 1.3 多内核架构和基本组成
  相关性: 补充说明多内核架构的实现机制

## 3. 系统服务层架构

系统服务层是OpenHarmony的核心能力集合，通过框架层对应用程序提供服务。该层包含四个主要的子系统集：系统基本能力子系统集为分布式应用在多设备上的运行、调度、迁移等操作提供了基础能力，由分布式软总线、分布式数据管理、分布式任务调度、公共基础库、多模输入、图形、安全、AI等子系统组成。基础软件服务子系统集提供公共的、通用的软件服务，由事件通知、电话、多媒体、DFX等子系统组成。增强软件服务子系统集提供针对不同设备的、差异化的能力增强型软件服务，包括智慧屏专有业务、穿戴专有业务、IoT专有业务等子系统。硬件服务子系统集提供硬件服务，由位置服务、用户IAM、穿戴专有硬件服务、IoT专有硬件服务等子系统组成。根据不同设备形态的部署环境，基础软件服务子系统集、增强软件服务子系统集、硬件服务子系统集内部可以按子系统粒度裁剪，每个子系统内部又可以按功能粒度裁剪。这种设计使得系统服务层能够灵活适应不同设备的需求，同时保持核心能力的完整性。

**本节要点：**
- 四个子系统集：基本能力、基础软件、增强软件、硬件服务
- 支持分布式应用
- 按需裁剪能力
- 核心能力集合

**来源：**
- 文件: `https://gitee.com/openharmony/docs/raw/master/zh-cn/OpenHarmony-Overview_zh.md`
  定位: 1 OpenHarmony开源项目 > 1.2 技术架构
  相关性: 详细描述系统服务层的组成和功能

## 4. 框架层和应用层

框架层为应用开发提供了C/C++/JS等多语言的用户程序框架和Ability框架，适用于JS语言的ArkUI框架，以及各种软硬件服务对外开放的多语言框架API。根据系统的组件化裁剪程度，设备支持的API也会有所不同。框架层起到了承上启下的作用，既为上层应用提供开发接口，又为下层系统服务提供调用通道。应用层包括系统应用和第三方非系统应用。应用由一个或多个FA（Feature Ability）或PA（Particle Ability）组成。其中，FA有UI界面，提供与用户交互的能力；而PA无UI界面，提供后台运行任务的能力以及统一的数据访问抽象。基于FA/PA开发的应用，能够实现特定的业务功能，支持跨设备调度与分发，为用户提供一致、高效的应用体验。这种应用架构设计使得应用能够在不同设备间无缝迁移和协同工作。

**本节要点：**
- 多语言框架支持
- Ability框架
- FA/PA应用模型
- 跨设备调度分发

**来源：**
- 文件: `https://gitee.com/openharmony/docs/raw/master/zh-cn/OpenHarmony-Overview_zh.md`
  定位: 1 OpenHarmony开源项目 > 1.2 技术架构
  相关性: 详细说明框架层和应用层的功能和特点

## 5. 系统类型与内核适配

OpenHarmony支持三种基础系统类型：轻量系统面向MCU类处理器，最小内存128KiB，支持轻量级网络协议和图形框架；小型系统面向应用处理器，最小内存1MiB，提供更高安全能力和标准图形框架；标准系统面向应用处理器，最小内存128MiB，提供增强交互能力和完整应用框架。内核与系统类型的适配关系为：轻量系统支持LiteOS-M，小型系统支持LiteOS-A和Linux，标准系统支持Linux。这种适配关系使得OpenHarmony能够覆盖从智能家居连接模组、传感器设备到高端冰箱显示屏等各种设备类型。系统采用组件化设计，支持根据设备能力进行灵活配置，设备开发者通过选择基础系统类型完成必选组件集配置后，便可实现其最小系统的开发。

**本节要点：**
- 三种系统类型：轻量、小型、标准
- 不同内核适配不同系统
- 最小内存要求不同
- 支持产品类型丰富

**来源：**
- 文件: `https://gitee.com/openharmony/docs/raw/master/zh-cn/readme/内核子系统.md`
  定位: 1 内核子系统 > 1.1 简介
  相关性: 说明不同系统类型与内核的适配关系

# 相关图片

## 图片 1
![OpenHarmony技术架构图，展示从内核层到应用层的四层架构设计，包括各层的具体组成和功能模块](https://gitee.com/openharmony/docs/raw/master/zh-cn/figures/1.png)

**说明：** OpenHarmony技术架构图，展示从内核层到应用层的四层架构设计，包括各层的具体组成和功能模块

**上下文：** 位于技术架构章节，用于直观展示OpenHarmony的整体架构层次

**与问题的相关性：** 直接展示了OpenHarmony的完整架构设计，是理解系统架构的关键图示

**尺寸：** 1783x866像素
**建议显示方式：** full-width

**来源文件：** `https://gitee.com/openharmony/docs/raw/master/zh-cn/OpenHarmony-Overview_zh.md`
**定位：** 1 OpenHarmony开源项目 > 1.2 技术架构

# 相关表格

## 表格 1: 内核与系统类型适配关系表

**描述：** 展示LiteOS和Linux内核在不同系统类型（轻量系统、小型系统、标准系统）中的支持情况

| 系统级别 | 轻量系统 | 小型系统 | 标准系统 |
| -------- | -------- | -------- | -------- |
| LiteOS | √ | √ | × |
| Linux | × | √ | √ |

**关键数据：**
- LiteOS支持轻量系统和小型系统
- Linux支持小型系统和标准系统
- 小型系统同时支持LiteOS和Linux

**来源文件：** `https://gitee.com/openharmony/docs/raw/master/zh-cn/readme/内核子系统.md`
**定位：** 1 内核子系统 > 1.1 简介

## 表格 2: OpenHarmony子系统简介表

**描述：** 列出OpenHarmony中的主要子系统及其功能和适用范围

| 子系统 | 简介 | 适用范围 |
| -------- | -------- | -------- |
| 内核 | 支持适用于嵌入式设备及资源受限设备，具有小体积、高性能、低功耗等特征的LiteOS内核；支持基于linux kernel演进的适用于标准系统的linux内核 | 小型系统<br>标准系统 |
| 分布式文件 | 提供本地同步JS文件接口 | 标准系统 |
| 图形 | 主要包括UI组件、布局、动画、字体、输入事件、窗口管理、渲染绘制等模块 | 所有系统 |
| 驱动 | OpenHarmony驱动子系统采用C面向对象编程模型构建，通过平台解耦、内核解耦，兼容不同内核 | 所有系统 |
| 电源管理服务 | 电源管理服务子系统提供如下功能：重启系统；管理休眠运行锁；系统电源状态管理和查询；充电和电池状态查询和上报；显示亮灭屏状态管理，包括显示亮度调节 | 标准系统 |
| 泛Sensor服务 | 泛Sensor中包含传感器和小器件，传感器用于侦测环境中所发生事件或变化，并将此消息发送至其他电子设备，小器件用于向外传递信号的设备，包括马达和LED灯，对开发者提供控制马达振动和LED灯开关的能力 | 小型系统 |

**关键数据：**
- 内核子系统支持多内核
- 图形子系统适用于所有系统
- 驱动子系统支持一次开发多系统部署
- 子系统按系统类型适配

**来源文件：** `https://gitee.com/openharmony/docs/raw/master/zh-cn/OpenHarmony-Overview_zh.md`
**定位：** 1 OpenHarmony开源项目 > 1.5 详细特征

# 相关代码

## 代码 1: 内核子系统目录结构

**功能说明：** 这段代码展示了OpenHarmony内核子系统的完整目录结构，包括Linux内核和LiteOS-A内核的组织方式。Linux内核部分包含多个版本（4.19/5.10/6.6）的支持，以及对应的补丁文件和配置目录。LiteOS-A内核部分则展示了从应用层、架构层、驱动层到文件系统、网络模块等完整的系统组件结构。这种目录组织体现了OpenHarmony的多内核架构和模块化设计理念。

**使用注意：** 该目录结构是理解OpenHarmony内核实现的基础，展示了系统的模块化组织和组件关系

**涉及API：** KAL接口, HDF驱动框架, POSIX接口

```shell
kernel/
├── linux
│   ├── common_modules                     # linux内核通用模块仓
│   ├── linux-4.19                         # OpenHarmony linux-4.19 Common kernel
│   ├── linux-5.10                         # OpenHarmony linux-5.10 Common kernel
│   ├── linux-6.6                          # OpenHarmony linux-6.6  Common kernel
│   ├── build
│   │   ├── BUILD.gn                       # 编译框架GN文件
│   │   ├── kernel.mk                      # 内核编译文件
│   │   └── ohos.build                     # 内核编译组件文件
│   ├── patches
│   │   ├── linux-4.19                     # linux-4.19 相关patch
│   │   │   ├── common_patch
│   │   │   │   └── hdf.patch              # linux-4.19 HDF patches
│   │   │   └── hispark_taurus_patch
│   │   │       └── hispark_taurus.patch   # linux-4.19 hispark_taurus SOC patches
│   │   ├── linux-5.10
│   │   │   ├── common_patch
│   │   │   │   └── hdf.patch              # linux-5.10 HDF patches
│   │   │   └── hispark_taurus_patch
│   │   │   │   └── hispark_taurus.patch   # linux-5.10 hispark_taurus SOC patches
│   │   │   └── rk3568_patch
│   │   │       ├── kernel.patch           # linux-5.10 rk3568 SOC patches
│   │   │       └── hdf.patch              # linux-5.10 rk3568 定制 HDF patches
│   │   └── linux-6.6
│   │       └── rk3568_patch
│   │           ├── kernel.patch           # linux-6.6  rk3568 SOC patches
│   │           └── hdf.patch              # linux-6.6  rk3568 定制 HDF patches
│   └── config
│       ├── linux-4.19
│       │   └── arch
│       │       └── arm
│       │          └── configs
│       │              ├── hispark_taurus_small_defconfig        # 厂商Hisilicon对应的开源开发板hispark_taurus小型系统的defconfig
│       │              ├── hispark_taurus_standard_defconfig     # 厂商Hisilicon对应的开源开发板hispark_taurus标准系统的defconfig
│       │              ├── small_common_defconfig                # 小型系统的内核的common defconfig
│       │              └── standard_common_defconfig             # 标准系统的内核的common defconfig
│       └── linux-5.10 or linux-6.6
│           ├── base_defconfig                                # 内核必选或安全红线模块基础配置
│           ├── type                                          # 形态配置目录
│           │   ├── small_defconfig                           # 小型系统常用配置文件
│           │   └── standard_defconfig                        # 标准系统常用配置文件
│           ├── form                                          # 版本配置目录
│           │   └── debug_defconfig                           # 调试版本配置文件
│           ├── rk3568                                        # 厂商平台配置目录
│           │   └── arch
│           │       └── arm64_defconfig                       # 芯片单板64位版本相关配置文件
│           └── product                                       # 相关产品类型配置目录
│               └── phone_defconfig                           # 手机类型产品相关配置文件
└── liteos_a               # liteos内核基线代码
├── apps               # 用户态的init和shell应用程序
├── arch               # 体系架构的目录，如arm等
│   └── arm            # arm架构代码
├── bsd                # freebsd相关的驱动和适配层模块代码引入，例如USB等
├── compat             # 内核接口兼容性目录
│   └── posix          # posix相关接口
├── drivers            # 内核驱动
│   └── char           # 字符设备
│       ├── mem        # 访问物理IO设备驱动
│       ├── quickstart # 系统快速启动接口目录
│       ├── random     # 随机数设备驱动
│       └── video      # framebuffer驱动框架
├── fs                 # 文件系统模块，主要来源于NuttX开源项目
│   ├── fat            # fat文件系统
│   ├── jffs2          # jffs2文件系统
│   ├── include        # 对外暴露头文件存放目录
│   ├── nfs            # nfs文件系统
│   ├── proc           # proc文件系统
│   ├── ramfs          # ramfs文件系统
│   └── vfs            # vfs层
├── kernel             # 进程、内存、IPC等模块
│   ├── base           # 基础内核，包括调度、内存等模块
│   ├── common         # 内核通用组件
│   ├── extended       # 扩展内核，包括动态加载、vdso、liteipc等模块
│   ├── include        # 对外暴露头文件存放目录
│   └── user           # 加载init进程
├── lib                # 内核的lib库
├── net                # 网络模块，主要来源于lwip开源项目
├── platform           # 支持不同的芯片平台代码，如hispark_taurus等
│   ├── hw             # 时钟与中断相关逻辑代码
│   ├── include        # 对外暴露头文件存放目录
│   └── uart           # 串口相关逻辑代码
├── platform           # 支持不同的芯片平台代码，如hispark_taurus等
├── security           # 安全特性相关的代码，包括进程权限管理和虚拟id映射管理
├── syscall            # 系统调用
└── tools              # 构建工具及相关配置和代码
```

**来源文件：** `https://gitee.com/openharmony/docs/raw/master/zh-cn/readme/内核子系统.md`
**定位：** 1 内核子系统 > 1.4 目录

# 相关概念

- 分布式软总线
- 内核抽象层（KAL）
- 硬件驱动框架（HDF）
- FA/PA能力模型
- 组件化架构
- 多内核设计

# 推荐阅读

- **OpenHarmony子系统详细文档**: 深入了解各个子系统的具体功能和实现细节
- **驱动开发指南**: 学习如何在OpenHarmony架构下进行驱动开发
- **分布式能力开发文档**: 掌握OpenHarmony的分布式特性和跨设备开发技术
