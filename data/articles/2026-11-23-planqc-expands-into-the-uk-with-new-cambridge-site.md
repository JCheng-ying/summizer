# planqc Expands Into the UK With New Cambridge Site
https://thequantuminsider.com/2026/11/23/planqc-expands-into-the-uk-with-new-cambridge-site/

(说明:原文为 planqc 的公司新闻稿,"最快、最可扩展的平台""可扩展到数百万量子比特"等表述属于公司自述,未经独立验证。)

这篇新闻稿表面上是一家德国量子公司在英国开了一个分部,背后更大的命题是:中性原子路线正在从"实验室里能做出几百个比特"走向"如何把比特数扩展到数百万",而扩展这一步的瓶颈越来越落在光学和激光工程上,而不是量子物理本身。

文章指出,planqc 成立了 planqc UK Ltd,在剑桥建立一个完整的中性原子实验室,用于量子计算系统的组装、集成和调试,包括激光和光学子系统,目标是从英国直接交付系统,公司在英国的投入是"两位数百万"级别。未来两年剑桥团队会招量子硬件工程师、纠错与系统集成工程师、软件和 FPGA 工程师,中期目标大约 20 人,其中部分岗位由慕尼黑和剑桥的现有同事转岗。技术合作方是剑桥大学卡文迪许实验室 Ulrich Schneider 教授的团队,双方一起开发下一代光晶格(optical lattice)技术。英国子公司由联合创始人兼 CTO Sebastian Blatt 负责。

技术上需要精确区分两种囚禁原子的方式。planqc 现在用的是光镊阵列(optical tweezer array),每一个原子由一束聚焦激光单独"夹住",阵列规模是数千个囚禁位点;文章提出的补充方案是光晶格,即多束激光相互重叠形成周期性的光强图案,天然产生可能多达数百万个完全相同的囚禁位点,再往里面装填原子。可以类比成:光镊是一个一个搭积木,光晶格是先浇筑出一整块蜂窝结构再往格子里放东西。后者在规模上天然占优,但对激光稳定性、相位控制和真空系统的要求也更高。文章还提到 Blatt 过去研究的是世界上最精确的原子钟,而光晶格原子钟用的正是同一套技术,这解释了为什么这家公司押注这条路线。

关于公司本身,文章给出的数字是:员工超过 130 人,种子轮和 A 轮共融资 5500 万欧元,另有 2900 万欧元的 DiNAQC 合同和 1910 万欧元的 MAQCS 联合体项目,合计超过 1 亿欧元。ARM 联合创始人、Amadeus Capital Partners 的 Hermann Hauser 自 2023 年起是投资人兼顾问委员会成员。在德国,planqc 正在为德国航空航天中心(DLR)和莱布尼茨超算中心(LRZ)建造量子计算机,并和空客、欧洲航天局(ESA)、弗劳恩霍夫研究所等合作开发早期应用;剑桥之前,它已经在因斯布鲁克设立了子公司。英国这边的应用重点是伦敦的金融服务和剑桥的制药与生命科学。另外文章强调 planqc 使用欧洲本土的激光、光子学和真空技术供应商。

这一点和 [Draft EU Quantum Act would favor European suppliers](2026-11-10-draft-eu-quantum-act-would-favor-european-suppliers-set-computing-and-security-t.md) 以及 [UK announces new funding to support quantum technology commercialisation](2026-11-08-uk-announces-new-funding-to-support-quantum-technology-commercialisation.md) 可以连起来看:欧洲和英国都在用政策和公共采购扶持本土量子供应链,planqc 的公共项目合同金额几乎和它的股权融资一样大,说明这个阶段欧洲量子公司的主要客户仍然是政府和超算中心。同样是中性原子路线,[Pasqal integrates quantum processors with Slurm](2026-11-19-pasqal-integrates-quantum-processors-with-slurm-hres.md) 走的是融入 HPC 调度体系的方向,两家公司在欧洲是直接竞争关系。

个人看法:中性原子路线目前的瓶颈可以拆成三个:第一是规模,原子阵列能不能从几千扩展到几十万甚至百万;第二是纠错,比特多了之后能不能形成足够多的逻辑比特;第三是速度,中性原子门操作相对慢,影响实际运算效率。光晶格主要解决的是第一个瓶颈,所以从投资角度看,真正受益的是解决"规模"这一层的上游:高功率、高稳定性的激光器和光学元件(比如 Coherent、IPG Photonics、德国的 TOPTICA 和 TRUMPF 这类激光与光子学厂商),以及超高真空系统供应商。这和超导路线依赖稀释制冷机(Bluefors、Oxford Instruments)是同一个道理——每条路线都有自己的"卖铲子"层。对量子计算板块来说,这是一个偏长期的利好信号,但要注意 planqc 是未上市公司,剑桥站点只有约 20 人规模,目前更多是研发布局而不是产能扩张。现在判断哪条路线胜出还太早,值得关注的是 planqc 交付给 LRZ 和 DLR 的系统最终达到多少比特、纠错指标如何,以及光晶格方案什么时候真正出现在产品路线图里。
