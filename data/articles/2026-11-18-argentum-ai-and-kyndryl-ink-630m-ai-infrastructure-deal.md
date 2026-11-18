# Argentum AI and Kyndryl ink $630m AI infrastructure deal
https://www.datacenterdynamics.com/en/news/argentum-ai-and-kyndryl-ink-630m-ai-infrastructure-deal/

这笔交易的有趣之处不在金额,而在于它揭示了 AI 算力扩张中一个被低估的供给来源:传统企业 IT 服务商手里那些"老"数据中心,正在被 neocloud 重新租用来装最新一代 GPU。如果这种模式铺开,电力和机房的稀缺性会让存量设施重新估值。

文章指出,AI 云服务商 Argentum AI 与 Kyndryl 签下 6.3 亿美元、为期 20 年的协议,租用 Kyndryl 位于科罗拉多州博尔德的数据中心 10MW 容量,用于部署 Nvidia B300 GPU,部署已经在进行中。这座数据中心最初由 IBM 建设(Kyndryl 于 2021 年 11 月从 IBM 拆分出来),2008 年扩建后总面积 30 万平方英尺,总容量 15MW。文章还提到,Argentum 官网称其拥有 344MW 已签约电力和 13 个独家站点,今年 6 月与一家未具名 AI 公司签下 41 亿美元合同,5 月与云游戏公司 Boosteroid 和 DL Invest Group 签下 25 亿美元协议,在波兰 Bielsko-Biala 一个 300MW 以上的新数据中心部署 GPU。

简单算一下:6.3 亿美元 / 20 年 / 10MW,约合每兆瓦每年 315 万美元。这个价格对一个 2008 年扩建的老园区来说相当可观,说明在今天的市场里,"已经通电、已经有并网容量"的机房本身就是稀缺资产,哪怕它原本是为传统企业 IT 设计的。

个人看法:这和今天读过的 [NVIDIA 澄清何时会继续为 neocloud 融资](2026-11-18-nvidia-clarifies-when-it-will-and-won-t-keep-financing-neoclouds.md)、以及 [Nebius 的 400 亿美元扩张计划](2026-11-12-nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending.md)是同一条线索:neocloud 的商业模式本质是"先锁电力和机房、再拿客户合同、再融资买 GPU",三个环节任何一个断了都会出问题。Argentum 披露的数字(344MW 签约电力、几十亿美元合同)都是公司自述,文章没有给出独立核实,客户也有未具名的,所以对这类公司要打折看。

先找瓶颈:这笔交易里卡住的是"可立即使用的已通电机房",不是 GPU。所以对 AI 板块,受益的层次会是:第一层仍然是 GPU,B300 的需求没有因为部署在老机房而减少,Nvidia 是确定性受益方;第二层是手握存量机房和并网容量的业主,Kyndryl 这类原本被视为低增长 IT 服务商的公司,可以把闲置或低效利用的机房以 AI 价格重新出租,这对它的估值叙事是正面的;第三层是老机房改造所需的液冷和配电升级——B300 机柜功率密度远高于老机房的设计水平,10MW 装进一个总容量 15MW 的园区,改造需求必然存在。

需要警惕的是 neocloud 层本身的信用风险:20 年的租约和几年就过时的 GPU 之间存在期限错配,如果 AI 算力租赁价格下滑,最先承压的就是 Argentum 这类中间层。值得跟踪的是还有没有其他传统 IT 服务商(比如拥有大量自建机房的老牌外包商)跟进出租存量机房。
