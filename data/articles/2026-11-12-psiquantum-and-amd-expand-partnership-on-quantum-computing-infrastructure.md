# PsiQuantum and AMD Expand Partnership on Quantum Computing Infrastructure
https://thequantuminsider.com/2026/11/12/psiquantum-amd-expand-quantum-computing-infrastructure-partnership/

(注:原文是双方联合发布的新闻稿,所称"超越当前最先进水平"的计算结果属于公司自述,未经独立验证。)

这条合作背后的命题是:容错量子计算机不是一台孤立的量子芯片,而是一整套量子 + 经典的混合系统,经典算力在里面占的比重比很多人想象的大。谁提供这部分经典基础设施,谁就提前站进了量子产业链。

文章指出,PsiQuantum 与 AMD 扩大战略合作,共同设计运行实用规模容错量子计算机所需的计算基础设施。合作原本基于 AMD 的 Versal FPGA(PsiQuantum 已选它用于容错平台开发),现在扩展到 Instinct GPU、EPYC CPU 和 ROCm 软件栈,再结合 PsiQuantum 的硅光子平台;AMD 还计划对 PsiQuantum 进行股权投资。双方首先聚焦制药和药物发现,已有的成果包括基于 GPU 的共价抑制剂模拟,以及一个叫 PRISM 的机器学习解码器,针对可编程硬件加速器做了低延迟优化,用于光子量子计算机的实时纠错。双方还会探索在芝加哥伊利诺伊量子与微电子园区(PsiQuantum 是锚定租户)落地。

这里可以拆成三个部分看经典算力在量子系统里扮演的角色:第一是实时纠错解码,量子比特的错误必须在微秒级别被识别并修正,这需要 FPGA 这类低延迟硬件;第二是混合算法里的经典部分,化学模拟往往把大问题拆开,一部分交给量子、一部分交给 GPU;第三是量子计算机真正可用之前的"过渡期"工作,用 GPU 跑量子启发的算法先产生商业价值。

个人看法:这和之前 [Oak Ridge、IBM 与 AMD 推出量子协同设计平台](2026-11-05-oak-ridge-national-laboratory-ibm-and-amd-launch-new-co-design-platform-for-quan.md)是同一条线,AMD 正在系统性地把自己放进量子计算的经典控制层。按先找瓶颈的思路,容错量子计算现在卡住的是纠错——之前 [QuEra、哈佛和 Anthropic 用 AI 减少量子线路资源](2026-11-10-quera-harvard-and-anthropic-use-ai-to-reduce-quantum-circuit-resource-requiremen.md)也是在攻这一环——而解码器需要的正是低延迟经典硬件。所以受益的层次会是:第一层是提供 FPGA/GPU/CPU 的经典算力厂商,AMD 在这里已经和 IBM、PsiQuantum 两条路线都绑定,这对量子计算板块和 AI板块是同时挂钩的;第二层是硅光子制造链,PsiQuantum 依赖标准半导体工艺,对代工厂是增量;第三层才是量子硬件公司本身,它们离实用规模仍然很远。

现在还早,PsiQuantum 的实用规模机器还没有明确时间表。值得关注的是 SC26 上双方会披露多少细节,以及 AMD 股权投资的具体金额。
