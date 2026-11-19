# D-Matrix bets stacked DRAM can solve inference’s memory bandwidth problem
https://siliconangle.com/2026/11/19/raptor-chip-stacks-3d-dram-tackle-inference-memory-limits-sc26/

(利益相关说明:这是 theCUBE 在 SC26 的厂商访谈,受访者是 d-Matrix 的 fellow,节目片段由 NYSE Wired 赞助。文中的能效、带宽和利用率数字均为厂商说法,未经独立验证。)

这篇访谈触及的是推理时代最核心的硬件约束:生成 token 的速度主要不取决于算力,而取决于能多快地把模型权重和 KV cache 从内存搬到计算单元。如果能在 SRAM 和 HBM 之间插入一个新的内存层级,推理芯片的设计空间就会被重新打开,HBM 一家独大的格局也可能出现松动。

文章指出,d-Matrix 的做法是先用测试芯片验证每一项高风险技术:Jayhawk 验证了芯片间(die-to-die)互连,Jayhawk II 验证了数字存内计算,两者结合的 Corsair 加速器今年早些时候进入全面量产;现在的测试芯片 Pavehawk 在验证把 3D DRAM 堆叠在逻辑芯片下方,这是明年推出的第二代芯片 Raptor 的核心技术。受访者 Satyam Srivastava 解释,堆叠保留了分布式内存架构,但把存储单元放到单独一层,不占用逻辑芯片面积,数据传输距离很短,也不经过中介层(interposer)。他把这种 3D DRAM 定位成介于 SRAM 和 HBM 之间的新层级,称其能效和带宽都是 HBM 的 10 倍,容量则介于两者之间。另外两个说法也值得注意:第一,把基于 Corsair 的服务器和现有 Hopper GPU 集群搭配使用,可以把利用率从约 20% 提高到最多 80%,也就是每美元产出更多 token;第二,d-Matrix 采用了英伟达的 NVLink Fusion 机架级基础设施,把自家加速器接入英伟达的 AI 工厂,受访者说这让他们能进入"世界上最流行的 AI 工厂"生态,并拿到成熟的 MGX 机架设计。他的整体判断是,AI 基础设施已经不是芯片问题,而是内存带宽、能效、互连和软件一致性的系统问题,未来会走向异构计算,由软件把 GPU、CPU 和 ASIC 加速器当作一个系统来编排,集群本身成为计算单元。

个人看法:这篇和 [超过 80% 的 scale-up 流量只是在搬运内存](2026-11-18-ai-s-hidden-energy-tax-more-than-80-of-scale-up-traffic-is-just-memory-moving-ar.md) 讲的是同一个瓶颈的两端:那篇说数据搬运吃掉了大量能耗,这篇则是从芯片设计上缩短搬运距离。今天的 [Axelera 风冷推理服务器](2026-11-19-ai-inference-servers-shrink-to-fit-the-air-cooled-racks-enterprises-already-run.md) 也是走存内计算路线,两家放在一起看,推理芯片创业公司的共识已经很明显——和训练不同,推理的瓶颈在内存墙。

更有意思的是 NVLink Fusion 这一点。英伟达把自己的机架互连开放给第三方加速器,看起来是在给竞争对手开门,但实际上是把异构计算的"系统层"留在自己手里:d-Matrix 这类公司负责解决某一段工作负载(比如解码阶段)的内存带宽问题,机架、互连和整个 AI 工厂的生态仍然是英伟达的。这和 [英伟达财报复盘](2026-11-19-what-we-learned-from-nvidia-s-first-earnings-call-without-jensen-huang.md) 里"英伟达的护城河是系统不是芯片"的判断是一致的。

所以按"先找瓶颈,再找解决瓶颈的那一层"来拆 AI板块,受益层次会是:第一层是内存本身,不管最后是 HBM 继续升级,还是 3D 堆叠 DRAM 这种新层级出现,内存带宽都是推理的核心约束,SK Hynix、Samsung、Micron 这些 DRAM 厂商是确定性最高的一层,而 3D DRAM 和逻辑芯片的混合键合还会带动先进封装和键合设备;第二层是英伟达的互连和机架生态,NVLink Fusion 让第三方加速器也成为英伟达系统的一部分,异构化程度越高,英伟达作为"系统集成平台"的地位反而越稳;第三层是能把异构集群编排起来的软件层,集群变成计算单元之后,调度和编排软件的价值会上升。对 d-Matrix 这类创业公司本身,我会更谨慎——10 倍于 HBM 的能效和带宽,以及利用率从 20% 到 80% 的提升,都是厂商在赞助访谈里给出的数字,没有说明测试条件。

现在 Raptor 还要到明年才推出,Pavehawk 仍是测试芯片。值得跟踪的是 Raptor 的实际量产时间和第三方基准,以及 NVLink Fusion 接入的第三方加速器里有没有出现大规模的云厂商订单。
