# Texas Advanced Computing Center builds AI inference service
https://www.datacenterdynamics.com/en/news/texas-advanced-computing-center-builds-ai-inference-service/

这篇新闻讨论的是一个容易被忽略、但很能说明趋势的变化：国家级的科研计算中心，过去几十年买的都是做模拟和训练的超算，现在开始专门建一套"常驻在线"的推理服务。如果这一点成立，说明推理正在从商业云的需求变成科研基础设施的标配，而这块需求里 GPU 并不是唯一选项。

文章指出，德州高级计算中心（TACC）正在建设一个名为 Sagebrush 的 AI 推理服务，由美国国家科学基金会（NSF）资助，目标是为全国科研社区提供始终在线的 AI 模型和工具访问。Sagebrush 会与 NSF 的领导级计算设施（NSF LCCF）并行运行、支持其使命。硬件上，它使用 SambaNova 的 AI 芯片以及 SambaStack（SambaNova 包含推理处理器和编译器的软硬件组合），TACC 此前已经以非生产用途提前试用过这些芯片，还将再采购四套系统来扩大常用模型的容量，不过目前部署的 SambaNova 芯片数量没有公开。功能上，Sagebrush 既支持通用 AI 查询，也提供面向特定领域工作流的托管 RAG 服务，其中一个 RAG 服务会用 LCCF 文档以及其他 HPC 和 AI 代码示例进行调优。

文章还提到，NSF 这笔资助从今年 9 月开始，前两年定位为"实验期"，团队会在这段时间评估需要什么、怎样最好地支撑这个平台。NSF 方面的 Katie Antypas 表示，Sagebrush 与 NSF LCCF 配套并接入 NAIRR，扩展了把新兴能力转化为科学发现所需的国家研究基础设施。SambaNova 的 Abhi Ingle 说，从编程到模拟，科学研究越来越依赖 AI 推理。TACC 的 Niall Gaffney 则强调，核心是提供帮助科研的推理服务，并支持更有领域针对性的 agentic 工作流。TACC 还表示会与同样在探索基于 SambaNova 的科研推理的洛斯阿拉莫斯国家实验室合作和共享信息。文章补充了 SambaNova 的背景：它在 2026 年 2 月发布了新一代 SN50 芯片，称专为 agentic AI 负载设计，并宣称其 RDU 比"竞争芯片"快 5 倍、总拥有成本低 3 倍，但没有说明对比的是哪款硬件——这组数字是厂商口径，未经独立验证。本月早些时候，Supermicro 表示将从 SambaNova 采购 1 万颗 SN50 RDU，用于构建和销售解耦式推理系统。

个人看法：我觉得这条新闻和之前写过的两条线索都能接上。第一条是"AI for Science"：之前分析 CIGaRS 框架时我说过，就算 AI 在企业端还没有证明生产力提升，科研实验室对 AI 基础算力的需求依然是实打实的，而 [Nvidia 在 SC26 上说 agent 是新的科学家](2026-11-17-nvidia-at-sc26-agents-are-the-new-scientists-and-they-need-a-lab.md) 和 [Nvidia 发布面向 agentic 科学计算的 Rubin HPC GPU](2026-11-16-nvidia-unveils-rubin-hpc-gpu-for-agentic-ai-powered-science-and-engineering-work.md) 讲的也是同一件事。Sagebrush 把这个判断往前推了一步：科研需要的不只是训练和模拟，还有一个 7×24 小时在线、能跑 RAG 和 agent 的推理层。第二条是"推理芯片多元化"：[推理已占 AI 负载的三分之二](2026-11-21-inference-now-drives-two-thirds-of-ai-workloads-changing-where-chips-get-deploye.md)、[d-Matrix 押注堆叠 DRAM](2026-11-19-d-matrix-bets-stacked-dram-can-solve-inference-s-memory-bandwidth-problem.md)、[Fractile 融资 7.2 亿美元](2026-11-11-british-inference-chip-developer-fractile-raises-720m-in-funding.md) 这几篇都说明，推理这一层的瓶颈是内存带宽和单位 token 成本，而不是峰值算力，这给了非 GPU 架构进入的窗口。一个国家级科研中心选择 SambaNova 而不是 Nvidia 来建推理服务，是这个窗口的一个实际落地案例。

按瓶颈去找受益层次：科研推理的瓶颈是"持续在线的推理成本"和"领域化的软件栈"，因此第一层是推理专用芯片，SambaNova（未上市）以及同类的 Groq、Cerebras 是直接受益方，再加上 Supermicro 这种把专用芯片集成成整机去卖的系统厂商；第二层是推理软件与编排，RAG 服务和 agentic 工作流需要的是模型服务、检索和调度软件，这一层更分散；第三层仍然是 AI 基础设施本身，NSF、LANL 这类公共资金对推理算力的持续采购，会成为 AI 板块里一个不太受商业周期影响的需求来源。所以我会把这条挂在 AI 板块上。但也要看到，这笔采购规模不大——四套系统、芯片数量未公开，前两年还只是实验期，它的意义更多是信号而不是营收。

值得跟踪的是两年实验期之后 Sagebrush 是否转为大规模生产部署，以及洛斯阿拉莫斯是否也正式采用 SambaNova 做科研推理；如果国家实验室体系开始成规模地采购非 GPU 推理硬件，那才说明推理芯片的竞争格局真的在松动。
