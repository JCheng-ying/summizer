# Massed Compute deploys GPUs at American Tower data center in Raleigh, North Carolina
https://www.datacenterdynamics.com/en/news/massed-compute-deploys-gpus-at-american-tower-data-center-in-raleigh-north-carolina/

这是一条规模很小的新闻,2MW 的数据中心、没有披露数量的 GPU,但它背后的命题值得记一笔:AI 算力的分布正在出现"两头化"——一头是吉瓦级的训练园区,另一头是建在通信铁塔脚下、只有几兆瓦的区域性节点。后者服务的不是前沿模型训练,而是大学、生命科学机构和初创公司这种"需要 GPU 但不想自己建机房"的长尾客户。

文章指出,AI 云服务商 Massed Compute 选择了 American Tower 位于北卡罗来纳州 Raleigh 的 Edge 数据中心部署 GPU,提供裸金属算力和 GPU 云服务。部署规模没有披露,但 American Tower 提到该站点第二个数据厅已经启用,总 IT 功率达到 2MW;站点 2025 年 5 月开业,第一个数据厅 4000 平方英尺、最初 1MW,满建后可达 4MW、16000 平方英尺。数据厅提供直接液冷(DLC)和后门热交换器(RDHX),可以支持更高密度负载。Massed Compute 是英伟达 Preferred Partner,联合创始人称把 GPU 放在 Research Triangle 的核心地带,让大学研究团队、生命科学机构和 AI 初创公司就近获得低延迟算力;客户还可以通过 American Tower 的 CoreSite 数据中心平台私有连接到存放在公有云里的数据,支持混合式 AI 和科研流程。这个站点建在一座现有的 American Tower 蜂窝铁塔底部,定位是云数据中心和边缘之间的"中间一英里"。

个人看法:这篇和之前写的 [英伟达想利用 Brightspeed 的局端机房做推理网络](2026-11-09-nvidia-looks-to-tap-brightspeed-central-offices-for-inference-network-report.md) 是同一个方向:把算力下沉到通信基础设施已有的物理节点上。那篇里我总结过推理下沉的三种载体,CDN 节点、电信局端机房、终端设备;这里出现的是第四种——铁塔公司的边缘机房。区别在于,局端机房是老建筑改造,电力密度低;American Tower 这个站点是新建的,一开始就有液冷,但体量也只有几兆瓦。

投资角度先找瓶颈:对长尾 AI 用户来说,瓶颈不是 GPU 买不到,而是没有资本和工程能力去运维裸金属集群,同时数据又分散在公有云里,迁移成本高。Massed Compute 卖的是"免运维的 GPU",American Tower 卖的是"离客户近、能私连公有云的机房"。受益的层次会是:第一层仍然是 GPU 本身,这类 neocloud 本质上是英伟达的渠道,长尾需求越分散,英伟达的客户结构越健康;第二层是拥有物理节点和互联能力的基础设施房东,American Tower 通过 CoreSite 做的是"互联中心 + 边缘机房"的组合,在铁塔租赁增长放缓的背景下,这是它的一条增量;第三层是小型机房的液冷和配电设备。这条新闻挂在 AI 板块上,机制是推理和科研算力需求在向区域节点扩散;它离 edge AI 板块说的端侧推理还有距离,这里的"Edge"是网络边缘,不是终端设备。规模太小,单条新闻说明不了什么,值得关注的是 American Tower 会不会在更多铁塔站点复制这种 GPU 租户模式,以及 Raleigh 站点能不能按计划扩到 4MW。
