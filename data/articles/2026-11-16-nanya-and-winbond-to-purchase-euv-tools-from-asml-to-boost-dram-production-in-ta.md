# Nanya and Winbond to purchase EUV tools from ASML to boost DRAM production in Taiwan
https://www.datacenterdynamics.com/en/news/nanya-and-winbond-to-purchase-euv-tools-from-asml-to-boost-dram-production-in-taiwan/

这条消息看起来是两家二线内存厂的设备采购,但它说明的是一件更大的事:EUV 光刻正在从"只有三星、SK 海力士、美光这样的头部 DRAM 厂才用得起的工具"往下渗透到二线厂商。DRAM 微缩到 1β、1γ 以后,不用 EUV 就得靠多重曝光,步骤多、良率低、成本高;二线厂如果不上 EUV,就会在制程上被永久拉开。所以这既是内存供给扩张的信号,也是 ASML 单一供应商地位被再次确认的信号。

文章指出,据台湾当地媒体报道,南亚科技(Nanya Technology)和华邦电子(Winbond Electronics)都计划向 ASML 采购 EUV 光刻机,但两家都没有披露金额。南亚会在 2027 年第一季度把 EUV 部署到台湾北部的 Fab 5A,预计同年年底开始生产;公司董事会 8 月批准了 2026 到 2029 年最高 105.3 亿美元的一期设备投资,其中包含 EUV 预算;新厂 2028 年产能每月 3 万片晶圆,2030 年目标满产每月 5 万片。华邦则预计大约两年后收到第一台 EUV,希望 2030 年在高雄厂用 EUV 生产第二代 14nm DRAM。文章还提到,High-NA EUV 每台约 3.7 亿美元,约是普通 EUV 的两倍,但每次曝光需要的光更少、单层打印时间更短;三星计划 2028 年起把 High-NA 用于内存芯片,台积电 2030 年起使用。(文章说 High-NA 是制造 3nm 和 5nm 芯片所必需的,这个表述并不准确,目前 3nm/5nm 量产用的是普通 EUV,High-NA 主要面向更往后的节点。)

个人看法:这篇要放在 AI 内存短缺的大背景里看。AI 服务器把 DRAM 产能大量吸到 HBM 和高容量 DDR5 上,三大厂优先保 HBM,普通 DRAM 和利基型 DRAM 的供给就被挤压,这是二线厂敢在这个时点上 EUV、砸百亿美元扩产的原因。和之前 [美光因劳资纠纷暂停 45 亿美元内存厂建设](2026-11-08-ongoing-labor-dispute-sees-micron-pause-construction-at-its-4-5bn-memory-fab-in-.md) 那篇对比,内存扩产卡住的地方各不相同:美光卡在建厂和劳动力,南亚和华邦卡在设备交期——华邦要等大约两年才能拿到第一台 EUV。

按瓶颈去找受益层次:第一层是 ASML,作为 EUV 唯一供应商,每一个想留在先进 DRAM 牌桌上的厂商最终都要排它的队,二线 DRAM 厂加入等于扩大了它的客户面;第二层是 EUV 配套链,包括光刻胶、光罩和光罩检测(比如 Lasertec、KLA)、以及涂胶显影设备(Tokyo Electron),EUV 渗透到新客户,这些环节会同步受益;第三层才是 DRAM 厂商本身,南亚和华邦的产能要到 2028 年之后才释放,短期承担的是资本开支压力。对 AI 板块来说,这条消息意味着 2028 年以后通用 DRAM 供给会有一定缓解,对算力基础设施整体是中性偏利好。对 edge AI 板块有一层间接联系:华邦在利基型、低功耗 DRAM 和 NOR Flash 上是重要供应商,这类内存大量用在边缘设备和终端 AI 模组里,如果它的 14nm 级 DRAM 按计划在 2030 年量产,边缘设备的内存成本和功耗会受益——但这个时间点太远,只能算长期观察。

现在能确认的只有采购意向,具体台数、金额、交期都没有公布。值得跟踪的是 ASML 下一次财报里来自内存客户的 EUV 订单占比有没有明显上升,以及南亚 Fab 5A 2027 年底能否按时投产——那是二线厂 EUV 能否真的跑通量产的第一个检验点。
