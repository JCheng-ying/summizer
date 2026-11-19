# Nscale brings Nvidia Vera Rubin NVL72 rack online
https://www.datacenterdynamics.com/en/news/nscale-brings-nvidia-vera-rubin-nvl72-rack-online/

这条新闻表面上是又一家云厂商点亮了 Nvidia 新一代机柜，背后更重要的命题是：AI 数据中心的交付方式正在从"现场组装"转向"工厂预制、整柜交付"。当 GPU 每一代都在变，真正决定上线速度的已经不只是能不能拿到芯片，而是从拿到芯片到投入生产要多少天。

文章指出，Nscale 上线了第一套 Nvidia Vera Rubin NVL72 机柜级系统，基于 Dell PowerEdge XE9812，并接入 Nscale 自己的云平台，这是未来几个月"全球部署"的第一套。Rubin 平台一共包含六颗芯片：Vera CPU、Rubin GPU、NVLink 6 交换芯片、ConnectX-9 SuperNIC、BlueField-4 DPU 和 Spectrum-6 以太网交换芯片。Vera 接替 Grace，Rubin 接替 Blackwell，Nvidia 称 Rubin 推理和训练性能分别是 Blackwell 的 5 倍和 3.5 倍。NVL72 由 36 颗 CPU 和 72 颗 GPU 组成，这一代是 100% 液冷，采用免线缆的模块化托盘设计，Nvidia 称安装时间可以从两小时缩短到五分钟。

文章还提到一个细节：Nscale 称自己是业内第一个部署 Dell 全集成液冷 L11 网络机柜的公司，基于 Dell IR9148 平台，机柜里集成了八台 Nvidia SN6600-LD 交换机、shuffle box、电源架、机柜控制器和柜内冷却液分配单元（CDU）。Dell 的 CTO Ihab Tarazi 说，Dell PowerRack 在工厂里就把计算、网络、电源、散热集成和验证好，减少现场工作量。文章没有披露机柜放在哪个数据中心，并提到 CoreWeave、Oracle 和 Google Cloud 也已经上线了 Vera Rubin。

个人看法：这篇和同日的 [NexGen Cloud 挖走 Nscale 的 Dan Thomas](2026-11-19-nexgen-cloud-hires-nscale-s-dan-thomas-as-chief-infrastructure-officer.md) 放在一起看很有意思：那篇里投资者质疑的正是 neocloud"签约容量多、实际上线少"，而 Nscale 这次的宣传重点恰恰是交付速度，此前它也宣布过 [2.5 个月内上线两个数据中心、25,000 张 GPU](2026-11-13-nscale-brings-online-two-data-centers-and-25-000-gpus-in-2-5-months.md)。对正在准备 Nasdaq IPO 的 Nscale 来说，"第一时间点亮新一代 GPU"既是技术进展，也是资本市场叙事。

按照"先找瓶颈"的思路，这一代的瓶颈是现场集成：100% 液冷意味着每个机柜都要接冷却液管路，网络机柜也要液冷，传统的"服务器运到现场、工程师插线调试"模式越来越慢。所以解决瓶颈的那一层是：第一层是整柜集成商，Dell、Supermicro、HPE 这类能在工厂完成计算+网络+电源+散热集成验证的厂商；第二层是液冷供应链，CDU、冷板、快接头，Vertiv、Schneider、CoolIT、Boyd 这些公司，而且这次连网络交换机也液冷化了，液冷的覆盖面在扩大；第三层仍然是 Nvidia 本身，六颗芯片全栈打包，NVLink、DPU、SuperNIC、以太网交换都是 Nvidia 的，这意味着 Broadcom、Marvell 在 Nvidia 机柜内部的空间被进一步压缩。利好 AI 板块，这一点比较确定，因为 Rubin 已经从发布进入多家云厂商的量产部署阶段。

但要克制：目前只是"第一套"机柜，Nscale 没有说规模和地点，性能倍数是 Nvidia 自己的说法。值得关注的是 Nscale 接下来几个月的全球部署规模，以及它的 IPO 招股书里会怎么披露已上线容量。
