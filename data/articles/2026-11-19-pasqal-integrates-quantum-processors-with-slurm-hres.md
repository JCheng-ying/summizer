# Pasqal Integrates Quantum Processors with Slurm HRES
https://thequantuminsider.com/2026/11/19/pasqal-integrates-quantum-processors-with-slurm-hres/

这篇是 Pasqal 的新闻稿(公司自述,利益相关),但它碰到的是量子计算商业化里一个经常被忽略的问题:量子计算机就算算得对,超算中心也要能把它"排进日程"。今天的超算中心是靠作业调度器运转的,一台设备如果不能被调度器识别、分配、回收,它就只能作为一个旁边单独登录的"孤岛"存在,用户需要另外开会话、另外排队,运维团队也要另外维护一套流程。文章讨论的就是把 QPU 变成调度器里"又一种资源"这一步。

文章指出,NVIDIA 在 SC26 上发布的 Slurm 26.11 新增了 Hierarchical Resources(HRES)能力,允许把 QPU 作为分层资源来寻址;Pasqal 则扩展了自己的 HPC-QC 混合平台,让 HRES 原生管理它的 QPU。具体来说,Slurm 可以检查 QPU 是否空闲、调度作业、管理访问权限并自动释放资源,用户可以在同一个工作流里组合 CPU、GPU 和 QPU,不用单独管理量子会话。这里要拆清楚三层东西:第一是接口层,也就是 2025 年 Pasqal 与 IBM、Rensselaer Polytechnic Institute、STFC Hartree Centre 一起开发的 Quantum Resource Management Interface(QRMI),它是厂商中立的,所以同样的方法也适用于 IBM 的处理器;第二是调度层,过去通过 QRMI 接 Slurm 要靠核心之外的自定义插件,现在借助 HRES 更接近 Slurm 原生架构,文章认为超算中心要维护的外部代码更少、集成风险更低,而且相比 Slurm 标准的通用资源模型和动态许可证,HRES 更适合在多用户、多作业之间共享量子计算机这种稀缺资源;第三是编程层,用户可以用 Pasqal 开源的 Pulser、QoolQit 和 QUBO 求解器等库,或者用 NVIDIA CUDA-Q(Pasqal 已在其中加入自家设备的仿真)。文章也说明了验证程度:这套架构目前是在模拟的本地 QPU 环境和 Pasqal Cloud 上验证通过的,真实落地还在意大利超算中心 CINECA 推进,通过 Pasqal 的开源中间件 Warden 和 QRMI,把 QPU 接到它现有的超算上。

这和读者熟悉的 GPU 历史很像。GPU 进超算中心并不是因为某一天算力突然够了,而是因为 Slurm 这类调度器里出现了 GRES(通用资源)对 GPU 的支持,CUDA 和各种库又让程序员不用关心底层,GPU 才从"实验卡"变成了集群里的标准配置。QPU 现在走的是同一条路,只是更早期。

个人看法:这几周关于量子与超算融合的新闻已经很密集,可以放在一起看出一个框架。目前让 QPU 进入数据中心大概有三条路径:1. 物理层托管,比如 [Diraq 把硅自旋量子计算机装进 Equinix 商业数据中心](2026-11-09-diraq-deploys-silicon-spin-quantum-computer-inside-a-commercial-data-center.md),解决的是供电、散热、安防和机房运维;2. 低延迟互联层,比如 [Altera、OQC 和 NVIDIA 把量子处理器接到 GPU 计算上](2026-11-16-altera-oqc-and-nvidia-link-quantum-processor-to-gpu-computing.md) 和 [IBM、NVIDIA 与 Fermilab 的模块化平台](2026-11-16-ibm-nvidia-and-fermilab-plan-modular-quantum-computing-platform.md),解决 QPU 和 GPU 之间的数据往返;3. 软件调度层,也就是这篇的 Slurm HRES,以及 [Qudora 集成 CUDA-Q](2026-11-17-qudora-integrates-nvidia-cuda-q-into-its-quantum-software-development-kit.md) 这类编程框架统一。前两条解决的是"能不能接上",第三条解决的是"超算中心愿不愿意天天用"。

先找瓶颈。量子计算现在卡住的不只是保真度和比特数,还有"采购后怎么用"——超算中心买一台 QPU,如果利用率低、需要专人维护单独的排队系统,这笔采购就很难复制。这篇解决的正是利用率和运维成本这个瓶颈,所以受益的层次是:第一层是掌握调度和编程入口的 NVIDIA,它通过扩展 Slurm 和推广 CUDA-Q,在量子路线还没分出胜负之前就占住了混合计算的软件入口,和它在 GPU 上的打法完全一致,不管最后中性原子、超导还是离子阱胜出,调度和编程层都绕不开它;第二层是像 Pasqal、IBM 这样主动做开放接口的硬件厂商,QRMI 这种厂商中立的接口降低了超算中心的试用门槛,也让多模态采购成为可能,但同时也意味着硬件本身更容易被替换,竞争会回到性能和价格上;第三层是超算中心和 HPC 集成商,它们的工作从"维护一个孤岛"变成"把 QPU 当成一种资源池运营"。这对量子计算板块是偏基础设施的利好,对 AI板块 的联系在于 GPU 仍然是混合工作流里的主力,NVIDIA 的软件生态在量子这一侧继续延伸。

需要克制的是,这还只是模拟环境和云上的验证,CINECA 的真实集成还没完成,而 Pasqal 自己 [第三季度收入下滑、QPU 服务收入增长](2026-11-08-pasqal-reports-third-quarter-revenue-decline-as-qpu-services-revenue-grows.md) 的财报说明商业化仍在早期。值得跟踪的信号是 CINECA 等超算中心后续有没有公布 QPU 的实际排队和利用率数据,这比任何比特数都更能说明量子是否真正进入了日常 HPC 运营。
