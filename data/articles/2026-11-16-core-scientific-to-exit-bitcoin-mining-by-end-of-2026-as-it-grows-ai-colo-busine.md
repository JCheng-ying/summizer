# Core Scientific to exit Bitcoin mining by end of 2026 as it grows AI colo business
https://www.datacenterdynamics.com/en/news/core-scientific-to-exit-bitcoin-mining-by-end-of-2026-as-it-grows-ai-colo-business/

这条新闻表面上是一家矿企转型,背后的命题其实是:在 AI 基础设施这一轮周期里,真正稀缺的资产不是矿机、也不是机房外壳,而是"已经接上电网的兆瓦"。比特币矿场恰好是过去几年里囤积这种资产最多的一类公司,所以它们转型做 AI 托管,本质上是把手里的电力指标按更高的价格重新出租。

文章指出,Core Scientific CEO Adam Sullivan 在 11 月 5 日的三季度电话会上表示,公司预计在年底前彻底退出比特币挖矿,2027 年起只做高密度托管(colocation)。CFO Jim Nygaard 说,9 月底在线矿机数量比 2025 年底少了近一半;10-Q 文件把挖矿、电气和 HPC 设备列为待售资产,剩余待售设备账面价值 2,970 万美元。财务数据上的转变非常明显:自营挖矿收入从去年同期的 5,740 万美元降到 1,230 万美元,托管第三方矿机收入从 870 万降到 520 万美元;而总收入从 8,110 万美元升到 2.329 亿美元,其中托管收入 2.154 亿美元(去年同期只有 1,500 万),占季度收入约 92.5%。调整后 EBITDA 1.336 亿美元,高于二季度的 4,110 万和去年同期的 650 万。账面净利润 11.8 亿美元主要来自认股权证重估的非现金收益,不能当成经营能力看。公司前九个月卖出 3,374 枚比特币换得 2.868 亿美元来支付资本开支,9 月底只剩 32 枚;同期资本开支(含土地和开发权收购)9.851 亿美元,期末现金 8.039 亿美元。

产能层面,文章给出三组数字:第一,9 月底计费托管容量 485MW,高于 6 月底的 395MW;第二,与 CoreWeave 签约 590MW,分布在五个园区,预计 2027 年初全部交付;第三,在与 AMD 的合作框架下签约 530MW,包括 AMD 直租和一家 AMD 支持的 neocloud 的租约,覆盖德州 Pecos 和 Hunt County、佐治亚 Dalton、俄克拉荷马 Muskogee 和阿拉巴马 Auburn,首批 2027 年上半年交付,2028 年底全部完成。此外,公司 8 月以约 4.44 亿美元完成对 Polaris DS 的收购,拿到 Muskogee 园区旁一个前加密矿场约 40 英亩土地和 440MW 并网电力,计划把该园区扩到 1.5GW 总电力。

个人看法:这篇和前几天写的 [CoreWeave 转向客户预付款和短期合同融资](2026-11-11-coreweave-turns-to-customer-prepayments-shorter-contracts-to-fund-ai-growth.md) 是同一条链条的上下游。那篇里 CoreWeave 说"已建成、带电的产能"最值钱,这篇就是那批产能的提供方之一——Core Scientific 有 590MW 是签给 CoreWeave 的。用"先找瓶颈"的思路看,这里卡住的瓶颈不是 GPU,而是电网接入:[挪威暂停数据中心并网申请](2026-11-09-norway-halts-grid-connection-applications-for-new-data-centers.md) 和 [欧洲 AI 的电力瓶颈](2026-11-01-europe-s-ai-ambitions-are-hitting-a-power-bottleneck.md) 说的都是同一件事。谁手里有现成的并网容量,谁就站在解决瓶颈的那一层。Polaris DS 那笔交易尤其说明问题:4.44 亿美元买的核心不是 40 英亩地,而是 440MW 的电。

目前来看矿企转型 AI 有三种路径:1. 像 Core Scientific 这样彻底退出挖矿,只做托管房东,收入稳定但上限取决于租约价格;2. 挖矿和 AI 托管并行,用比特币价格的波动去对冲 AI 需求的波动;3. 自己买 GPU 做 neocloud,收益最高但资本负担和风险也最大。Core Scientific 选择了第一种,并且把客户集中在 CoreWeave 和 AMD 生态两边,这意味着它的风险已经和 neocloud 的融资能力绑在一起。

所以受益的层次会是:第一层是能源板块里提供并网容量、变电和电力设备的环节,因为这批转型说明"带电的土地"已经成为 AI 数据中心最硬的约束,Vertiv、Eaton、Schneider 这类电源和配电设备商会随着 1.5GW 级园区的建设持续受益;第二层是 AI 板块里的算力供给方,AMD 直接租下 530MW 本身就是一个信号——它不只卖芯片,还在为自己的生态锁定电力和机房,这和英伟达通过投资 neocloud 锁定需求是类似的打法;第三层才是 Core Scientific 这类房东本身,它们的估值取决于租户能不能按时付钱。需要提醒的是,11.8 亿美元的账面利润主要是非现金的权证重估,9.85 亿美元的资本开支加上几乎卖光的比特币储备,说明它的扩张高度依赖外部融资和租户预付款。现在还在观望阶段,值得跟踪的是 2027 年初 CoreWeave 那 590MW 能否如期全部交付,以及 AMD 相关的 530MW 首批交付是否落在 2027 年上半年。
