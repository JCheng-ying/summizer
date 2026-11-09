# AI-Assisted Proof Settles Longstanding Question About Quantum Speedups
https://thequantuminsider.com/2026/11/06/ai-assisted-proof-settles-longstanding-question-about-quantum-speedups/

这篇文章同时触及两个大命题:一是量子计算的理论边界被进一步划清,指数级量子加速必须依赖问题本身的结构;二是 AI 再次独立完成了一个悬而未决多年的数学证明,而且是在形式化验证工具里被检查过的。

文章指出,一篇由 Physical Superintelligence(PSI)的 David Turturean 发布的论文证明了 Aaronson-Ambainis 猜想,这个问题可以追溯到 Scott Aaronson 2008 年的一次讲座。猜想问的是:在没有特殊结构、输入只是随机 0/1 串的情况下,量子算法还能不能获得指数级优势?研究用的是"查询模型",它不计算全部运算量,只计算算法读取输入的次数。证明的结论是,对于回答是/否的问题,在绝大多数随机输入上,经典算法可以用多项式倍数(而不是指数倍数)的读取次数,近似出量子算法回答"是"的概率。打个比方,输入是一排关着的盒子,经典查询一次打开一个,量子查询可以同时和多个盒子作用;证明说明,在没有隐藏规律的情况下,经典方法只要优先打开"影响最大的盒子",就不需要多打开指数级数量的盒子。技术上,证明沿用了 Shachar Lovett 和 Jiapeng Zhang 的方法,提出了一种新的输入匹配方法,强化了 Reimer 的蝴蝶引理,同时发现 Lovett 和 Zhang 提出的一个一般性命题并不成立。

关于 AI 的作用,PSI 称其内部研究系统使用多个非公开 Anthropic 模型实例,检索文献、提出思路、组合方法、检验论证,第三天找到完整证明,之后又两次改进了界;主定理和形式化在 Lean 里通过了内核检查,斯坦福的研究者也在审读全文。Turturean 负责选题、运行系统和审改草稿,并对正确性负责。文章也强调了局限:这个定理只限制读取次数,不限制总计算时间,因此仍为结构化问题上的巨大加速、以及非结构化问题上的中等加速留有空间;它也不说明这个 AI 系统能否稳定地解决其他难题。

个人看法:这和之前 [Claude Fable 5 推翻 87 年数学猜想](2026-08-05-claude-fable-5-ai-finds-a-tiny-formula-that-topples-an-87-year-old-math-conjecture.md)、[Claude 削弱量子密码锁](2026-08-07-claude-weakens-a-quantum-lock-anthropic-engineers-used-claude-mythos-to-identify-cryptographic-weaknesses-in-hawk-and-aes.md) 是一条线:AI 在形式化数学上的进展越来越像一个可重复的研究工具,而 Lean 这类验证器解决了"AI 证明能不能信"的瓶颈。对量子计算来说,这个结果不是利空,而是把方向说得更清楚:想要指数加速,就去找有结构的问题,比如化学模拟、周期查找、特定物理系统,这正好和今天 [24 个量子优势问题清单](2026-11-08-study-maps-24-problems-where-quantum-computers-could-gain-an-edge.md) 互相印证。先找瓶颈:量子板块的瓶颈是"到底哪些问题值得用量子计算机",这个证明减少了无效探索。受益的层次会是:第一层是专注化学、材料等结构化应用的量子软件和算法公司;第二层是有能力跑到容错规模的硬件公司;对 AI 板块来说,这是前沿模型做科研的又一个证据,利好的是能提供这种长时间多实例推理的算力和模型层。我会把它挂在量子计算板块和 AI 板块。但要注意论文还是 GitHub 上的预印本,模型非公开,结果能否复现还需要观察。
