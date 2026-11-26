# Quanta inks $367m deal with Bloom Energy for two fuel cell anchored microgrid systems
https://www.datacenterdynamics.com/en/news/quanta-inks-367m-deal-with-bloom-energy-for-two-fuel-cell-anchored-microgrid-systems/

这条消息看起来只是一笔采购，但它背后的命题是：AI 产业链上"等不起电网"的已经不只是数据中心运营商，连给数据中心造服务器的工厂也开始自建电源了。电力约束正在从数据中心一路往上游传导到 AI 硬件制造环节。

文章指出，台湾服务器代工厂广达（Quanta）以美国子公司 Quanta Manufacturing Nashville 的名义，向 Bloom Energy 购买两套燃料电池微电网系统，据报道总价约 3.67 亿美元，包含技术服务：一个加州项目约 2.499 亿美元，一个田纳西项目约 1.171 亿美元，更多细节未公开。Quanta Manufacturing Nashville 是广达在美国制造、组装、维修和翻新服务器与云硬件的工厂。这已经是双方第三笔交易，此前 2024 年 4 月有 2000 万美元两套系统、2024 年 10 月有 8000 万美元三套系统。

文章还梳理了 Bloom 在数据中心市场的布局：Bloom 做固体氧化物燃料电池（SOFC），产品 Bloom Box 用电化学方式把燃料转化为电力而不燃烧，虽然可以用氢气，但目前绝大多数用天然气。它近期签下了 NTT Data 900MW 的合同（见之前那篇 [NTT DATA signs 900MW fuel cell supply deal with Bloom Energy](2026-11-08-ntt-data-signs-900mw-fuel-cell-supply-deal-with-bloom-energy.md)）、把与 Oracle 的协议扩大到最多 2.8GW（但 Oracle 在新墨西哥 Doña Ana 县的 Jupiter 数据中心因供气管道延伸遭反对而受阻）、与 Equinix 在 19 个数据中心部署超过 100MW、与 American Electric Power 签了最多 1GW 的离网 SOFC 供应，而 AEP 又在 10 月和 Google 签了 20 年购电协议，从怀俄明州 Cheyenne 附近一个使用 Bloom 燃料电池的项目购买 702MW 电力（和 [Google 在 Cheyenne 的 170 亿美元园区](2026-11-08-google-announces-17bn-data-center-campus-in-cheyenne-wyoming.md) 是同一条线）。

个人看法：这里的瓶颈很明确，就是并网排队。一座新工厂或者数据中心向电网申请大容量接入，等变电站和输电线往往要数年，而 AI 服务器的订单不会等。燃料电池的价值不在于便宜，而在于快，可以在电网到位之前先现场发电，之后再转为备用或者调峰。所以能源板块里真正受益的层次是：第一层是 Bloom 这样能快速交付现场发电的厂商；第二层是天然气上游和管道，因为 Bloom 绝大部分靠天然气运行，Oracle 那个项目恰恰卡在了管道上，说明"燃料供应"本身可能变成新的瓶颈；第三层才是长期的氢能路线，目前还看不到。对 AI 板块的意义则是间接的：广达是英伟达 GB 系列整机柜的核心代工厂之一，它在美国扩产并为工厂单独配电，说明美国本土 AI 服务器制造在加速，这对整机柜、液冷和电源这些配套环节是持续需求。

需要克制的是，3.67 亿美元的金额来自报道，具体装机容量和交付时间都没有披露，而且燃料电池依赖天然气，在减碳和社区反对上都有隐患（Oracle 项目就是例子）。值得跟踪的信号是 Bloom 后续财报里数据中心和制造业客户的收入占比，以及有没有更多 AI 硬件制造商跟进自建电源。
