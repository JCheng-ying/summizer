# Nscale brings online two data centers and 25,000 GPUs in 2.5 months
https://www.datacenterdynamics.com/en/news/nscale-brings-online-two-data-centers-and-25000-gpus-in-25-months/

这篇报道的素材是 Nscale 新一版 IPO 招股书。它真正回答的问题是:一家 neocloud 签下的合同和它实际交付出来的算力之间,差距到底有多大,而填补这个差距的钱又从哪里来。

文章指出,Nscale 自 2026 年 8 月 31 日以来新上线了两座数据中心和约 2.5 万块 GPU,活跃 GPU 从上一版招股书的约 2.5 万块翻倍到约 5 万块,但计划总量是 46.1 万块,也就是说目前只交付了大约十分之一。活跃站点从 5 个(55MW)增加到 7 个,另有 10 个在规划中,不过新版没有披露 7 个站点的总容量。Nscale 称已有 1.37GW 的活跃和已签约容量,其中 1GW 在自有站点、200MW 在租赁站点、165MW 在托管数据中心,并对 10GW 潜在电力容量有"line of sight"。合同口径的数字涨得更快:按照 take-or-pay 长期合同计算,活跃 TCV 约 64 亿美元,活跃加已签约 TCV 约 1058 亿美元,而 2025 年底这两个数字分别是 5 亿美元和 380 亿美元。

财务披露的口径变化值得注意。文章指出,上一版招股书给的是 2026 年上半年数据:收入 1.406 亿美元,公司称同比增长 1252%,同期亏损扩大到 10.2 亿美元(2025 年同期为 3.689 亿美元);新版则改为聚焦 2025 全年,收入 3300 万美元,同比增长 73%。也就是说,半年亏损超过 10 亿美元,而全年收入只有几千万到一两亿的量级,合同总额和账面收入之间差了两个数量级。

文章还补充了与 Anthropic 合作的细节。8 月双方就西弗吉尼亚 Monarch 园区签下 450 亿美元算力协议;招股书确认,Anthropic 已于 9 月 29 日行使了对 2 号楼追加算力的权利,双方有 60 天(可协商延期)谈定协议,且 2 号楼协议签署后 15 个工作日内 Anthropic 还可以对 3 号楼行使同样的权利。Nscale 表示将通过"外部融资和经营现金流"为这部分部署出资,并称已与市场参与者测试过融资深度,相信能在规定期限内拿到合格融资,但文章特别强调,目前还没有任何已签署的融资协议。如果 Nscale 不能按时交付 GPU 基础设施(包括供应链延迟的情况),Anthropic 有权无责终止对应批次。据报道 Nscale 希望通过 IPO 募集数十亿美元,目标估值约 300 亿美元,发行日期未定。

个人看法:之前写过两篇 Nscale 的相关新闻,分别是 [Nvidia 考虑为 Nscale 西弗吉尼亚项目做担保](2026-11-01-nvidia-weighs-playing-the-cosigner-for-nscale-s-ai-data-center-in-west-virginia.md) 和 [微软放弃得州扩容选择权](2026-11-05-microsoft-declined-option-for-expanded-compute-contract-in-texas-with-nscale.md),和这篇合起来能看清这家公司的完整链条。先找瓶颈:Nscale 的瓶颈不是需求,1058 亿美元的合同 TCV 已经说明客户在排队;也不完全是电,1.37GW 已签约容量加上 10GW 的"视野"说明它在主动囤电;真正卡住的是资产负债表。Anthropic 条款里"交付延迟可无责终止"这一条,把供应链风险全部压在了 Nscale 身上,而它又要靠还没签下的融资去买 GPU、建楼,任何一个环节晚了,合同就可能变成没有收入的在建资产。和 [CoreWeave 转向客户预付款和更短合同](2026-11-11-coreweave-turns-to-customer-prepayments-shorter-contracts-to-fund-ai-growth.md)、[Nebius 计划 400 亿美元支出](2026-11-12-nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending.md) 放在一起看,整个 neocloud 赛道都在面对同一个问题:合同易签,融资难做。

所以从 AI 板块看,受益层次是:第一层仍然是 GPU 和服务器,Nvidia 以及 Supermicro、Dell 这类整机厂,46.1 万块 GPU 的交付不管由谁出资最终都要变成芯片订单,而且 Nvidia 已经通过担保和可转债把自己绑在了这条链上;第二层是为这些资产提供融资的信贷方,项目级 GPU 融资会是接下来最忙的一层;第三层才是 Nscale 这样的 neocloud 本身,它的股权价值取决于融资能否跟上交付节奏,风险最高。能源板块的逻辑和之前一致:1GW 自有站点意味着 Nscale 自己承担了拿电、建变电和现场发电的工作,这部分会转化为电网设备和表后发电的订单。对 AI 板块整体是中性偏利好,需求确认了,但融资端的脆弱性也被更清楚地写进了招股书。现在还在观望阶段,值得跟踪的是 Monarch 2 号楼协议能否在 60 天内签下、对应的融资方是谁,以及 IPO 最终定价是否接近 300 亿美元的目标。
