# With $23M in funding, Luminal is the latest startup to put Nvidia’s CUDA moat in its crosshairs
https://siliconangle.com/2026/11/12/with-23m-in-funding-luminal-is-the-latest-startup-to-put-nvidias-cuda-moat-in-its-crosshairs/

Nvidia 真正的护城河从来不是 GPU 本身,而是 CUDA 这一层软件生态。这篇文章讨论的是另一种拆护城河的方式:不去造更好的芯片,而是让模型在任何芯片上都能跑得一样快。

文章指出,Luminal 完成 2300 万美元 A 轮融资,由 Standard Capital 领投,Y Combinator、Felicis 等老股东跟投,累计融资超过 2800 万美元。它的产品有两部分:第一是一个"搜索式编译器",系统性地探索神经网络在目标芯片上的各种执行方式,对每种变体做基准测试,找到最优路径后自动生成代码,并缓存实现以便在重复的推理负载中复用;第二是全托管的推理云。文章提到,Luminal 四个月前才上线,目前每月已处理超过 45 万亿 token,大约相当于 Together AI 四年多来累计 token 量的 10%;它与 AWS 合作密切,相当一部分负载跑在 AWS 的 Trainium 上。目标场景是 AI 编程工具、图像和视频生成、实时语音 agent 这类高吞吐、持续在线的推理应用。竞争方面,Google 和 AWS 都在推自家框架,初创公司 Spectral Compute 做 CUDA 代码在其他芯片上原生运行的工具链,开源的 UXL 基金会 OneAPI 也在做类似转换。

文章解释了 CUDA 为什么是护城河:几乎所有主流框架,包括 TensorFlow 和 PyTorch,都原生构建在 CUDA 上,模型在 Nvidia GPU 上不用改就能跑,换到其他芯片则需要大量重写代码。所以哪怕 AMD、Google、AWS 的芯片更便宜,开发者也不愿意花几个月迁移。

个人看法:这和同一天 [Cerebras 拿下微软](2026-11-12-surging-ai-chip-revenue-and-microsoft-deal-boost-cerebras-systems-stock-by-17.md)、[Nvidia CEO 辞职](2026-11-12-nvidia-ceo-jensen-huang-resigns-following-affairs-scandal.md)放在一起,构成了一条完整的线索:替代芯片已经存在,真正卡住它们的瓶颈是软件迁移成本。谁解决这个瓶颈,谁就是"去 Nvidia 化"里杠杆最高的那一层。对 AI板块来说,受益的层次会是:第一层是自研芯片的云厂商(AWS Trainium、Google TPU),编译器越成熟,它们的芯片越容易被外部客户采用;第二层是跨硬件编译器和推理云本身,它们的价值和芯片多样化程度成正比;第三层是推理需求最大的应用层。不过 Luminal 目前规模还很小,2300 万美元在这个赛道里只是入场券。

现在只能观望。值得跟踪的是 Luminal 的 token 量能否在下个季度继续高速增长,以及有没有大模型公司公开把生产负载迁到非 Nvidia 硬件上。
