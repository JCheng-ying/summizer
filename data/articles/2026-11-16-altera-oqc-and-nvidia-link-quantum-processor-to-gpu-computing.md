# Altera, OQC and NVIDIA Link Quantum Processor to GPU Computing
https://thequantuminsider.com/2026/11/16/altera-oqc-and-nvidia-link-quantum-processor-to-gpu-computing/

(说明:这篇是 Altera 的公司新闻稿,三家公司都是利益相关方,下面关于密度、功耗、延迟的说法属于厂商表述,未经独立验证。)

这条新闻背后更大的命题是:量子计算机规模化的瓶颈,正在从"量子比特本身"往"围绕量子比特的经典控制系统"转移。一台超导量子计算机除了稀释制冷机里的芯片,外面还有成排的射频链路、数模/模数转换器和互联设备,每加一个量子比特,控制硬件就要跟着加。如果控制层不能变得更密、更省电、更低延迟,量子比特数量涨得再快也塞不进机房。

文章指出,Altera 与 Oxford Quantum Circuits(OQC)、NVIDIA 合作开发了一套基于 FPGA 的端到端量子系统控制器参考设计,核心是 Altera 的 Agilex 9 Direct RF FPGA。这里可以拆成三层来看。第一层是 FPGA 本身:芯片内集成了模数和数模转换器,控制和读出信号不再需要外部的射频上变频/下变频,再通过频分复用让多个读出通道共用一个射频端口,目的是减少系统扩展时额外的射频硬件。第二层是 OQC 的射频调理电子和新一代 QPU,FPGA 在这里实时执行量子比特控制、谐振腔读出和谱学测量,并在各功能之间做同步调度。第三层是 GPU:FPGA 通过 NVIDIA NVQLink 连到 GPU,由 GPU 承担校准和基于机器学习的读出分类这类计算量大的任务,CUDA 函数反过来驱动 FPGA 上的 QPU 系统逻辑。参考设计还带一条仿真路径,开发者可以在没有真实量子硬件时先把控制器跑起来。三家会在芝加哥 SC26 展示,参考设计预计 2027 年 1 月发布。

个人看法:这篇和之前 [Atom Computing 拿到商务部 1 亿美元研发资助](2026-11-13-atom-computing-finalizes-100-million-u-s-department-of-commerce-r-d-award.md) 里我提到的判断是同一条线——量子计算机最终大概率会作为 AI/HPC 数据中心里的一个加速器存在,NVIDIA 的 CUDA-Q 和 NVQLink 就是在抢这一层的编排接口。和 [Oak Ridge、IBM、AMD 的量子协同设计平台](2026-11-05-oak-ridge-national-laboratory-ibm-and-amd-launch-new-co-design-platform-for-quan.md)、[PsiQuantum 与 AMD 扩大合作](2026-11-12-psiquantum-and-amd-expand-partnership-on-quantum-computing-infrastructure.md) 放在一起看,GPU 厂商都在争当"量子 + 经典"混合系统的经典那一半。

按"先找瓶颈再找解决瓶颈的那一层"来拆,量子计算板块当下的工程瓶颈之一是控制电子学的体积、功耗和反馈延迟,解决这一层的受益者大致有三类:第一是 FPGA 和高速数据转换芯片厂商,这里是 Altera,同类还有 AMD(Xilinx 的 RFSoC 早就被很多量子实验室用作控制板);第二是专门做量子控制栈的公司,比如 Quantum Machines、Qblox、Zurich Instruments,参考设计降低了门槛,对它们既是生态扩大也是竞争;第三是 GPU 和互联,NVIDIA 通过 NVQLink 把"校准、读出分类、未来的实时纠错解码"这类经典计算吸到 GPU 上,对 AI 板块算是一个很小的增量需求,更多是生态位置的意义。对 OQC 这样的 QPU 厂商来说,好处是可以少做一点控制硬件、把精力放回量子比特本身。

不过这毕竟是一份参考设计新闻稿,没有给出任何量化指标(比如每个量子比特的功耗或反馈延迟具体降了多少)。值得跟踪的是 2027 年 1 月正式发布后,有没有 OQC 以外的 QPU 厂商采用这套设计,以及实时纠错解码是否真的跑在 GPU 上——那才说明 NVQLink 这一层变成了事实标准,而不只是又一个合作演示。
