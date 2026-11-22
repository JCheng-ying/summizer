# Daniel Ek backs AI researcher’s fusion power startup. Here’s what they’re building.
https://techcrunch.com/2026/11/20/daniel-ek-backs-ai-researchers-fusion-power-startup-heres-what-theyre-building/

这篇文章是一条篇幅不长的融资新闻,但背后的命题值得展开:核聚变研发正在从"硬件驱动"转向"模拟和数据驱动"。如果 AI 模拟能大幅减少昂贵的物理试验次数,聚变商业化的时间表和资本需求都会被改写,而聚变一旦可行,就是 AI 能源瓶颈最彻底的解法。

文章指出,Spotify 创始人 Daniel Ek 投资了一家处于隐身状态的英国聚变初创公司 Europa Fusion。公司今年 2 月成立,创始人 Nantas Nardelli 有很深的 AI 背景,曾在 Google DeepMind、Facebook AI Research 和微软剑桥研究院工作,最近担任加州聚变公司 Pacific Fusion 的机器学习负责人。Pacific Fusion 刚在新墨西哥州开建示范设施,和大多数同等规模的聚变公司一样,它非常依赖物理装置来验证理论、改进模拟。文章称,Nardelli 不认同这种以硬件为中心的做法,认为聚变公司应该更多投入模拟和数据驱动的方法。Europa Fusion 和 Pacific Fusion 一样走脉冲功率路线,也就是用巨大、精确定时的电流脉冲压缩燃料靶,直到原子核发生聚变释放能量。文章也提醒,至今没有人建成能向电网供电的聚变电站,但如果商业化成功,它可能成为几乎无限燃料的零碳电源,也有望缓解对 AI 能耗的担忧。Nardelli 在个人网站上写道,自己的背景是电子和控制工程,曾以造机器人为生,但"是时候彻底解决气候变化了"。

和 [AI can now control fusion plasma faster than humans can react](2026-09-10-ai-can-now-control-fusion-plasma-faster-than-humans-can-react.md) 那篇联系起来看,AI 正在从两个方向进入聚变:一是实时控制等离子体,二是这篇说的用模拟替代部分物理试验。

个人看法:我觉得这篇和之前写过的 Transfer Learning 宇宙学论文逻辑很像——都是用便宜的模拟去替代昂贵的物理实验/高精度模拟,先在虚拟环境里学大致规律,再用少量真实数据校准。聚变公司的真正瓶颈其实是迭代速度:每建一个物理装置要几年和数亿美元,一次试验失败就意味着很长的周期。如果模拟足够准,迭代就从"年"变成"周"。但风险也很明显,聚变里的等离子体不稳定性恰恰是模拟最难准确刻画的部分,纯模拟路线有可能在关键物理上踩坑,这也是 Pacific Fusion 坚持做硬件的原因。所以对能源板块来说,这是一个长期、方向性的信号,而不是近期利好:受益的层次会是,第一层是脉冲功率和高压电力电子的供应链(大电容、高速开关、高压电源),无论 Pacific Fusion 还是 Europa Fusion 都需要;第二层是科学计算和 HPC/GPU 算力,模拟驱动路线本质上是把资本开支从实验装置转移到算力上,这也间接利好 AI 板块的基础设施层;第三层才是聚变公司本身,目前都在一级市场,二级市场几乎没有纯标的。这里也能看到一个有意思的现象:AI 人才正在流向能源领域,反过来解决 AI 自己的能源约束。现在非常早期,公司还在隐身,连融资金额都没披露,只能观望,值得关注的是 Europa Fusion 未来会不会公布具体的模拟平台和第一个验证目标。
