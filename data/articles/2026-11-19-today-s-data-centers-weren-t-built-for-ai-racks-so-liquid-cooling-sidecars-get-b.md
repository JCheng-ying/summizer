# Today’s data centers weren’t built for AI racks, so liquid-cooling sidecars get bolted on
https://siliconangle.com/2026/11/19/deployment-services-drive-supermicro-s-race-time-online-sc26/

先说明利益相关:这篇是 SiliconANGLE 旗下 theCUBE 在 SC26 对 Supermicro 首席营收官 Matthew Thauberger 的访谈,theCUBE 是 SC26 的付费媒体合作方,内容基本是 Supermicro 高管的自述,关于液冷产能"最大"等说法未经独立验证。

这篇访谈背后的命题是:AI 基础设施的竞争维度正在从"谁能卖出更多 GPU 服务器"转向"谁能让一座 AI 工厂最快跑起来"。文章的说法是,服务器厂商过去比拼 time to market,现在被考核的是 time to production。

文章指出,Supermicro 在 7 月报告了 600 亿美元的订单积压,并把它的服务器"积木式"模式扩展到整个数据中心层面。Thauberger 的说法是,neocloud 希望工厂尽快运转,企业客户也开始把推理和 agentic AI 视为长期需求;客户向 Supermicro 提出的两大需求是"分配"和"部署服务",也就是在供给受限的环境下能多快拿到货、多快上线、多快派人到现场部署,Supermicro 的服务团队会负责把系统拉起来、跑通客户负载之后再交付。另一个障碍是老旧机房:很多设施在设计时没有考虑现代 AI 机架的液冷和功率密度,所以 Supermicro 提供侧挂式液冷单元(sidecar)和列间冷却液分配单元(in-row CDU)这类改造方案,同时在产品线里加入预组装的 AI 机架来缩短安装时间。Thauberger 还强调公司在加州拥有大规模液冷产能,作为美国总部公司可以更快在美国境内部署。

技术上需要说清楚 sidecar 是什么:传统风冷机房没有设施级的液体回路,直接液冷(冷板贴在 GPU 上)需要冷却液在机架内循环,再把热量交换出去。侧挂单元相当于在机架旁边放一个自带液-气换热器的柜子,把冷板回来的热量在本地交换成热风,再交给机房原有的空调处理。它的好处是不用改造建筑的冷冻水系统,代价是最终散热仍然受制于机房原有的风冷能力,所以它更像是一个过渡方案,而不是高密度 AI 机房的终局。

个人看法:这篇和前两天 [CoolIT 与 Ecolab 推出 3MW CDU](2026-11-18-coolit-ecolab-launch-3mw-cdu.md)、[Dell 押注液冷软件定义存储](2026-11-17-dell-bets-liquid-cooled-software-defined-storage-can-keep-ai-factories-fed.md)、[三星洽购 Modine](2026-11-13-samsung-in-talks-to-acquire-data-center-cooling-company-modine-manufacturing-rep.md) 是同一条线索:液冷已经从可选项变成 AI 部署的前置条件,大家都在抢这个环节。我的框架是,机房适配 AI 机架目前来看有三种方式:1. 新建原生液冷机房,性能最好但周期最长,还会撞上之前反复写到的电力瓶颈;2. 在老机房上做 sidecar 和 CDU 这类改造,上线最快,但密度受原有风冷能力限制;3. 预制模块化数据中心,把机架、冷却、电力在工厂里集成好再整体运过去。Supermicro 这次讲的其实是 2 和"预组装机架"这半步 3,本质是在卖"缩短上线时间"。

投资角度,先找瓶颈:瓶颈有两个,一是 GPU 分配本身仍然紧张,二是现有机房的散热和功率密度跟不上 AI 机架。解决第二个瓶颈的那一层才是这篇真正利好的:第一层是液冷关键部件和 CDU 厂商,比如 Vertiv、CoolIT、Modine,以及冷却液和冷板供应链;第二层是能提供整机柜集成和现场部署服务的系统厂商,Supermicro、Dell 都在这一层,但要注意 Supermicro 的 600 亿美元积压是它自己报的数字,积压能否按时转成收入还要看 GPU 分配和交付执行;第三层仍然是 GPU 本身,NVIDIA 和 AMD 是这一切的源头需求。对 AI 板块来说,这是算力基础设施层继续确定性受益的又一个证据;对能源板块的间接含义是,老机房改造上 AI 机架会推高单机房功率密度,进一步加剧电力约束。

这篇信息量有限,主要是厂商立场的表述。值得跟踪的是 Supermicro 下一季财报里积压转收入的速度,以及液冷改造方案在老机房里实际能支撑到多高的单机架功率。
