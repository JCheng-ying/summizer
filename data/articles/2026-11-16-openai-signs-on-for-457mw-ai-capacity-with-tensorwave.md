# OpenAI signs on for 457MW AI capacity with TensorWave
https://www.datacenterdynamics.com/en/news/openai-signs-on-for-457mw-ai-capacity-with-tensorwave/

这笔合同的意义在于,AMD 第一次通过一家专做 AMD 的 neocloud,把自己的整机柜方案卖进了头部 AI 实验室的数百兆瓦级部署。过去两年"AMD 能不能在训练和推理的大规模集群里替代 Nvidia"一直停留在 benchmark 和意向书阶段,457MW、六年期、单租户的合同,是一个可以落到电力和机柜上的具体数字。

文章指出,OpenAI 与 TensorWave 签下六年协议,由 TensorWave 在多个数据中心地点为 OpenAI 提供 457MW 的 IT 容量,使用 AMD Instinct MI455X GPU,以 Helios 整机柜系统的形式部署,作为 OpenAI 专属的单租户容量运营。按目前计划,2027 年上半年开始运营,2028 年初全部部署完成。这是 TensorWave 迄今最大的部署合同。Helios 机柜在 7 月发布,把 MI455X GPU、第六代 Epyc "Venice" CPU、ROCm 软件和 Pensando 网络整合成一个整机柜架构。单个机柜最高提供 2.9 exaflops FP4 峰值算力、1.4 exaflops FP8、31TB 的 HBM4 显存和每秒 1.7PB 的内存带宽。文章还引用了 AMD 自己的对比:相比 Nvidia Vera Rubin NVL72 机柜公开的规格,Helios FP4 峰值高 15%,HBM 容量高 50%,HBM 带宽高 6%,横向扩展带宽高 50%,每美元 token 数最多高 30%——需要强调这是 AMD 的自述,不是第三方测试。OpenAI 的计算 CTO 说,这笔协议是在推进此前已宣布的与 AMD 的合作。

文章还交代了 TensorWave 的背景:2026 年 6 月完成 3.5 亿美元 B 轮融资,声称在美国锁定了 2GW 长期数据中心容量,是 TecFusions 的已知客户,1 月还和 TecFusions 签了宾夕法尼亚和亚利桑那的 20MW 协议。而 TecFusions 原本计划在 Fermi 的 Project Matador 园区租用容量,本月初双方也已正式分道扬镳。

个人看法:这篇要和 [Fermi 失去 TensorWave 租约](2026-11-13-fermi-does-600mw-power-deal-with-hyperscaler-but-tensorwave-lease-is-officially-.md) 放在一起读。三天前 TensorWave 刚刚放弃了在 Fermi 园区由 AMD 提供信用担保的 650MW 租约,今天就拿下了 OpenAI 的 457MW。这说明 TensorWave 缺的从来不是客户,而是"能按时通电的场地",它选择离开一个电力还停留在理论上的园区,转去多个已经能交付的地点。用"先找瓶颈"的方法看,这里有两个瓶颈:第一是 Nvidia 的供给和定价权,OpenAI 需要第二供应商来压价、分散风险,这是 AMD 拿到订单的根本原因;第二仍然是电力和场地,合同写的是 2027 年上半年才开始运营,说明即使客户和芯片都到位,机房建设依然是最慢的一环。

所以受益的层次会是:第一层是 AMD,这是 AI 板块里 GPU 层的第二供应商故事第一次有了确定的规模;第二层是 HBM 供应商,Helios 的卖点就是 HBM 容量多 50%,每个机柜 31TB HBM4,SK Hynix、三星、美光的 HBM 需求会因为 AMD 的放量而进一步扩大;第三层是能按期交付电力和机房的数据中心开发商,TensorWave 背后的 TecFusions 这类公司就在这一层,这也挂在能源板块,因为 457MW 的电要在 2028 年前接上;第四层才是 TensorWave 这样的 neocloud 本身,它的风险和 [Firmus](2026-11-16-firmus-looks-to-raise-3bn-in-private-equity-and-secure-prepayments-report.md) 一样:合同签下来了,但建设资金从哪里来,文章没有说。值得跟踪的是 ROCm 在 OpenAI 实际负载上的表现,以及 2027 年上半年第一批容量能不能按时上线。
