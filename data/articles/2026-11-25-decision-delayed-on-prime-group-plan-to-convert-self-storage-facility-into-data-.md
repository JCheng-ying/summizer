# Decision delayed on Prime Group plan to convert self-storage facility into data center in South Carolina
https://www.datacenterdynamics.com/en/news/decision-delayed-on-prime-group-plan-to-convert-self-storage-facility-into-data-center-in-south-carolina/

这条地方新闻有意思的地方在于规模:这不是一个几百兆瓦的园区,只是把一个自助仓库三分之二的面积改成 5MW 的"AI 推理点"。连这么小的项目也开始遭遇社区阻力,说明数据中心选址的社会许可问题已经从超大规模园区蔓延到了分布式边缘推理节点。

文章指出,南卡罗来纳州 Greenville 县议会一致投票将一个数据中心项目退回规划与开发委员会,实际上推迟了决定。这个项目申请把 Taylors 一块 4.76 英亩的地块从商业用地改为 S1 服务区用地,以建设一个 5MW 的"AI inference point";地块上现在是 Prime Storage 运营的自助仓库,约三分之二的建筑会改作数据中心,其余继续作为仓库。县规划委员会上个月已经建议批准,县工作人员也认为这符合县综合规划,但 Change.org 上反对该项目的请愿已有近 1900 人签名,下一次委员会会议在 11 月 30 日。

文章还交代了 Prime 的整体布局。房地产公司 Prime Group Holdings 通过 Prime Storage 在美国拥有数百处自助仓库资产,今年早些时候宣布在部分仓库站点部署边缘数据中心和电池储能系统(BESS);通过关联公司 Edge Inference LLC,它已经在马萨诸塞州 Swansea 和佐治亚州 Marietta 提交了建设"AI 推理点"的申请,还计划在南卡 Surfside Beach、佐治亚 Holly Springs 和弗吉尼亚 Norge 的仓库部署算力。但在马萨诸塞州 Salem,地方委员会已经撤销了项目许可,市长提出了禁止数据中心的分区条例,州长 Maura Healey 最近也签署了限制未来数据中心的行政令。

个人看法:Prime 这个模式本身是一个挺聪明的 edge AI 落地思路。推理和训练不同,训练可以集中到偏远的吉瓦级园区,推理却需要靠近用户以降低延迟,而自助仓库恰好有三个天然优势:第一,遍布城郊、离人口近;第二,建筑大、用电低,有现成的电力接入和空余面积;第三,和 BESS 组合后可以削峰填谷,减轻对本地电网的冲击。如果 5MW 这种规模的推理点能批量复制,它会是"AI 推理下沉到城市边缘"最务实的实现方式之一。

但先找瓶颈,这篇文章恰恰说明瓶颈已经不是技术或资本,而是审批和社区接受度。它和 [堪萨斯 Ottawa 通过 10 年数据中心暂停令](2026-11-11-10-year-data-center-moratorium-approved-in-ottawa-kansas.md)、[Loudoun 县正式通过 12 个月暂停令](2026-11-18-virginia-s-loudoun-county-officially-adopts-12-month-moratorium-on-data-center-d.md)、以及 [Kraft Group 在马萨诸塞州 Sutton 的 900MW 园区计划](2026-11-11-kraft-group-could-build-900mw-data-center-campus-in-sutton-massachusetts-investi.md) 所面对的州层面限制是同一股力量,区别只是现在连贴近社区的小型推理点也被一并抵制——而越是贴近人口的边缘站点,越容易遇到邻避。所以受益的层次会是:第一层是能把推理节点做得"看不见"的方案,也就是嵌在现有建筑、电信机房、基站和企业园区里的小型推理设备,它们不需要改变用地性质,这挂在 edge AI 板块上;第二层是 BESS 和表后储能,Prime 把储能和数据中心打包申请,储能本身对社区和电网的"友好度"是项目能否获批的筹码,这挂在能源板块上;第三层才是 Prime 这类地产转型者,它们的价值取决于审批通过率,目前看并不乐观。

现在只是推迟,不是否决,结论还看 11 月 30 日的委员会会议。值得关注的是 Prime 在佐治亚和弗吉尼亚等对数据中心相对友好的州能否顺利获批,如果南方州也开始对 5MW 级别的推理点设限,那"推理下沉到社区"这条路就得换成更隐蔽的形态。
