# FCC clears SpaceX to put up to 1 million Starmind data centers in space
https://siliconangle.com/2026/11/25/fcc-clears-spacex-to-put-up-to-1-million-starmind-data-centers-in-space/

轨道数据中心这个叙事过去一年一直卡在"技术上能不能做、钱从哪来"两个问题上,这条新闻第一次把一个监管层面的问号去掉了:美国监管机构正式承认"太空数据中心星座"是一种可以被发牌照的东西。它并不证明这件事能成,但它把太空算力从概念推进到了有时间表、有违约条件的阶段。

文章指出,SpaceX 获得美国联邦通信委员会(FCC)批准,可以部署最多 100 万颗被设计成在轨数据中心的 Starmind 卫星。这项由 FCC 太空局在授权范围内发出的命令,被 FCC 称为"美国历史上第一份太空数据中心星座的授权"。按批准条款,Starmind 卫星分布在 500 到 1002 公里之间的六个轨道壳层,低于 SpaceX 原申请里 2000 公里的上限;大部分通信走与其他卫星(包括 Starlink)之间的光链路,牌照本身覆盖的是一套用于紧急遥测、跟踪和指令的 Ka 波段备份无线电系统。

批准是有条件的,而这些条件恰好就是这件事的难点。第一是轨道碎片,SpaceX 的碎片处置计划只在 600 公里以下被认定合规,而六个壳层里有四个在这条线以上,部署更高轨道之前必须另外提交修改申请和最终碎片计划;让部分高轨卫星退役到绕地或绕日的弃置轨道、而不是五年内再入大气层的请求,也因信息不足被搁置。第二是时间表,SpaceX 必须在 2033 年 11 月 25 日前让第一颗 Starmind 投入运行,之后 2035 年达到 10 万颗、2038 年 50 万颗、2040 年 100 万颗,错过任何一个节点牌照就作废。第三是反对意见,Amazon 的 Amazon Leo 卫星业务、Viasat 和美国天文学会(American Astronomical Society)的驳回申请都被拒绝,Amazon 3 月曾把这个计划形容为"远大抱负而不是真实计划";FCC 认为规则里没有限制单一星座的卫星数量,天文学家关于红外亮度的担忧也被认定不属于无线电牌照的审查范围。

技术路线上,文章提到第一代 Starmind 卫星 AI1 围绕一个太空优化版的英伟达 Vera Rubin NVL72 机柜级系统打造,Musk 称最早可能在明年第三季度入轨。这和之前那篇 [SpaceX 为轨道数据中心定制 Vera Rubin 机架 Kessel](2026-11-12-spacex-developing-custom-nvidia-vera-rubin-rack-dubbed-kessel-for-its-orbital-da.md) 对得上,说明 SpaceX 的硬件路线一直是 NVL72 的改造版。竞争者方面,文章提到 Blue Origin 3 月申请了最多 51600 颗数据中心卫星的 Project Sunrise,创业公司 Starcloud 8 月以 23 亿美元估值融资 2.5 亿美元。当天 SpaceX 股价收涨 1.3%。

个人看法:这件事最值得注意的是牌照的结构——它其实是一张"按里程碑兑现"的期权,而不是一张通行证。用"先找瓶颈"的思路看,监管这一层的瓶颈现在算是松开了,但剩下的瓶颈一个都没变:第一是融资,之前那篇 [Chips can survive the space environment — can their financing?](2026-11-21-chips-can-survive-the-space-environment-can-their-financing.md) 讲过,贷方要求以芯片作抵押的融资不能用于轨道部署,[440 亿美元的 SpaceX GPU 融资](2026-11-23-apollo-and-goldman-sachs-lead-44bn-spacex-gpu-financing-deal.md) 也明确落在地面;第二是散热和表面积,这在 [发射变便宜后航天器瓶颈从质量转向表面积](2026-08-14-cheaper-launch-has-moved-the-spacecraft-bottleneck-mass-is-out-surface-area-is-in.md) 那篇里已经讲过;第三是碎片,FCC 这次只对 600 公里以下放行,本身就是在告诉市场高轨部分还没想清楚。所以如果太空数据中心真的走下去,受益的层次会是:第一层仍然是英伟达,AI1 本身就是 Vera Rubin 的改造;第二层是发射和星间光链路,也就是 SpaceX 自己的 Starship 和 Starlink 体系,以及做光通信终端的供应商;第三层是航天级电源和热控,太阳能阵列、电源转换、辐射散热板,这是太空数据中心真正的物理瓶颈;第四层是在轨服务和空间机器人,100 万颗卫星的规模意味着维护和退役不可能靠人工,这是太空经济板块和机器人板块的交汇点。对太空经济板块来说这是明确的利好信号,对 AI 板块是边际利好(多了一个长期算力出口),但兑现时间以年计。

现在离第一颗 Starmind 上天最早也还有将近一年,离 10 万颗的里程碑更是十年量级,只能观望。值得关注的是 AI1 能不能按 Musk 说的明年第三季度入轨,以及 SpaceX 什么时候为 600 公里以上的壳层提交最终碎片计划——这两个节点会比任何估值叙事都更早告诉我们这件事是真是假。
