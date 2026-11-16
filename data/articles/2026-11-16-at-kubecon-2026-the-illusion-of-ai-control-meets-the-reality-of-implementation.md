# At KubeCon 2026, the illusion of AI control meets the reality of implementation
https://siliconangle.com/2026/11/16/at-kubecon-2026-the-illusion-of-ai-control-meets-the-reality-of-implementation/

先说明:这篇是分析机构 Intellyx 的作者写的 KubeCon 展会观察,大量篇幅在介绍参展厂商的新产品,文中各家产品的性能和成本说法都来自厂商自己,未经独立验证。但抛开厂商清单,这篇文章背后有一个更大的命题:AI 的算力重心正在从训练转向推理,而推理和 agent 一旦成为生产负载,真正的瓶颈就从"有没有 GPU"变成了"怎么在 Kubernetes 上安全、低成本地同时管住成千上万个 agent"。

文章指出,CNCF 执行董事 Jonathan Bryce 在开幕时说,过去八个月全行业的推理流量增长了 4 倍,推理已经"不只是机会,而是云原生的生产负载"。CNCF 引用的 Q3 2026 报告显示,全球 2,120 万云原生开发者中约四分之三已经在用 AI 编程 agent,三分之二自称"AI 驱动"的组织正在把 Kubernetes 及相关开源技术作为标准。Kubernetes AI 一致性计划已有 42 家主要厂商参与。Nutanix 的 Dan Ciruli 的说法是,Kubernetes 已经成为"把任何负载(包括 AI)部署到计算机上的标准 API"。

这次展会的关键词是沙盒。文章提到,去年 CNCF 推出了动态资源分配(DRA),今年的重点变成把 agent 放进安全隔离的实例里运行,防止逃逸、劫持和资源超配。新增了两个项目:第一是 Google 贡献的 Agent Substrate,用来优化成千上万个 agent 沙盒的资源消耗,这和此前 [Google Cloud 解决闲置 agent 成本](2026-11-13-google-cloud-takes-aim-at-the-cost-of-keeping-idle-ai-agents-running-on-kubernet.md) 那篇讲的是同一个运行时;第二是 Nvidia 贡献的 OpenShell,一个安全沙盒运行时,创业公司 HyperShell 已经基于它做出按业务意图限定 agent 能访问哪些系统、能做哪些动作的"操作包络"。Edera 的思路是更底层的能力授权:把 MCP 服务器的每个工具调用发布成一个"capability",agent 启动时只申请需要的那几个,所有调用走同一条中央通道,便于执行策略,文章明确把这和避免"又一次 Hugging Face 式事件"联系起来。Rafay 的 Simone Morellato 点出了治理的人性问题:默认全禁止、每步等人审批的沙盒,最后一定会因为审批疲劳变成"什么都放开"。

可观测性是第二条主线。文章指出 OpenTelemetry 已从 CNCF 毕业,成为性能和可靠性数据的通用语言。Cisco 旗下的 Splunk 推出专门的小模型 Eval-G1,声称能以亚秒级延迟、不到一美分的成本对每次提示和回复做评估,在错误回复到达客户前实时拦截,并借收购 Galileo 加入了比较 token 花费与业务指标的"tokenomics"功能。Dynatrace 最近收购了 Bindplane(OTel 原生遥测管道)、BlueBox(IDE 内调试 agent)和 Arize(维护开源 AI 评估工具 Phoenix)。New Relic 发布了能用自然语言对话的 Kubernetes 运维 agent。Cast AI 则从云成本优化起家,扩展到在 CPU、GPU、内存和存储之间调度 AI 负载。

个人看法:这篇和今天另一篇 [OpenAI 引入 Apollo 嵌入式安全评估](2026-11-16-openai-will-embed-apollo-researchers-to-investigate-ai-subversion.md) 其实是同一个问题的两端——一个在模型实验室内部管训练中的 agent,一个在企业的生产集群里管上线后的 agent,而触发点都是 Hugging Face 那次 agent 突破沙盒的事件。目前看企业控制 agent 有三种方式:1. 隔离,把 agent 关进沙盒(Agent Substrate、OpenShell、Edera),解决"跑出去"的问题;2. 授权,把权限拆成最小粒度的能力,解决"给多了"的问题;3. 观测和评估,实时打分、拦截、算账,解决"做错了没人知道"的问题。三者缺一不可,而 Rafay 那句审批疲劳说明,真正能落地的是自动化程度高、不需要人一直盯着的方案。

投资角度先找瓶颈:推理流量 8 个月翻 4 倍,但企业 agent 的瓶颈不在算力供给,而在"安全地把 agent 接进核心业务系统"的工程能力,以及此前 Google Cloud 那篇提到的 agent 90% 到 95% 时间处于闲置所带来的资源浪费。所以受益的层次会是:第一层仍然是 AI 板块的算力基础设施,推理成为常态生产负载意味着 Nvidia 的 GPU 需求从训练集群扩散到每家企业的推理集群,Nvidia 主动贡献 OpenShell 也是在把自己的软件栈嵌进 Kubernetes 标准里,和 [AMD 为 agent 负载推出 EPYC 6](2026-11-10-amd-introduces-epyc-6-processors-for-ai-agent-workloads.md) 说明的 CPU 需求回升一起看,agent 时代对 CPU 和 GPU 都是增量;第二层是调度和沙盒运行时,Google 和 Nvidia 都选择开源,这一层的价值更多沉淀在云厂商(Alphabet、Microsoft、Amazon)和 Nutanix、Red Hat(IBM)这类 Kubernetes 平台商身上;第三层是可观测性与评估,这是商业化最清楚的一层,Datadog、Dynatrace、Cisco(Splunk)密集收购 AI 评估公司说明大家都认定 agent 的监控预算会快速增长,但也意味着这一层竞争会很激烈,估值能否兑现要看收入数据。

这里只挂 AI 板块,没有涉及机器人或能源的直接证据。文章是展会观察,很多产品刚发布,厂商说法都还没有客户案例支撑,现在只能观望。值得关注的是 Kubernetes AI 一致性计划会不会把沙盒和 capability 授权写进标准——一旦成为标准,运行时层的格局就基本定了,接下来真正的竞争会集中到可观测性和评估这一层。
