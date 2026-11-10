# IBM deploys Quantum System Two in Chicago, Illinois
https://www.datacenterdynamics.com/en/news/ibm-deploys-quantum-system-two-in-chicago-illinois/

这条新闻表面上是 IBM 在伊利诺伊州落地一台量子计算机，背后真正值得看的是美国量子产业正在形成的"区域集群"模式：州政府出钱建园区、大学托管、大公司放机器、国家实验室配算法中心，用地方产业政策把量子计算从单个公司的研发项目变成区域基础设施。

文章指出，IBM 与芝加哥大学、伊利诺伊州政府以及伊利诺伊量子与微电子园区（IQMP）合作，在芝加哥部署了一台 IBM Quantum System Two。机器目前由芝加哥大学托管在 Hyde Park Labs，IQMP 园区建成后会永久迁入，这是 IBM 在伊利诺伊州的第一台量子计算机，供全州的科研机构、高校和企业与 IBM 以及 IQMP 的国家量子算法中心（NQAC）合作开发下一代算法和应用。文章介绍，Quantum System Two 于 2023 年底首次推出，比上一代 System One 更大，包含三台制冷机和三块 QPU，组成一个六边形的大系统，使用 156 量子比特的 Heron 处理器，而且可以与更多 System Two 联网扩展。IBM CEO Arvind Krishna 称它"今天就能交付科学上有用的结果"，州长 Pritzker 则把重点放在就业和产业机会上。

文章还提到了上周 IBM 与 AMD 以及美国能源部橡树岭国家实验室（ORNL）量子科学中心共同推出的量子纠错协同设计平台：在 IBM 纽约州 Poughkeepsie 站点，一块 120 量子比特的 Nighthawk 处理器与 ORNL 名为 Umbra 的 HPC 系统共址，后者使用 AMD Instinct MI355X GPU 和第五代 EPYC CPU。这项工作服务于能源部的 Quantum Genesis Mission，目标是到 2028 年底实现 100 个逻辑量子比特运行 10 万次困难操作。IBM 研究院负责人 Jay Gambetta 说，问题已经不再是纠错能不能在量子硬件上工作，而是如何加速和优化它。

个人看法：协同设计平台那部分我们在 [ORNL、IBM 与 AMD 推出量子协同设计平台](2026-11-05-oak-ridge-national-laboratory-ibm-and-amd-launch-new-co-design-platform-for-quan.md) 里写过，这里补充的是"部署"这一侧。结合起来看，IBM 的打法很清楚：一边用 System Two 这种模块化大系统在各地铺"量子基础设施"，一边和 AMD、国家实验室解决纠错所需的经典实时解码问题。量子纠错有一个经常被忽视的事实：每一轮纠错都需要经典处理器在微秒级时间内完成解码，所以逻辑比特越多，对紧耦合 HPC 的需求越大。

投资上先找瓶颈：量子计算今天卡住的是纠错，而纠错同时卡在两个地方——物理比特的质量和数量，以及实时经典解码的算力和延迟。那么受益的层次是：第一层是量子硬件本身，IBM 作为超导路线的领头者，地方政府和国家实验室的订单给了它稳定的部署场景，利好量子计算板块；第二层是给量子做实时解码的经典算力，也就是 AMD 这类 GPU/CPU 供应商以及低延迟互联，这是量子与 AI 板块的交叉点，量子越接近实用，它对 GPU 的需求反而越大；第三层是稀释制冷机、低温电子和微波控制这类配套设备供应商（比如 Bluefors 这类制冷机厂商）。不过伊利诺伊这台机器的意义更多是生态和人才而非算力，100 个逻辑比特的目标在 2028 年底，现在只能观望，值得跟踪的是 Quantum Genesis Mission 的 Q Competition 会公布哪些中期指标。
