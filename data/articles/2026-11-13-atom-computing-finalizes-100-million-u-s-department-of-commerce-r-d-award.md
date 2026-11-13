# Atom Computing Finalizes $100 Million U.S. Department of Commerce R&D Award
https://thequantuminsider.com/2026/11/13/atom-computing-finalizes-100-million-u-s-department-of-commerce-r-d-award/

(说明:这篇是 Atom Computing 的公司新闻稿,由 The Quantum Insider 转载,属于利益相关方的自我陈述。文中"首个超过 1000 qubit 的平台""首家演示低于阈值纠错的中性原子公司"等技术里程碑,都是公司自己的说法,这里按未经独立验证处理。)

这篇新闻稿背后更大的命题是:美国政府对量子计算的支持方式,正在从"资助科研项目"变成"直接给单个公司的工程化和供应链扩产出钱"。如果这种模式持续下去,量子计算板块的竞争就不再只是比谁的 qubit 更多、保真度更高,而是比谁能拿到政府的长期资金,把实验室里的系统变成可以量产、可以交付的机器。

文章指出,Atom Computing 与美国商务部签署了最高 1 亿美元的协议,用于加速容错、实用规模(utility-scale)量子计算机的研发。这笔钱是今年早些时候意向书(Letter of Intent)的正式落地,而不是一笔全新的消息。新闻稿同时提到,Atom Computing 刚刚被选为唯一一家进入 DARPA 量子基准计划(Quantum Benchmarking Initiative,QBI)C 阶段的中性原子公司,该阶段潜在资金最高 3 亿美元。也就是说,这家公司在几周之内同时拿到了民用(商务部)和国防(DARPA)两条政府资金线的认可。

新闻稿把这 1 亿美元的用途拆成三块。第一是把关键技术放到公司内部自研,提高系统性能、可靠性和垂直整合程度;第二是扩建并行的工程和测试平台(testbed)基础设施,加快新方案的验证和产品开发;第三是加强与关键供应链伙伴的研发合作,支撑制造规模化。值得注意的是,这三条里没有一条是"做出新的物理突破",全部是工程、测试和供应链——这和公司 CEO Ben Bloom 在稿中说的"科学突破必须迅速转化为商业现实"是一致的。

技术上,Atom Computing 走的是中性原子路线:用光镊(optical tweezers)把单个中性原子困在阵列里,用原子的核自旋作为 qubit。这条路线的优势是 qubit 之间天然一致、阵列容易扩展到上千个原子,所以它最先跨过 1000 qubit 并不意外;难点在于门操作速度相对超导路线慢,以及大规模阵列需要高功率、高稳定性的激光系统和超高真空系统。新闻稿还提到,公司 2025 年把第一台商用本地部署量子计算机卖给了 QuNorth,这是一个由 EIFO 和诺和诺德基金会(Novo Nordisk Foundation)资助的北欧量子计划。

个人看法:这篇和今天早些时候写的 [U.S. Quantum Ambitions Face a Supply Chain Test](2026-11-13-u-s-quantum-ambitions-face-a-supply-chain-test-policy-analysts-warn.md) 正好可以对照着看。那篇政策分析说,美国量子的瓶颈不在 qubit,而在制冷、激光、同位素和光学器件这些使能层,并建议联邦资金直接投到制造产能、建立采购需求信号;而 Atom Computing 这 1 亿美元的三项用途里,有两项(垂直整合关键部件、和供应链伙伴一起扩产)恰好就是在回应这个瓶颈。再往前看,[Commission on U.S. Quantum Primacy](2026-11-10-commission-on-u-s-quantum-primacy-urges-sustained-investment-to-turn-quantum-dis.md) 那篇呼吁的"持续投资,把科学突破变成产业",这里也算是一个具体落地的例子。图谱里商务部此前已经和 D-Wave、Rigetti 有投资关系,现在再加上 Atom Computing,说明商务部的量子资金是在多条技术路线上同时下注,而不是押某一种路线。

如果按"先找瓶颈,再找解决瓶颈的那一层"来拆量子计算板块,我觉得目前政府资金解决的是第一个瓶颈——资金和工程化周期太长,私人资本不愿意承担;但中性原子路线自己的瓶颈是激光和光学系统。所以受益的层次可能是:第一层是激光和光学元件,中性原子阵列需要大量稳定的窄线宽激光、光镊用的空间光调制器和高数值孔径光学系统,像 Toptica、Coherent、Thorlabs、Hamamatsu 这一类公司是上游;但和那篇供应链文章里说的一样,Coherent 这类公司的产能和收入主要由 AI 光模块决定,量子订单对它们的弹性很小。第二层是真空和控制电子学,中性原子系统不像超导那样依赖稀释制冷机,但需要超高真空腔和高速的测控系统,Keysight、Quantum Machines 这类测控厂商会受益。第三层才是整机公司本身,Atom Computing 是非上市公司,二级市场上没法直接参与;同一路线的竞争者里,[Pasqal](2026-11-08-pasqal-reports-third-quarter-revenue-decline-as-qpu-services-revenue-grows.md) 和 [QuEra](2026-11-10-quera-harvard-and-anthropic-use-ai-to-reduce-quantum-circuit-resource-requiremen.md) 也都是非上市公司,所以这条消息对上市的量子股更多是情绪面的——它说明政府确实在掏钱,而不是只出报告。另外图谱里 Atom Computing 和 Microsoft 有研发合作、和 Nvidia 有合作关系,如果之后 Microsoft 基于 Atom 的硬件推出逻辑 qubit 云服务,那才是大公司层面真正能被资本市场定价的环节。

这条消息对 AI 板块也有一个间接联系:量子计算机最终大概率会作为 AI/HPC 数据中心里的一个加速器存在,Nvidia 的 CUDA-Q 和 NVQLink 就是在做这层混合编排。但这是很长期的逻辑,不足以单独支撑 AI 板块的判断,这里不硬挂。

不过,"最高 1 亿美元"和"潜在资金最高 3 亿美元"都是上限,实际拨付通常和里程碑挂钩,新闻稿里也没有披露分几年、按什么条件发放。现在还只能把它看作量子板块政策支持在加码的一个信号。后续值得跟踪的是 DARPA QBI C 阶段的评估结果,以及 12 月《国家量子战略》更新里有没有出现针对整机或关键部件的采购承诺——如果有,激光和光学这一层会比整机厂商更早看到订单。
