# Trump announces plan to tax US companies that build data centers abroad
https://siliconangle.com/2026/11/20/trump-announces-plan-to-tax-us-companies-that-build-data-centers-abroad/

这篇文章报道的政策信号背后,是一个更大的命题:AI 算力正在从"商品"变成"战略资产",政府开始不仅管芯片卖给谁,还要管数据中心建在哪里。如果对境外数据中心征税真的落地,全球 AI 基础设施的地理分布会被政策重新划分,而美国本土本来就紧张的电力和土地约束会被进一步放大。

文章指出,特朗普在白宫简报会上宣布,计划对在海外建数据中心的美国公司征收"巨额税",理由是"中国会把它们全拿走"。文章推测重点可能是 AI 优化的数据中心,因为有报道称中国科技公司正在马来西亚等国的 AI 数据中心训练模型,以绕开美国对先进 AI 芯片的出口限制。但具体哪些设施算数并不清楚:AWS 等云厂商的海外数据中心有大量 GPU,也跑通用负载,有些建于大模型出现之前。文章提到 AWS 上个月宣布明年在德国投资 180 亿欧元,Google 几周前承诺在芬兰投入 130 亿欧元,一项针对海外项目的新税可能让一些公司修改投资计划。特朗普表示宣布前没有和白宫官员讨论过,美联社称目前没有任何实施细节。他说"我们希望他们建在这里,如果不去德州或加州,就去西弗吉尼亚"。文章同时提到,本月中期选举中多个州的选民通过了限制数据中心建设的投票提案;几天前商务部刚出台了针对海外 AI 设施的新限制,据金融时报报道,至少两家芯片商暂停了部分发货,neocloud 公司 Nscale 需要拿到商务部许可证才能继续和其最大客户合作。

这篇和 [US tightens AI chip export controls to deter Chinese companies from accessing compute](2026-11-16-us-tightens-ai-chip-export-controls-to-deter-chinese-companies-from-accessing-co.md)、[Alibaba Cloud launches sixth data center in Malaysia](2026-11-20-alibaba-cloud-launches-sixth-data-center-in-malaysia.md) 是同一条线:商务部堵远程访问,总统又要对境外建设征税,而中国云厂商在东南亚的扩张还在继续。

个人看法:我觉得这项政策目前更多是一个姿态,细节完全空白,但它暴露出一个结构性矛盾。政府想把数据中心留在美国,可美国本土建数据中心的真正瓶颈是电力、并网排队和社区反对——文章自己也提到中期选举里多个州的选民刚投票限制数据中心建设,和 [A taxonomy of American data center opposition](2026-11-01-a-taxonomy-of-american-data-center-opposition-politics-misinformation-and-conspi.md) 那篇说的一致。所以如果税真的落地,按"先找瓶颈再找解决瓶颈的那一层"来看,真正受益的不是云厂商(它们的成本会上升、选址自由度下降),而是解决美国本土电力瓶颈的那一层:第一层是燃气轮机和现场发电(GE Vernova、Siemens Energy、Caterpillar、Bloom Energy),因为把大量项目挤回美国意味着更多表后发电需求;第二层是输配电设备和变压器(Eaton、Hubbell、Quanta Services);第三层是已经握有电网接入和土地的场地方,包括转型做 AI 托管的前矿企。对能源板块这是边际利好。对 AI 板块则偏利空:海外扩张受限、成本上升,对 AWS、Google、Microsoft 的欧洲和亚洲投资计划构成不确定性,对依赖跨境客户的 neocloud(比如 Nscale)冲击更直接。另外这可能也给海外本土云厂商和主权 AI 项目让出空间。现在没有细节,只能观望,值得跟踪的信号是财政部或商务部有没有出台具体定义,以及 AWS、Google 的欧洲项目会不会有调整。
