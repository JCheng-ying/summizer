# Swiss data center firm Green hooks up data center to heating network in Dielsdorf, Switzerland
https://www.datacenterdynamics.com/en/news/swiss-data-center-firm-green-hooks-up-data-center-to-heating-network-in-dielsdorf-switzerland/

这条新闻和之前写过的 [NTT Docomo 用余热养虾](2026-11-13-ntt-docomo-to-pilot-data-center-heat-reuse-for-on-shore-shrimp-farm-in-japan.md) 正好构成对照:那篇是"就近低温直接利用"的小试点,这篇则是我当时归纳的第二种模式——接入区域供热网络,而且规模已经到了可以服务上万户家庭的程度。它背后的命题是:在电网和土地越来越紧张的欧洲,数据中心想要拿到地方政府的支持,可能需要把自己从"耗电大户"重新定位成"城市供热基础设施的一部分"。

文章指出,瑞士数据中心运营商 Green 正在把数据中心余热供给 Dielsdorf 的住宅,这是一个计划覆盖六个市镇、最多 11,500 户家庭的区域供热网络的一部分。能源中心由瑞士能源公司 Energie 360° 开发,11 月 19 日正式投运,首批住宅已经接入;网络覆盖 Dielsdorf、Niederhasli、Steinmaur、Regensdorf、Buchs 和 Dällikon,通往 Regensdorf 的管网正在施工。全部建成后,整个供热计划的供热能力为 60MW,每年供热约 166GWh,Energie 360° 称每年可减少约 2.7 万吨二氧化碳排放。技术上,回收的热量在能源中心被提升到约 70°C 再输送给用户,而管网回流的冷水又被用来辅助数据中心冷却,形成一个闭环。Green 2024 年的可持续发展报告显示其数据中心余热能力为 30MW,中央能源单元可达 36MW;它把余热回收的技术要求直接写进了园区设计,余热再利用已经是新设施参考设计的一部分。文章还介绍,Green 成立于 1995 年,总部在 Lupfig,在瑞士四个地点运营七个数据中心,两大园区位于苏黎世附近的 Lupfig 和 Dielsdorf;2025 年 10 月被澳大利亚基础设施投资机构 IFM Investors 从法国 InfraVia Capital Partners 手中收购。Lupfig 园区的第四个数据中心设计为向 Naturenergie Eigenamt 网络供热,据报道 Birr 的新园区也将纳入余热回收。

这里有一个技术细节值得说清楚:数据中心的排热本身温度不高,文章说的"提升到约 70°C"意味着中间几乎一定有一级热泵在做升温,而热泵本身要耗电。所以这类项目的经济性取决于两件事:第一是余热的原始温度,温度越高,热泵需要补的电越少;第二是回水能不能反过来给数据中心降温,把冷却的电省回来。Green 这个闭环设计同时在两头做文章,这是它比单纯"卖热"更合理的地方。

个人看法:从投资角度先找瓶颈。欧洲数据中心当下最大的瓶颈是并网和许可,之前 [挪威暂停新数据中心并网申请](2026-11-09-norway-halts-grid-connection-applications-for-new-data-centers.md) 就是一个极端例子,而余热利用并不能直接解决电力短缺,它解决的是"社区和政府为什么要接受你"这个问题。所以这条新闻对能源板块的利好仍然是边际的,机制是提升数据中心整体能源效率、让数据中心更容易拿到选址许可。受益的层次会是:第一层是液冷和热管理,Vertiv、Schneider Electric、Modine 这类公司,因为液冷出水温度更高,直接决定了余热的品位和热泵的耗电;第二层是大型热泵和区域供热设备厂商,比如 Danfoss、Trane、Daikin,以及像 Energie 360° 这样的地方能源公司,它们是把低品位热变成可卖商品的那一层;第三层是基础设施资本,IFM Investors 这类长期资金收购数据中心运营商,看中的正是这种和城市公共事业绑定后更稳定、更像公用事业的现金流。

和养虾试点相比,这已经是商业化落地而不是示范项目,但 60MW 的供热规模相对于 AI 时代动辄几百兆瓦的园区仍然很小。值得关注的是,瑞士或欧盟层面会不会把余热回收写进数据中心的审批条件——德国已经在朝这个方向走,如果更多国家跟进,热泵和液冷这一层的需求就会被政策放大。
