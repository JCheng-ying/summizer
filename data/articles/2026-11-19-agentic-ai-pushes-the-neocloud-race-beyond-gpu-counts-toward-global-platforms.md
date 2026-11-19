# Agentic AI pushes the neocloud race beyond GPU counts toward global platforms
https://siliconangle.com/2026/11/19/global-cloud-availability-sets-neocloud-platforms-apart-sc26/

先说明利益相关:这篇是 SiliconANGLE 在 SC26 上对 Vultr 两位高管的访谈,文末披露这一段节目由 Vultr 赞助,所以文中关于 Vultr 自身定位和竞争对手的判断都是厂商视角,未经独立验证。但它提出的命题值得认真看:neocloud 的竞争正在从"谁手里 GPU 多"转向"谁是一个平台",如果 agentic AI 真的需要完整的云服务栈而不只是裸 GPU,那么过去两年靠出租机柜起家的那批 neocloud 会面临一次洗牌。

文章指出,Vultr 首席营销官 Kevin Cochrane 认为,能支撑真正 agentic AI 部署的,是那些拥有完整服务的全球云平台;传统 neocloud 的数据中心是"孤岛",彼此不连通,不是统一的全球网络和平台,只是为了某个定制客户合同快速建起来的单个站点。Vultr 则按区域组织数据中心,一个区域可以在同一张网络和同一套 API 下管理多个设施,开发者可以直接接入 Terraform 模板。第二个论点来自解决方案工程副总裁 Duncan Ng:推理模型让 agent 可以串联几十个步骤、调用工具并在过程中校验结果,这部分工作高度依赖 CPU,所以 agentic AI 在重新拉动 CPU 需求。Vultr 在 GPU 热潮之前已经做了十多年云,多年来用 AMD 处理器作为 CPU 主力,现在把合作扩展到加速器,下了 12 亿美元的 AMD Helios 机架级系统订单。第三是需求侧,Ng 称企业正在把 agent 工作负载从试点推进到生产,举的例子是一家四大全球系统集成商用 Vultr 作为风险管理服务的底座,把过去需要咨询人员逐一翻表格、发票、申报单的工作大部分自动化。

这里"孤岛 vs 平台"的区分,可以用一个熟悉的例子理解:早期的 IDC 托管和后来的 AWS 之间的差别,不在于服务器多少,而在于 AWS 把计算、存储、网络、数据库和身份管理变成了同一套 API 下可组合的服务。agent 应用需要的恰恰是这种可组合性——它要调用数据库、对象存储、消息队列、CPU 实例来跑工具调用,GPU 只是其中一环。

个人看法:这篇和昨天 [Dell 与 AMD 抢每一瓦电力、agentic AI 让 CPU 回到中心](2026-11-18-agentic-ai-puts-the-cpu-back-at-center-stage-as-dell-and-amd-chase-every-watt.md) 是同一个判断从不同厂商嘴里说出来,也呼应 [AMD 推出面向 AI agent 负载的 EPYC 6](2026-11-10-amd-introduces-epyc-6-processors-for-ai-agent-workloads.md)。当多家厂商同时在讲同一个故事时,要警惕它有一部分是营销叙事,但 agent 工作流里工具调用、检索、校验这些步骤确实跑在 CPU 上,这个技术逻辑是成立的。再结合 [Nebius 400 亿美元支出计划检验 neocloud 打法](2026-11-12-nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending.md) 和 [NVIDIA 说明何时继续为 neocloud 融资](2026-11-18-nvidia-clarifies-when-it-will-and-won-t-keep-financing-neoclouds.md),我觉得 neocloud 大概会分化成三类:1. 绑定单一大客户的"GPU 房东",收入集中、合同驱动,融资依赖供应商托底;2. 向全栈平台转型的,比如这篇里的 Vultr 和 Nebius,资本开支更大但客户更分散;3. 被并购或退出的。第一类在融资收紧时风险最高。

先找瓶颈。agentic AI 落地的瓶颈已经不只是 GPU 数量,而是第一,完整服务栈和全球网络;第二,CPU 与加速器的混合算力配比;第三,企业对可靠性和合规的要求。按"谁在解决瓶颈"来看受益层次:第一层是 AMD,它同时卖 CPU(EPYC)和机架级加速器(Helios),12 亿美元订单是一笔看得见的收入,而且 agent 推高 CPU 需求的逻辑对它比对纯 GPU 厂商更有利;第二层是网络和互联,区域内多设施统一网络需要大量数据中心互联和交换设备,Arista、Broadcom 这一层会受益;第三层是做平台而非机柜的云厂商,超大规模云(AWS、Azure、Google Cloud)本来就在这个位置,neocloud 里能转型成功的会分到一部分企业 agent 负载。这对 AI板块 是结构性利好,但利好的是基础设施里的 CPU、网络和平台层,而不是单纯 GPU 数量。

现在还早,访谈里的企业案例没有给出规模,"孤岛 neocloud 会被淘汰"也是一家竞争者的说法。值得跟踪的是 AMD 后续财报里数据中心 CPU 收入的增速有没有明显抬头,这是检验"agent 拉动 CPU"是否从叙事变成订单的最直接信号。
