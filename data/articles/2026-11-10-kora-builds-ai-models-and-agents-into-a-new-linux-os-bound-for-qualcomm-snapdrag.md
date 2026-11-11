# Kora builds AI models and agents into a new Linux OS bound for Qualcomm Snapdragon PCs
https://siliconangle.com/2026/11/10/kora-builds-ai-models-and-agents-into-a-new-linux-os-bound-for-qualcomm-snapdragon-pcs/

（说明：用户规模和支出预测是 Kora 自己的估算；产品最早 2027 年才上市。）

这篇文章背后的命题是：如果 AI Agent 要真正接管电脑上的工作，它需要的可能不是一个更聪明的聊天窗口，而是一个从内核开始就围绕模型重写的操作系统。这是对 Windows 和 macOS 桌面格局的一次正面挑战。

文章指出，Kora Systems 发布了基于 Linux 的操作系统 Kora，把 AI 模型和 Agent 直接做进系统里，Qualcomm 花了近一年时间和它合作，把它带到骁龙 PC 上。Kora 的论点是：macOS 和 Windows 上的 AI 软件大多跑在浏览器标签页或应用沙盒里，看不到下面的系统，而因为这两个系统是封闭的，集成就止步于此。它的核心是一个叫 Cortex 的推理引擎，把 PC 的 CPU、GPU、NPU 以及网络上其他机器统一调度成一台计算机，模型默认在本地运行，重任务才调用前沿模型。界面上取消了传统的文件夹和应用布局，改为按任务组织的"神经工作区"，底层是神经文件系统，记忆和上下文保留在本机。和 Qualcomm 的合作已经让完整的 Linux 桌面跑在骁龙 X2 Elite 上，可以本地运行 260 亿参数的语言模型，Qualcomm 也在把 X2 Elite 支持推进到 Linux 主线内核。Kora 还做了转译技术，让部分 Windows x86-64 应用能在其中运行。首批机器会运行与沙特 AI 公司 HUMAIN 共同开发的企业系统 HUMAIN OS，2027 年上市，Kora 本身也在 2027 年晚些时候推出。团队来自做过 Cyanogen 和 Android 的人，此前做过游戏 Linux 系统 GameOS。

个人看法：这篇和之前写过的 [Underdog 展示 32MB 语音模型](2026-11-08-underdog-shows-off-a-32mb-speech-model-in-new-demo.md) 都在说同一件事：端侧 AI 不只是"把模型压小"，还需要系统层面的重新设计，让 CPU、GPU、NPU 协同。按瓶颈来看，edge AI 板块今天的瓶颈不是芯片算力（X2 Elite 已经能跑 260 亿参数模型），而是软件生态——NPU 算力在 Windows 上大部分时间是闲置的，没有应用能真正用起来。Kora 这类项目就是在解决这一层。受益层次上：第一层是端侧 SoC 厂商，Qualcomm 最直接，它需要证明 NPU 有用，这和之前 [Qualcomm 营收不及预期](2026-11-05-the-chips-are-down-qualcomm-falls-on-revenue-miss-weak-guidance-arm-and-globalfo.md) 的压力是相关的；第二层是 Arm 架构生态；第三层是本地运行的小模型和开源模型。但要清醒的是，挑战 Windows 的尝试历史上几乎都失败了，Kora 的首批出货又是通过沙特企业市场，消费端的接受度完全未知，现在只能观望，值得跟踪的是 2027 年 HUMAIN OS 机器的实际出货量和 x86 应用的兼容性体验。
