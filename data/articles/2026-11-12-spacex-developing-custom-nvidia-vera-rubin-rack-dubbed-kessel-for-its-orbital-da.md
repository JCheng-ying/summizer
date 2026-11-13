# SpaceX developing custom Nvidia Vera Rubin rack dubbed Kessel for its orbital data centers – report
https://www.datacenterdynamics.com/en/news/spacex-developing-custom-nvidia-vera-rubin-rack-dubbed-kessel-for-its-orbital-data-centers-report/

这条短新闻的意义在于:轨道数据中心开始从"愿景"落到"机柜级别的工程选择"上,而且 SpaceX 选择的路线是绕开 Nvidia 的整机方案、自己掌控供应链。

文章援引 SemiAnalysis 的报道指出,SpaceX 正在开发一款基于 Nvidia Vera Rubin NVL72 的定制机柜,代号 Kessel。它保留 NVL72 的基本配置——72 个 GPU 封装,分布在 18 个计算托盘和 9 个交换托盘上——但把 NVLink 线缆盒换成了一块 84 层的印刷电路板中板。SpaceX 计划把 Kessel 同时用于地面和轨道部署。SemiAnalysis 把它形容为"规模更小的 mini Kyber":Nvidia 的 Kyber 机柜要容纳 576 颗 GPU,背板是 156 层、采用 M9 覆铜板的 PCB,而 Kessel 只用 84 层的 M10 中板,层数少意味着更可行的制造路径。文章还提到,SpaceX 只向 Nvidia 采购芯片封装,绕过 Nvidia 的 L6 计算板,其余部件直接采购,从而掌控供应商选择;而 Nvidia 的 Kyber 机柜此前已因 PCB 中板的制造问题推迟 12 个月以上,发布推迟到 2028 年。

把这条和地面的机柜工程放在一起看会更清楚。第一,高层数 PCB 中板本身就是当前超大规模互联的一个制造瓶颈,Nvidia 自己的 Kyber 就卡在这里;第二,SpaceX 用"缩小 scale-up 域"换取可制造性,这和太空环境里对质量、功耗和散热面积的约束是一致的——之前那篇[发射变便宜后航天器瓶颈从质量转向表面积](2026-08-14-cheaper-launch-has-moved-the-spacecraft-bottleneck-mass-is-out-surface-area-is-in.md)讲的正是散热面积成为新约束。

个人看法:这和 style_reference 第一篇讨论的 SpaceX 轨道数据中心是同一个故事的工程续集,也和 [SpaceXAI 在亚利桑那规划数据中心](2026-11-08-spacexai-plans-data-center-in-arizona-musk-s-firm-claims-it-will-have-6gw-capaci.md)、[Google 第一颗数据中心卫星上线](2026-11-01-google-s-first-data-center-satellite-is-online-and-writing-poetry.md)互相呼应。先找瓶颈:轨道算力最先卡住的不是 GPU 本身,而是互联板的可制造性、抗辐射和散热。受益的层次会是:第一层仍然是 GPU 封装,Nvidia 依然是芯片供应方,利好 AI板块的算力层;第二层是高层数 PCB 和高端覆铜板供应链,因为 SpaceX 绕开 L6 板直接采购,这类零部件厂商的议价位置在上升;第三层是太空经济板块里的发射与在轨基础设施,Kessel 的存在说明 SpaceX 在把"自己发射、自己部署算力"做成闭环。值得注意的是,SpaceX 自己掌控供应链也意味着 Nvidia 在整机环节的附加值被削薄,这一点在 Nvidia 管理层动荡时尤其值得留意。

这仍然是第三方研究机构的报道,SpaceX 和 Nvidia 都没有官方确认。后续值得跟踪的是 Kessel 是否先在地面集群落地,以及 Starship 能否把这样的机柜以经济的频率送入轨道。
