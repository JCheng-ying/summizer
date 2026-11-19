# Intel secures first external customer for 18A-P process node
https://www.datacenterdynamics.com/en/news/intel-secures-first-external-customer-for-18a-p-process-node/

这条新闻背后的命题是：全球先进制程代工到底能不能从"台积电一家独大"变成"至少有第二个可信供应商"。对 AI 产业来说，这个问题的分量远超 Intel 一家公司的股价，因为先进制程产能本身就是算力供给的上游瓶颈。

文章指出，Intel CEO 陈立武（Lip-Bu Tan）在奥斯汀的 TomorrowX 峰会上宣布，Intel 18A 系列制程拿到了第一个外部客户；CTO Pushkar Ranade 随后在 X 上确认，这个客户签的是 18A-P 节点，该节点 6 月已进入风险试产。Intel 没有公布客户名字，文章只提到今年早些时候《华尔街日报》报道过 Intel 与 Apple 在洽谈代工部分 Apple 设备芯片的协议，但并没有说这次的客户就是 Apple，这一点不能混为一谈。

技术上，文章介绍 18A 是 Intel"四年五个节点"路线图的最后几个节点之一，第一次同时引入两项关键技术：第一是 RibbonFET，也就是全环绕栅极（GAA）晶体管，相比 FinFET 能提高晶体管密度和栅极控制能力，这和台积电 N2、三星 3nm GAA 是同一代技术；第二是 PowerVia，即背面供电，把电源走线从晶圆正面挪到背面，让正面布线专门给信号用，缓解先进制程里供电和信号争抢金属层的问题。18A-P 是 18A 的增强版，与 18A 设计完全兼容，目的是提升性能、延长节点寿命。陈立武在 Q3 财报会上说 Intel 3 和 18A 良率都在继续提升，18A 以两位数速度改善，两个节点的晶圆产出都超预期，18A-P 按计划年底在内部产品上量产。

个人看法：我之前写过 [Intel 因 PC 市场放缓指引疲弱、股价暴跌 30%](2026-11-01-intel-shares-plummet-30-following-weak-guidance-blamed-on-pc-market-slowdown.md)，当时的核心担忧是 Intel 的产品业务撑不起庞大的晶圆厂资本开支。代工业务拿到外部客户正是解决这个矛盾的唯一出路：晶圆厂是重资产，只有外部订单把利用率填满，摊销成本才降得下来。所以这次瓶颈很明确，就是"外部客户信任"，一个签约客户是从零到一，但离填满产能还差得远。

如果代工这条路走通，受益的层次会是：第一层是 Intel 自己的代工业务（Intel Foundry），它是唯一一家在美国本土有先进逻辑制程的公司，地缘政治上有天然溢价；第二层是半导体设备，背面供电和 GAA 都需要新的刻蚀、沉积和量测工艺，Applied Materials、Lam Research、KLA、ASML 都会因为 Intel 扩产受益，而且不管最后是 Intel 还是台积电赢，设备商都在；第三层是需要分散供应链的芯片设计公司，无论是 Apple 还是做 AI 加速器的公司，都有动力在台积电之外找第二供应源。这条新闻挂在 AI 板块，因为先进制程产能是 AI 芯片供给的源头；也挂在 edge AI 板块，因为 18A 系列首先服务的是 PC、手机这类终端芯片，端侧 AI 芯片对能效敏感，背面供电对功耗有直接帮助。

不过要克制：客户名字、订单规模、量产时间都没有公布，"第一个外部客户"可能只是一个小批量的试单。另外文章里还有一条背景值得注意：Nvidia 本周把它持有的 Intel 股份减少了 25%（见同日的 [Nvidia 出售过半 Nokia 股份](2026-11-19-nvidia-sells-more-than-half-of-nokia-stake.md)），大股东在减持、代工在拿单，信号是混合的。值得跟踪的是这个客户何时被公开，以及 18A-P 年底是否如期量产。
