# Exclusive: Onyx Security brings AI agent governance to Glean’s enterprise AI platform
https://siliconangle.com/2026/11/13/exclusive-onyx-security-brings-ai-agent-governance-to-gleans-enterprise-ai-platform/

需要先说明：这篇是基于两家公司联合公告的独家报道，文中关于企业“尚未准备好管理 Agent 风险”的判断主要来自 Onyx 自己的说法，属于利益相关方的表述，产品效果未经独立验证。

这篇文章背后更大的命题是：当企业 AI 从“问答助手”走向“有权限、能动手的自主 Agent”，安全问题的形态就变了——过去管的是人和账号，现在要管的是一群会自己调用工具、读写数据的软件实体。谁来给这些 Agent 建立“户口”、权限边界和审计记录，正在成为企业 AI 落地的一道门槛。

文章指出，Onyx Security 宣布与企业 AI 平台 Glean 集成，分工是 Glean 提供构建、部署和运行 Agent 的平台，Onyx 的“安全 AI 控制平面”负责把治理和安全覆盖到整个 AI 环境。具体拆开有几层：第一是发现，Onyx 可以盘点 Glean 上的每一个 Agent 以及它拥有的访问权限和能力，并为每个 Agent 指定负责人、业务用途和风险等级；第二是策略与持续评估，在应用企业的治理与合规策略之后，持续监控每个 Agent 被授予的权限、工具和数据访问的变化；第三是运行时控制，对提示词、回复和 Agent 动作施加“意图感知”的控制，可以直接拦截不安全请求，或把偏离预期的动作拉回策略范围内；第四是集中的审计证据，让 Agent 从部署到运行到扩展都处在同一套治理模型下。

资本层面，文章提到 Onyx 迄今融资 1.53 亿美元，其中包括 7 月由 Bessemer Venture Partners 领投的 1.13 亿美元 B 轮，公司今年 3 月才带着 4000 万美元种子和 A 轮亮相；Glean 上一次融资是 2025 年 6 月的 1.5 亿美元 F 轮，估值 72 亿美元。Onyx 联合创始人兼首席 AI 官 Gil Elbaz 此前在 Nvidia CTO 手下工作过。

个人看法：一家今年 3 月才成立的公司，半年多就拿到 1.53 亿美元，说明资本已经把“Agent 治理”当成一个独立赛道在押注。和今天同批的[LangChain 估值达到 30 亿美元](2026-11-13-ai-agent-startup-langchain-hits-3b-valuation.md)、[ChatGPT 推出让 Agent 代为购物结账的钱包](2026-11-13-chatgpt-s-new-wallet-lets-ai-agents-shop-and-check-out-for-you.md)放在一起看，Agent 的能力边界在快速外扩——能写代码、能花钱、能读企业全部数据——而能力每扩一步，权限和审计的缺口就大一步。按“先找瓶颈”的思路，企业 AI Agent 大规模部署当下卡住的不完全是模型能力，而是 CISO 和合规部门能不能签字放行；谁能让安全团队“看得见、管得住”，谁就在解决这个瓶颈。

这条线上受益的层次大致是：第一层是 Agent 的身份与权限管理，这本质上是传统身份安全（比如 Okta、CyberArk 这类公司）向“非人类身份”的延伸，传统厂商和 Onyx 这类新创之间会有正面竞争；第二层是运行时防护和审计，类似 Onyx 这种控制平面，以及大型安全平台（Palo Alto Networks、CrowdStrike 等）在 AI 安全上的布局；第三层才是 Glean 这类 Agent 平台本身——集成安全能力能帮它们更快进入受监管行业，但这类合作很容易被复制，护城河有限。挂到板块上，这是 AI 板块偏软件层的利好信号：它说明企业 Agent 部署在推进，并且配套的治理层开始有真金白银投入；但它不直接影响算力层，也和机器人、能源等板块关系不大。

还要说的是，这类“控制平面”产品是否有效，最终要看真实部署中拦截了多少风险、误拦了多少正常操作，而这篇文章里没有任何客户或效果数据。现在只能当作赛道热度的一个信号来看，值得跟踪的是 Onyx 或同类公司有没有公开的大客户案例，以及 Microsoft、Google 这类平台方会不会把 Agent 治理直接做成自带功能，压缩第三方的空间。
