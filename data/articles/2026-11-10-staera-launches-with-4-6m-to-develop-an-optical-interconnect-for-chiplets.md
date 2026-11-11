# Staera launches with $4.6M to develop an optical interconnect for chiplets
https://siliconangle.com/2026/11/10/staera-launches-with-4-6m-to-develop-an-optical-interconnect-for-chiplets/

（说明：Lightwire 的带宽和密度指标均为公司自述，产品计划 2030 年才开始商业出货。）

这篇文章背后的命题是：AI 加速器的下一个瓶颈可能不在计算单元，而在芯片内部的"导线"。当一颗加速器由多个 chiplet 拼成，chiplet 之间、以及计算芯片和 HBM 之间的数据搬运，正在被铜线的物理极限卡住。

文章指出，Staera Semiconductor 获得 460 万美元种子前融资，由新加坡的 Openspace Capital 领投，SGInnovate 等参投。文章先解释了结构：高端 AI 加速器由多个 chiplet 组成，它们通过 interposer（中介层）或更便宜的 bridge（桥接）连接，两者都用微小的铜线传输数据。Staera 想把铜线换成光链路，CEO 的说法是铜的性能在毫米到米这个 AI 加速器最关键的距离范围内会急剧下降，而外挂式光学又会增加功耗和复杂度，所以他们要把整条光链路做进芯片里。第一款产品 Lightwire 用氮化硅波导传光，氮化硅支持的波长范围更宽、损耗更低；光源是氮化镓微型 LED，氮化镓是直接带隙材料，发光不需要声子参与，效率更高。公司称 Lightwire 每条链路最高 8Gbps，每平方毫米可以做 600 多条光链路，用在 HBM4 存储堆栈上可以做到 24Tbps，而现有技术是 2.8Tbps。

个人看法：这篇和之前 [Arista 那篇](2026-11-05-arista-s-record-quarter-shows-the-network-has-become-central-to-ai.md) 讲的"网络成为 AI 核心"是同一条主线往更小尺度的延伸：机柜之间用光，机柜内用铜和共封装光学，现在连封装内部也开始考虑用光。值得注意的是它用微型 LED 而不是激光器，走的是"低速、大量并行"的路线，和今天 [QuiX](2026-11-10-quix-quantum-leads-national-mission-to-develop-100-qubit-photonic-quantum-comput.md) 用到的氮化硅波导也是同一种材料平台。按瓶颈来看，AI 板块现在的显性瓶颈是存储带宽（也就是"内存墙"），HBM 的带宽决定了推理速度，所以真正能解决这一层的是：第一层是 HBM 厂商本身（SK hynix、Samsung、Micron）；第二层是先进封装，TSMC 的 CoWoS 这类产能；第三层才是像 Staera 这样试图改变互连介质的新技术。但 460 万美元的种子前融资、2030 年才出货，现在离产业影响还很远，只能当作一个技术方向的信号，值得跟踪的是有没有 HBM 或封装大厂和这类光互连公司建立合作。
