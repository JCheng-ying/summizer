# AI cloud startup Marlowe secures $277m in seed funding
https://www.datacenterdynamics.com/en/news/ai-cloud-startup-marlowe-secures-277m-in-seed-funding/

这条新闻背后的命题是:推理时代的 AI 云,资本开始押注"多芯片"而不是"只买 NVIDIA"。一家成立半年的公司拿到 2.77 亿美元种子轮,而它的卖点不是拿到了多少 H100/B300,而是用 AMD 和 Etched 这类非 NVIDIA 芯片按工作负载定制推理算力——这说明一级市场认为推理成本(每瓦 token 数)已经成为比训练算力更值钱的瓶颈。

文章指出,Marlowe 由两位前微软副总裁 Dan Lewis 和 Kutta Srinivasan 创立,2026 年 5 月正式成立,现在带着 2.77 亿美元种子轮走出隐身状态,领投方包括 Accel、Bessemer、Altimeter、Atreides、Eclipse、Journey、Valor 等。公司把自己定位为"multi-silicon AI factory",CEO Lewis 的逻辑是:AI 算力需求超过供给,专门为推理设计、利用新兴芯片的基础设施可以在不牺牲性能的前提下更高效、更便宜地提供算力,具体做法是针对每个工作负载协同设计算力,以提升每瓦 token 数。

目前 Marlowe 已与 AMD 和 Etched 签了算力合作:和 AMD 合作是为客户提供 Helios 机架级系统,和 Etched 合作是做其"frontier inference clusters"最早的生产站点之一。公司有两个项目已签约,第一个预计几个月内上线,第二个计划在 2027 年上半年;还有三家推理客户签了算力承购(offtake)。Lewis 还提到正在推进的项目会用到 AMD、Etched、Broadcom 等公司的技术。交付形态从 IaaS 到"Tokens-as-a-Service"都可以。但数据中心选址和部署规模都还没有公布。

个人看法:这和之前写的 [推理已占 AI 工作负载三分之二](2026-11-21-inference-now-drives-two-thirds-of-ai-workloads-changing-where-chips-get-deploye.md) 以及 [Fractile 融资 7.2 亿美元做推理芯片](2026-11-11-british-inference-chip-developer-fractile-raises-720m-in-funding.md) 是同一条线索:推理负载占比上去以后,算力的竞争维度从"谁有最多 GPU"变成"谁的每 token 成本最低"。在训练时代,NVIDIA 的 CUDA 生态几乎是唯一选择;推理负载更标准化、对成本更敏感,才给了 AMD、Etched 这类替代芯片空间。而之前 [NVIDIA 说明何时会继续为 neocloud 提供融资](2026-11-18-nvidia-clarifies-when-it-will-and-won-t-keep-financing-neoclouds.md) 那篇也提示,很多 neocloud 是靠 NVIDIA 的融资和供货关系起家的,Marlowe 这种公开站在"多芯片"一边的新玩家,算是 neocloud 的另一种打法。

先找瓶颈:Marlowe 自己说的瓶颈是"需求超过供给",但更准确地说,卡住的是三件事。第一是芯片供给——NVIDIA 高端 GPU 仍然紧张,替代芯片能让新玩家绕过排队;第二是电力——每瓦 token 数直接决定在有限电力下能卖出多少算力,这是协同设计真正的价值;第三是客户承购,三家 offtake 客户是这笔种子轮能这么大的关键。受益的层次会是:第一层是非 NVIDIA 推理芯片,AMD(Helios 机架)和 Etched(专用 Transformer ASIC)直接拿到了生产部署机会;第二层是网络与互联,Broadcom 的以太网交换和定制芯片在多芯片架构里更重要,因为不同芯片要靠开放网络而不是 NVLink 连接;第三层才是 Marlowe 这样的云运营方。我把这条挂在 AI 板块上。但需要冷静的是,现在既没有选址,也没有部署规模,2.77 亿美元对建数据中心来说并不多,大部分算力很可能还需要后续债务融资。值得跟踪的信号是第一个项目上线时公开的规模和实际每 token 成本,以及 Etched 芯片在生产环境里的真实表现。
