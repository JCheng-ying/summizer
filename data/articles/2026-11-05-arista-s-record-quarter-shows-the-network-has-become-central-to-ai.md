# Arista’s record quarter shows the network has become central to AI
https://siliconangle.com/2026/11/04/aristas-record-quarter-shows-the-network-has-become-central-to-ai/

需要说明,这篇是 SiliconANGLE 的分析评论,作者在文中明确表达了看好 Arista 的立场,文中关于"Arista 将不成比例受益"的判断是作者观点,财务数据来自公司财报。它的核心命题是:AI 集群的瓶颈正在从计算转到网络,网络从"连好就行的管道"变成了决定 GPU 利用率的性能部件。

文章指出,Arista 第三季度收入 36.6 亿美元,同比增长 58.5%,是上市以来最快增速,远超 33 亿美元指引;毛利率 64%,经营利润率 49.1%,现金 144 亿美元、无负债。全年指引今年第四次上调至约 133 亿美元,并首次给出 2027 年约 185 亿美元的展望,其中 AI 网络从 35 亿美元翻倍到约 70 亿美元。CEO Jayshree Ullal 说行业正在从"以计算为中心的垂直栈"转向"以网络为中心的整体方案",推理正在从集中式训练变成分布式推理,prefill、decode、存储和 KV 缓存分散在不同资源上。作者的论证是经济账:丢包或链路故障会让昂贵的加速器空转,多 GW 级集群里 GPU 利用率提高 5%,价值远超交换机本身。作者认为 Arista 有三个优势:第一是加速器多样化,随着客户引入 AMD、微软 Maia、Meta MTIA、Qualcomm、Cerebras 等芯片,很多客户会偏好不卖竞品加速器的网络供应商,而 NVIDIA 的 Spectrum-X 已经赢下 Meta 和 Oracle;第二是跨园区互联(scale-across),电力限制迫使算力分散到多个建筑和地区,这部分约占今年 AI 需求的 30%;第三是机柜内互联(scale-up),Arista 基于 ESUN 以太网规范的方案 2027 年试点、2028 年量产,试图替代 NVLink 和 UALink。文章还提到 Arista 与 Anthropic、Google、OpenAI 合作把 AI 漏洞发现集成进软件流程。分析师的担忧包括递延收入持平、研发费用从 2.78 亿增至 4.085 亿美元、毛利率从 65.2% 下滑;股价在财报前一个月跌了 20% 以上。

个人看法:这正好验证了用户自己反复用的那条判断:不管哪条应用路线胜出,算力基础设施里的高速互联几乎总是确定受益方。这篇更进一步,说明了为什么:先找瓶颈,当 GPU 越来越多、越来越分散,瓶颈就从单卡算力转到卡与卡、楼与楼之间的通信。最有意思的是"scale-across 占 30%"这个数字,它把网络需求和电力瓶颈直接连了起来,因为单个园区拿不到足够的电,算力被迫拆到多个地点,于是需要更多长距离高可靠互联,这和同一天 [Nscale 的电力接入问题](2026-11-05-microsoft-declined-option-for-expanded-compute-contract-in-texas-with-nscale.md) 是同一个约束的两面。受益层次是:第一层是以太网交换和路由,Arista、Broadcom;第二层是光模块和光互联芯片,Qualcomm 刚提到的光互联协议也在这层;第三层是网络运维和安全软件。所以这篇对 AI 板块是明确利好,对能源板块是间接的佐证。但 ESUN 能否撼动 NVLink 还很早,递延收入持平也值得留意。值得跟踪的是 2027 年 AI 网络 70 亿美元的目标能否兑现。
