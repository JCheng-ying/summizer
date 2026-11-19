# AI’s next build-out: Inference racks that resize themselves for every new model
https://siliconangle.com/2026/11/19/memory-pooling-helps-liqid-fix-ai-inference-tokenomics-sc26/

先说明利益相关:这篇是 SiliconANGLE 旗下 theCUBE 在 SC26 上对 Liqid 联合创始人兼 CTO Sumit Puri 的访谈,原文披露这一段由 Liqid 赞助,所以下面关于 Liqid 技术效果和市场判断的说法都属于厂商自述,未经独立验证。

这篇文章背后更大的命题是:当 AI 从训练转向推理,数据中心的硬件形态可能也要从"固定配比的服务器"转向"按需拼装的资源池"。原因很简单,训练集群可以针对一个已知的大模型精心设计,但推理端面对的是不断更新、大小各异的模型,六个月后要部署什么模型谁也不知道。

文章指出,今天大多数 AI 服务器出厂时 GPU 和内存的配比是固定的,并且在整机生命周期内都不会变,Puri 认为这和推理负载的不确定性很不匹配。Liqid 的思路是把 GPU 和内存从服务器里拿出来,放进机架级的资源池,再根据要部署的模型或负载,动态地分配给需要它们的服务器。文章提到 Liqid 用"tokenomics"来衡量回报,标准是每秒 token 数、每瓦 token 数,最重要的是每美元 token 数。Puri 还提出,内存是 AI 基础设施里供应最紧张的部件之一,如果能做到内存池化、共享,并按应用需要的量精确分配,就能直接缓解一部分供应链问题。此外,Liqid 在 SC26 上发布了 Liqid as a Service(全托管、单租户),并在走向预配置一体机,背后的判断是大多数企业会部署模型而不是自己训练模型,因此需要自己的专属算力。

这里可以把"内存池化"拆成三个技术层面来理解:第一是互联层,要把内存和 GPU 从主板上解耦,需要 PCIe 或 CXL 这类低延迟的机架级互联,这决定了池化之后性能损失有多大;第二是编排层,也就是谁来决定什么时候把哪块资源分配给哪台服务器,这本质上是软件;第三是商业模式层,也就是文章里提到的托管服务和一体机。原文没有给出任何具体的性能或节省数据,所以"能提高多少每美元 token 数"目前只是方向性的说法。

个人看法:这篇和之前那篇 [AI 隐性能耗税:超过 80% 的 scale-up 流量只是在搬运内存](2026-11-18-ai-s-hidden-energy-tax-more-than-80-of-scale-up-traffic-is-just-memory-moving-ar.md) 正好是同一个问题的两个侧面——推理时代真正的瓶颈越来越像是内存,而不是 GPU 算力本身。再加上 [Nanya 和 Winbond 采购 EUV 设备扩产 DRAM](2026-11-16-nanya-and-winbond-to-purchase-euv-tools-from-asml-to-boost-dram-production-in-ta.md) 和 [Micron 内存晶圆厂因劳资纠纷暂停建设](2026-11-08-ongoing-labor-dispute-sees-micron-pause-construction-at-its-4-5bn-memory-fab-in-.md),可以看到内存供给侧也确实很紧。

先找瓶颈:推理端的瓶颈是内存的供给和利用率。解决这个瓶颈的路径目前有三种:1. 多生产内存,也就是 SK Hynix、Samsung、Micron 扩产;2. 让每块内存用得更满,也就是 Liqid 这类池化和组合式基础设施;3. 让模型本身少用内存,比如量化、KV cache 压缩。受益的层次会是:第一层仍然是存储芯片厂商,不管哪种方式胜出,总需求都在上升;第二层是机架级互联,CXL 交换芯片和 PCIe 交换芯片供应商(比如 Broadcom、Astera Labs)是池化方案能否落地的前提;第三层才是 Liqid 这样的编排软件和系统集成商,它们的价值取决于池化能带来的利用率提升能不能抵消额外互联的成本和延迟。所以这篇主要挂在 AI 板块上,因为它讨论的是 AI 推理基础设施的效率问题;如果"每家企业都有自己的 token 机器"这个判断成立,本地化部署会变多,也会对 edge AI 板块有一定带动,但这一点目前更像是厂商愿景。

现在还在观望阶段。值得关注的信号是:有没有第三方或者大客户公开池化方案在真实推理负载下的利用率和每美元 token 数提升,以及 Nvidia、Dell 这类主流服务器厂商会不会在标准产品里引入类似的机架级内存池化设计——如果主流厂商自己做了,独立的池化厂商的空间就会被压缩。
