# Inference now drives two-thirds of AI workloads, changing where chips get deployed
https://siliconangle.com/2026/11/21/inference-two-thirds-ai-workloads-chip-deployment-positron-sc26/

先说明利益相关:这篇是 SiliconANGLE 旗下 theCUBE 在 SC26 上对 Positron AI 销售负责人的访谈,该环节由 NYSE Wired 赞助,内容基本是厂商自己的说法,下面的负载比例、功耗和客户数据都应视为未经独立验证。

即便如此,它提出的命题很重要:AI 基础设施的主导负载已经从训练切换到推理。如果这个判断成立,算力投资的逻辑就会从"谁能建最大的训练集群"转向"谁能最快、最便宜地把电力变成可以收费的 token",数据中心的选址、规模和芯片架构都会跟着变。

文章指出,Positron 的 Cameron McCaskill 称,现在 AI 基础设施里约三分之二的负载是推理、三分之一是训练,而 2023 年是 85% 训练、15% 推理,所以推理正在主导基础设施的经济决策。Positron 9 月以 50 亿美元估值融资 8.75 亿美元,第一代 Atlas 服务器基于可编程芯片,计划明年初流片自研芯片用于 Titan 服务器;甲骨文本季度在其云上上线约 340 台 Atlas 服务器,一家 neocloud 也签了 Atlas 并承诺采用 Titan。它最核心的设计选择是不用 HBM 而用普通商品化内存,McCaskill 的理由是 HBM 供应非常有限、非常贵。这也让功耗足够低,单台服务器约 4,500 瓦,一整柜 Titan 在 40 千瓦以内,可以用风冷。文章称,现在越来越多 0.5、1 或 2.5 兆瓦的模块化数据中心找上门,很多推理玩家的目标是"从拿到土地和电力到产出可变现的 token 只用 90 到 120 天"。

这和这几天的几篇文章是一组:[AI inference servers shrink to fit the air-cooled racks enterprises already run](2026-11-19-ai-inference-servers-shrink-to-fit-the-air-cooled-racks-enterprises-already-run.md)、[d-Matrix bets stacked DRAM can solve inference’s memory bandwidth problem](2026-11-19-d-matrix-bets-stacked-dram-can-solve-inference-s-memory-bandwidth-problem.md)、以及 11 月 18 日那篇讲数据中心建设停滞、推理芯片转向电信机房找空间的[文章](2026-11-18-stalled-data-center-buildouts-send-inference-chips-hunting-for-space-in-telco-an.md),都在讲推理芯片绕开 HBM 和大型数据中心约束。

个人看法:这里可以清楚看到"先找瓶颈再找解决瓶颈的那一层"。推理时代的瓶颈有三个:第一是 HBM 供应,SK 海力士、三星、美光的 HBM 产能被训练 GPU 占满;第二是大型数据中心的电力和并网排队;第三是部署速度,推理是按 token 收费的,晚一个季度上线就少一个季度收入。Positron、d-Matrix 这类公司都是在用架构选择绕开前两个瓶颈,而模块化数据中心是在解决第三个。所以受益的层次会是:第一层是推理专用芯片和非 HBM 内存方案,包括商品化 DRAM/LPDDR 供应商(这对美光、三星的标准 DRAM 业务是边际利好);第二层是模块化、预制化数据中心和风冷设备供应商,以及能在几兆瓦级别快速提供电力的小型发电和储能;第三层是分布式推理网络,也就是把算力放到离用户更近的地方,这正是 edge AI 板块的逻辑——推理负载小型化、低功耗化之后,部署可以下沉到电信机房、企业机房甚至园区边缘。对 AI 板块整体,推理占比上升意味着算力需求从一次性训练变成持续消耗,需求更稳定;但对 Nvidia 来说,推理市场的竞争远比训练激烈,护城河会被侵蚀。需要克制的是,三分之二这个比例来自一个推理芯片厂商的销售负责人,天然有立场。值得跟踪的是 Positron 自研 Titan 芯片明年初流片能否按期,以及甲骨文那 340 台 Atlas 上线后的实际使用情况。
