# OpenAI claims its models have delivered chip design improvements across both in-house and AMD-designed hardware
https://www.datacenterdynamics.com/en/news/openai-claims-its-models-have-delivered-chip-design-improvements-across-both-in-house-and-amd-designed-hardware/

这篇文章背后更大的命题是:AI 开始反过来设计承载它自己的芯片。如果这件事成立,芯片迭代的瓶颈就会从"工程师人力和设计周期"部分转移到"模型能力和算力",硬件和模型之间会形成一个自我加速的闭环——更好的模型设计出更好的芯片,更好的芯片又训练出更好的模型。需要先说明的是,这篇报道的信息来源是 OpenAI 自己的博客,所有数字都是 OpenAI 单方面披露的,AMD 的部分也是"据报道",目前没有第三方独立验证。

文章指出,OpenAI 在 2025 年初用 GPT-o3 mini 参与设计自研推理芯片 Jalapeño,带来了"非平凡"的 PPA(功耗、性能、面积)改进,其中向量单元的标准单元面积减少 13%,矩阵单元减少 10%。在和 AMD 的合作中,文章称相对于"已经高度优化的基线",在旗舰 GPU IP 上实现了最高 14% 的改进;AMD 即将推出的 CPU 在关键模块上也获得了个位数百分比的 PPA 提升。更值得注意的是,文章提到一个未具名的 OpenAI 模型通过重写描述电路的 SystemVerilog RTL 代码找到了进一步改进,OpenAI 称这相当于在不到五个月里完成了一年的进展;据报道 AMD 已经把这些修改放进了一款正在制造阶段的芯片,并计划在未来版本的生产设计文件里加入更多改动。

这里需要把芯片设计流程拆开看,才能理解这些数字落在哪一环。第一是架构定义,决定有多少计算单元、怎样的存储层级;第二是 RTL 设计,用 SystemVerilog 这类硬件描述语言把架构写成可综合的代码;第三是综合与物理设计,由 EDA 工具把 RTL 变成标准单元网表再做布局布线;第四是验证与签核。文章里的"标准单元面积减少"和"重写 RTL"主要发生在第二和第三环,这恰好是最接近"写代码"的部分,也是大模型的 coding 能力最容易迁移过来的地方。换句话说,这本质上是把 Coding Agent 的能力从软件迁移到硬件描述语言,和之前那篇 [GPT-6 Astra 安全调优版找出 Linux root 级漏洞](2026-11-13-openai-s-security-tuned-version-of-gpt-6-astra-closed-root-level-linux-holes-for.md) 是同一条路径:先在某个专业代码领域做针对性调优,再进入真实生产流程。

文章还提到,OpenAI 用 GPT-5.5、GPT-5.5 Sol、GPT-6.1 Sol、GPT-6 Astra、GPT-6.2 Astra 五个模型在两个开源 32 位 RISC-V 核上做测试,一类任务是给出原始硬件描述要求提高吞吐量,另一类是给出书面需求和模板要求从头设计。结果五个模型都在"从需求从头设计"上得分更高,而不是"改进现有设计"。这一点很有意思:修改一个已经被人类高度优化过的设计,需要理解大量隐含的设计约束和历史取舍,模型更容易在这里犯错;而从清晰的需求出发,模型反而能发挥得更好。最后文章指出,OpenAI 将与 Synopsys 合作训练一个新模型 GPT-Synopsys,让模型像芯片工程师一样使用 Synopsys 的 EDA 工具。

个人看法:我理解目前"AI 进入芯片设计"有三种方式:1. 在 EDA 工具内部嵌入 AI 做局部优化(比如布局布线的参数搜索),这是 Synopsys、Cadence 过去几年已经在做的;2. 让大模型直接写和改 RTL,也就是这篇文章里 Jalapeño 和 AMD 的案例;3. 让模型作为 Agent 去操作整套 EDA 工具链,模仿工程师的完整工作流,这就是 GPT-Synopsys 想做的方向。第三种如果成立,影响最大,因为它不是在某一环省几个百分点,而是在压缩整个设计周期。

从投资角度先找瓶颈:今天 AI 芯片的瓶颈之一是设计周期和顶尖芯片工程师的稀缺,一代 GPU 从定义到流片往往要两三年,而模型的迭代周期已经缩短到几个月,这种节奏错配本身就是约束。谁在解决这个瓶颈,受益的层次会是:第一层是 EDA 工具商,Synopsys 是这次被直接点名的合作方,而 Cadence 作为另一家头部 EDA 公司大概率也会被推着走同样的路线,AI 不会绕开 EDA,反而会让 EDA 成为模型的"执行环境",这对 EDA 是加强而不是替代;第二层是 AMD 这类芯片设计公司,如果 14% 的 PPA 提升属实,在同样的工艺节点上就能拿到接近半代工艺的收益,这对一直在追赶 Nvidia 的 AMD 是实打实的竞争工具,也和之前 [AMD 发布面向 Agent 负载的 EPYC 6](2026-11-10-amd-introduces-epyc-6-processors-for-ai-agent-workloads.md) 呼应;第三层是 OpenAI 自身,Jalapeño 的推进意味着它在降低对外部 GPU 的依赖,这和 [OpenAI 与 TensorWave 签下 457MW 算力](2026-11-16-openai-signs-on-for-457mw-ai-capacity-with-tensorwave.md) 一起看,说明它在同时做"多买算力"和"自己造推理芯片"两件事;第四层仍然是算力基础设施,训练和运行这些芯片设计 Agent 本身也需要大量 GPU。所以这篇主要利好 AI 板块,同时推理芯片 PPA 提升、单位功耗下降也会间接利好 edge AI 板块,因为对端侧来说,面积和功耗正是最核心的约束。

但现在还早,所有数字都是 OpenAI 自己的说法,"一年的进展压缩到五个月"这种表述也比较难量化。值得跟踪的信号是:AMD 那颗已经进入制造阶段的芯片流片后,AMD 自己会不会在产品发布时承认并量化 AI 设计的贡献,以及 GPT-Synopsys 是否真的作为商业产品出现在 Synopsys 的工具链里。
