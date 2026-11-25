# Ohio regulators approve up to 800MW gas plant set to power EdgeConneX data center in Pickaway County
https://www.datacenterdynamics.com/en/news/ohio-regulators-approve-up-to-800mw-gas-plant-set-to-power-edgeconnex-data-center-in-pickaway-county/

这条新闻和九天前 Prologis 起诉 Trenton 市那件事放在一起看,回答的是同一个问题的另一面:当地方选民用投票反对数据中心时,最后到底谁说了算。Trenton 那边是开发商去联邦法院挑战地方公投;这次在同一个州,州一级的监管机构直接给出了答案——州的许可权高于地方投票结果。如果这种做法站得住,AI 数据中心"社会许可"这个瓶颈的解法,很可能是把审批权往上收到州一级。

文章指出,俄亥俄州电力选址委员会(Ohio Power Siting Board)批准了在 Pickaway County 建设一座最高 800MW 的天然气电厂,这座电厂以表后(behind the meter)方式直接给 EdgeConneX 的数据中心供电。整个过程是:Ashville 村议会 4 月先批准了数据中心和配套电厂,EdgeConneX 承诺向当地社区提供最多 1.02 亿美元;但居民以电费上涨、噪声和环境影响为由收集签名,迫使项目进入公投,在中期选举中 81% 的选民反对与 EdgeConneX 的协议。尽管如此,选址委员会认为开发商满足了"符合公共利益"的法定要求,理由是潜在的经济收益、村议会的支持以及施工期控制噪声的承诺,并明确表示自己拥有发放许可的最终权力,不受公投结果约束。反对者有 30 天申请复议,之后可能上诉到俄亥俄州最高法院。

文章还交代了 EdgeConneX 的背景:2009 年成立,在全球 50 多个市场运营或开发超过 90 个数据中心,早期做美国的小型边缘数据中心,后来逐步转向定制建设和超大规模机房。更重要的是,它越来越依赖天然气自建电源,除了 Ashville 之外,还申请在俄亥俄 New Albany 为另一处数据中心建一座 430MW 的表后燃气电厂。

这里可以拆出三个层次的含义。第一是电源模式,800MW 和 430MW 两座表后燃气电厂,说明大型数据中心开发商已经不再等电网,而是自带发电,这和 [Anthropic 签下 34 亿美元燃气发电机订单那篇](2026-11-09-anthropic-signs-3-4bn-gas-generator-deal-to-support-1-7gw-of-data-center-power.md) 是同一个趋势。第二是治理层级,村议会批准、选民否决、州委员会再批准,这个反转说明在俄亥俄,州一级的能源审批可以压过地方民意。第三是政治成本,1.02 亿美元的社区补偿都没能换来选民支持,说明"给钱换同意"这条路的效果在下降。

个人看法:把这篇和 [Prologis 起诉 Trenton](2026-11-16-prologis-sues-ohio-s-trenton-city-after-residents-vote-against-data-centers.md)、[Google 出资 1080 万美元给 Ohio Power 升级输电线](2026-11-20-google-to-fund-10-8m-transmission-line-upgrade-for-ohio-power-in-columbus.md) 连起来,俄亥俄几乎就是美国数据中心选址矛盾的一个缩影:电网要靠云厂商出钱扩容,地方要靠公投挡住项目,州里再用许可权把项目放行。目前来看开发商绕开地方阻力有三种方式:1. 走法院,像 Prologis 那样挑战公投的追溯效力;2. 走州级审批,像这次 EdgeConneX 依靠选址委员会的最终权力;3. 走自带电源,用表后燃气电厂减少对公共电网和居民电费的冲击,削弱反对者最有力的论据。但第二种方式的代价是把矛盾从地方转到州层面,之前 Conserve Ohio 推动把 25MW 上限写进州宪法,就是在针对这一点。

从投资角度看,先找瓶颈:这篇文章里卡住项目的不是 GPU,也不是电网容量,而是许可;而 EdgeConneX 选择的解法是自建燃气电厂。所以受益的层次会是:第一层是能源板块里的燃气发电设备,GE Vernova、Siemens Energy、三菱重工的燃气轮机,以及 Caterpillar、Wärtsilä 这类往复式发电机组厂商,表后电厂越多,它们的订单越确定;第二层是天然气上游和中游,像 EQT 这样的阿巴拉契亚产区天然气生产商和管道公司,800MW 级别的稳定负荷是长期需求;第三层才是 AI板块里的数据中心开发商本身,EdgeConneX 这类有能力自建电源的开发商在拿地上有优势,但它们同时承担了法律和政治风险。对 AI 板块整体是偏正面的,因为它说明至少在俄亥俄,州层面仍然愿意为数据中心放行。

现在结论还不稳,30 天复议期和可能的州最高法院上诉都还没走完。值得跟踪的是两个信号:一是俄亥俄州最高法院如果受理上诉,会不会推翻选址委员会"可以无视公投"的立场;二是 New Albany 那座 430MW 电厂的审批是否顺利——如果同样被放行,说明州一级给数据中心开绿灯已经成为常态。
