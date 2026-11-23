# KKR could acquire majority stake in EdgeCore for up to $10bn - report
https://www.datacenterdynamics.com/en/news/kkr-could-acquire-majority-stake-in-edgecore-for-up-to-10bn-report/

这条新闻表面上是一笔还没谈成的并购传闻，背后其实是一个更大的问题：在 AI 板块情绪明显降温的这一周里，最懂"基础设施定价"的那批长期资本，到底是在撤离 AI 数据中心，还是在借回调接盘？如果这笔交易最终落地，它会成为二级市场之外一个很重要的估值锚。

文章指出，据 Bloomberg 报道，KKR 正在和 EdgeCore Digital Infrastructure 目前的大股东 Partners Group 谈判，可能以 80 亿到 100 亿美元的估值收购 EdgeCore 的多数股权，收购主体是 KKR 旗下专门做 AI 基础设施的投资平台 Helix Digital Infrastructure。文章也特别说明，谈判仍在进行，消息人士称最终也可能谈不成。如果成交，这将是 Helix 的第一笔交易。Helix 今年 6 月成立，承诺资本 100 亿美元，由前 AWS CEO Adam Selipsky 领导，定位是交付"自带配套电力供应协议"的超大规模数据中心；它的出资方包括 Nvidia 和科威特投资局，Nvidia 同时作为战略合作伙伴支持 Helix 的基础设施部署。

被收购的一方，文章给出的画像是：EdgeCore 2018 年成立，2022 年被 Partners Group 收购，近几个月拿下了多笔大额融资，目前已承诺资本 80 亿美元、规划投资超过 160 亿美元，公司自称组合规模超过 2GW，运营和在建设施分布在硅谷、凤凰城、里诺以及弗吉尼亚的多个园区。KKR 这一侧，文章列举了它已有的数据中心资产：Singtel 数据中心业务 20% 的股份、与 Singtel 一起持有 STT GDC 的多数股权、欧洲运营商 GTR，以及与 BlackRock 旗下 GIP 共同持有的 CyrusOne。KKR 管理资产接近 8000 亿美元，数字基础设施归在 119 亿美元规模的 Infrastructure for Wealth 板块下面，而 KKR 的七个数据中心平台只占这个板块 AUM 的约 6%。

最值得注意的是文章引用的 KKR CEO Scott Nuttall 在三季度财报会上的表态：被问到美国中期选举结果可能带来的限制是否会让 KKR 放慢数据中心投资时，他说公司在"适当地谨慎"，而且大部分投资在云而不是 AI；CyrusOne 的长期租约对手方是政府或投资级的超大规模云厂商，Helix 则更像是给超大规模云厂商的"一站式服务"。文章最后把这笔交易放进当下的市场背景里：对 AI 投资规模的担忧、中期选举结果，再加上 Nvidia 的丑闻，过去一周引发了科技股抛售，AI 供应链普遍下跌，Anthropic 也正是在这种波动中完成了 IPO。文章的判断是，Helix 收购 EdgeCore 可能会成为其他想要出手 AI 资产的投资者的一个参照。

个人看法：我觉得这条新闻最值得拆开看的，是"谁在买、买的是什么、用什么逻辑定价"。第一，买方不是追题材的二级市场资金，而是 KKR 这种以长期租约现金流为核心定价逻辑的基础设施资本；第二，买的不是 GPU，而是 2GW 的场地、电力接入和在建产能，也就是我们之前反复说的数据中心四大系统里最慢、最难复制的那几层；第三，Helix 的卖点是"数据中心 + 配套电力协议"打包交付，这说明在今天的产业链里，真正稀缺的已经不是机柜本身，而是能按时通电的机柜。这和之前 [Anthropic 签 34 亿美元燃气发电机合同](2026-11-09-anthropic-signs-3-4bn-gas-generator-deal-to-support-1-7gw-of-data-center-power.md) 以及 [数据中心建设停滞、推理芯片去电信机房找空间](2026-11-18-stalled-data-center-buildouts-send-inference-chips-hunting-for-space-in-telco-an.md) 那两篇是同一个瓶颈：电力和可交付的场地。

但另一方面，Nuttall 那句"大部分投资在云而不是 AI"也要认真读。这其实是一个对冲性的表态：他在向投资者强调，KKR 的数据中心资产对手方是投资级租户和政府，风险不取决于 AI 模型公司能不能赚钱。这和之前 [Anthropic IPO 检验 AI 循环融资](2026-11-19-anthropic-s-ipo-puts-ai-s-circular-financing-boom-to-the-test.md) 那篇的担忧是呼应的——Nvidia 既是 Helix 的出资方又是战略伙伴，又是数据中心最终的 GPU 供应商，这种"上游出钱、下游买货"的结构在情绪好的时候是加速器，情绪坏的时候就是被市场重点审视的地方。再结合 [Nvidia 说明何时继续为新云厂商提供融资](2026-11-18-nvidia-clarifies-when-it-will-and-won-t-keep-financing-neoclouds.md) 那篇，Nvidia 在管理层变动之后对这类投资的态度本身就是一个变量。

从投资角度，受益的层次我会这样拆：第一层是已经拿到电力和土地的数据中心资产本身，也就是 EdgeCore、CyrusOne 这类运营商，以及上市的 Equinix、Digital Realty，如果私募市场愿意给 2GW 资产 80-100 亿美元的估值，二级市场的数据中心 REIT 至少有一个参照；第二层是电力侧，Helix 把"配套电力协议"写进商业模式，意味着燃气轮机（GE Vernova、Siemens Energy）、现场发电、变电和输配电设备仍然是卡脖子的那一层，这是能源板块的逻辑；第三层才是 AI 板块里的 GPU 和网络设备，Nvidia 作为出资方直接绑定了未来的采购，但这一层在当前抛售环境里波动最大。我会把这条挂在 AI 板块和能源板块上，但要强调，交易还没成交，文章本身也说可能谈崩。

现在还只是传闻阶段，结论下早了。值得跟踪的信号是：这笔交易最终是否成交、成交估值落在 80 亿还是 100 亿那一端，以及是否有其他私募基础设施资本跟进出手或接盘 AI 数据中心资产——如果成交价接近区间上沿，说明长期资本对"带电的数据中心"依然愿意付溢价，抛售更多是二级市场的情绪问题；如果谈崩或者大幅折价，那才是真正值得警惕的信号。
