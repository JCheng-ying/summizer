# What could 1,000x more reliable quantum computation unlock?
https://www.datacenterdynamics.com/en/opinions/what-could-1000x-more-reliable-quantum-computation-unlock/

先说明利益相关:这是一篇厂商署名的观点文章,文中把 QuEra 的 Libra 系统称为"我们的公开路线图",所以作者来自 QuEra,涉及自家产品的指标未经独立验证。

文章提出的命题是:量子计算的衡量标准要从物理比特数转向可靠运算次数。这有点像今天的 [AGIBOT introduces Worken](2026-11-01-agibot-introduces-worken-to-measure-robot-productivity-at-agibot-innovation-day-.md) 把机器人衡量标准从出货量转向有效产出,都是行业走向落地时的指标切换。

文章指出,物理比特脆弱易错,决定实用性的是纠错后能执行多少可靠操作,行业用 megaquop 和 gigaquop 分别表示约一百万和十亿次可靠逻辑操作。第一是 megaquop:QuEra 称 2028 年路线图上的 Libra 系统目标是 256 个逻辑比特、由超过 1 万个物理比特构成、逻辑错误率百万分之一,这能支持部分材料和量子动力学模拟,但不足以处理大型工业分子。第二是 gigaquop:可解决的问题范围会明显扩大。第三是基础设施:量子处理器会成为异构计算中的专用加速器,需要 CPU 和 GPU 配合,控制系统、纠错、读出和经典计算可能比处理器本身占用更多资源,不同架构对冷却的要求也差很多,所以不会有统一的量子数据中心模式。文章也承认,优化和机器学习上的量子优势证据还不充分,最先受益的是材料和化学模拟,并建议运营商现在不必押注某种架构,先做工作负载梳理和混合流程测试。

个人看法:这和 [Foxconn Aims to Become World's Largest Quantum Computer Manufacturer](2026-11-01-foxconn-aims-to-become-world-s-largest-quantum-computer-manufacturer.md) 对"加速器"的判断完全一致,说明这已经是行业共识,这一点比具体数字更重要。既然量子必须和经典算力配合,那么受益的不只是量子公司:第一层是控制电子和纠错解码,这里需要大量经典算力,Nvidia 的量子相关布局就在这里;第二层是专用低温和光学配套;第三层是能提供混合环境的云和超算中心。这篇利好量子计算板块,但要注意作者的立场,且路线图要到 2028 年。还处于观望阶段。值得跟踪的是各家能否公布第三方验证的逻辑错误率,而不是继续比较物理比特数。
