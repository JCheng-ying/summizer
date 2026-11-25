# Rajiv Ramaswami to step down as Nutanix begins hunt for its next CEO
https://siliconangle.com/2026/11/24/rajiv-ramaswami-to-step-down-as-nutanix-begins-hunt-for-its-next-ceo/

这条新闻表面上是一次 CEO 交接,但背后的命题是:企业私有云/混合云这一层软件公司,在"AI 时代"到底能不能找到第二条增长曲线。Nutanix 选在季报当天宣布 CEO 将卸任,市场的反应很直接——不是看单季度,而是看谁来带它进入下一个阶段。

文章指出,Rajiv Ramaswami 在给员工的信里表示,他会继续担任 CEO,直到董事会通过猎头公司找到继任者,之后再以高级顾问身份留任一段时间,但没有说明离任原因。同一天发布的第一财季数据本身不差:调整后每股收益 0.73 美元,高于市场预期的 0.61 美元;营收 7.724 亿美元,同比增长 15%,高于预期的 7.627 亿美元;下季度营收指引 8.2 亿到 8.3 亿美元,与市场一致预期 8.204 亿美元基本持平。问题出在全年:公司给出的 2027 财年营收指引是 31.8 亿到 32.3 亿美元,中值低于市场预期的 32.2 亿美元。文章提到,保守的全年指引叠加领导层的不确定性,导致股价盘后下跌 8%,而常规交易时段本已下跌超过 5%(当天科技股整体走弱)。

Ramaswami 在电话会上把 Nutanix 的历史分成三章:第一章是他上任前,公司在超融合基础设施(HCI)领域确立领导地位;第二章是他任内,公司转型订阅制软件、实现盈利增长,产品从 HCI 扩展成跨云、支持外部存储、具备云原生能力的平台;第三章则是 AI。文章还提到,他今年 4 月在 theCUBE 上讲过 Nutanix 正在从 HCI 转向"解耦式基础设施"(disaggregated infrastructure),以支撑自主 AI agent 的需求。董事会成员 Virginia Gambale 的评价也落在同一点:订阅制转型、全球企业客户基础、以及"为 AI 时代做好准备"的技术组合。顺带一提,Ramaswami 当年是在辞去 VMware 首席运营官两天后加入 Nutanix 的,VMware 随后起诉他违反职责,一年后庭外和解——这段历史说明 Nutanix 与 VMware 的竞争关系从一开始就写在这家公司的基因里。

个人看法:这件事要放在今天同一批的几篇财报里一起看。[Workday](2026-11-24-workday-shares-fall-as-soft-subscription-forecast-overshadows-third-quarter-beat.md) 是"单季度超预期、订阅指引偏软、股价下跌",[HPE](2026-11-23-hpe-s-stock-slides-despite-record-revenue-growth-and-upbeat-forecast.md) 是"营收创纪录、指引上调、股价照样下跌",Nutanix 则是"单季超预期、全年指引略低于预期、再叠加 CEO 交接"。三家的共同点是:市场已经不太为企业 IT 软件/硬件的稳健增长买单,而是在问"AI 到底给你带来了多少增量"。按"先找瓶颈"的思路,企业 AI 落地现在卡住的地方大致有三层:第一是算力,企业自建 GPU 集群贵且利用率低;第二是数据和存储,企业数据分散在私有云、公有云和边缘,模型很难直接用起来;第三是运维和编排,也就是 [KubeCon 那篇](2026-11-16-at-kubecon-2026-the-illusion-of-ai-control-meets-the-reality-of-implementation.md) 里 Nutanix 的 Dan Ciruli 所说的,Kubernetes 正在成为部署包括 AI 在内所有负载的标准 API。Nutanix 想卡的是第二和第三层,也是 [Tokenomics 那篇](2026-11-21-tokenomics-putting-a-price-on-intelligence.md) 里其首席 AI 官用"买房、长租、Airbnb"类比讨论的那一类"自建 vs 租 GPU vs 按 token 付费"的决策——Nutanix 的机会在于做"买房"那一档客户的底层平台。它还出现在 [ChronoScale 与 STN 合资](2026-11-19-chronoscale-and-stn-form-jv-to-develop-data-center-campus-in-odessa-texas.md) 的出资方名单里,说明它也在尝试往 AI 数据中心的上游靠。

对 AI 板块来说,这条新闻的含义偏中性:它不改变算力基础设施(GPU、网络、数据中心)这一层的确定性,但再次说明企业软件中间层的估值逻辑在切换——受益的层次仍然是第一层的芯片和数据中心,第二层是能真正把企业数据接进 AI 的存储与数据平台,第三层才是 Nutanix 这种跨云编排平台,而第三层能不能吃到 AI 增量,还要看新 CEO 的方向。另一个我会关注的背景是 Broadcom 收购 VMware 后的授权调整,这一直被视为 Nutanix 迁移客户的机会(原文没提,是我自己的延展),新 CEO 如果来自 AI 或云原生背景,大概率会加速"第三章";如果来自传统企业销售背景,更可能是继续收割 VMware 迁移需求。

现在判断还早,继任者是谁、来自哪里,比这一季的数字更能说明 Nutanix 的方向。值得跟踪的信号是下一两个季度它的 AI 相关产品是否开始单独披露收入或客户数,如果一直只停留在"为 AI 时代做好准备"的表述,市场的怀疑大概不会消散。
