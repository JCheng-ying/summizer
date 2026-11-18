# Stalled data center buildouts send inference chips hunting for space in telco and colo sites
https://siliconangle.com/2026/11/18/ai-data-centers-delays-push-inference-chips-existing-sites-sc26/

先说明利益相关:这是 SiliconANGLE 旗下 theCUBE 在 SC26 上对 SambaNova 产品副总裁的访谈,该节目片段由 NYSE Wired 赞助,内容基本是 SambaNova 自己的说法,产品性能和市场判断都按"未经独立验证"处理。但它提出的命题值得记下:如果新数据中心的建设速度跟不上推理需求,那么推理芯片的竞争维度就不只是性能和价格,还包括"能不能塞进已有的老机房"。

文章指出,推理需求正在跑赢新 AI 数据中心的建设速度,电力、资本和审批延误把新增容量越推越远,于是芯片厂商开始在已有设施里找空间。SambaNova 的 Anton McGonnell 认为,许多老的电信机房和托管机房有空间也有电,但大多数没法承载今天高密度、液冷的 GPU 机柜,除非花大钱改造;新一代 GPU 机柜可能需要加固地板和每柜 120 到 250 千瓦的电力,而电力和冷却设备本身还有 18 到 24 个月的交货期。这就给风冷推理系统留出了机会。

技术上,文章把推理拆成两个阶段:预填充(prefill)是处理输入、计算密集的阶段;解码(decode)是逐个生成输出 token、瓶颈在数据搬运的阶段。SambaNova 第五代芯片 SN50 专攻解码,机柜保持风冷、重量也轻,能放进现有设施;预填充则交给合作伙伴,SC26 上它展示的是用 Intel 的 D-Series GPU 做预填充、SambaRack SN50 做解码的风冷异构方案。McGonnell 称 Intel 这颗芯片在预填充上性价比高得多,因为预填充是计算受限问题,所以它干脆不用 HBM。文章还提到,SambaNova 在 7 月的估值为 110 亿美元。

个人看法:这篇和 [英伟达想改造 Brightspeed 局端机房那篇](2026-11-09-nvidia-looks-to-tap-brightspeed-central-offices-for-inference-network-report.md) 是同一个问题的两种解法。那篇里英伟达的思路是"改造老机房去适配 GPU",瓶颈落在电力和冷却升级;这篇里 SambaNova 的思路是"改造芯片去适配老机房",用风冷和低功率密度直接绕过改造。再加上 [Arista 押注分布式推理那篇](2026-11-17-arista-takes-aim-at-the-next-ai-network-battleground-distributed-inference.md),推理下沉的路线越来越清楚。

更值得关注的是"预填充/解码分离"(disaggregated inference)这个架构趋势。目前推理硬件大概有三种组合方式:1. 同一种 GPU 同时做预填充和解码,也是现在的主流;2. 同一家厂商用两种不同芯片分别优化两个阶段;3. 像这篇这样,不同厂商的芯片按阶段拼在一起,预填充用不带 HBM 的高算力芯片,解码用带宽优化的专用芯片。第三种如果走通,意味着推理不再必须买一整套英伟达系统,这对 [Fractile](2026-11-11-british-inference-chip-developer-fractile-raises-720m-in-funding.md) 这类专注推理的挑战者是结构性机会,对 HBM 的需求结构也会有影响,预填充那一侧可能不再需要昂贵的 HBM。

先找瓶颈:这里的瓶颈是新机房的交付速度,以及电力冷却设备 18 到 24 个月的交货期。受益的层次会是:第一层是能在低功率密度、风冷条件下跑推理的芯片厂商,SambaNova、Groq、Fractile 这类推理专用芯片,以及 Intel 这种在预填充上找到新定位的厂商,挂 AI 板块;第二层是手握大量存量机房的电信运营商和托管商,它们的闲置空间重新有了价值,这一层和推理下沉到离用户更近的位置直接相关,挂 edge AI 板块;第三层是网络,异构推理意味着预填充和解码之间要高速传输 KV cache,对机柜间网络提出更高要求。

不过这些都来自厂商访谈,SambaNova 没有给出任何客户部署数量或性价比数据。值得跟踪的是有没有电信运营商或托管商公开宣布部署风冷推理机柜,以及 Intel D-Series 是否在其他异构推理方案里出现。
