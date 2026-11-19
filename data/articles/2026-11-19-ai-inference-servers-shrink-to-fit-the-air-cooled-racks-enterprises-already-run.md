# AI inference servers shrink to fit the air-cooled racks enterprises already run
https://siliconangle.com/2026/11/19/power-efficient-inference-chips-let-enterprises-own-ai-hardware-sc26/

(利益相关说明:这是 theCUBE 在 SC26 的厂商访谈,受访者是 Axelera AI 产品负责人,该节目片段由 NYSE Wired 赞助。下面涉及的芯片性能和功耗对比均为厂商说法,未经独立验证。)

这篇访谈背后的命题是:推理算力会不会从"租用云端 GPU"重新回到"企业自有机房"。如果推理硬件能塞进企业已经在用的风冷机柜,那么 AI 推理的部署边界就不再由液冷和百万美元级的 GPU 机柜决定,企业私有部署会成为一个新的需求池。

文章指出,随着 AI 从训练模型转向日常运行模型,昂贵的 GPU 机柜和它们所需的液冷让很多公司只能租用算力,这给挑战者留出了空间。Axelera 原本在边缘侧做低功耗芯片和边缘 AI 开发工具,现在把这套技术带进数据中心。受访者 Manuel Botija 的说法是,企业因为成本和功耗被"锁在外面",无法拥有自己的基础设施。具体产品上,第一,Europa 芯片自 9 月开始出货;第二,SC26 前公司发布了第三代架构 Titania,把设计扩展到 400 瓦单芯片,对应的服务器功率约 6 千瓦,厂商称其性能可对标领先的数据中心 GPU,同时能放进普通企业数据中心现有的 20 到 30 千瓦风冷机柜;第三,技术底座是源自创始人研究的数字存内计算(digital in-memory computing),厂商称这带来了每瓦性能优势。作为对比,受访者称一个 GPU 机柜至少 100 万美元,通常要液冷。他的结论是企业可以把这笔投资摊销掉、降低运营支出。

个人看法:这篇和今天的 [d-Matrix 3D 堆叠 DRAM](2026-11-19-d-matrix-bets-stacked-dram-can-solve-inference-s-memory-bandwidth-problem.md) 、前几天的 [Fractile 融资 7.2 亿美元](2026-11-11-british-inference-chip-developer-fractile-raises-720m-in-funding.md) 是同一条线:推理芯片创业公司都在绕开 HBM 加 GPU 的组合,用存内计算或近存计算换每瓦性能。它也和 [数据中心建设停滞让推理芯片去电信机房找空间](2026-11-18-stalled-data-center-buildouts-send-inference-chips-hunting-for-space-in-telco-an.md) 呼应——当新建机房的电力和液冷成为瓶颈,能塞进存量风冷机柜就成了一种卖点。

按"先找瓶颈"来看,企业自建推理的瓶颈不是芯片算力,而是机柜功率密度和散热:一个现代 GPU 机柜动辄需要液冷和远超 30 千瓦的供电,而大部分企业机房是按风冷、20 到 30 千瓦设计的。所以真正解决问题的是"每瓦性能"这一层,而不是"峰值性能"。从这个角度,受益的层次会是:第一层是低功耗推理芯片本身,Axelera 之外还有 Qualcomm 的 Cloud AI 系列、Hailo 等从边缘起家的公司,这也是我把信号挂到 edge AI板块 的原因——边缘侧积累的低功耗架构正在向上渗透进企业机房;第二层是承接企业私有化部署的服务器 OEM 和系统集成商,比如 Dell、HPE、Supermicro,自有推理需求起来它们是直接出货方;第三层对 AI板块 是需求结构的变化,如果推理大量回流企业自有机房,云端 GPU 租赁的部分增量会被分流,但整体推理 token 的需求仍在扩张。

但要保持谨慎,"性能对标领先数据中心 GPU"是厂商在赞助访谈里的说法,原文没有给出具体基准测试或客户名称,Titania 也还只是发布的架构。值得关注的是 Titania 服务器的第三方基准成绩和首批企业客户落地,尤其是在不改造机房的前提下实际跑大模型推理的案例。
