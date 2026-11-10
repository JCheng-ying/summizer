# Google advances agentic AI custom silicon expanding TPU family with 8tx and 8i Max
https://siliconangle.com/2026/11/09/google-advances-agentic-ai-custom-silicon-expanding-tpu-family-with-8tx-and-8i-max/

这次发布背后的命题是：AI 芯片正在从"一款通用加速器"走向"按负载细分的产品线"。当推理成为算力需求的主体，而且 agent 和超长上下文成为主流用法时，芯片设计的瓶颈就从算力本身转向了内存容量、数据搬运和安全隔离。

文章指出，Google 在第八代 TPU 架构下新增两款专用芯片。此前在 4 月的 Google Cloud Next 2026 上，Google 已经发布了面向大规模训练的 TPU 8t 和面向实时推理的 TPU 8i。这次新增的 TPU 8i Max 面向超大上下文窗口和最高机柜算力密度，计算、SRAM 和高带宽内存（HBM）都是 8i 的两倍，并且在同样的机柜占地中放进两倍的硅，降低了每平方英尺和每瓦的数据中心空间占用。文章解释了原理：上下文窗口相当于模型的工作空间，窗口越大，芯片需要越频繁地搬入搬出数据，因此需要更多片上内存和更强的芯片间连接；增加片上内存可以减少处理器之间的数据移动，降低延迟和功耗。Google 说 8i Max 是与 Gemini 推进超大上下文同步开发的，Gemini 支持 100 万 token，约合 75 万个英文单词、1500 页文本。另一款 TPU 8tx 则面向安全、机密的推理：它基于 TPU 8t 架构，搭配定制的 AMD CPU 主机，在硬件层直接内置安全隔离区，在模型处理数据时保护敏感数据和模型权重；它结合了训练级算力和快速推理，让受监管行业和政府可以在同一个机密系统里完成私有数据微调、大模型蒸馏和强化学习训练 agent，而不需要在不同集群之间迁移数据。

个人看法：这和今天 [英伟达 CEO 丑闻](2026-11-09-trump-stands-by-nvidia-boss-jensen-huang-despite-spy-scandal-but-fbi-is-investig.md) 那篇放在一起看很有意思：在市场开始担心 Nvidia 关键人风险的同一天，Google 又往 TPU 产品线里加了两款细分芯片，"去单一供应商依赖"的叙事在加强。之前 [Gemini 4 Carbon 登顶智能指数](2026-11-08-google-gemini-4-carbon-tops-intelligence-index-cybersecurity-benchmarks.md) 那篇也说明 Google 是少数在模型和芯片两端都有顶级能力的公司。我觉得 AI 芯片的细分正在沿三个维度展开：1. 训练 vs 推理（8t vs 8i）；2. 推理里再按内存需求细分（8i vs 8i Max），因为超长上下文和 agent 的瓶颈是内存而不是算力；3. 按安全和合规需求细分（8tx），专门服务政府和受监管行业。第三个维度很少被讨论，但它打开的是一个对价格不太敏感、但对主权和保密要求极高的市场。

投资角度先找瓶颈：这里的瓶颈非常明确——内存。8i Max 把 HBM 和 SRAM 都翻倍，说明超长上下文推理吃的是内存带宽和容量。那么受益的层次是：第一层是 HBM 供应商，SK 海力士、三星、美光，每一代芯片的 HBM 用量都在成倍增长，这是 AI 板块里确定性最高的一层之一；第二层是先进封装和代工，HBM 堆叠和 CoWoS 类封装产能仍然紧张，TSMC 是核心；第三层是为 Google 设计定制芯片的合作伙伴（市场普遍认为是 Broadcom）以及这次被点名提供 CPU 主机的 AMD；第四层是数据中心本身，"同样机柜装两倍硅"意味着单柜功率密度继续上升，液冷和供电设备的需求会跟着走，这一点挂能源板块。至于 8tx 指向的机密计算，对政府和金融客户是新的增量市场。值得跟踪的是 8i Max 和 8tx 的上市时间与可用区域，以及 Google 是否会把 TPU 对外部客户（比如 Anthropic 这样的大租户）的供给进一步扩大。
