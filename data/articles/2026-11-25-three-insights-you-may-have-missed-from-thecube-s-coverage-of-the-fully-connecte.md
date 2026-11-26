# Three insights you may have missed from theCUBE’s coverage of the Fully Connected event
https://siliconangle.com/2026/11/25/three-insights-missed-thecubes-coverage-fully-connected-event-fullyconnected/

先说明利益相关:原文末尾披露 theCUBE 是 CoreWeave Fully Connected 活动的付费媒体合作方,文中受访者也基本是 CoreWeave 及其合作伙伴,所以下面的产品指标和客户说法都应按"厂商口径、未经独立验证"来看。即便如此,这篇文章还是提出了一个值得认真对待的框架:AI 基础设施的经济性正在从"买到多少算力"转向"用这些算力生产智能的成本",推理而不是训练开始决定基础设施怎么设计。

文章指出,随着推理需求的增长超过训练,基础设施提供商和客户都需要在不同比增加运营成本的前提下提高有效计算时间,而持续学习的 agent 和物理 AI 应用让这个问题更复杂。theCUBE Research 的 Dave Vellante 认为 CoreWeave 正在从纯算力向外扩张,加上了网络、存储、可观测性软件层和安全,形成评估、观测和运行时之间的闭环。

文章的第一个观点是,AI 基础设施经济性取决于"有效产能"。英伟达的 Ian Buck 说数据中心天然的上限是电力,英伟达每一代 GPU 都确保每瓦 token 数提升 10 倍以上,Blackwell 最终实现了 30 倍;他还提到英伟达与 Vera Rubin 平台配合的 Groq 3 LPX 推理加速器在金融科技等需要实时处理的行业受到关注。内存管理是另一个维度,文章提到一个 50 万 token 的会话可能占用 GPU 显存的 5% 到 10%,Vast Data 联合创始人兼 CTO Alon Horev 认为把会话上下文保存在持久化存储里可以减少昂贵的重算,KV cache 可以通过网络迁移或者从 Vast 读取,把推理当作一个跨 GPU 显存、CPU 内存和 Vast 存储的分布式调度问题。LlamaIndex CEO Jerry Liu 则说他们每天为金融、法律和保险客户处理数百万页文档,推理约占 75% 的工作负载。

第二个观点是降低运营风险就是保护投资。Dell 开发了适配不同供电和散热配置的模块化机柜设计,和 CoreWeave 的合作包括把 CoreWeave 的 Racky 管理软件集成进工厂测试、改进液冷泄漏检测,Dell 的 Sarat Krishnan 说他们把最复杂的硬件故障诊断"左移"到制造环节,因为越到后期修复越贵。Cognition 的研究负责人 Silas Alberti 说,大规模训练里只要一个副本宕机整个训练就会中断,所以 99.99% 的可靠性是关键指标;CoreWeave 为此推出了连接推理、评估和模型改进的平台 Forge,内含追踪 agent 活动的 Agent Lens。IBM 则因为新硬件的供电和散热需求选择与 CoreWeave 合作,并扩展到身份管理和工作负载隔离(CoreWeave Sandboxes)的联合工程,IBM 的 Brian Belgodere 把安全形容为一个"从上到下的供应链问题"。

第三个观点是物理 AI 在检验基础设施投资。Aston Martin F1 每辆赛车每秒产生 100 万个数据点,在严格的预算和开发期限下运作;Walden Robotics 用大规模虚拟仿真为机器人的实际部署做准备,其联合创始人 Adrien Gaidon 称其机器人自 5 月起已经与人类一起跑完整生产班次,从事上下料、零件配套和子装配等工作,并强调机器必须能在部署中持续学习。

个人看法:这篇文章里有两个点和之前读过的内容能串起来。第一是 KV cache,之前那篇 [AI’s hidden energy tax: more than 80% of scale-up traffic is just memory moving around](2026-11-18-ai-s-hidden-energy-tax-more-than-80-of-scale-up-traffic-is-just-memory-moving-ar.md) 和 [d-Matrix bets stacked DRAM can solve inference’s memory bandwidth problem](2026-11-19-d-matrix-bets-stacked-dram-can-solve-inference-s-memory-bandwidth-problem.md) 讲的都是推理的瓶颈正在从算力转向内存,而 Vast Data 的思路是第三条路——不去扩显存,而是用存储层接住被挤出来的上下文,这在 [内存涨价 45%](2026-11-23-ai-server-oems-hiking-prices-by-45-as-memory-shortage-bites-report.md) 的背景下尤其有意义。第二是 CoreWeave 往软件层扩张,结合 [CoreWeave 转向客户预付款和更短合同](2026-11-11-coreweave-turns-to-customer-prepayments-shorter-contracts-to-fund-ai-growth.md) 那篇,我觉得这是 neocloud 在融资变贵之后提高客户粘性的一种方式:纯卖 GPU 时长没有护城河,加上可观测性、评估和沙箱之后客户迁移成本才会上来。

所以用"先找瓶颈"的思路看,这篇文章指向的瓶颈是推理时的显存和可靠性,受益的层次会是:第一层仍然是英伟达,每瓦 token 数是它的核心叙事;第二层是内存和存储,Micron、SK Hynix 这类内存厂,以及 Vast Data、Pure Storage 这类面向 AI 的存储厂,它们在解决 KV cache 被挤出显存的问题;第三层是 Dell、HPE 这类整机厂,把可靠性左移到工厂是它们相对白牌服务器的差异化;第四层是机器人板块,Walden Robotics 这种"仿真训练+部署中持续学习"的工业机器人如果真的能跑满生产班次,说明物理 AI 已经开始变成稳定的推理负载。这对 AI 板块和机器人板块都是偏正面的信号,但因为是赞助活动的内容,我会更谨慎地对待里面的数字。值得关注的是 Walden Robotics 后续有没有公开的客户名单或部署规模,这比活动上的说法更能证明物理 AI 的实际落地速度。
