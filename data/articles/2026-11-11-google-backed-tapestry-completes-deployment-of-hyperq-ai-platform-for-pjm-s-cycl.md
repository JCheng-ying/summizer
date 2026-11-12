# Google-backed Tapestry completes deployment of HyperQ AI platform for PJM's Cycle 1 interconnection review
https://www.datacenterdynamics.com/en/news/google-backed-tapestry-completes-deployment-of-hyperq-ai-platform-for-pjms-cycle-1-interconnection-review/

这篇文章触及的是 AI 和能源之间一个很少被讨论、但非常具体的瓶颈：电网并网排队。大家常说 AI 的瓶颈是电力，但电力不足很多时候不是因为没人想建电厂，而是新电源申请卡在电网运营商的审查队列里一等就是好几年。如果 AI 能把这个审查流程加速，等于是在用 AI 解决 AI 自己的电力约束。

文章指出，Google 支持的能源软件公司 Tapestry 完成了 HyperQ AI 平台在 PJM Interconnection 第一轮 Cycle 1 窗口中的首次部署。Cycle 1 是 PJM 改革后的第一个申请窗口，用大批量、并行的方式处理新发电项目的并网申请。HyperQ 在不到一天的时间里审查了 220GW 拟建发电容量的场址控制文件，Tapestry 称人工完成同样工作通常需要两个月，快了约 60 倍；平台为 811 份申请生成了准备度报告，单份中位运行时间 6 分 15 秒，其中 202GW 的容量进入了第一阶段研究。所谓场址控制，就是开发商证明自己有权在某块土地上建设的法律文件。HyperQ 用多模态 AI 分析 PDF、地图和法律文件，每个判断都会链接到原文中的具体页面、条款或坐标，最终合规判断仍由 PJM 的工程师做出。PJM 的评价是，这为实现其 12 个月并网时间目标提供了"可重复的模式"。但 Tapestry 也说明，这些数字只覆盖初始的场址控制评估，不包括下游的技术和工程研究。下一步，Tapestry 计划把 HyperQ 扩展到三个方面：第一是技术数据校验，在集群研究开始前审计单线图、并网模型文件、潮流模型中的错误；第二是提交前界面，帮助开发商在进入队列前发现合规缺口；第三是统一模型管理，用一个同步、可交互的电网模型取代静态规划文件。Tapestry 是 Google X 的 "moonshot" 项目，目标是建立第一个统一的电网模型。

个人看法：这篇和之前的 [挪威暂停新数据中心并网申请](2026-11-09-norway-halts-grid-connection-applications-for-new-data-centers.md)、[欧洲 AI 雄心撞上电力瓶颈](2026-11-01-europe-s-ai-ambitions-are-hitting-a-power-bottleneck.md) 是同一条线索的另一面：那两篇讲的是电网接不进来，这篇讲的是怎么让电网接得更快。用"先找瓶颈"的方法拆，电力供给受限可以分成三段：第一段是发电资产本身（燃气轮机、光伏、储能的产能）；第二段是并网审批和电网研究；第三段是输电线路建设。Tapestry 解决的是第二段中最前面的那一小步，而且只是文书审查，真正耗时的技术研究还没有覆盖到。

所以受益的层次会是：第一层是 PJM 区域内已经在队列里的发电和储能开发商，审查提速意味着项目更早进入研究阶段；第二层是电网规划和仿真软件，如果 Tapestry 后续把潮流模型校验做成，传统电网软件厂商要么被整合、要么被替代；第三层是 Alphabet 自己，Google 既是 Tapestry 的支持者，也是最需要 PJM 区域电力的数据中心运营者之一。这利好能源板块，因为它针对的是能源供给链上一个具体卡点；对 AI 板块的意义在于展示了一个"人类审核 + AI 引用溯源"的受监管行业落地范例。但目前只覆盖了初始审查，值得关注的是 HyperQ 能否进入技术研究阶段，以及 PJM 能否真正把并网周期压到 12 个月。
