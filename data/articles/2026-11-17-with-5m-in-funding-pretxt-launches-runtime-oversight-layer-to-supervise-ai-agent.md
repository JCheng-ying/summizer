# With $5M in funding, Pretxt launches runtime oversight layer to supervise AI agents in real time
https://siliconangle.com/2026/11/17/with-5m-in-funding-pretxt-launches-runtime-oversight-layer-to-supervise-ai-agents-in-real-time/

需要先说明:这篇是基于公司融资发布的报道,文中"比 LLM-as-a-Judge 快 60 倍""违规率降到零"等性能说法都来自 Pretxt 自己,属于利益相关方的表述,未经独立验证。

这条新闻背后更大的命题是:当企业开始把退款、改数据库记录这类有后果的任务交给 AI agent,"agent 是否安全"和"agent 是否在正确地完成被分配的工作"就变成了两个不同的问题。前者是传统安全工具的思路,后者更接近一个"监工"——而后者恰恰是目前 agent 落地最大的信任缺口。

文章指出,Pretxt AI 今天以 500 万美元种子轮融资正式亮相,由 Deciens Capital 领投,Howdy Partners、Service Provider Capital 和 NSV Wolf Capital 跟投。它的产品是一个运行时的"AI 监督"层:在 agent 工作的过程中持续把它的行为和企业的规则、政策做比对,一旦发现 agent 开始偏离,就立刻介入把它拉回正轨,而不是事后标记错误。文章认为现有安全工具大致有两种做法,第一种是粗暴地直接拦截 agent,代价是工作变慢;第二种是事后标记,但那时损害可能已经发生。两位联合创始人 Brian Soby(CEO)和 Aaron Costello(CTO)此前在 SaaS 安全公司 AppOmni 共事,Soby 之前还在 Salesforce 和 Mitre 担任过高级安全职务;文章提到他们在 AppOmni 期间发现了 Salesforce 和 ServiceNow 开发的 AI agent 中的若干重大漏洞。

技术路线上,文章指出很多 agent 监控工具用第二个大模型当"裁判"(LLM-as-a-Judge)去监督干活的那个模型,Pretxt 刻意避开了这种做法,理由是它增加延迟、增加算力成本、而且判断带有猜测成分;取而代之的是一个"近似确定性"的引擎,在毫秒级评估 agent 的动作,拦截违规操作。公司称这比基于 LLM 裁判的工具快最多 60 倍,在 Zapier 的 AutomationBench 测试中把 agent 违规率从大约五分之一降到零。用户只需要用自然语言选择哪些政策和护栏适用于某个 agent,平台支持追踪审批、回滚计划版本,并在遇到未曾预想的情况时暂停 agent、交给人类决定规则。产品目前处于早期访问阶段,主要面向金融服务、保险、医疗和客服等强监管、容错率极低的行业。Enterprise Management Associates 分析师 Chris Steffen 的评价是,多数工具问的是 agent 是否安全、合规、可观测,而很少有工具能说明 agent 是否在正确地完成交给它的工作。

这和我之前写过的 Stroop Test 那篇的结论是直接呼应的:Transformer 的 attention 不等于人类的执行控制,上下文越长越容易偏离最初的目标。Pretxt 的产品其实就是在 agent 外面加一个"执行控制"的外挂——既然模型本身守不住目标,就由一个外部的、确定性的系统替它守。它也和之前几篇连成一条线:[Exclusive: Onyx Security brings AI agent governance to Glean's enterprise AI platform](2026-11-13-exclusive-onyx-security-brings-ai-agent-governance-to-glean-s-enterprise-ai-plat.md) 管的是 agent 的身份、权限和审计,属于"agent 能做什么";Pretxt 管的是运行中每一步动作,属于"agent 正在做什么";而 [California state AG sues OpenAI over rogue agent incidents](2026-11-16-california-state-ag-sues-openai-over-rogue-agent-incidents.md) 则说明 agent 失控的后果已经开始进入法律追责。

个人看法:目前给 agent 加监督大致有三种方式:1. 模型内部对齐,靠训练让模型自己守规则,这是前沿实验室的路线,但效果不可审计;2. LLM 裁判,用另一个模型盯着,灵活但慢、贵、本身也会出错;3. 确定性规则引擎,也就是 Pretxt 这种,快、可解释,但只能覆盖事先写清楚的规则,遇到没想到的情况只能停下来交给人。按"先找瓶颈"的思路,企业 agent 落地现在卡住的不是模型能力,而是"出了错谁负责、能不能证明没出错"——这是一个合规和信任瓶颈。解决这一层的受益方首先是 agent 治理和安全这个新兴细分,但这一层目前融资规模很小(500 万美元种子轮),竞争者也很多,而且 Salesforce、ServiceNow、Microsoft 这些 agent 平台方完全可能把类似功能内置,独立小公司的护城河并不清楚;反而更确定的受益方是 agent 平台本身,因为监督层越成熟,企业越敢把高价值任务交给 agent,平台的调用量才能真正放大。所以这篇挂的是**AI板块**,机制是"监督与合规工具降低企业部署 agent 的风险门槛,从而扩大 agent 在高价值场景的使用",而不是直接利好算力。值得一提的是,Pretxt 刻意避开 LLM 裁判、减少额外推理调用,这对算力需求其实是轻微的反向信号,但量级可以忽略。

现在这个赛道还在非常早期,产品也只是早期访问,只能观望。值得关注的是金融、保险这类强监管行业里,有没有真正的大客户公开在生产环境中用这类运行时监督工具,以及大型 agent 平台会不会通过收购的方式把这一层整合进去。
