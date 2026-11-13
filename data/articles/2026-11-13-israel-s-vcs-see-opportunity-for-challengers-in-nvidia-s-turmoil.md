# Israel’s VCs see opportunity for challengers in Nvidia’s turmoil
https://techcrunch.com/2026/11/13/israels-vcs-see-opportunity-for-challengers-in-nvidias-turmoil/

黄仁勋辞职之后,市场讨论的焦点正在从"Nvidia 股价跌多少"转向一个更结构性的问题:一个由创始人个人意志推动的生态,在失去推动者之后,还会不会以同样的速度扩张——如果不会,空出来的那部分速度会被谁拿走。

文章从以色列的视角切入。文章指出,以色列被黄仁勋称为 Nvidia 的"第二个家":2019 年他主导以 69 亿美元收购以色列芯片公司 Mellanox,并以此为基础建立了 Nvidia 在美国以外最大的研发中心,还计划在以色列北部建设一个数十亿美元的园区,目前在当地雇用约 6000 人。因此当地关心的不只是 Nvidia 本身,而是换帅之后公司对以色列的投入会不会保持。文章提到,临时 CEO Colette Kress 在 2023 年的采访里说过自己作为 CFO 每天先开以色列的会;外界流传的继任人选中有两位以色列人——苹果的 Johny Srouji 和 Nvidia 的 Michael Kagan,但都不在名单最前面。

文章的核心论点来自两位以色列风投合伙人。Vertex Ventures Israel 的 Yanai Oron 认为,Nvidia 决策变慢可能给竞争对手打开窗口,但如果这种不确定性同时拖慢了整体 AI 支出,挑战者可能只是"在一块更小的蛋糕里拿到更大的份额"。Selah Ventures 的 Adi Levanon 则认为,黄仁勋离开并不会拆掉 Nvidia 的技术和生态,但会给竞争对手更多空间去塑造下一阶段;随着企业把越来越吃算力的 AI agent 部署进工作流,已经有不少风险资本流向 AI 专用芯片和推理软件,但"这些挑战者现在有一个窗口去证明不同的方案能带来更好的经济性,单靠领导层变动赢不了生意"。文章还提到,黄仁勋任内 Nvidia 用现金储备在整个产业链大规模投资,这个帝国未必会倒,但变成彻底垄断的可能性下降了。

个人看法:这篇文章本身是情绪和观点,没有新的数据,但它把一个判断讲得很准确——Nvidia 的护城河分两部分:第一是技术和生态(CUDA、NVLink、Mellanox 带来的网络栈),这部分不会因为换 CEO 而消失;第二是资本推动力,也就是黄仁勋用 Nvidia 的现金去投资客户、担保融资、扶持 neocloud,把需求提前"造出来",这部分高度依赖个人。在 [黄仁勋辞职那篇](2026-11-12-nvidia-ceo-jensen-huang-resigns-following-affairs-scandal.md) 里我已经写过,真正被动摇的是融资这一环。所以先找瓶颈:挑战者过去的瓶颈并不是芯片性能,而是客户愿不愿意为了更好的单位经济性去承担迁移成本和供应链风险;Nvidia 管理层动荡降低的恰恰是"选非 Nvidia 方案"的心理和政治成本。

受益的层次会是:第一层是已经有大客户验证的替代推理芯片,比如 [拿下微软的 Cerebras](2026-11-12-surging-ai-chip-revenue-and-microsoft-deal-boost-cerebras-systems-stock-by-17.md)、Google TPU、AWS Trainium,以及 [刚融资 7.2 亿美元的 Fractile](2026-11-11-british-inference-chip-developer-fractile-raises-720m-in-funding.md);第二层是降低迁移成本的软件,也就是 [Luminal 这类针对 CUDA 护城河的编译器](2026-11-12-with-23m-in-funding-luminal-is-the-latest-startup-to-put-nvidia-s-cuda-moat-in-i.md) 和推理优化公司——Levanon 说的"更好的经济性",很大程度上要靠这一层来证明;第三层仍然是不管谁赢都受益的制造端,台积电的先进制程和封装、HBM 供应商。但 Oron 那句"更小蛋糕里更大份额"值得认真对待:如果 Nvidia 减少对客户的融资支持,整个 AI板块的资本开支增速可能放缓,挑战者拿到的份额增长未必能抵消总量的收缩。所以对 AI板块的判断是结构利好挑战者、总量偏谨慎。

现在还在观望阶段。值得跟踪的信号是接下来一两个季度有没有大型云厂商或前沿实验室公开宣布把一部分推理负载从 Nvidia 迁到其他架构,而不只是"签约""测试"——这才是窗口真正被利用的证据。
