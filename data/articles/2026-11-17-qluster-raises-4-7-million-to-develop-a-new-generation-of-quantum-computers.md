# Qluster Raises €4.7 Million to Develop a New Generation of Quantum Computers
https://thequantuminsider.com/2026/11/17/qluster-raises-e4-7-million-to-develop-a-new-generation-of-quantum-computers/

(说明:这是 Qluster 的新闻稿,"室温下数百万量子比特"等说法出自公司和投资方,未经独立验证。)

量子计算过去十年的竞争基本是"量子比特本位"的:先选一种量子比特技术,再想办法把它做多、做好。这篇文章背后的命题是这个顺序可能要反过来——先从要解决的工业问题算出需要多少资源,再倒推机器应该长什么样。如果这种"架构优先"的方法论成立,量子计算的竞争焦点会从单个量子比特的保真度,转向整台机器的资源效率。

文章指出,总部位于巴黎的 Qluster 完成了 470 万欧元的 pre-seed 融资,由量子技术专业基金 Quantonation 领投,Quantum Launchpad 和法国公共投资银行 Bpifrance 支持。Qluster 是 Laboratoire Kastler Brossel(卡斯特勒-布罗塞尔实验室)的衍生公司,成立仅几个月,四人团队:CEO David Fainsin、CTO Ambroise Boyer、COO Clarisse Thibault(曾在 CNRS Innovation)、CSO Valentina Parigi(索邦大学教授)。公司已经拿到 2026 年 i-Lab 大奖,资金将用于建自己的研发实验室,并招募实验物理、量子计算理论和架构方面的人才。目标是 2032 年做出可解决初步工业问题的中等规模量子计算机,2036 年做出大规模容错的通用量子计算机。

技术路线上可以拆成两部分。第一是连续变量光量子计算:用光的电磁场的连续性质来编码信息,生成被称为"cluster"的纠缠态,作为量子运算的资源;文章认为这种方式可以在室温下处理大量量子模式,更易扩展和稳定。Qluster 的基础是 Parigi 和 Fainsin 在实验室开发的一种已获专利的微型光子源,原理已在期刊上发表并经实验验证。第二是"Architecture First":把业务问题翻译成量子电路,算出所需的量子比特数、电路深度、执行速度和能耗,再据此设计机器架构。文章说这种方法在北美和日本已有大量投资,在欧洲还比较少。

个人看法:光量子这条线最近已经写了好几篇。[Xanadu 和 HyperLight 降低光开关损耗](2026-11-10-xanadu-and-hyperlight-reduce-photonic-switch-loss-to-7-mdb.md)里的 Xanadu 同样走连续变量路线,而今天的 [QuiX 室温单光子探测器](2026-11-17-quix-quantum-and-partners-develop-near-room-temperature-detectors-for-photonic-q.md)走的是离散变量(单光子)路线。两条路线的差别可以简单说成:离散变量用"有没有一个光子"编码,难点在于确定性地产生和探测单个光子;连续变量用光场的振幅和相位编码,大规模纠错态更容易生成,但要实现通用和容错,通常仍需要非高斯资源(比如 GKP 态),这一步往往又依赖光子数分辨探测,而这类探测器多数仍然要低温。所以"室温下数百万量子比特"这句话来自投资方,只能当作愿景,而不是已经证明的结论。

至于"Architecture First",我的理解是它对应的就是资源估算,和之前 [24 个量子计算可能有优势的问题](2026-11-08-study-maps-24-problems-where-quantum-computers-could-gain-an-edge.md)那篇是同一个思路——先问"什么问题值得算、要多少资源",再谈硬件。方法本身是对的,但它更像是一种设计哲学,很难构成壁垒,任何整机公司都可以这么做。

投资角度先找瓶颈:光量子的瓶颈仍然是损耗和非高斯资源的产生,而一家刚成立、470 万欧元 pre-seed 的公司,距离解决这些瓶颈还有十年的路线图。这篇真正的信号不在 Qluster 本身,而在资本结构:Quantonation 是欧洲量子领域最活跃的早期基金,Bpifrance 代表法国国家资本,这和 [欧盟量子法案草案](2026-11-10-draft-eu-quantum-act-would-favor-european-suppliers-set-computing-and-security-t.md)、Planckian 拿到 EIC 支持是同一条线——欧洲在用公共资本 + 专业基金的组合,在光子这个它自认为有优势的领域多点下注。受益的层次会是:第一层是光子供应链,包括非线性光学晶体、低损耗波导、高效探测器,不管 CV 还是 DV 路线都需要;第二层是已经有硬件交付的光量子公司,比如 Xanadu、Quandela、QuiX,新进入者越多,说明这条路线的人才和资本池在变大。这挂在量子计算板块上,但影响非常间接。

现在太早,只能观望。值得关注的是 Qluster 能否在实验室阶段把专利光子源的 squeezing 水平和集成度做成可公开比较的指标,以及它会不会在 2027–2028 年拿到更大一轮融资——种子期之后的融资规模,才是市场对这条路线信心的真实读数。
