# NTT signs MoU with B.Grimm for 400MW data center project in Thailand
https://www.datacenterdynamics.com/en/news/ntt-signs-mou-with-bgrimm-for-400mw-data-center-project-in-thailand/

这篇新闻反映的是东南亚 AI 数据中心正在出现的一种组合方式:数据中心开发商不再单独去找电,而是直接和当地最大的发电企业绑在一起做项目。如果这种"电力公司 + 数据中心开发商"的模式在泰国跑通,意味着东南亚新兴市场的算力扩张会越来越由谁手里有电、有地决定,而不是由谁有 GPU 决定。

文章指出,泰国电力企业 B.Grimm Power 宣布与 NTT Global Data Centers 签署谅解备忘录,共同推进一个 400MW 的数据中心项目,涵盖数字基础设施、AI 生态和能源基础设施,投资额约 1130 亿泰铢(约 33 亿美元),但没有披露更多细节。B.Grimm 成立于 1993 年,是泰国最大的工业电力生产商之一,装机容量超过 3.3GW,目标是到 2030 年拿到总计 10GW 的购电协议。B.Grimm 此前已经和 NTT 签过多笔能源协议,为 NTT 在春武里(Chonburi)园区的设施供电,同时也和亚太运营商 Digital Edge 有合作。NTT 目前在曼谷周边运营三个数据中心:Bangkok 1 是 1.6MW 的边缘机房,Bangkok 2 是 3.6MW,Bangkok 3 是 12MW,第四个 Bangkok 4 今年夏天动工,预计 2027 年第二季度上线。

规模对比很能说明问题:NTT 在泰国现有三座机房加起来不到 20MW,而这份 MoU 是 400MW,相当于二十倍以上的跳跃。这不是在原有业务上的渐进扩张,而是一个面向 AI 负载的量级跃迁。

文章同时提到另一个泰国项目,体量小得多但很有代表性。纳斯达克上市的 Aether Holdings 旗下 Aether Compute 与泰国孔敬(Khon Kaen)的拖车和客车制造商 Cho Thavee、新加坡资本方 Advance Capital Partners(ACP)签了有约束力的三方框架协议,拟成立合资公司,把 Cho Thavee 约 14 英亩的工厂改造成 AI 数据中心。现有电力容量只有约 850kW,还需要场地评估和审批;Cho 以低于市场价的长期租约和购买选择权把场地注入合资公司,Aether 和 Cho 各持股 47.5%,ACP 持股 5%。Aether 是一家金融科技公司,今年夏天才成立 Aether Compute,推出自己的模块化设备 AetherPod VG100,8 月收购了技术基础设施服务公司 Noviant 60% 的股权。CEO 的说法是这种结构能让公司"有限使用资产负债表"参与 AI 基础设施。

个人看法:这两个项目放在一起,正好是东南亚 AI 数据中心两种截然不同的打法。先找瓶颈:新兴市场 AI 数据中心的瓶颈第一是电,第二是能落地的场地,第三才是资金。目前来看解决这个瓶颈有三种方式:1. 电力公司直接入局,像 B.Grimm 这样手里有 3.3GW 装机、还在扩 PPA 的发电企业,和 NTT 这种全球开发商合作,电和客户一次性对接,确定性最高;2. 开发商自己现场发电,比如 NTT DATA 之前 [与 Bloom Energy 签的 900MW 燃料电池协议](2026-11-08-ntt-data-signs-900mw-fuel-cell-supply-deal-with-bloom-energy.md),解决的是"等电网"的时间问题;3. 利用存量工业资产改造,像 Aether 盯上一个已经有电力接入的工厂,但 850kW 这个量级离真正的 AI 训练集群差了几个数量级,更像是推理或企业级算力的小规模试点。

第三种方式我会更谨慎看待。一家金融科技公司刚成立算力子公司几个月,就通过合资、低价租约、轻资产的方式切入,这和过去几年加密矿企转型 AI 托管的路径很像,概念先行,真正的交付能力还没验证。这类公告值得注意的是它反映了"AI 数据中心"这个标签的资本吸引力,而不是它本身能带来多少算力。

NTT 这边则可以和之前几篇串起来看:NTT 一边在 [日本试点数据中心余热养虾](2026-11-13-ntt-docomo-to-pilot-data-center-heat-reuse-for-on-shore-shrimp-farm-in-japan.md) 这种边际优化,一边在泰国做 400MW 量级的扩张,而今天 [DatacenterHawk 的报告](2026-11-24-datacenterhawk-global-data-center-supply-grows-two-thirds-but-vacancy-shrinks.md) 恰好说亚太第三季度租赁量已超过去年全年、neocloud 愿意为快速交付付溢价——NTT 选择和本地电力龙头绑定,正是在抢"能最快交付"这个稀缺位置。泰国也不是孤例,之前读到的 [阿里云在马来西亚开第六个数据中心](2026-11-20-alibaba-cloud-launches-sixth-data-center-in-malaysia.md) 说明整个东南亚都在被纳入 AI 算力布局。

受益的层次会是:对能源板块,第一层是像 B.Grimm 这样拥有装机和 PPA 能力的本地发电企业,数据中心把它们从"工业园区供电商"变成 AI 基础设施的核心合作方,而泰国电力结构以天然气为主,配套的燃机和输配电设备也会受益;第二层是数据中心开发商,NTT DATA 这样有全球客户关系的运营商能把超大规模云厂商和 neocloud 的需求带到新市场;对 AI 板块,第三层仍然是 GPU、服务器和网络,400MW 一旦落地最终都会转化为芯片采购。需要强调的是,这只是一份 MoU,没有客户、时间表和电源结构的细节,从 MoU 到最终投资决定往往还有很长的路。

现在还只是意向阶段。值得关注的信号是这份 MoU 什么时候转为正式协议,以及有没有披露锚定租户——如果背后是某家超大规模云厂商的长期租约,那这 400MW 的确定性会高得多。
