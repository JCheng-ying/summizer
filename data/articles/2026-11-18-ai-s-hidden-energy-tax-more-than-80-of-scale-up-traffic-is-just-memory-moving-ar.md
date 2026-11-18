# AI’s hidden energy tax: More than 80% of scale-up traffic is just memory moving around
https://siliconangle.com/2026/11/18/memory-bottlenecks-ai-how-photonics-shared-pools-help-sc26/

需要先说明:这是 SiliconANGLE 在 SC26 上 theCUBE 的访谈,这一段由 Penguin Solutions 赞助(原文有披露),受访的是 Marvell 和 Penguin 两家公司的高管,所以产品能力和能耗数字都是厂商自述,未经独立验证。但它点出的命题是值得认真看的:当推理取代训练成为算力的主要用途,AI 数据中心的瓶颈正在从"算得够不够快"转向"数据搬得够不够快",而大部分被搬来搬去的数据其实是内存。

文章指出,推理时代 GPU 经常闲着等数据,而 HBM(高带宽内存)被焊死在各自的处理器旁边,别的处理器用不上。Marvell 光子互联(Photonic Fabric)业务负责人 Preet Virk 的说法是,今天数据中心的效率还有很大提升空间,浪费的是 GPU 利用率很低带来的"空转算力"。他给出的关键数字是:在 scale-up 网络(也就是一个 pod 内成千上万块 GPU 之间的互联)里,超过 80% 的流量是内存事务;机架内铜缆还能用,但跨越整个 pod 就必须用光。Penguin Solutions 的 MemoryAI Photonic Appliance 就是这个思路的产品化:把 HBM 从 GPU 旁边搬到一个距离 GPU 几十米外的独立机箱里,通过 Marvell 的 Photonic Fabric 连接,每台设备装 16TB 的 HBM 和 DDR5,可以被多个机架的服务器共享。Virk 称,相比铜缆的数据搬运,这种方案每比特能耗可以直接降到四分之一。

为什么需要共享内存池,Penguin 的 Andy Mills 讲得很直白,可以拆成三层:第一是长上下文,要让大模型"记得十分钟前你说了什么",需要大量内存和更长的 token 长度;第二是 Agent,Agent 产生的 token 请求远多于人类用户;第三是 KV cache,它之所以成功,是因为避免了对同一段数据的重复计算,而如果这份缓存能在更多机架之间共享,重复计算就更少,整体效率就更高。所以他的结论是,推理越分布式,越需要共享。

技术上可以这样理解:今天的 GPU 服务器是"每块 GPU 自带一小块极快的内存",这和早期每台服务器自带硬盘很像;而共享内存池是把内存从计算节点里拆出来,变成一个可以被很多节点调度的资源,这和后来存储从本地盘走向 SAN、再走向云存储是同一条"解耦"路线。区别在于,内存对延迟和带宽的要求比存储苛刻几个数量级,所以必须靠光互联才能把距离从几厘米拉到几十米。

个人看法:先找瓶颈。这篇文章说的瓶颈很具体,不是 GPU 不够,而是三件事叠在一起:HBM 容量有限且供给紧张(和之前 [美光桃园 HBM/DRAM 晶圆厂因劳资纠纷暂停施工](2026-11-08-ongoing-labor-dispute-sees-micron-pause-construction-at-its-4-5bn-memory-fab-in-.md) 是同一条供应链)、HBM 被单块 GPU 独占导致利用率低、以及跨机架搬数据的能耗。解决这个瓶颈的那一层才是真正受益方:第一层是光互联芯片,Marvell 本身,以及 Broadcom、Coherent、Lumentum 这类光模块和硅光厂商,scale-up 网络从铜走向光是确定性方向,只是节奏未定;第二层是内存本身,HBM 和 DDR5 的需求不会因为"共享"而减少,反而因为长上下文和 Agent 被放大,SK hynix、Samsung、Micron 继续受益;第三层是系统集成商,Penguin 这类把光互联、内存和服务器做成可交付设备的公司,但这一层壁垒最低,能不能吃到利润取决于有没有大客户落地。我会把它挂在 AI 板块,机制是推理和 Agent 的扩张把内存墙变成了下一个必须花钱解决的瓶颈。能耗的部分(每比特能耗降到四分之一)对能源板块只是间接的效率改善,不足以单独挂。

这和 [NVIDIA 在 SC26 讲 Agent 需要实验室](2026-11-17-nvidia-at-sc26-agents-are-the-new-scientists-and-they-need-a-lab.md) 是同一个背景:Agent 带来的 token 量才是推动基础设施重构的力量。另一个对照是 [Q.ANT 的混合光子 GPU](2026-11-17-q-ant-demonstrates-hybrid-photonic-gpu-system-for-language-models.md),那边是用光做计算,这边是用光搬数据,后者离商业化近得多。现在还处在展会演示和赞助访谈阶段,值得关注的是有没有大型云厂商或 AI 实验室公开采用这类共享内存设备,以及 NVIDIA 自己的 NVLink 路线会不会把光学内存池纳入进来,如果 NVIDIA 自己做,第三方集成商的空间会被大幅压缩。
