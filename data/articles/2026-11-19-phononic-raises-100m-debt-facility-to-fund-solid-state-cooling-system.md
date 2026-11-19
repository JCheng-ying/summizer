# Phononic raises $100m debt facility to fund solid-state cooling system
https://www.datacenterdynamics.com/en/news/phononic-raises-100m-debt-facility-to-fund-solid-state-cooling-system/

（说明：同一事件 DCD 还刊登了一篇由 Trinity Capital 署名的赞助新闻稿，下文涉及"部署在美国主要超大规模云厂商""已盈利"等说法均来自该新闻稿，属于利益相关方表述，未经独立验证。）

这条融资新闻背后的命题是：AI 数据中心的散热问题正在从"整栋楼怎么降温"细化到"单个元器件怎么降温"。当 GPU、HBM 和光模块的功率密度越来越高，局部热点会先于整体温度成为性能上限，于是出现了一个新的细分赛道：芯片级、点对点的精准热控。

文章指出，北卡罗来纳州的固态散热公司 Phononic 从 Trinity Capital 获得 1 亿美元债务融资，用于扩大制造产能以满足客户需求。Phononic 的产品是热电制冷（thermoelectric cooling），原理是给一类特殊半导体材料通电，在材料两端产生温差，把热量从 IT 硬件上吸走再排到别处。这种方案没有运动部件，也不需要冷却液，但文章明确说，这项技术的效率还不足以给整个数据中心降温。所以 Phononic 的打法是做"补充冷却"：把器件直接贴在激光器、内存芯片这类具体部件上，理论上提升这些元件的性能，同时减轻主冷却系统的压力。它还提供一套管理散热硬件的软件。赞助新闻稿进一步称，其 Thermal Control Systems 面向 GPU、HBM、网络芯片和光模块，Thermal Fabric 软件层可以根据 AI 负载实时调整热控，并称公司已盈利、产品已部署在美国主要超大规模云厂商。

技术上需要说清楚的一点是：热电制冷（帕尔贴效应）的能效比远低于液冷，它自己也会发热，所以它不是液冷的替代，而是"在液冷之上再对最敏感的点做精细温控"。这一点最适合的场景是光模块：激光器的波长和寿命对温度非常敏感，共封装光学（CPO）和高速光模块越来越密，局部温控的价值越来越大。

个人看法：今天早些时候写过的 [液冷如何推动数据中心变革（赞助文章）](2026-11-19-sponsored-how-liquid-cooling-can-actually-facilitate-a-data-center-revolution.md)，以及前几天的 [三星洽购散热公司 Modine](2026-11-13-samsung-in-talks-to-acquire-data-center-cooling-company-modine-manufacturing-rep.md) 和 [Chemours 推出两相液冷液](2026-11-05-chemours-releases-two-fluids-for-two-phase-liquid-cooling.md)，加上这一篇，散热赛道的资本动作非常密集。我的框架是散热链条现在分成三层：1. 设施级（冷却塔、冷水机、CDU），Vertiv、Modine、Trane 这类；2. 机柜/芯片级液冷（冷板、两相冷却液、浸没式），CoolIT、Boyd、Chemours；3. 元器件级精准热控，也就是 Phononic 这种。按"先找瓶颈"的思路，前两层解决的是总热量，第三层解决的是局部热点和光互联的性能稳定，而后者随着 1.6T/3.2T 光模块和 CPO 普及，可能会变成新的瓶颈。

这条新闻利好 AI 板块，因为散热被 Phononic CEO 直接点名为"增长的关键瓶颈"，光模块链条（Coherent、Lumentum、中际旭创这类光模块和激光器厂商）也会因为热控改善而受益；也挂在能源板块，因为精准热控的卖点之一是减少整体冷却能耗和用水。但要克制：这是一笔债务融资而不是股权融资，Phononic 是非上市公司，产品效率和客户部署情况都来自公司自己和贷款方的表述，热电方案能否在大规模部署中证明经济性还需要观察。值得跟踪的是有没有光模块厂商或 GPU 厂商公开把它纳入参考设计。
