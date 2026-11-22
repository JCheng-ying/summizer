# Chips can survive the space environment — can their financing?
https://techcrunch.com/2026/11/20/chips-can-survive-the-space-environment-can-their-financing/

这篇文章提出了一个太空数据中心讨论里很少被提到、但可能比散热和辐射更早卡住商业化的问题:钱从哪里来。如果轨道上的芯片没办法像地面芯片那样被当作抵押物,那太空算力的资本成本天生就比地面高,"太空更便宜"的论证就少了一条腿。

文章指出,今天的数据中心生态依赖债务融资:云厂商借钱建数据中心,再用收入还贷,而贷款通常以芯片本身作抵押,一旦违约,贷方可以收走芯片转卖。这个兜底机制让芯片融资变便宜,而且旧芯片仍然保值——文章引用 Compute Credit Index Research 的数据,部分 H100 的售价约为 2023 年原始成本的一半,部分 H200 配置的价格和 2024 年刚推出时一样。但卫星在 300 英里高空以每小时 17,500 英里飞行,芯片是收不回来的。文章援引金融时报报道,SpaceX 那笔 400 亿美元芯片融资的贷方要求这批芯片不得用于轨道数据中心计划,但不清楚 SpaceX 是否接受了这个条款。

文章认为,短期内这对 SpaceX 影响不大,因为它在地面站部署算力已经很赚钱,Musk 在最近一次财报电话会上还提到派火箭团队工程师去加速建设,比如以比现有供应商更快的速度铸造发电机涡轮叶片。但地面扩张同样面临土地、电力、地方反对和需求不确定的问题。至于 Musk 年初说的"两三年后太空是运营数据中心最便宜的地方",文章认为在 Starship 实现完全复用之前不太可能——而最近一次飞行恰好是二级回收成功、一级失败(见 [Following Ship 42’s catch, SpaceX looks to the future](2026-11-21-following-ship-42-s-catch-spacex-looks-to-the-future.md))。更关键的是,SpaceX 以及 Starcloud、Cowboy Space Corporation、Sophia Space、Orbital 等初创公司都要买芯片,如果融资条件更差,它们买芯片的成本就会比地面同行更高。文章最后点出,这可能反而是 Google 的优势,因为 Google 通过 Project Suncatcher 部署的是自家 TPU;SpaceX 和 Tesla 正合作在美国建芯片厂 Terafab,但还没开工,要很多年和数十亿美元才能量产。

个人看法:这篇文章补上了我之前分析太空数据中心时漏掉的一层。之前我把瓶颈拆成能源、散热、辐射、维护四个物理问题,但这里其实还有第五个瓶颈,就是金融结构。地面 GPU 之所以能用这么高的杠杆扩张,是因为有一个活跃的二手 GPU 市场在给抵押物定价,太空芯片没有残值回收路径,等于把"折旧风险"全部压在运营方身上。这里可以看出,谁能解决这个瓶颈才是真正受益的那一层:第一种是自己有芯片、不需要外部芯片融资的玩家,比如 Google 的 TPU、以及未来如果 Terafab 建成的 SpaceX/Tesla;第二种是资产负债表足够厚、可以用股权而不是芯片抵押贷款来融资的公司,SpaceX 的地面算力现金流就是这个作用;第三种是专门为太空资产设计的保险和融资产品,这个目前还几乎是空白。所以这篇文章对太空经济板块是偏中性略谨慎的信号:它不否定太空算力,但说明初创公司的资本成本会比想象中高,早期最可能跑出来的仍然是 SpaceX 和 Google 这种自带资金和芯片的大玩家。对 AI 板块来说,H100/H200 二手价格保值这个数据点本身反而是利好,说明地面算力的抵押品价值还很稳,GPU 云的融资链条暂时没有松动。和 [SpaceX developing custom Nvidia Vera Rubin rack dubbed Kessel](2026-11-12-spacex-developing-custom-nvidia-vera-rubin-rack-dubbed-kessel-for-its-orbital-da.md) 那篇联系起来看,SpaceX 一边在定制轨道用的 Nvidia 机柜,一边贷方又在限制芯片上天,后续值得关注的是 SpaceX 最终用什么钱、什么芯片把第一批轨道算力送上去。
