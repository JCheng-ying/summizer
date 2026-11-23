# Apollo and Goldman Sachs lead $44bn SpaceX GPU financing deal
https://www.datacenterdynamics.com/en/news/apollo-and-goldman-sachs-lead-44bn-spacex-gpu-financing-deal/

这条消息篇幅很短,但它确认了一件过去两年只在私募市场里发生、现在被摆到台面上的事情:GPU 已经成为一种可以被华尔街标准化定价的资产类别。一家公司要买 440 亿美元的芯片,不是靠股权融资或者自有现金流,而是像买飞机、买船一样发行以资产为基础的债券。如果这种结构能持续扩大,AI 算力扩张的速度上限就不再只取决于 Nvidia 能造多少芯片,而是取决于信用市场愿意为这些芯片提供多少杠杆。

文章指出,Apollo 和 Goldman Sachs 确认完成了 440 亿美元优先级和次级票据的定价,用于为 SpaceX 采购 GPU。这笔交易超额认购,由 Apollo 和 Goldman Sachs 牵头,BlackRock 和 Goldman Sachs Asset Management 管理的基金及账户、以及 KKR 提供咨询的资本账户作为基石投资人认购。两家机构称这是迄今为止规模最大的 GPU 融资。资金将用于采购 Nvidia Vera Rubin 芯片,部署在 SpaceX 的地面算力建设中,硬件预计 2027 年上半年交付。文章还提到,Musk 上个月已经确认 SpaceX 在为数据中心和其他 AI 基础设施寻求融资。Apollo 合伙人 Jamshid Ehsani 的表态里有一句值得注意:Apollo 强调的是"下行保护的、以资产为基础的结构"。

这句话正好接上了之前那篇 [Chips can survive the space environment — can their financing?](2026-11-21-chips-can-survive-the-space-environment-can-their-financing.md)。那篇文章指出,数据中心债务融资之所以便宜,是因为芯片本身可以作抵押,一旦违约贷方能收走芯片转卖;而它援引金融时报的报道说,SpaceX 那笔约 400 亿美元芯片融资的贷方要求芯片不得用于轨道数据中心。这次正式公告的措辞恰好是"支持地面算力建设",和那个条款的逻辑一致——虽然公告本身没有提到这项限制,所以只能说是吻合,不能说已被证实。换句话说,债权人愿意出钱的前提是芯片留在地面、收得回来。这和 [SpaceXAI 亚利桑那 6GW 数据中心那篇](2026-11-08-spacexai-plans-data-center-in-arizona-musk-s-firm-claims-it-will-have-6gw-capaci.md) 也是一条线:SpaceX 的算力扩张眼下实际落在地面,太空数据中心仍然是远期叙事,而 [SpaceX 为轨道数据中心定制 Vera Rubin 机架那篇](2026-11-12-spacex-developing-custom-nvidia-vera-rubin-rack-dubbed-kessel-for-its-orbital-da.md) 里的 Kessel 至少在这笔融资里还拿不到钱。

个人看法:这笔交易里真正的瓶颈不是芯片供应,而是资本成本。拆开来看,一个超大规模的 AI 算力项目要同时解决三件事:第一是买到芯片,第二是找到电和地,第三是找到愿意在芯片快速折旧的前提下提供长期资金的人。前两件过去讨论得很多,第三件现在开始显性化。Apollo、BlackRock、KKR 这类私募信贷机构进场,说明 GPU 抵押贷款正在从 CoreWeave 式的个案变成标准化产品。受益的层次会是:第一层仍然是 Nvidia,这 440 亿美元几乎全部会变成 Vera Rubin 的订单,也会顺带传导到 SK Hynix、Samsung、Micron 的 HBM 和台积电的 CoWoS 产能;第二层是电力和散热,芯片 2027 年上半年交付,意味着对应的电力、变压器、液冷要在此之前到位,Vertiv、Schneider、Eaton 这一层是确定性跟着走的;第三层才是金融中介本身,私募信贷平台把 GPU 变成可以分层销售的票据,自己赚的是结构化和分销的钱。这对 AI 板块是利好,因为它证明大型买家仍然能在信用市场上拿到便宜的钱;对太空经济板块反而是一个中性偏谨慎的信号,因为最大的一笔资金明确流向地面,而不是轨道。

但也要注意风险在哪里。用债务买一种两三年就会被下一代替代的资产,前提是 GPU 的二手残值能撑住,而这恰好是 [Anthropic IPO 循环融资那篇](2026-11-19-anthropic-s-ipo-puts-ai-s-circular-financing-boom-to-the-test.md) 讨论过的同一个问题的另一面:只要终端需求不掉,这套杠杆就是加速器;一旦需求或芯片价格松动,压力会顺着票据的次级层先传出来。现在还看不到这个信号,值得跟踪的是这批票据后续在二级市场的利差,以及其他算力买家会不会很快复制同样的结构。
