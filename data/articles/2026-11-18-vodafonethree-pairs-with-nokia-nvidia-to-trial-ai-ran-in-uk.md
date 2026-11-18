# VodafoneThree pairs with Nokia, Nvidia to trial AI-RAN in UK
https://www.datacenterdynamics.com/en/news/vodafonethree-pairs-with-nokia-nvidia-to-trial-ai-ran-in-uk/

这条消息本身只是一次试验公告,但它代表的方向值得注意:基站正在从专用通信设备,变成一种可以同时跑无线信号处理和 AI 推理的分布式计算节点。如果 AI-RAN 走通,那么电信运营商的无线网络就会变成离用户最近的一层 edge AI 基础设施,这和过去"推理只在大型数据中心里做"的格局不一样。

文章指出,VodafoneThree 将与 Nokia 合作,在英国移动网络上试验 AI-RAN,测试的是 Nokia 的 AI 原生 anyRAN 软件,运行在 Nvidia 的 Aerial RAN 计算机上,先在受控实验室环境进行,再推进到选定站点的外场试验。文章提到,VodafoneThree 是继 Virgin Media O2 上个月在伦敦 Paddington 的 Giga Site 测试、以及 EE 确认明年将在现网试验之后,又一家和 Nokia 合作测试 AI-RAN 的英国运营商,而 Nokia 推动 AI-RAN 主要是和 Nvidia 合作。运营商列出的潜在用例包括无线优化、移动性管理、能效、异常检测、覆盖与容量优化、QoS 保障,以及在 RAN 与 AI 工作负载之间共享加速算力。试验还会考察 AI 能否支持其 SuperMobile 服务,该服务基于网络切片,宣称速度最高是标准套餐的四倍、最低保障速率最高 15Mbps。VodafoneThree 会把试验结果和现有网络性能做基准对比,看 AI 在哪些环节最有价值。

个人看法:这里要把两类用例分开看,因为它们对应完全不同的投资逻辑。第一类是"AI for RAN",也就是用 AI 优化无线网络本身,比如频谱利用、能效和异常检测,这本质上是给运营商降本,受益方是 Nokia、Ericsson 这类 RAN 设备商和软件商,市场空间受运营商资本开支约束,增量有限;第二类是"AI on RAN",也就是用例列表最后那条"在 RAN 与 AI 工作负载之间共享加速算力",把基站闲时的 GPU 算力拿出来跑推理,这才是真正能改变产业链格局的部分,因为它意味着运营商可以把基站当成 edge AI 节点出租。这和之前写过的 [Nvidia 考虑利用 Brightspeed 的电信局端机房搭建推理网络](2026-11-09-nvidia-looks-to-tap-brightspeed-central-offices-for-inference-network-report.md) 是同一个思路:Nvidia 在把电信网络的物理位置变成推理网络的一部分。Nokia 最近也频繁出现在其他合作里,比如 [和 Nscale、Telia 等组建 gigafactory 联盟](2026-11-17-nokia-nscale-skeleton-telia-and-verda-form-gigafactory-consortium.md) 和 [与 Telia、QMill 在 5G 网络里演示量子加密](2026-11-17-telia-nokia-and-qmill-demonstrate-quantum-powered-encryption-in-a-5g-network.md),可以看出它在努力把自己从传统设备商重新定位成 AI 网络公司。

按瓶颈来看,AI-RAN 当下卡住的不是技术可行性,而是经济性:基站上放 GPU 的成本和功耗远高于专用 ASIC,只有在第二类用例能带来额外收入时才算得过账。所以受益的层次会是:第一层是提供加速平台的 Nvidia,Aerial 是目前 AI-RAN 试验里最常见的底座,这一点利好 edge AI 板块和 AI 板块;第二层是把 RAN 软件做成能跑在通用加速硬件上的 Nokia,它是这几次英国试验的共同供应商;第三层是运营商自身,如果"AI on RAN"能变现,它们的边缘站点资产会被重新估值。但目前三家英国运营商都还停留在试验阶段,VodafoneThree 甚至还没出实验室,现在判断为时尚早。值得跟踪的信号是试验结束后有没有运营商公布基站算力对外出租或者商用部署的具体规模,只有到那一步,edge AI 板块的逻辑才算真正落地。
