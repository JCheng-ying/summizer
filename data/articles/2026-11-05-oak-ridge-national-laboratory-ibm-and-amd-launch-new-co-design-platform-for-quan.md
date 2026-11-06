# Oak Ridge National Laboratory, IBM And AMD Launch New Co-Design Platform for Quantum Error Correction
https://thequantuminsider.com/2026/11/05/oak-ridge-national-laboratory-ibm-and-amd-launch-new-co-design-platform-for-quantum-error-correction/

这是 IBM、橡树岭国家实验室(ORNL)和 AMD 的联合新闻稿。它点出的命题是:量子纠错下一阶段的瓶颈,有很大一部分在经典计算那一边。量子计算机越接近实用,需要配套的 GPU 和 CPU 就越多。

文章指出,三方推出了一个量子纠错协同设计平台,首个部署把 IBM 的量子计算机(包括 120 比特的 Nighthawk 处理器)和 ORNL 的 Umbra 高性能计算系统放在一起,Umbra 使用 AMD Instinct MI355X GPU 和第五代 EPYC CPU,负责纠错解码优化和软件编排。这项工作对应美国能源部 Quantum Genesis Mission 的目标:到 2028 年底实现 100 个逻辑比特运行 10 万次困难操作。文章给出的现状是,IBM 已演示最多 70 个逻辑比特、438 次困难操作,也就是还需要约 230 倍的提升。平台还会连接 ORNL 的领导力计算设施,让量子、AI 和高性能计算一起演进。

这里的技术逻辑值得说清楚。纠错的做法是用很多物理比特编码一个逻辑比特,不断测量"症状",再由经典计算机实时解码出哪里出错、如何修正。比特越多、速度越快,解码的计算量就越大,而且必须在量子比特退相干之前完成,所以这本质上是一个低延迟、高吞吐的经典计算问题。

个人看法:和同一天的 [IonQ 把量子机接入 NVIDIA 超算](2026-11-05-ionq-raises-revenue-forecast-as-quarterly-sales-climb-to-173-8-million.md) 放在一起看,量子-经典混合已经是行业共识,区别只是选 NVIDIA 还是 AMD 的 GPU。所以量子计算板块的受益层次是:第一层是量子硬件本身,IBM 是超导路线里纠错进展最公开的;第二层是做解码和控制的经典算力,AMD 在这里拿到了一个具体的落脚点,这也是 AI 板块 GPU 层的一个新增需求;第三层是控制电子学和编排软件。我认为这对量子计算板块是偏利好的,但 230 倍的差距要在两年内追上,难度很大。值得跟踪的是 2028 年前 IBM 在 Quantum Advantage Tracker 上的困难操作数怎么变化。
