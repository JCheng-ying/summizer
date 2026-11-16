# Amazon loses 40 satellites after ULA rocket launch anomaly
https://www.datacenterdynamics.com/en/news/amazon-loses-40-satellites-after-ula-rocket-launch-anomaly/

这次失败把低轨宽带竞争里最脆弱的一环暴露得非常直接:对 Amazon Leo 来说,卫星不是瓶颈,能可靠、高频地把卫星送上天的火箭才是。一枚火箭的失败,损失的不只是 40 颗卫星,而是一整段原本排好的发射节奏。

文章指出,11 月 15 日从卡纳维拉尔角起飞的 Leo Vulcan 1(LV-01)任务搭载了 40 颗 Amazon Leo 卫星,是亚马逊迄今单次数量最多的一批,也本应是与 ULA 合作的 38 次发射中的第一次。ULA 表示火箭在飞行约 10 分钟时出现异常,未能把载荷送入轨道,有效载荷全部损失;这是 ULA 自 2006 年由 Boeing 和 Lockheed Martin 的火箭部门合并成立以来第一次完全失败。根据发射直播的更新,级间分离、Centaur V 上面级点火和整流罩分离都按计划完成,最后一条更新显示火箭位于约 95 英里高度、速度超过每小时 11000 英里。文章援引 Ars Technica 的多方消息称,这次异常发生在芯级(booster stage),而不是 Centaur V 上面级或固体助推器。

这一点值得单独拆开看。Vulcan 今年 2 月出过固体助推器喷管异常,ULA 与供应商 Northrop Grumman、美国太空军等机构做了调查,5 月完成了成功测试。也就是说,这次大家原本最担心的是喷管问题会不会复发,结果如果 Ars Technica 的说法属实,出问题的反而是另一个部位。与此同时,LV-01 本身叠加了好几个"第一次":第一是首次使用缩短优化后的 Centaur V 上面级以装下更多卫星;第二是首次以六枚助推器构型飞行;第三是首次使用亚马逊出资在卡纳维拉尔角新建的专用垂直总装厂房和移动发射平台。新构型叠加新基础设施,本身就是风险集中的一次飞行,亚马逊自己的声明也承认"首飞任务尤其有风险"。目前原因还没查明,ULA 说暂时没有具体数据。

文章提到,按计划 LV-02 原本会在 LV-01 正常完成后"几周内"发射,亚马逊发射系统负责人上周还说 Vulcan 将发射第一代星座接近一半的卫星,是未来几年的"主力"。Amazon Leo 自 2025 年 4 月首发以来已经通过 14 次任务发射了近 400 颗卫星,另外还与 Arianespace、Blue Origin 和 SpaceX 签了发射合同,下一次是 Arianespace 的 Leo Europe 4,最早 11 月 23 日从库鲁发射 36 颗卫星。

个人看法:上周写 [Vulcan 复飞预告](2026-11-12-ula-s-vulcan-set-to-return-to-flight-with-first-amazon-leo-payload.md)时,我说值得关注的信号是 LV-02 的间隔——如果几周内能接着发,说明运力瓶颈开始松动。现在答案是反方向的:Vulcan 再次停飞几乎是确定的,而它原本要承担近一半的第一代星座。结合那篇文章里 FCC 把期限延到 2029 年 7 月完成整个星座、初步服务需要 578 颗卫星的背景,这次损失 40 颗卫星本身可以再造,真正难补的是发射窗口。按"先找瓶颈,再找解决瓶颈的那一层"来看,太空经济板块里受影响的层次会是:第一层,非 SpaceX 的可靠运力变得更稀缺,亚马逊分散下单的另外几家——Arianespace、Blue Origin 的 New Glenn——的议价能力和交付压力同时上升,而 SpaceX 作为竞争对手反而是在帮亚马逊发射的那个最稳定选项,这本身就说明了运力格局的不对称;第二层,ULA 母公司 Boeing 和 Lockheed Martin 的航天业务短期是负面的,如果故障最终被确认在芯级,BE-4 发动机所在的 Blue Origin 也会被牵连进调查,而 Northrop Grumman 的固体助推器这次可能反而洗清了一部分嫌疑,但这要等正式结论;第三层才是星座运营商本身,Amazon Leo 追赶 Starlink 的时间表大概率会后移。和 [AST SpaceMobile 坚持要自研火箭](2026-11-12-ast-spacemobile-presses-case-for-developing-own-launch-vehicle.md)放在一起看,星座公司对"运力被别人卡脖子"的担忧这次得到了一个很具体的例证。

对 AI 板块的影响相对间接:DCD 把这条新闻放在数据中心频道,是因为低轨星座被视为未来边缘连接和部分太空计算的承载层,但目前 Amazon Leo 还没商用,这次失败对算力需求本身没有直接冲击,这里就不硬挂了。

现在还在事故调查初期,原因、停飞时长都不清楚。值得关注的是两个信号:一是 ULA 和 Ars Technica 后续对故障部位的确认,如果确实在芯级,牵涉 BE-4 发动机,影响面会扩大到 New Glenn;二是 11 月 23 日 Arianespace 的 LE-04 能否按时发射,这会决定亚马逊短期内还剩下多少运力冗余。
