# Cryptominer Sato Technologies secures neocloud Datum as customer for Canadian data center
https://www.datacenterdynamics.com/en/news/cryptominer-sato-technologies-secures-neocloud-datum-as-customer-for-canadian-data-center/

这条新闻的意义不在于交易规模(文章没有披露细节),而在于一个数字:22 天。它再次说明,在当前的 AI 基础设施周期里,最稀缺的不是 GPU,也不是资本,而是"已经通了电的建筑",谁手里有现成的电力容量,谁就能把交付周期从几年压缩到几周。

文章指出,多伦多创业板(TSXV)上市的前加密矿企 Sato Technologies 通过子公司 Qritical AI 与 Datum Technology 签署了主服务协议和首份订单,10 月底签约、11 月交付场地。Datum 已经在 Sato 位于魁北克 Joliette 的 20MW 水电供电站点完成了首批 Nvidia B300(Blackwell Ultra)服务器部署,用的是原来挖比特币的机房,其他机房的挖矿业务仍在继续。Datum 又把这些算力交给了自己的客户,包括一家 AI 编程初创公司和一个推理平台。Sato CEO 的原话是,从签约到交付只用了 22 天,"这就是现成供电容量对 AI 客户的意义";Datum CEO 则说客户增长很快,但新建数据中心资产"昂贵且缓慢"。

文章还交代了双方背景。Datum 是一家总部在纽约的 AI 云和网络服务商,由裸金属云 Packet 的联合创始人创立,用 Nvidia BlueField DPU 构建开放网络云,让云、数据中心和边缘环境作为一个可编程网络运行,此前已在 DataBank 位于 Ashburn、达拉斯和盐湖城的设施中部署网络接入点,总共覆盖 16 个区域。Sato 成立于 2017 年,2021 年上市,Joliette 的数据中心 2022 年启用、2024 年 6 月发生过火灾;除了改造加拿大矿场,它还计划在不丹的 Gelephu Mindfulness City 建一个 100MW 的 AI 园区,一期 5MW,声称可以扩到 500MW。

个人看法:这和今天写的 [Exaion 签下 7900 万美元 GPUaaS 合同那篇](2026-11-25-exaion-signs-79m-gpuaas-contract-with-us-customer.md) 是同一个模式的不同规模版本——Mara 通过 Exaion、[Core Scientific 计划 2026 年底前退出比特币挖矿](2026-11-16-core-scientific-to-exit-bitcoin-mining-by-end-of-2026-as-it-grows-ai-colo-busine.md)、现在 Sato 通过 Qritical AI,矿企转型 AI 托管已经从个别大公司的战略变成了整个行业的标准动作,连 20MW 这种小矿场也在做。背后的逻辑很简单:矿企手里有三样 AI 客户最缺的东西,第一是已经批下来的电力接入合同,第二是已经建好的变电和配电设施,第三是低价电(魁北克是水电)。

但先找瓶颈的话,也要看清楚矿场改造的局限。矿机是风冷、低功率密度,而 B300 机柜需要高得多的功率密度,很多情况下需要液冷,所以"改造"并不是简单地把矿机换成 GPU,能改多少取决于原有电力和散热设施的余量;20MW 的总容量也决定了它只能服务 Datum 这种中小型 neocloud,而不是超大规模客户。所以受益的层次会是:第一层是持有低价、已并网电力的站点所有者,电力容量本身就是资产,这挂在能源板块上,魁北克、北欧这类水电丰富地区的站点溢价会持续;第二层是帮矿场做改造的配电、液冷和模块化机电供应商,改造周期短意味着他们的订单周转快;第三层是 Datum 这类专注推理和开发者市场的小型 neocloud,它们靠快速拿到现成容量去和大云竞争,但抗风险能力弱,这和 [Nvidia 明确什么情况下会继续为 neocloud 融资那篇](2026-11-18-nvidia-clarifies-when-it-will-and-won-t-keep-financing-neoclouds.md) 讨论的风险是同一件事。GPU 这一层照例是背景受益,AI 板块里"推理需求外溢到小型 neocloud"这个信号是正面的。

这笔交易金额未披露,Sato 本身体量很小,单看这一单不能说明太多。值得关注的是 Sato 后续能不能把剩下的挖矿机房也转给 AI 客户,以及不丹那个 100MW 园区能不能真正落地——前者说明矿场改造的需求有多深,后者则会检验"去电力便宜但很偏远的地方建 AI 算力"这条路走不走得通。
