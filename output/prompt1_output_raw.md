```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpenHarmony 的核心目的</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'oh-blue': '#007AFF',
                        'oh-cyan': '#5AC8FA',
                        'oh-violet': '#AF52DE',
                        'oh-dark': '#0B0F19',
                        'oh-darker': '#050811'
                    }
                }
            }
        }
    </script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #0B0F19 0%, #050811 100%);
            color: #E2E8F0;
            min-height: 100vh;
            overflow-x: hidden;
        }
        .glass-card {
            background: rgba(30, 41, 59, 0.4);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .hero-bg {
            background: radial-gradient(circle at top right, rgba(92, 107, 192, 0.15) 0%, transparent 40%),
                        radial-gradient(circle at bottom left, rgba(33, 150, 243, 0.15) 0%, transparent 40%);
        }
        .glow-text {
            text-shadow: 0 0 10px rgba(92, 107, 192, 0.7);
        }
        .pulse {
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(92, 107, 192, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(92, 107, 192, 0); }
            100% { box-shadow: 0 0 0 0 rgba(92, 107, 192, 0); }
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2), 0 10px 10px -5px rgba(0, 0, 0, 0.1);
        }
        .terminal {
            background: rgba(15, 23, 42, 0.8);
            border-radius: 0.5rem;
            padding: 1.5rem;
            font-family: 'Fira Code', monospace;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .architecture-diagram {
            background: url('https://gitee.com/openharmony/docs/raw/master/zh-cn/figures/1.png') center/contain no-repeat;
            min-height: 400px;
        }
        .component-diagram {
            background: url('https://gitee.com/openharmony/docs/raw/master/zh-cn/design/figures/Component-Definition.png') center/contain no-repeat;
            min-height: 300px;
        }
        .tab-content {
            display: none;
        }
        .tab-content.active {
            display: block;
            animation: fadeIn 0.5s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="text-gray-200">
    <!-- Header -->
    <header class="glass-card border-b border-white/10 sticky top-0 z-50">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-2">
                <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-oh-blue to-oh-cyan flex items-center justify-center pulse">
                    <i class="ph-light ph-atom text-white text-2xl"></i>
                </div>
                <h1 class="text-2xl font-bold">OpenHarmony</h1>
            </div>
            <nav class="hidden md:flex space-x-6">
                <a href="#" class="hover:text-oh-cyan transition-colors">首页</a>
                <a href="#" class="hover:text-oh-cyan transition-colors">技术架构</a>
                <a href="#" class="hover:text-oh-cyan transition-colors">开发指南</a>
                <a href="#" class="hover:text-oh-cyan transition-colors">生态</a>
            </nav>
            <button class="md:hidden">
                <i class="ph-light ph-list text-2xl"></i>
            </button>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero-bg py-16 md:py-24">
        <div class="container mx-auto px-4 text-center">
            <h1 class="text-4xl md:text-6xl font-bold mb-6 glow-text">
                OpenHarmony 的核心目的
            </h1>
            <p class="text-xl md:text-2xl max-w-3xl mx-auto mb-10 text-gray-300">
                面向全场景、全连接、全智能时代，搭建智能终端设备操作系统的框架和平台，促进万物互联产业的繁荣发展。
            </p>
            <div class="flex flex-col sm:flex-row justify-center gap-4">
                <button class="bg-gradient-to-r from-oh-blue to-oh-cyan text-white px-8 py-3 rounded-lg font-semibold hover:opacity-90 transition-opacity">
                    开始探索
                </button>
                <button class="glass-card px-8 py-3 rounded-lg font-semibold border border-white/10 hover:border-oh-violet transition-colors">
                    查看文档
                </button>
            </div>
        </div>
    </section>

    <!-- Core Purpose -->
    <section class="py-16">
        <div class="container mx-auto px-4">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold mb-4">核心使命</h2>
                <div class="w-24 h-1 bg-gradient-to-r from-oh-blue to-oh-cyan mx-auto rounded-full"></div>
            </div>
            
            <div class="grid md:grid-cols-2 gap-12 items-center">
                <div>
                    <h3 class="text-2xl font-bold mb-6">构建万物互联的操作系统平台</h3>
                    <p class="text-gray-300 mb-6">
                        OpenHarmony 是由开放原子开源基金会孵化及运营的开源项目，其核心目的是面向全场景、全连接、全智能时代，搭建一个智能终端设备操作系统的框架和平台，促进万物互联产业的繁荣发展。
                    </p>
                    <div class="space-y-4">
                        <div class="flex items-start">
                            <i class="ph-fill ph-check-circle text-oh-cyan text-xl mt-1 mr-3"></i>
                            <p>采用组件化设计，支持从128KiB到xGiB RAM资源的广泛设备</p>
                        </div>
                        <div class="flex items-start">
                            <i class="ph-fill ph-check-circle text-oh-cyan text-xl mt-1 mr-3"></i>
                            <p>实现硬件资源的可大可小，在多种终端设备间按需弹性部署</p>
                        </div>
                        <div class="flex items-start">
                            <i class="ph-fill ph-check-circle text-oh-cyan text-xl mt-1 mr-3"></i>
                            <p>通过分布式架构和统一OS设计，解决硬件和产品碎片化问题</p>
                        </div>
                    </div>
                </div>
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <div class="terminal">
                        <div class="flex space-x-2 mb-4">
                            <div class="w-3 h-3 rounded-full bg-red-500"></div>
                            <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
                            <div class="w-3 h-3 rounded-full bg-green-500"></div>
                        </div>
                        <pre class="text-sm text-gray-200 overflow-x-auto">
<span class="text-oh-cyan">// OpenHarmony 核心理念</span>
<span class="text-oh-violet">class</span> <span class="text-white">OpenHarmony</span> {
  <span class="text-oh-blue">purpose</span>: <span class="text-green-400">"构建万物互联的操作系统平台"</span>,
  <span class="text-oh-blue">architecture</span>: <span class="text-green-400">"分布式"</span>,
  <span class="text-oh-blue">design</span>: <span class="text-green-400">"组件化"</span>,
  <span class="text-oh-blue">deployment</span>: <span class="text-green-400">"弹性"</span>,
  <span class="text-oh-blue">vision</span>: <span class="text-green-400">"一次开发，多端部署"</span>
}</pre>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Key Features -->
    <section class="py-16 bg-gradient-to-b from-oh-dark to-oh-darker">
        <div class="container mx-auto px-4">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold mb-4">核心技术特性</h2>
                <div class="w-24 h-1 bg-gradient-to-r from-oh-blue to-oh-cyan mx-auto rounded-full"></div>
            </div>
            
            <div class="grid md:grid-cols-3 gap-8">
                <div class="glass-card rounded-2xl p-8 border border-white/10 feature-card transition-all duration-300">
                    <div class="w-16 h-16 rounded-xl bg-gradient-to-br from-oh-blue to-oh-cyan flex items-center justify-center mb-6">
                        <i class="ph-light ph-arrows-split text-2xl text-white"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-4">硬件互助资源共享</h3>
                    <p class="text-gray-300">
                        通过分布式软总线、分布式数据管理、分布式任务调度和设备虚拟化等模块实现设备间无缝互联。
                    </p>
                </div>
                
                <div class="glass-card rounded-2xl p-8 border border-white/10 feature-card transition-all duration-300">
                    <div class="w-16 h-16 rounded-xl bg-gradient-to-br from-oh-cyan to-oh-violet flex items-center justify-center mb-6">
                        <i class="ph-light ph-code-simple text-2xl text-white"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-4">一次开发多端部署</h3>
                    <p class="text-gray-300">
                        提供用户程序框架、Ability框架和UI框架，保证应用在多终端运行时的一致性。
                    </p>
                </div>
                
                <div class="glass-card rounded-2xl p-8 border border-white/10 feature-card transition-all duration-300">
                    <div class="w-16 h-16 rounded-xl bg-gradient-to-br from-oh-violet to-oh-blue flex items-center justify-center mb-6">
                        <i class="ph-light ph-puzzle-piece text-2xl text-white"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-4">统一OS弹性部署</h3>
                    <p class="text-gray-300">
                        通过组件化和组件弹性化设计方法，实现硬件资源的可大可小，在多种终端设备间按需弹性部署。
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Architecture -->
    <section class="py-16">
        <div class="container mx-auto px-4">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold mb-4">技术架构</h2>
                <div class="w-24 h-1 bg-gradient-to-r from-oh-blue to-oh-cyan mx-auto rounded-full"></div>
            </div>
            
            <div class="glass-card rounded-2xl p-6 border border-white/10 mb-12">
                <div class="architecture-diagram rounded-xl mb-6"></div>
                <p class="text-center text-gray-300">
                    OpenHarmony采用分层架构设计，从下向上依次为内核层、系统服务层、框架层和应用层。
                </p>
                <div class="flex justify-center mt-4">
                    <a href="https://gitee.com/openharmony/docs/raw/master/zh-cn/OpenHarmony-Overview_zh.md" target="_blank" class="flex items-center text-oh-cyan hover:text-oh-blue transition-colors">
                        <i class="ph-light ph-link mr-2"></i>
                        查看原始文档 (定位: 1 OpenHarmony开源项目 > 1.2 技术架构)
                    </a>
                </div>
            </div>
            
            <div class="grid md:grid-cols-2 gap-8">
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <h3 class="text-2xl font-bold mb-4">部件化设计</h3>
                    <div class="component-diagram rounded-xl mb-4"></div>
                    <p class="text-gray-300 mb-4">
                        通过将系统能力抽象为部件，每个部件作为系统能力的基本单元，具有独立的文件和目录，在不同设备上可以实例化为对应的库或可执行文件。
                    </p>
                    <a href="https://gitee.com/openharmony/docs/raw/master/zh-cn/design/OpenHarmony部件设计和开发指南.md" target="_blank" class="flex items-center text-oh-cyan hover:text-oh-blue transition-colors">
                        <i class="ph-light ph-link mr-2"></i>
                        查看原始文档 (定位: 1 OpenHarmony部件设计和开发指南 > 1.1 基本概念 > 1.1.1 部件定义)
                    </a>
                </div>
                
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <h3 class="text-2xl font-bold mb-4">系统类型</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full text-sm">
                            <thead>
                                <tr class="border-b border-white/10">
                                    <th class="py-2 text-left">类型</th>
                                    <th class="py-2 text-left">最小内存</th>
                                    <th class="py-2 text-left">适用场景</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-white/10">
                                    <td class="py-2">轻量系统</td>
                                    <td class="py-2">128KiB</td>
                                    <td class="py-2">传感器、穿戴设备</td>
                                </tr>
                                <tr class="border-b border-white/10">
                                    <td class="py-2">小型系统</td>
                                    <td class="py-2">1MiB</td>
                                    <td class="py-2">摄像头、路由器</td>
                                </tr>
                                <tr>
                                    <td class="py-2">标准系统</td>
                                    <td class="py-2">128MiB</td>
                                    <td class="py-2">高端显示屏</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <p class="text-gray-300 mt-4">
                        通过定义三种基础系统类型来实现对不同硬件能力设备的广泛覆盖。
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Ecosystem Value -->
    <section class="py-16 bg-gradient-to-b from-oh-darker to-oh-dark">
        <div class="container mx-auto px-4">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold mb-4">产业价值与生态意义</h2>
                <div class="w-24 h-1 bg-gradient-to-r from-oh-blue to-oh-cyan mx-auto rounded-full"></div>
            </div>
            
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <div class="w-12 h-12 rounded-lg bg-oh-blue/20 flex items-center justify-center mb-4">
                        <i class="ph-light ph-puzzle-piece text-oh-blue text-xl"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-2">解决碎片化问题</h3>
                    <p class="text-gray-300">
                        通过统一的OS平台解决了当前物联网设备碎片化严重的问题，为设备厂商提供了标准化的开发基础。
                    </p>
                </div>
                
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <div class="w-12 h-12 rounded-lg bg-oh-cyan/20 flex items-center justify-center mb-4">
                        <i class="ph-light ph-rocket-launch text-oh-cyan text-xl"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-2">降低开发成本</h3>
                    <p class="text-gray-300">
                        降低了开发门槛和成本，通过组件化设计和弹性部署能力适应不同行业、不同场景的设备需求。
                    </p>
                </div>
                
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <div class="w-12 h-12 rounded-lg bg-oh-violet/20 flex items-center justify-center mb-4">
                        <i class="ph-light ph-users text-oh-violet text-xl"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-2">促进协作创新</h3>
                    <p class="text-gray-300">
                        开源特性促进了技术共享和协作创新，吸引了全球开发者的参与，形成了良性的技术发展循环。
                    </p>
                </div>
                
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <div class="w-12 h-12 rounded-lg bg-oh-blue/20 flex items-center justify-center mb-4">
                        <i class="ph-light ph-shield-check text-oh-blue text-xl"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-2">中立公正运营</h3>
                    <p class="text-gray-300">
                        由开放原子开源基金会运营确保了中立性和公正性，避免了单一厂商控制的风险。
                    </p>
                </div>
                
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <div class="w-12 h-12 rounded-lg bg-oh-cyan/20 flex items-center justify-center mb-4">
                        <i class="ph-light ph-network text-oh-cyan text-xl"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-2">分布式协同</h3>
                    <p class="text-gray-300">
                        分布式特性为未来智能设备间的协同工作提供了技术基础，为实现真正的万物互联奠定支撑。
                    </p>
                </div>
                
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <div class="w-12 h-12 rounded-lg bg-oh-violet/20 flex items-center justify-center mb-4">
                        <i class="ph-light ph-globe text-oh-violet text-xl"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-2">全场景支持</h3>
                    <p class="text-gray-300">
                        全面覆盖ARM、RISC-V、x86等各种CPU架构，实现从MCU到应用处理器的全场景支持。
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- References -->
    <section class="py-16">
        <div class="container mx-auto px-4">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold mb-4">参考资料</h2>
                <div class="w-24 h-1 bg-gradient-to-r from-oh-blue to-oh-cyan mx-auto rounded-full"></div>
            </div>
            
            <div class="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <h3 class="text-xl font-bold mb-4 flex items-center">
                        <i class="ph-light ph-book-open text-oh-cyan mr-2"></i>
                        OpenHarmony概述
                    </h3>
                    <p class="text-gray-300 mb-4">
                        详细介绍了OpenHarmony的基本定位、核心目标和技术架构。
                    </p>
                    <a href="https://gitee.com/openharmony/docs/raw/master/zh-cn/OpenHarmony-Overview_zh.md" target="_blank" class="text-oh-cyan hover:text-oh-blue transition-colors flex items-center">
                        <i class="ph-light ph-link mr-2"></i>
                        查看文档
                    </a>
                </div>
                
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <h3 class="text-xl font-bold mb-4 flex items-center">
                        <i class="ph-light ph-gear text-oh-cyan mr-2"></i>
                        部件设计和开发指南
                    </h3>
                    <p class="text-gray-300 mb-4">
                        解释了OpenHarmony部件化设计的核心概念和优势。
                    </p>
                    <a href="https://gitee.com/openharmony/docs/raw/master/zh-cn/design/OpenHarmony部件设计和开发指南.md" target="_blank" class="text-oh-cyan hover:text-oh-blue transition-colors flex items-center">
                        <i class="ph-light ph-link mr-2"></i>
                        查看文档
                    </a>
                </div>
                
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <h3 class="text-xl font-bold mb-4 flex items-center">
                        <i class="ph-light ph-device-mobile text-oh-cyan mr-2"></i>
                        设备开发指南
                    </h3>
                    <p class="text-gray-300 mb-4">
                        介绍了三种系统类型的技术规格和适用场景。
                    </p>
                    <a href="https://gitee.com/openharmony/docs/raw/master/zh-cn/device-dev/device-dev-guide.md" target="_blank" class="text-oh-cyan hover:text-oh-blue transition-colors flex items-center">
                        <i class="ph-light ph-link mr-2"></i>
                        查看文档
                    </a>
                </div>
                
                <div class="glass-card rounded-2xl p-6 border border-white/10">
                    <h3 class="text-xl font-bold mb-4 flex items-center">
                        <i class="ph-light ph-rocket text-oh-cyan mr-2"></i>
                        快速入门概述
                    </h3>
                    <p class="text-gray-300 mb-4">
                        详细说明了OpenHarmony三种基础系统类型的技术规格。
                    </p>
                    <a href="https://gitee.com/openharmony/docs/raw/master/zh-cn/device-dev/quick-start/quickstart-overview.md" target="_blank" class="text-oh-cyan hover:text-oh-blue transition-colors flex items-center">
                        <i class="ph-light ph-link mr-2"></i>
                        查看文档
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="glass-card border-t border-white/10 py-12">
        <div class="container mx-auto px-4">
            <div class="flex flex-col md:flex-row justify-between items-center">
                <div class="mb-6 md:mb-0">
                    <div class="flex items-center space-x-2">
                        <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-oh-blue to-oh-cyan flex items-center justify-center">
                            <i class="ph-light ph-atom text-white"></i>
                        </div>
                        <span class="text-xl font-bold">OpenHarmony</span>
                    </div>
                    <p class="text-gray-400 mt-2">构建万物互联的操作系统平台</p>
                </div>
                <div class="flex space-x-6">
                    <a href="#" class="text-gray-400 hover:text-white transition-colors">
                        <i class="ph-fill ph-github-logo text-2xl"></i>
                    </a>
                    <a href="#" class="text-gray-400 hover:text-white transition-colors">
                        <i class="ph-fill ph-globe text-2  xl"></i>
                    </a>
                    <a href="#" class="text-gray-400 hover:text-white transition-colors">
                        <i class="ph-fill ph-envelope text-2xl"></i>
                    </a>
                </div>
            </div>
            <div class="border-t border-white/10 mt-8 pt-8 text-center text-gray-500">
                <p>© 2025 OpenHarmony. 由开放原子开源基金会运营.</p>
            </div>
        </div>
    </footer>

    <script>
        // Simple tab functionality for demonstration
        document.addEventListener('DOMContentLoaded', function() {
            const tabs = document.querySelectorAll('.tab-button');
            tabs.forEach(tab => {
                tab.addEventListener('click', () => {
                    // Remove active class from all tabs and content
                    document.querySelectorAll('.tab-button').forEach(t => t.classList.remove('active'));
                    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
                    
                    // Add active class to clicked tab
                    tab.classList.add('active');
                    
                    // Show corresponding content
                    const target = tab.getAttribute('data-tab');
                    document.getElementById(target).classList.add('active');
                });
            });
        });
    </script>
</body>
</html>
```