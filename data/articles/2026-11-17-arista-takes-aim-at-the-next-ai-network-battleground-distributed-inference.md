# Arista takes aim at the next AI network battleground: distributed inference
https://siliconangle.com/2026/11/17/arista-takes-aim-at-the-next-ai-network-battleground-distributed-inference/

这篇文章讨论的是 AI 网络投资重心可能发生的一次转移:过去两年大家关注的是"后端网络"——把成千上万块 GPU 连成一个训练集群的那张网;而如果推理走向分布式,下一轮需求会出现在"前端网络",也就是把推理请求从用户送到各地算力点、再在站点之间搬运的那张网。如果这个判断成立,AI 网络的受益者就不再只是做超大规模交换机的那几家。

需要先说明,这是 ZK Research 首席分析师 Zeus Kerravala 为 SiliconANGLE 写的分析文章,内容基于 Arista 的发布会和会前简报,文中关于产品功耗、客户反馈等表述来自厂商,未经独立验证。

文章指出,Arista 在 SC26 上发布了一系列 Etherlink R4 路由平台,定位是它所谓的"分布式推理",同时推出用于数据中心互联的可插拔光线路系统。产品包括:1RU 的 7020R4 和 7020HR4 接入路由器,25G 到 400G 端口,深缓冲,每个端口可选线速加密,其中 HR4 是耐温加固版,面向蜂窝基站和户外场景;带双引擎的 7282R4 边缘/核心路由器;25.6Tbps、64 个 400G 端口、一半支持 ZR/ZR+ 相干光模块的 7280R4,用来把本地网络桥接到广域网;以及在一对光纤上承载 25.6Tbps 的可插拔光线路系统。全部基于 Broadcom 的 Jericho 和 Qumran 芯片,宣称功耗比竞品 7nm、16nm 平台低最多 60%;除了 7020HR4 要到 2027 年初出货,其余现已上市。

文章认为推理会因为三个相互强化的原因走向分布式:第一是延迟,集中式集群适合逐行输出文本的聊天机器人,但不适合 Agentic AI,一个请求可能触发几十次链式模型调用,每一毫秒都会累积;第二是数据主权,监管越来越要求推理请求和数据留在本国境内,欧洲 IT 负责人不愿把数据送到美国云;第三是电力和空间,企业会在任何有容量的地方部署推理,网络必须跟上。由此得出的推论是,前端网络不能再被当成管道,它需要具备后端网络的属性:深缓冲、流量工程、多租户和加密,因为流量现在要离开机房。Arista 的产品线管理副总裁 Brendan Gibbs 还提到,Arista AI 业务里大约 30% 已经是跨站点(scale-across)。

作者的几点判断也值得注意。第一,这次发布是 Arista "向下走",产品更小更便宜,补齐了它此前没有合适产品的前端层级;入门级产品也配 400G 上行,目标是 10 年生命周期,升级时换光模块而不是换机箱;7280R4 是和一家超大规模客户联合设计的。第二,加固版 7020HR4 面向 5G 和 AI-RAN 基站,作者认为电信运营商基本缺席了这轮 AI 建设,但它们拥有最后一公里和靠近用户的机房,这正是低延迟推理需要的,而且在欧洲和亚太这个机会可能大于美国,BT、NTT、Telstra 等有条件做托管 AI 工厂。第三,线速 MACsec/IPsec 是差异点,但 Arista 无意取代防火墙,预期 Palo Alto Networks 继续部署在它后面。

个人看法:这篇和之前那篇 [Arista 创纪录季度说明网络已成为 AI 核心](2026-11-05-arista-s-record-quarter-shows-the-network-has-become-central-to-ai.md) 正好形成前后呼应——那篇讲的是后端网络已经被证明,这篇讲的是 Arista 押注下一块还没定型的前端。它也和 [Nvidia 据报想利用 Brightspeed 的电信中心机房做推理网络](2026-11-09-nvidia-looks-to-tap-brightspeed-central-offices-for-inference-network-report.md)、以及 [主权云买方指南](2026-11-13-sovereign-or-not-the-2026-hyperscaler-buyer-s-guide.md) 是同一条线索:推理在往离用户更近、在法域上更"本地"的地方走。按"先找瓶颈再找解决瓶颈的那一层"来拆,这里的瓶颈不是 GPU 数量,而是三件事:Agent 链式调用的延迟、跨站点流量的加密和隔离、以及分散站点的电力和运维。受益的层次会是:第一层是网络芯片,无论 Arista 还是别家做前端路由,Broadcom 的 Jericho/Qumran 这一类商用芯片都在里面,这是 AI 板块里相对确定的一层;第二层是网络设备商,Arista 是直接参与者,但前端路由这块 Cisco、Juniper(已并入 HPE)、Nokia 都是老牌玩家,Arista 是挑战者而不是默认赢家;第三层是光互联,ZR/ZR+ 相干光模块和光线路系统的需求会随跨站点流量增长,Ciena、Coherent、Marvell 这类公司在这一层;第四层是 edge AI 板块,因为推理下沉到基站、电信机房和本地站点,本身就是 edge AI 的基础设施化,AI-RAN 是其中最值得关注的具体场景。

但也要克制一点看:作者本人对 Arista 明显偏乐观,而"Agent 会让流量暴增"目前还只是推测,文章自己也说"没人知道 Agent 会对流量造成什么影响"。值得跟踪的信号是 Arista 后续财报里非超大规模客户和电信客户的收入占比,以及 7020HR4 明年初出货后有没有运营商公开采用——如果欧洲或亚太的运营商真的拿它去做托管推理,前端网络这个判断才算落地。
