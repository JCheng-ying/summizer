# Google Cloud takes aim at the cost of keeping idle AI agents running on Kubernetes
https://siliconangle.com/2026/11/13/distributed-training-inference-google-s-agent-projects-kubeconna/

（说明：这是 theCUBE 在 KubeCon 上的访谈节目，原文披露该环节由 Google Cloud 赞助，受访者是 Google Cloud 的产品负责人；文中"成本降低 10 倍"等数字是 Google 自己的说法，未经独立验证。）

这篇文章背后的命题是：Agent 的成本问题不只在模型推理本身，还在"等待"。一个 Agent 大部分时间并不在计算，而是在等模型返回、等测试跑完、等人类审批，如果它的容器或虚拟机一直开着，客户就要为空等付钱。当 Agent 数量从几个变成成千上万，这部分闲置成本会成为 Agent 规模化部署的一个真实瓶颈，而解决它的是调度和运行时这一层软件，而不是更多 GPU。

文章指出，Google Cloud AI 基础设施产品管理总监 Allan Naim 把 Kubernetes 的发展分成几幕：第二幕是 Kubernetes 成为训练和推理的事实标准，现在进入第三幕，Agent 的负载形态和 Kubernetes 最初的设计假设非常不同。Naim 称 Agent 有 90% 到 95% 的时间处于闲置状态。为此 Google 开发了开源运行时 Agent Substrate，在 Kubernetes 上把每个 Agent 放在隔离环境里运行：Agent 被挂起时，运行时把它的内存和本地文件存成快照并释放算力给其他 Agent，工作恢复时再从快照在可用的沙箱里还原。Naim 称，与直接在专用虚拟机和容器上运行相比，他们看到成本降低了 10 倍。文章还提到 Google 向云原生计算基金会（CNCF）捐赠了三个项目，但没有逐一说明是哪三个。

第二个问题是安全。产品经理 Gari Singh 指出，Agent 会为了解决问题想尽各种绕路的办法，所以需要确保它没有改动底层安全设置、没有发起外部网络调用、没有打开不该打开的文件。Google 2018 年开源的 gVisor 运行在宿主机内核之上，可以拦截或审计 Agent 发出的每一个系统调用。第三是训练侧：Google 与 Anyscale 合作的 KubeRay 让 Anyscale 的 Ray 平台原生运行在 Kubernetes 上，平台团队可以把分布式训练和推理提供给多个研究组；OpenRL 则把同样的思路用到强化学习上，Naim 的说法是过去做强化学习需要一群博士研究员，现在希望让平台工程团队在自己的 Kubernetes 环境里跑强化学习，持续改进 Agent 负载。

技术上，Agent Substrate 做的事情可以类比成操作系统里的进程休眠和换出：进程不运行时把状态写到磁盘、把内存让给别人，需要时再换回来。区别在于这里的"进程"是一个带文件系统和工具环境的 Agent 沙箱，而且恢复不要求回到原来那台机器。gVisor 则是一层用户态内核，Agent 的系统调用先经过它，而不是直接落到宿主机内核，这样即使 Agent 做出意料之外的操作，影响范围也被限制在沙箱里。

个人看法：这篇和之前读过的几篇其实在讲同一个瓶颈的不同侧面。[AMD 发布 Epyc 6](2026-11-10-amd-introduces-epyc-6-processors-for-ai-agent-workloads.md) 那篇讲的是 Agent 的工具调用跑在 CPU 上，用"每瓦多少 Agent"来卖芯片；[Gemini 4 Hydrogen](2026-11-12-google-releases-gemini-4-hydrogen-a-lower-cost-model-said-to-outscore-argon.md) 讲的是用更便宜的模型和模型路由降低单位任务成本；[Meta 的 Muse Ember](2026-11-09-meta-introduces-muse-ember-to-power-cost-efficient-ai-agents.md) 也是围绕 Agent 成本。这篇则是从运行时层面切入：如果 Agent 九成时间都在等，那最直接的降本办法是不让它在等的时候占着资源。先找瓶颈：Agent 规模化的瓶颈是"每个 Agent 的总持有成本"，其中闲置占用和安全隔离是两块容易被忽略的成本。解决这一层的受益者大致可以分三层：第一层是云厂商自己，Google Cloud 把这些项目开源捐给 CNCF，本质上是在定义 Agent 运行时的事实标准，让 Agent 负载更自然地落在托管 Kubernetes（GKE）上，这和它在 TPU 和 Gemini 上的布局是同一个方向；第二层是 Kubernetes 生态里的编排、沙箱和可观测性软件，包括 Anyscale 这样的分布式计算平台，以及做容器安全和运行时审计的公司；第三层仍然是算力基础设施，表面上看 10 倍降本意味着同样的 Agent 用更少的机器，但更可能的结果和模型降价一样，是部署的 Agent 数量大幅增加，CPU 和内存（快照需要存储和高速恢复）的总需求不一定减少。所以这对 AI板块是偏利好的，利好的是 Agent 基础设施软件层和云平台，而不是某个模型。

需要保留的是，这是赞助访谈，10 倍降本是相对于"专用虚拟机一直开着"这个比较弱的基准得出的，实际效果取决于 Agent 的闲置比例和快照恢复的延迟，文章没有给出恢复要多久。值得跟踪的是 Agent Substrate 在 CNCF 里能否得到 AWS、微软等其他云厂商的采用，如果只有 Google 自己在用，它更多是 GKE 的产品功能，而不是行业标准。
