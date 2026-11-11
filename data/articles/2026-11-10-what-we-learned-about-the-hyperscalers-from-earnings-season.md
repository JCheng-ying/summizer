# What we learned about the hyperscalers from earnings season
https://siliconangle.com/2026/11/10/what-we-learned-about-the-hyperscalers-from-earnings-season/

（说明：这是 ZK Research 首席分析师 Zeus Kerravala 为 SiliconANGLE 写的观点文章，排名判断是作者个人观点，文中部分数据转引自第三方媒体，未逐一核实。）

这篇文章背后的命题是：三大云厂商的 AI 战略已经从"谁的模型最强"分化成"谁的平台最开放、谁的推理成本最低、谁能自己掏钱建算力"。作者的结论很直接：Amazon 长期胜出，Microsoft 稳居第二，Google 是"遥远的第三"。

文章指出，第一，AWS 证明了规模不是速度上限：第三季度收入 460 亿美元，增长 39.3%，连续六个季度加速，年化 1840 亿美元，营业利润 178 亿美元，积压订单从 2025 年底的 2440 亿美元升到 5780 亿美元，Jassy 预计 2027 和 2028 年增长都超过 40%。作者认为 AWS 的核心是 Bedrock 的"模型中立"，提供 100 多个模型，财富 500 强在 Bedrock 上的支出同比增长近 7 倍，token 量增长近 17 倍；大部分 Bedrock 推理跑在自研的 Trainium 上，Jassy 还表示 2027 年底开始对外销售 Trainium。代价是 2026 年约 2200 亿美元的资本开支和负的自由现金流。第二，Microsoft 的护城河是客户：Azure 增长 48% 到 332 亿美元，超过 5 万个 Copilot 席位的客户同比增长 8 倍以上，但它高度依赖越来越像竞争对手的 OpenAI，CFO 还提到部分第三方算力交付延迟。第三，作者认为 Google Cloud 的高增长掩盖了脆弱的基础：收入增长 103% 到 307 亿美元，但 TPU 系统销售是重要贡献，硬件销售波动大；搜索占 Alphabet 收入首次低于一半；资本开支 514 亿美元，自由现金流为负，2027 年资本开支预计超过 3000 亿美元。作者还认为 Oracle 靠借债和客户预付款扩张，债务达 1250 亿美元，IBM 则基本不参与算力竞赛。

个人看法：这篇里我最在意的不是作者的排名（他自己也承认 Google Cloud 现在体量只比 Azure 略小），而是两个结构性信号。第一是推理成本正在成为企业采购的核心指标，作者直接建议 IT 领导把"每次推理成本"变成董事会级别的指标，这和 [Google 扩展 TPU 家族](2026-11-09-google-advances-agentic-ai-custom-silicon-expanding-tpu-family-with-8tx-and-8i-m.md) 以及 AWS 要对外卖 Trainium 是同一个趋势：自研推理芯片开始走出自家云，直接和 Nvidia 在企业机房竞争。第二是资本开支已经大到要看"谁能自己掏钱"，这和之前 [AI 繁荣缺失的资产负债表问题](2026-11-08-the-ai-boom-s-missing-balance-sheet-question-what-has-actually-been-verified.md) 呼应。按瓶颈来看，AI 板块现在的瓶颈是"推理的单位成本"和"建设的资金来源"，所以受益层次是：第一层是定制推理芯片的设计和代工链条，Broadcom、Marvell 这类 ASIC 合作方和 TSMC；第二层是不管谁赢都要买的电力和数据中心基础设施，能源板块在 2200 亿和 3000 亿这种资本开支下是确定性需求方；第三层才是平台本身。这几家的资本开支都在加速，说明需求还在，但自由现金流转负是需要持续盯的信号，尤其是 Oracle 这种靠借债扩张的。
