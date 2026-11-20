# Nexalus and Renda launch liquid-cooled AI server for data center retrofit market
https://www.datacenterdynamics.com/en/news/nexalus-and-renda-launch-liquid-cooled-ai-server-for-data-center-retrofit-market/

这篇新闻背后的命题是:AI 算力的下一批增量,很可能不是来自新建的液冷园区,而是来自大量现存的风冷机房——前提是有人能把"液冷"装进一台不需要改造机房的服务器里。新建液冷数据中心要等电力接入、管道、CDU 和审批,而存量风冷机房已经有电、有机柜、有客户,卡住它们的只是散热能力。

文章指出,爱尔兰科克的散热厂商 Nexalus 和英国服务器厂商 Renda 联合推出了 Renda Nova8:一台 4U 单机,内置八颗 Nvidia Blackwell GPU,把 CPU、内存、存储、电源和冷却全部集成在机箱内,可以直接塞进现有风冷机房的标准 19 英寸机柜,厂商的说法是运营方"不需要新增管道或冷却基础设施"就能替换现有设备。技术上它用的是 Nexalus 的射流冷却(jet cooling):冷却液不是在冷板的流道里流过,而是直接喷射到冷板上,厂商称这样可以在一个 4U 机箱里压住满功率运行的 CPU 和八颗 GPU,相比同类风冷配置能效提升 22%,AI token 吞吐最多提升 20%。需要说明的是,这是两家公司的联合声明,能效和吞吐数字都是厂商口径,未经独立验证。文章还提到,两家公司把为 F1 车队冷却 GPU 服务器的经验用在了这款产品上(称与 11 支车队中的 8 支合作),而 Nexalus 已经和 HPE 等服务器厂商合作,把液冷技术用进对方的系统。

把它和这两天写过的几篇放在一起看,散热路线其实已经分出三种做法:第一是改造机房,加 CDU 和二次侧管道,比如 [CoolIT 和 Ecolab 的 3MW CDU](2026-11-18-coolit-ecolab-launch-3mw-cdu.md);第二是机柜旁挂"液冷边车",在不动楼宇管道的前提下给几个机柜单独做液-气换热,也就是 [liquid cooling sidecars 那篇](2026-11-19-today-s-data-centers-weren-t-built-for-ai-racks-so-liquid-cooling-sidecars-get-b.md);第三就是这篇的思路,把液冷闭环整个收进服务器机箱里,对机房来说它仍然是一台"风冷设备"。和 [AI 推理服务器缩小到适配风冷机柜](2026-11-19-ai-inference-servers-shrink-to-fit-the-air-cooled-racks-enterprises-already-run.md) 那篇是同一个方向的不同解法——那篇是降低芯片功耗去迁就机柜,这篇是把散热能力塞进机箱去迁就机柜。

个人看法:先找瓶颈——存量机房跑不了高密度 GPU,卡的是单机柜散热和改造停机时间,而不是 GPU 供给。解决这个瓶颈的那一层才是受益方。受益的层次会是:第一层仍然是 GPU,无论是改造还是新建,Nvidia Blackwell 都在机箱里,这是确定性的部分;第二层是"机箱内液冷"这类散热技术供应商,Nexalus 这种小公司本身不是上市标的,但它向 HPE 这类整机厂授权,意味着价值可能沉淀在整机厂(HPE、Dell、Supermicro)的产品差异化上;第三层是机房改造这条更传统的路线,Vertiv、Schneider 这些做 CDU 和配电的公司,反而可能因为"机箱内闭环"方案的普及而少拿到一部分存量改造订单,这一点值得留意。整体上利好 **AI板块**的基础设施层,对 **能源板块**是间接的——能效提升 22% 如果成立,同样电力能跑更多算力,但这是厂商数字。需要克制的是,4U 塞八颗 Blackwell 的热密度非常高,射流冷却在长期运行下的可靠性、泵和喷嘴的维护成本都还没有公开数据。值得关注的是 HPE 等大厂是否把这类方案做成标准 SKU,以及有没有具名的存量机房客户披露部署规模。
