# AT&T uses agentic AI to reinvent business processes from the ground up
https://siliconangle.com/2026/11/14/att-uses-agentic-ai-to-reinvent-business-processes-from-the-ground-up/

先说明来源性质:这篇报道的内容来自 AT&T Business 数字化转型与 AI 助理副总裁 Luke Corbin 在 Amazon Web Services 波士顿活动上的发言,属于企业高管在供应商活动上的自述,文中所有规模和回报数字都是 AT&T 自己报的,未经独立验证。

这篇文章背后的命题,是上一篇 [Can enterprise AI pay for the boom?](2026-11-01-can-enterprise-ai-pay-for-the-boom.md) 里留下的那个问题:企业端到底能不能从"任务提效"走到"流程重构",也就是走过生产率 J 曲线最难的那一段。如果像 AT&T 这样一家 151 年历史、经历过大量并购、系统极其陈旧的公司都能把 agent 真正放进生产流程,那企业 AI 的需求就不只是员工用聊天助手,而是持续、可计量的 token 消耗。

文章指出,AT&T 目前每天处理约 450 亿个 AI token,agentic 平台每月处理超过 100 万笔交易,已有近 500 个 agentic 工作流投入生产,计划明年把这个数字翻三倍。负责这件事的是 2025 年初成立的 Business Agent Foundry。文章强调它的方法不是收集员工零散的自动化点子,而是用行业框架把整条业务流程画出来,再找可以去掉的冗余步骤、部门间交接和对老旧应用的依赖。两个具体例子:第一,光纤安装订单变更过去需要员工从队列里取工单、在大型机上手动改记录再放回流程,agent 接管了其中一部分,减少了延迟;第二,在已经铺好光纤的楼宇里开通专线互联网的时间缩短了一半。销售端也在用,agent 先核实潜在客户的地址和光纤覆盖情况,销售再去跟进。

技术架构上,文章认为 AT&T 的做法和常见的"大量独立专用 agent"路线不同:它只维护一小组 agent,业务逻辑集中存放在上下文或记忆里,由检索 agent 找到适用的知识,再由规划 agent 决定用哪些工具和数据完成任务。治理分两层:员工可以自己建个人效率 agent,但凡是会接触客户的工作流都必须经过 Foundry,做安全、隐私和合规审查。每个生产工作流一开始都有人类监督,准确率达到九成五上下、且在可接受的风险范围内之后才允许自主运行,之后持续监控性能和漂移。衡量指标包括人力节省、收入、运营成本和客户满意度,Corbin 说生产环境的 AI 投入一年内拿到了五倍回报。文章也提到真正的难点不在模型:AT&T 经历了多次并购,数据极度分散,要先整合数据、打通数据中心、云和一线人员之间的连接。

个人看法:这篇最有价值的地方不是"五倍回报"这个数字(自报的、没有口径说明,只能当作方向性参考),而是它把企业 agent 落地的瓶颈讲得很具体。按"先找瓶颈"的思路,可以拆成三层:第一是数据和遗留系统,AT&T 自己承认数据基础设施是并购堆出来的,agent 要和大型机对话,这说明真正卡住的是数据整合和系统集成,而不是模型能力;第二是问责,也就是上一篇提到的"问责层",AT&T 的解决办法是人类监督 + 准确率门槛 + 漂移监控,这和 [Onyx Security 给 Glean 加 agent 治理](2026-11-13-exclusive-onyx-security-brings-ai-agent-governance-to-glean-s-enterprise-ai-plat.md) 是同一个需求;第三是架构,少量通用 agent + 集中业务逻辑 + 记忆,其实印证了之前 Stroop 测试那篇里的判断,Transformer 本身不擅长长期保持目标,所以需要外面加 planner 和 memory 这一层,这和 [LangChain 估值到 30 亿美元](2026-11-13-ai-agent-startup-langchain-hits-3b-valuation.md) 押的是同一个方向。

落到 AI 板块,受益的层次会是:第一层仍然是算力和云,每天 450 亿 token、明年工作流翻三倍,意味着推理需求是持续的,不是一次性的试点,AWS、Microsoft Azure、Google Cloud 以及背后的 NVIDIA、AMD 都在这条线上;第二层是数据整合和集成,像 Snowflake、Databricks 这类数据平台,以及帮老企业做系统改造的集成商,因为瓶颈恰好在这里;第三层是 agent 编排和治理软件,包括 ServiceNow 这类本来就在流程层的公司和 LangChain 这类框架,AT&T 自建了 Foundry,说明大企业未必直接买现成平台,这一层的竞争会比较激烈。不过要注意,文章里 Corbin 也说他的团队"长期来看不应该存在",也就是说 agent 能力最终会分散到各业务部门,而不是集中采购,这对卖平台的公司未必是好消息。电信行业本身的话,AT&T 把 agent 用在开通和销售上,短期是降本,和 edge AI 板块没有直接关系,不硬挂。

整体来看,这是企业 AI 从"员工生产力"转向"流程重构"的一个正面样本,但只是一家公司的自述。值得跟踪的是 AT&T 后续财报里有没有把 AI 带来的成本节省单独披露,以及其他运营商(比如 T-Mobile US、Verizon)是否给出类似的 token 用量和生产工作流数字,这比一句"五倍回报"更能说明企业端需求有没有真正起来。
