# AI server OEMs hiking prices by 45% as memory shortage bites - report
https://www.datacenterdynamics.com/en/news/ai-server-oems-hiking-prices-by-45-as-memory-shortage-bites-report/

这篇文章说明的是,AI 基础设施的瓶颈正在从 GPU 往下游一层转移到内存,而且已经严重到打破商业合同惯例的程度。服务器厂商在交付时要求比合同价高出最多 45% 的价格,这意味着内存短缺已经不是芯片行业内部的问题,而是开始直接改变数据中心项目的预算和交付节奏。如果 SK Hynix 说的"2030 年才缓解"成立,那么未来几年 AI 算力的真实成本曲线可能不是往下走,而是往上走。

文章援引金融时报报道指出,Dell、Lenovo、Supermicro、Hewlett Packard Enterprise 等服务器厂商在设备准备交付时,向客户要求的价格远高于最初签约价,涨幅最高达 45%,而且已经波及超大规模云厂商以外的大客户,比如自建 IT 基础设施的金融交易公司。原因被认为是厂商把内存短缺带来的成本暴涨转嫁给客户。短缺已经让企业网络设备涨价,包括固定无线接入设备和园区以太网交换机;SK Hynix 则把预期中的缓解时间从 2028 年推迟到 2030 年。文章提到一些厂商在尝试缓和,HPE 承诺对 100 万美元以下的计算、存储和基础设施报价锁价,并把报价有效期从 15 天延长到 30 天;Cisco 8 月也把服务器报价有效期提高到 14 天。但这种做法很少见。据 FT 的消息源,GPU 服务器价格近期至少上涨 20% 到 30%,CPU 节点价格则涨了两倍。TrendForce 的数据显示,服务器 DRAM 合约价仅 2025 年下半年就上涨 64%,到今年年底可能累计涨到 270%;HBM 在 2027 年可能再涨 70% 到 140%。

文章认为,工程师们只能在现有硬件上想办法,并举了两类方向。第一是架构层面的卸载和复用,比如 Nvidia 的 scale-in 网络把安全和存储等较重的任务从主处理器上卸载,以及优化 KV cache 来减少内存占用、避免浪费容量;第二是软件层面用便宜的存储替代昂贵的内存,AMD 最近收购的 Mext 让操作系统把闪存当作高速 DRAM 来用,通过预测内存需求,把不常用的内存页在 DRAM 和 NVMe 闪存之间换入换出,号称在每比特成本便宜 50 倍、每比特功耗低 30 倍的介质上达到相同性能(厂商说法,未经独立验证)。

有一个细节值得注意:CPU 节点涨幅反而比 GPU 服务器大得多。合理的解释是 GPU 服务器的总价里 GPU 本身占了大头,内存涨价被摊薄了;而 CPU 节点的物料成本里 DRAM 占比高,涨价被直接放大。这说明内存短缺打击的不只是 AI 训练集群,而是整个通用计算,这和 [推理已占三分之二 AI 负载那篇](2026-11-21-inference-now-drives-two-thirds-of-ai-workloads-changing-where-chips-get-deploye.md) 里讲的趋势叠在一起会更麻烦:推理负载对内存容量和带宽的依赖比训练更强。

个人看法:先找瓶颈,这次的瓶颈非常清楚,就是 DRAM 和 HBM 的产能。往下拆,解决这个瓶颈有三条路。第一是扩产,这是 Samsung、SK Hynix、Micron 三家以及正在上 EUV 的南亚、华邦在做的事(见 [Nanya and Winbond to purchase EUV tools from ASML](2026-11-16-nanya-and-winbond-to-purchase-euv-tools-from-asml-to-boost-dram-production-in-ta.md)),但新厂从开工到量产要两三年,这也是 SK Hynix 把缓解推迟到 2030 年的原因,而 [Micron 爱达荷内存厂因劳资纠纷暂停施工那篇](2026-11-08-ongoing-labor-dispute-sees-micron-pause-construction-at-its-4-5bn-memory-fab-in-.md) 说明扩产本身也有不确定性;第二是新的内存层级,比如 [d-Matrix 用 3D 堆叠 DRAM 插在 SRAM 和 HBM 之间那篇](2026-11-19-d-matrix-bets-stacked-dram-can-solve-inference-s-memory-bandwidth-problem.md),以及 CXL 内存扩展;第三是软件压缩需求,也就是这篇文章里的 KV cache 优化和 Mext 式的分层内存,让同样的 DRAM 撑更多的负载。所以受益的层次会是:第一层是存储原厂,在供不应求时它们拥有定价权,这是这一轮最直接的赢家;第二层是半导体设备,尤其是 ASML 的 EUV 和刻蚀、沉积设备商,因为所有扩产最后都要落到设备订单上;第三层是 NAND 和企业级 SSD,如果 Mext 这类方案普及,闪存会被拉进内存层级,SanDisk、Kioxia 这一类也会被重新定价;第四层是做内存效率的软件和芯片架构公司。反过来,被挤压的是服务器 OEM 本身,它们夹在原厂涨价和客户合同之间,即使能转嫁,也要付出客户关系的代价。

这对 AI 板块是一个结构性的分化信号,不是简单的利好或利空:基础设施里掌握稀缺产能的那一层继续受益,但整体算力成本上升会压缩云厂商和模型公司的利润,也会让中小买家更难拿到算力。对 edge AI 板块是一个间接利好,因为同样的 DRAM 短缺会推高集中式推理的成本,让端侧推理在一部分场景里更有性价比,不过端侧设备本身也要用 DRAM,所以这个逻辑只能算边际上的。现在还很难判断内存超级周期会持续多久,值得跟踪的是下一季度 TrendForce 的合约价数据,以及 Dell、Supermicro 的财报里毛利率有没有因为转嫁不及时而被压缩。
