# Indian chip startup Bharat Semi lands $24M seed round as it eyes global AI sensor market
https://techcrunch.com/2026/11/15/indian-chip-startup-bharat-semi-lands-24m-seed-round-as-it-eyes-global-ai-sensor-market/

这篇文章表面上是一笔 2400 万美元的种子轮融资，但背后其实是 edge AI 一个越来越清晰的方向：AI 推理正在从数据中心、从终端的 SoC 继续往下沉，一直沉到传感器本身。如果"在像素旁边就把图像看懂"这条路线成立，那么一台空调、一架无人机甚至一个监控摄像头，就不再需要一块独立的、昂贵的处理器来做视觉理解，整个视觉系统的成本结构和功耗结构都会被改写。

文章指出，总部位于新德里的 Bharat Semi 成立将近五年，目前仍未产生收入，这轮全股权种子轮由 Info Edge Group、South Park Commons 和 Indus Bridge Ventures 领投，Valour Capital、Micromax、Gaingels 以及个人投资者跟投。公司声称已经拿到了美国国防科技公司 General Atomics 和印度 Kaynes Semicon 的 design win，但需要注意的是，它的图像传感器仍在开发中，首批商业化量产的目标是 2027 年。第一代传感器已经进入原型阶段，带有更强 AI 能力的第二代预计 2027 年中进入原型，年底前交到客户手里。

技术上，文章提出 Bharat Semi 做的是可编程图像传感器，把图像采集、图像处理和 AI 能力集成在同一颗芯片上。传统的视觉系统其实是三块芯片串在一起：第一是图像传感器（CMOS image sensor），负责把光信号变成原始像素数据；第二是图像信号处理器（ISP），负责去噪、白平衡、去马赛克等，把原始数据变成可用的图像；第三是 SoC，负责在图像上跑检测、识别这类 AI 模型。三块芯片之间要不停搬运大量像素数据，而数据搬运本身就是功耗和成本的大头。联合创始人 Vrinda Kapoor 声称，把这三层合成一颗芯片，系统成本相比传统方案至少能降低 70%——这个数字来自公司自己，产品也还没量产，只能当作目标而不是已验证的指标。她用的说法是从"sensors"走向"sense-making"，举的例子是能判断房间里有没有人并自动调节的空调，以及在没有昂贵算力硬件的情况下也能处理视觉信息的无人机。目标市场是智能家居、工业自动化、安防监控和航空航天。

团队方面，CTO Boyd Fowler 此前在图像传感器厂商 OmniVision 担任同一职位，这是这家公司最硬的背书之一；另一位联合创始人 Vinayak Dalmia 出身麦肯锡和私募。公司约 75 名员工，其中 10 到 12 人在美国 Santa Clara 做工程和业务拓展，计划 2027 年中把美国团队扩到约 20 人，并开始在欧洲招工程师。文章还提到，Bharat Semi 在 2024 年宣布过一个与美国太空军（U.S. Space Force）有技术合作的印度晶圆厂项目，但这个项目仍在开发中、还在找本土合作方来建设和运营，与图像传感器业务是分开的；公司本身坚持 fabless 模式，这轮融资不会投到晶圆厂上。

个人看法：先找瓶颈。今天 edge AI 视觉落地卡住的，往往不是模型不够好，而是第一，端侧算力芯片的成本和功耗，让很多低价设备（空调、家电、小型无人机）根本装不起一块能跑视觉模型的 SoC；第二，传感器到处理器之间的数据带宽和搬运功耗。Bharat Semi 想解决的正是这两层，所以它所在的位置——"传感器内计算"——才是这篇文章真正值得关注的点，而不是"印度又一家芯片公司拿到钱"。这个方向也不是它独有的，Sony 早在几年前就推出过集成 AI 处理的智能视觉传感器，OmniVision、Ambarella 这类公司也在视觉 SoC 上做边缘推理，所以一个 75 人、尚无收入的种子轮公司要面对的是成熟大厂的竞争，CTO 的 OmniVision 背景能帮它缩短路径，但还不能证明它能赢。

从板块来看，受益的层次会是：第一层是 edge AI 板块，这是最直接的挂钩，如果传感器内 AI 推理能把视觉系统成本真的压下来，就会把视觉 AI 推向大量原本装不起算力的终端，Sony、OmniVision、Ambarella 这类视觉芯片厂商以及做端侧 NPU IP 的 Arm、Cadence 都处在同一条链上；第二层是机器人板块，工业自动化和无人机都是它点名的场景，更便宜、更低功耗的视觉感知会直接降低机器人和无人机的 BOM 成本，这和之前写过的 [Skydio 那篇非对称无人机](2026-11-15-why-skydio-built-a-lopsided-drone.md)、[Ring 家用安防无人机](2026-11-10-ring-known-for-its-doorbell-cameras-launches-a-home-security-drone-and-an-enterp.md)讨论的消费/安防无人机走在同一个方向上；第三层是 AI 板块里"推理下沉"的那部分，与 [Fractile 融资 7.2 亿美元做推理芯片](2026-11-11-british-inference-chip-developer-fractile-raises-720m-in-funding.md)类似，资本都在押注专用推理硅片，只不过 Fractile 押的是数据中心推理，Bharat Semi 押的是最末端的传感器。至于太空经济板块，General Atomics 的 design win 和与太空军的晶圆厂合作只是给航空航天场景开了一条缝，规模还谈不上，这次不硬挂。

另外值得一提的是印度这条线。最近几篇写的 [STT GDC 在 Noida 上线 22MW 数据中心](2026-11-13-sttgdc-launches-22mw-data-center-in-noida-india.md)和 [AirTrunk 在安得拉邦签下 1.8GW 数据中心 MoU](2026-11-14-airtrunk-signs-mou-for-1-8gw-of-data-center-capacity-in-andhra-pradesh-india.md)，说的都是印度在 AI 基础设施"重资产"那一层吸引资本；而 Bharat Semi 代表的是另一面——印度在芯片制造上还没站稳，于是本土团队选择走 fabless、做设计和软件，从细分的专用芯片切入全球市场。这条路径更轻，但也意味着它的量产依赖外部代工，在 2027 年量产之前，design win 能不能变成真实订单还是未知数。

现在还很早，一家无收入的种子轮公司离影响板块还有很长距离，只能观望。但值得关注的是 2027 年中第二代原型和年底的客户交付节点，以及 General Atomics、Kaynes Semicon 的 design win 会不会转成量产订单——如果能看到这些信号，"传感器内 AI"这条 edge AI 路线的可信度会高很多。
