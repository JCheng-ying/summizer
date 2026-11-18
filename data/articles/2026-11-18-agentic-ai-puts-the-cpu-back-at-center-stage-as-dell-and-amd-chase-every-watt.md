# Agentic AI puts the CPU back at center stage as Dell and AMD chase every watt
https://siliconangle.com/2026/11/18/business-development-agentic-ai-era-puts-cpus-first-dellatsc26/

先说明利益相关:这是 SiliconANGLE 在 SC26 上的 theCUBE 访谈,这一段由 Dell 赞助,受访者是 AMD 和 Dell 的高管,文中关于服务器能效和整合比例的数据都来自厂商自己,未经独立验证。但它提出的命题值得认真对待:在 Agent 时代,CPU 可能重新成为数据中心的瓶颈之一,而不是 GPU 的配角。如果这个判断成立,AI 基础设施的受益面会从 GPU 扩展到服务器 CPU,数据中心的功耗分配逻辑也会跟着变。

文章指出,这个变化已经酝酿了好几年。AMD 负责 HPC 和主权 AI 业务拓展的副总裁 Scott Tease 表示,客户在一个 CPU 上挂越来越多的 GPU 后发现,CPU 喂不饱昂贵的加速器,导致 GPU 闲置;而且 Agent 本身不完全是 GPU 的事,它会非常吃 CPU,因为既要快,又要高并发。文章提出,功耗依然是最硬的约束:Dell 在两年半前规划产品线时,企业客户预测单机柜功率会维持在 15 到 20 千瓦,而且经常在机柜还没放满之前就先用完了电。Dell 的回应是 PowerEdge R9825,一台基于 AMD 第六代 EPYC 9006 的 3U 服务器。Dell 的 David Schmidt 称,一台 EPYC 9006 服务器可以替换 13 台老机器,同时把用于散热的系统功耗降低 80%,省下来的电可以还给客户。Tease 则认为,这部分回收的电力会被 Agent 工作负载吃掉,因为 Agent 可以把一个研究员的想法变成成千上万个计算任务,"研究员数量不变,但算力需求大幅增加"。

把这个逻辑拆开看,Agent 对 CPU 的需求来自三个地方:第一是编排,Agent 的规划、调度、工具调用、API 请求和代码执行大多是分支密集、并发量高的通用计算,不适合 GPU;第二是数据搬运,GPU 训练和推理前的数据预处理、检索、KV cache 管理都需要 CPU 和内存带宽;第三是数量放大,单个 Agent 可能并不重,但一个任务会拆成成千上万个子任务,累积起来就是大量 CPU 核时。这和风格参考里那篇 Stroop Test 文章提到的方向一致:为了弥补 Transformer 缺乏长期目标保持能力,行业在模型外面套 Planner、Scheduler、Supervisor 这些管理层,而这些管理层恰恰主要跑在 CPU 上。

个人看法:这篇文章和之前写过的 [AMD 发布面向 AI Agent 工作负载的 EPYC 6 处理器](2026-11-10-amd-introduces-epyc-6-processors-for-ai-agent-workloads.md) 是同一个叙事的延续,AMD 在明确把"Agent 需要 CPU"当作新的增长故事来讲;Dell 这边也和 [Dell 把集群管理从服务器层移到机架层](2026-11-18-scripts-can-t-run-ai-factories-dell-moves-cluster-management-from-the-server-to-.md) 一起构成了它在 SC26 的整体定位。按"先找瓶颈"的方法看,这里的瓶颈不是 CPU 算力本身,而是机柜功率预算:企业机房里 15 到 20 千瓦的上限是固定的,谁能在同样功率里塞进更多有效算力,谁就受益。所以受益的层次会是:第一层是服务器 CPU 厂商,AMD EPYC 是直接受益者,Intel Xeon 和基于 Arm 的 Nvidia Grace、AWS Graviton 也在争同一块市场,这是 AI 板块里过去被 GPU 光环遮住的一部分;第二层是做服务器整机和替换周期的 Dell、HPE、Supermicro,"一台换十三台"如果属实,本质上是一个由能效驱动的换机周期;第三层是能效与散热,省下来的散热功耗本身就是能源板块的逻辑,也和前面写的液冷、电源管理那条线相连。

但也要保持谨慎,"Agent 很吃 CPU"目前更多是厂商的叙事,还缺少独立的工作负载数据支撑,而且这段访谈是赞助内容。值得跟踪的信号是接下来几个季度 AMD 和 Intel 的数据中心 CPU 收入增速,是否真的出现和 GPU 收入脱钩的单独加速,如果出现,才说明 Agent 带来的 CPU 需求是真实存在的增量。
