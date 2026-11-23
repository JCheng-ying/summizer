# Amazon snaps up Decart’s AI optimization tech for $7.5B as it prepares to sell Trainium chips
https://techcrunch.com/2026/11/23/amazon-snaps-up-decarts-ai-optimization-tech-for-7-5b-as-it-prepares-to-sell-trainium-chips/

这笔收购背后的命题是:自研 AI 芯片想挑战 Nvidia,最贵的部分可能不是芯片本身,而是让客户愿意把工作负载搬过来的那一层软件。Amazon 花 75 亿美元买的不是一个模型、也不是一条产品线,而是一套让模型在不同硬件上跑得更高效的优化栈。如果这个判断成立,那么未来 AI 芯片竞争的核心战场,会从晶体管和制程更多地转移到编译器、运行时和优化工具上。

文章援引 Bloomberg 指出,Amazon 同意以 75 亿美元收购以色列初创公司 Decart 的很大一部分。Decart 以实时交互式世界模型(最新是 Oasis 3)和 AI 视频生成工具出名,但文章认为它真正与众不同的是底层的 Decart Optimization Stack(DOS),这套软件能让 AI 模型在 Nvidia、Amazon 和 Google 的硬件上高效运行。按 Amazon 的博客,交易内容包括 DOS 背后的技术,以及 Decart 的创始团队和 AI 研究、工程团队。Amazon 负责基础 AI 模型、定制芯片和量子计算的 SVP Peter DeSantis 说,AI 的每一次飞跃都始于从每块芯片里榨出更多性能,更高效的计算意味着更好的训练、强化学习、更快的推理,以及更低成本的更好模型。文章还指出,Amazon 此前一直只在自己的数据中心里使用 Trainium 芯片,现在准备开始对外出售,和 Nvidia 竞争,而 Decart 的技术可以让客户更容易把负载跑在 Amazon 的芯片上,而不是一直以来作为黄金标准的 Nvidia 上。

值得注意的是收购的结构:买的是技术和团队,而不是整家公司,世界模型和视频生成业务的归属文章没有说清楚。这种"收购式招聘加技术授权"的做法,和过去两年几家大厂对 AI 初创公司的交易方式很像,通常也是为了绕开完整并购的审查周期,但这篇文章本身没有涉及监管问题,只能算推测。

个人看法:这篇文章和 [Luminal 挑战 CUDA 护城河那篇](2026-11-12-with-23m-in-funding-luminal-is-the-latest-startup-to-put-nvidia-s-cuda-moat-in-i.md) 是同一条线索的两个阶段。那篇文章说 Nvidia 真正的护城河是 CUDA,几乎所有框架都原生构建在 CUDA 上,换芯片就得重写代码;Luminal 用搜索式编译器去解决,而且相当一部分负载就跑在 AWS 的 Trainium 上。Decart 的 DOS 本质上是同一类东西,只是 Amazon 这次选择直接把它买下来、内化成 Trainium 生态的一部分。所以先找瓶颈:Trainium 对外销售卡住的不是算力指标,而是迁移成本,也就是客户的模型和代码都是围绕 CUDA 写的。谁在解决这个瓶颈,谁就是这一层真正的受益方。

目前来看,挑战 Nvidia 的路径大概有三种:第一是做更好的芯片,比如各家推理芯片初创公司和 [Fractile 那篇](2026-11-11-british-inference-chip-developer-fractile-raises-720m-in-funding.md) 里的思路;第二是做硬件无关的编译和优化层,比如 Luminal、Spectral Compute,以及现在的 Decart DOS;第三是云厂商自己把芯片、软件和云服务打包,用价格和可得性抢客户,Google 的 TPU 和现在的 Trainium 都是这条路。Amazon 这次实际上是把第二种并入第三种。受益的层次会是:第一层是 Trainium 的供应链,包括为 Amazon 做 ASIC 设计服务的 Marvell 和 Alchip、负责代工和先进封装的台积电,以及 HBM 供应商,如果 Trainium 真的开始对外卖,这些订单会超出 Amazon 自用的规模;第二层是 AWS 本身,芯片对外销售会让它从"租算力"变成"卖算力和卖芯片"两条腿;第三层是剩下的独立编译器和推理优化公司,这笔 75 亿美元的价格给它们做了一次估值锚定,Luminal 这类公司被大厂收购的可能性也随之上升。对 Nvidia 来说,短期影响很小,它的供给仍然不够卖,但长期看 CUDA 护城河在被一点点侵蚀,而侵蚀它的恰恰是它最大的几个客户。

这篇文章主要挂在 AI 板块上,机制是 AI 算力供给的多元化和推理成本下降。Decart 的实时世界模型如果能留在 Amazon 内部继续发展,对机器人板块其实也有间接意义,因为交互式世界模型是机器人仿真训练的一个方向,但文章没有说世界模型业务会怎么处理,所以这一点只能观望。值得跟踪的是 Trainium 第一批对外客户是谁、什么价格,以及 DOS 会不会以开发者工具的形式公开出来。
