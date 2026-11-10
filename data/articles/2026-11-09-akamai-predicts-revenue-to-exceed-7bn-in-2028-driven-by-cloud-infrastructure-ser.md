# Akamai predicts revenue to exceed $7bn in 2028, driven by cloud infrastructure services growth
https://www.datacenterdynamics.com/en/news/akamai-predicts-revenue-to-exceed-7bn-in-2028-driven-by-cloud-infrastructure-services-growth/

这篇财报新闻值得关注，是因为它展示了 AI 算力需求正在把一类原本不被看作"AI 公司"的企业拉进来：一个靠 CDN 起家的边缘网络公司，凭借遍布各地的小型节点，突然成了前沿 AI 实验室的大额算力供应商。如果这个模式成立，AI 推理的部署形态会从"少数超大园区"向"大量分散的中小节点"扩散。

文章指出，Akamai CEO Tom Leighton 在财报电话会上预计 2028 年总收入可能超过 70 亿美元。最新一季总收入 11.22 亿美元，同比增长 6%；云基础设施服务（CIS）收入 1.09 亿美元，同比增长 34%，是增长最快的业务。公司预计 2027 年 CIS 收入 11 亿到 13 亿美元，总收入增长 17% 到 22%。驱动这一切的是最近与 Anthropic 签下的 116 亿美元合同，CFO Ed McGowan 说已经锁定了交付所需约 70% 的硬件、内存等部件；算上 5 月与 Anthropic 签的另一单、两家未具名 AI 公司的大单和众多企业客户，今年签下的 CIS 多年期承诺已超过 140 亿美元。公司预计每兆瓦合同电力约产生 2200 万美元收入，并称这是大型长约的"价格下限"。

但文章也给出了代价：公司遇到"轻微的供应链和第三方数据中心延期"，Q4 收入会低于预期；Q3 资本开支 4.64 亿美元，Q4 将跃升到 24.45 亿至 26.45 亿美元，其中 17 亿用于 Anthropic 合同；非 GAAP 营业利润率 25%，同比下降 6 个百分点，调整后 EBITDA 下降 5%。McGowan 解释说，大规模建设时托管成本先于收入到来，加上长期托管合同的价格递增条款要做直线法摊销，所以会出现非现金费用。财报后 Akamai 宣布发行两笔各 11 亿美元的可转债（2028 年和 2031 年到期）。文章特别提到一个差异化点：Akamai 主攻推理和企业级规模模型的训练，主要用 CPU 承载，CPU 更便宜、更省电，其 CPU 产能已按七年期合同租出。

个人看法：结合 [Anthropic S-1](2026-11-08-anthropic-s-s-1-outlines-company-s-strong-financials-methods-potential-risks-aft.md) 那篇看，Anthropic 正在把算力采购分散到几乎所有能提供容量的供应商，从超大规模云、neocloud、比特币矿企到 Akamai 这种边缘网络公司。这说明前沿实验室的瓶颈已经不是"选最好的供应商"，而是"能拿到的容量都要"。目前 AI 算力的供应方大概有三类：1. 超大规模云（Google、Amazon、Microsoft），容量大但排队长；2. GPU neocloud 和转型矿企（CoreWeave、Nscale、TeraWulf、Riot），靠已有电力和场地快速交付；3. 像 Akamai 这样的分布式边缘网络，靠现成的骨干网和大量小站点快速铺开，主打推理。第三类和 edge AI 板块的逻辑直接相关：推理越来越需要靠近用户、低延迟，而不是集中在一个园区。

投资角度先找瓶颈：这里的瓶颈是"可快速交付的已通电容量"，Akamai 的优势正是不需要等一个吉瓦级园区建成。但风险也很明确：营业利润率下降、资本开支暴增、靠可转债融资、收入高度集中在单一客户 Anthropic。受益层次上，第一层是交付这些容量的硬件，包括服务器 CPU（AMD EPYC、Intel Xeon）和内存，因为 Akamai 明确走的是 CPU 推理路线，利好 AI 板块里的通用算力和内存；第二层是托管数据中心运营商，因为 Akamai 大量容量是向第三方租的；第三层是 Akamai 自己，但它的估值要等大合同全部爬坡、利润率回到 30% 以上才能验证。对 edge AI 板块来说，这是一个分布式推理有真实大额订单的证据。现在值得跟踪的是 Q4 第三个大合同能否按时开始确认收入，以及"轻微延期"会不会扩大。
