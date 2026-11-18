# From store outlets to methane leaks, every scrap of power is now fair game for AI compute
https://siliconangle.com/2026/11/18/distributed-inference-turns-stranded-power-ai-compute-dellatsc26/

需要先说明利益相关：这是 SiliconANGLE 旗下 theCUBE 在 SC26 上对 Dell AI、计算与网络 CTO Ihab Tarazi 的访谈，原文披露该节目片段由 Dell 赞助，所以文中关于产品"首个"、部署时间等说法都来自厂商，未经独立验证。

这篇访谈背后真正有意思的命题不是 Dell 又发了什么产品，而是标题那句话：如果连门店插座、甚至甲烷泄漏这种零散电力都开始被当成 AI 算力的来源，说明"电力在哪里，算力就去哪里"已经从一个口号变成了推理部署的实际约束。过去是先建数据中心再找电，现在是反过来先找电再决定把推理放在哪。

文章指出，Tarazi 认为 AI 和传统高性能计算最大的区别是规模：几万、几十万块 GPU 最终连在同一张网络上，即使分成多个集群也是如此。Dell 的应对思路是卖完整系统而不是零部件，这次的重点是它所说的首个 100% 液冷网络系统——交换机、光模块和线缆在工厂预先测试好，整机柜交付。Tarazi 的说法是，原本要在现场组装几百个部件、花两三周排错，现在装好之后几小时就能上线。此前 Dell 已经推出液冷存储，至此计算、网络、存储共用同一套冷却和供电规格，他的原话意思是不用再为 GPU 和网络分别建两个数据中心，时间和成本都能大幅下降。

第二个重点是软件。文章称客户希望有一个统一的控制平面，能跨不同的 GPU 和 CPU，把多达 1000 个各自有少量富余电力的小站点连起来，从而把"搁浅电力"（stranded power）变成 AI 算力，给那些没法快速建大型数据中心的公司用。Tarazi 说电力可用性的含义会让人意外，不只是门店里有电，也可能是逸出的甲烷——任何可能的电力来源，大家都在倒推如何用这些电做分布式推理。

个人看法：这篇和昨天的 [Arista takes aim at the next AI network battleground: distributed inference](2026-11-17-arista-takes-aim-at-the-next-ai-network-battleground-distributed-inference.md) 以及更早的 [Nvidia looks to tap Brightspeed central offices for inference network](2026-11-09-nvidia-looks-to-tap-brightspeed-central-offices-for-inference-network-report.md) 是同一条线索的第三个侧面：Arista 文章里推理走向分布式的第三个理由正是"企业会在任何有容量的地方部署推理"，Brightspeed 那篇是电信老机房，这篇则把载体继续往下推到门店和能源现场。同一周 Dell 还谈了 [液冷软件定义存储](2026-11-17-dell-bets-liquid-cooled-software-defined-storage-can-keep-ai-factories-fed.md) 和 [机柜级集群管理](2026-11-18-scripts-can-t-run-ai-factories-dell-moves-cluster-management-from-the-server-to-.md)，能看出它整个 SC26 的叙事是把 AI 工厂当成一个整体系统来卖。

先找瓶颈：这篇里推理部署的瓶颈不是 GPU，而是有电可用的地点，以及把上千个小而分散、硬件异构的站点当成一台机器来管理的能力。解决这个瓶颈的层次大概是：第一层是编排和控制平面软件，能跨异构芯片、跨站点调度推理负载，这层是最稀缺的，Dell 想占这个位置，但云厂商、Nvidia 自己的软件栈以及 Kubernetes 生态都在竞争；第二层是前端和跨站点网络，Arista、Cisco，以及相干光模块厂商，因为流量要离开机房；第三层是能源侧，"搁浅电力"包括油气田伴生气、甲烷利用这类场景，之前 Crusoe 就是用油气田的伴生气发电跑算力起家的，此外还有小型燃气发电机、燃料电池和储能；第四层是液冷和整机柜集成，Dell、Supermicro 这类服务器厂商，以及 Vertiv 这类热管理和电源公司。对应到板块，这是 AI 板块（推理部署扩张、编排软件和网络）、能源板块（分散电力被重新定价）和 edge AI 板块（推理从大园区下沉到门店和现场）的共同信号，其中 edge AI 板块的挂钩最直接。

但必须克制地看：这是厂商赞助的访谈，"1000 个小站点""甲烷"更像是 CTO 描述的需求方向，没有给出任何具体客户、规模或已部署的案例。小站点算力的经济性也还是问题，每个站点电力有限、运维分散，单位算力成本未必比集中式园区低。现在还早，值得关注的是后续有没有真实落地的分布式推理项目公开披露站点数量和电力来源，尤其是能源企业或连锁零售商作为客户出现。
