# Why a Crusoe investor is betting on solar and batteries to power future AI data centers
https://techcrunch.com/2026/11/24/why-a-crusoe-investor-is-betting-on-solar-and-batteries-to-power-future-ai-data-centers/

这篇文章讨论的是 AI 电力问题里一个路线之争：数据中心是继续抢燃气轮机，还是转向"太阳能 + 长时储能 + 离网"。如果后者成立，AI 数据中心的电源结构、选址逻辑和许可流程都会被改写。需要先说明利益相关：受访者 Brook Porter 是 G2 Venture Partners 的合伙人，G2VP 领投过 Crusoe 的 C 轮，而文中点名的长时储能公司 Antora Energy 也是 G2VP 的投资组合公司，所以下面的观点和数据都应当看作投资人的立场，未经独立验证。

文章指出，美国电网在短短几年里从几乎零增长变成每年新增数吉瓦，Porter 的原话是"这是原子而不是比特"。由于供应链扩张需要时间，很多公司在用各种方式抢电，包括购买、租赁和部署燃气发电。Porter 认为应该看更大的图景：他给出的对比是全球燃气发电每年新增产能只有约 60-70GW，而太阳能已经远超每年 1TW。他的核心论据是 Wright's Law——同一个东西重复制造得越多，成本下降越快，而太阳能和多数长时储能都是小型、模块化、可大规模制造的产品。G2VP 估计到本十年末数据中心投资将超过 4 万亿美元，并认为下一波会分成两条路径：一是小型并网、自带发电能力的设施；二是由太阳能和长时储能供电的大型数据中心。Porter 说"大想法是离网"，这样可以绕开并网和空气许可等约束，大幅缩短上线时间。文章也承认，锂离子电池用来做全天候供电仍然太贵，Form Energy 和 Antora 这一代长时储能把每兆瓦时成本降了很多，但离被数据中心开发商广泛接受还有几年。

这里有一个技术细节值得说清楚：太阳能对数据中心的难点不是发电成本，而是容量因子。数据中心是 24 小时近乎恒定的负载，太阳能只在白天发电，要做到全天候离网，需要把一天中大部分时间的用电量储存下来，再加上应对连续阴天的冗余。这正是锂电池"太贵"的原因——它擅长几小时的调峰，不擅长十几小时甚至多天的放电。长时储能要解决的就是这一段：Form Energy 做的是铁空气电池，Antora 做的是热储能，原文没有展开具体技术，这里是根据公开信息补充的背景。

个人看法：这篇和之前写过的几篇形成了一个完整的对照组。一边是燃气路线：[Anthropic 签下 34 亿美元燃气发电机合同](2026-11-09-anthropic-signs-3-4bn-gas-generator-deal-to-support-1-7gw-of-data-center-power.md)，以及 [SoftBank 亏损可能给 AI 燃气野心封顶](2026-11-12-softbank-s-billion-dollar-loss-may-have-put-a-cap-on-ai-s-natural-gas-ambitions.md)；另一边是储能和新电源：[意大利初创的海上储能](2026-11-17-italian-startup-targets-data-centers-with-offshore-energy-storage.md)、[Proper Voltage 的钠离子 UPS 电池柜](2026-11-24-proper-voltage-launches-sodium-ion-battery-cabinet-for-data-center-ups-systems.md)。而今天的 [Vantage 撤出 Aurora 项目](2026-11-24-vantage-drops-plans-for-trident-data-center-after-colorado-s-aurora-city-passes-.md) 恰好给"离网能绕开许可"这个论点提供了反面注脚：离网能绕开并网排队和空气许可，但绕不开土地和社区——大面积太阳能阵列反而需要更多土地。

按"先找瓶颈"的方法看，当下的瓶颈是"上线速度"，燃气路线的问题是燃气轮机产能有限（Porter 的 60-70GW/年），太阳能路线的问题是长时储能的成本和成熟度。所以真正决定胜负的是长时储能这一层。受益的层次会是：第一层是长时储能技术本身，Form Energy、Antora 这类公司，挂能源板块，但它们大多还是私有公司，且自己也承认离广泛采用还有几年；第二层是太阳能制造和逆变器、电力电子，First Solar、Enphase 这类公司（原文未提及）在"离网 + 太阳能"路线里是确定的上游，同样挂能源板块；第三层是像 Crusoe 这样本来就以"把算力搬到电源旁边"为卖点的开发商，挂 AI板块，如果离网模式跑通，它们的选址自由度和上线速度会成为竞争优势。

现在还早，这更多是一位投资人在为自己的投资组合描绘路线图，而不是已经发生的产业转向。值得关注的信号是：有没有超大规模云或 Crusoe 这类开发商签下以长时储能为主力电源的真实合同，以及长时储能的单位成本什么时候能和燃气发电正面竞争——在那之前，燃气仍然会是最现实的"桥接电源"。
