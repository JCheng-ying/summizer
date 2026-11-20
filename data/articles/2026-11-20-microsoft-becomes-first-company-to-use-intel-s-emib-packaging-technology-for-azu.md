# Microsoft becomes first company to use Intel’s EMIB packaging technology for Azure hardware
https://www.datacenterdynamics.com/en/news/microsoft-becomes-first-company-to-use-intel-s-emib-packaging-technology-for-azure-hardware/

这条新闻背后的命题是：AI 芯片的供给瓶颈正在从"晶圆能不能造出来"往后移到"芯片能不能封装出来"，而先进封装这一层到目前为止几乎是台积电一家说了算。如果超大规模云厂商开始把自研芯片的封装交给台积电以外的供应商，那么 AI 算力供应链上最紧的那一个环节就第一次出现了真正的第二来源。

文章指出，Intel 与 Microsoft 签了一份多年协议，Microsoft 将成为第一家在自研芯片上使用 Intel EMIB（Embedded Multi-die Interconnect Bridge，嵌入式多芯片互连桥）先进封装技术的公司。Microsoft 同时表示，这份协议也确认了 Intel Xeon 处理器（包括下一代服务器 CPU）的长期供应，双方还会在支持 CXL（Compute Express Link）的 Xeon 上合作，以提高 Azure 的内存利用效率。文章也坦白说明了信息的边界：两家公司都没有透露 Microsoft 会把 EMIB 用在哪款硬件上，也没有给出制造和部署时间表。文章还提到背景：2024 年 2 月 Intel 曾宣布与 Microsoft 达成一笔 150 亿美元的协议，用 18A 制程代工 Microsoft 设计的定制芯片。

技术上需要讲准确。今天的大芯片已经很难做成一整块单晶硅，原因有两个：第一是光罩尺寸上限，单颗芯片面积有物理天花板；第二是良率，芯片越大，一个缺陷报废整颗芯片的概率越高。所以行业转向 chiplet，把计算、I/O、HBM 内存拆成多个小芯片，再在一个封装里高速互连起来。文章解释，EMIB 是一种 2.5D 封装技术，用嵌在基板里的硅桥把多个 chiplet 连起来。它和台积电 CoWoS 的区别在于：CoWoS 是在所有芯片下面垫一整块大面积的硅中介层（interposer），而 EMIB 只在两颗芯片相邻的边缘埋一小块硅桥，用到的硅面积小得多。前者互连密度和成熟度更高，后者理论上成本更低、更容易做大尺寸封装。至于 CXL，它是建立在 PCIe 之上的缓存一致性互连协议，可以让 CPU 挂载和共享额外内存，解决的是数据中心里"内存被困在单台服务器里用不满"的问题。

个人看法：这篇和昨天写的 [Intel 18A-P 拿到首个外部客户](2026-11-19-intel-secures-first-external-customer-for-18a-p-process-node.md) 是同一条线上的两个信号。那篇的瓶颈是"外部客户信任"，晶圆厂要靠外部订单填满利用率；这篇说明 Intel Foundry 能卖的不只是制程，还有封装，而且封装可能是更容易先打开局面的那一层——因为客户不需要把整颗芯片的前道制造都搬到 Intel，只需要把后道封装这一步交过来，切换成本低得多。回到 [Intel 股价暴跌 30%](2026-11-01-intel-shares-plummet-30-following-weak-guidance-blamed-on-pc-market-slowdown.md) 那篇的担忧，Intel 需要的恰恰是这种不依赖 PC 周期的数据中心收入。

按"先找瓶颈再找解决瓶颈的那一层"来拆：过去两年 AI 加速器出货量真正被卡住的地方，很多时候不是台积电的先进制程晶圆，而是 CoWoS 封装产能和 HBM 供给。因此受益的层次会是：第一层是提供第二封装来源的 Intel Foundry 本身，Microsoft 这样的大客户背书对其他自研芯片的云厂商有示范效应；第二层是封装上下游的材料和设备，比如 ABF 基板（Ibiden、Unimicron）、封装与测试设备（BE Semiconductor、Onto Innovation 这类做混合键合和量测的公司），不管最后是 CoWoS 还是 EMIB 胜出，封装产能扩张都需要它们；第三层是自研芯片的云厂商自己，Microsoft、Google、Amazon、Meta 都在做 ASIC，多一个封装来源就意味着少一分被单一供应商卡脖子、议价能力更强。这条新闻挂在 AI 板块，机制就是先进封装是 AI 加速器供给的直接瓶颈，第二来源会扩大整个行业的算力供给上限。

需要克制的地方也很明显：用在什么硬件上、什么时候量产、量有多大，文章一个都没说。"第一家使用 EMIB 的公司"更像一个合作框架而不是具体订单，Xeon 长期供应那部分也是对现有关系的确认而非新增量。而且 2024 年那笔 150 亿美元的 18A 代工协议，两年后外界依然很难看清落地到了什么程度。现在还只能观望，但值得关注的是 Microsoft 下一代 Maia 加速器或 Cobalt CPU 的公开资料里，会不会出现 Intel 封装甚至 Intel 制程的明确说明——那才是 Intel 代工从"签框架"走到"真出货"的信号。
