# Vodafone, AST SpaceMobile switches on Earth-space station in Málaga, Spain
https://www.datacenterdynamics.com/en/news/vodafone-ast-spacemobile-switches-on-earth-space-station-in-m%C3%A1laga-spain/

手机直连卫星(direct-to-device,D2D)这件事,过去讨论最多的是天上那一半:卫星够不够大、能不能发上去、频谱够不够。这篇短新闻讲的是地上那一半——一颗低轨卫星要变成运营商网络的一部分,中间必须有网关、有核心网对接、有芯片和终端的联合验证。如果这一半没有打通,星座再大也只是一张独立的网,而不是运营商可以"无缝切换"的覆盖延伸。

文章指出,Vodafone 和 AST SpaceMobile 在西班牙 Málaga 启用了两家公司所称的欧洲首个"地球—太空站"(Earth-space station),它属于双方与 Málaga 大学电信工程学院、以及 Mobile & Aerospace Networks Lab(Mobilenet)合作建立的 Málaga Satellite Centre。这个中心的用途是验证和优化 D2D 智能手机宽带接入,以及在地面覆盖薄弱或空白区域的应用。文章提到 Vodafone 是 AST SpaceMobile 众多战略投资方和合作运营商之一,AST 的低轨星座可以通过网关直接接入运营商的地面网络,这次用的网关是一个 0.9 米口径的天线。Vodafone 此前已在距 Málaga 约 125 公里的 Granada 开始初步激活,和 Granada 大学合作安装了一套自动化系统,能远程采集 AST 卫星、Málaga 网关和地面网络之间交换的视频、数据和通话日志。

文章列出的测试方向可以拆成三类:第一是终端和芯片层,Vodafone 把这里定位成运营商、芯片厂商和手机厂商联合测试软硬件的场所,目标包括改善性能和电池续航;第二是行业应用层,包括远程或危险场所的自主巡检机器人、联网汽车、安全无人机等能在地面网络和低轨卫星网络之间无缝切换的设备;第三是公共安全层,Vodafone 暗示还会测试专用于公共保护与救灾(PPDR)机构——消防、急救、救援——的频段,以及地面与非地面网络(NTN)的互操作场景。

个人看法:这篇要和之前写过的两篇 AST 文章连起来看。[AST SpaceMobile presses case for developing own launch vehicle](2026-11-12-ast-spacemobile-presses-case-for-developing-own-launch-vehicle.md) 和 [AST SpaceMobile to build its own 20-ton “Blacklift” rockets](2026-11-16-ast-spacemobile-to-build-its-own-20-ton-blacklift-rockets-with-firefly-aerospace.md) 讲的是 AST 在发射班次这个瓶颈上被迫垂直整合;而这篇讲的是另一端——卫星上天之后,怎么被运营商真正用起来。AST 的商业模式和 Starlink 的直连业务不同,它更依赖和运营商分成、借用运营商的频谱和客户,所以 Vodafone 这类既是股东又是渠道的合作方愿不愿意投入地面验证,本身就是 AST 能否变现的前提。这也和 [BT delays Starlink partnership](2026-11-11-bt-delays-starlink-partnership-amid-recent-ukrainian-disruption-report.md) 形成对照:欧洲运营商对 Starlink 有依赖顾虑,而 Vodafone 把测试中心放在欧盟、强调"让欧盟成员国合作开发关键通信系统",可以理解为在给自己参股的另一条路线争取位置。

按先找瓶颈的方法看,D2D 当下卡住的不只是卫星数量,还有终端侧:手机直连低轨卫星时链路预算很紧,功耗、天线增益、在两张网之间切换的时延和稳定性,都需要芯片和终端厂商配合调优,而这类联合测试过去缺少一个运营商级别的真实环境。所以受益的层次会是:第一层是星座运营商本身,AST SpaceMobile 能否把"欧洲首个"的测试网关变成正式商用,决定了它在欧洲的收入兑现节奏,这直接挂在太空经济板块上;第二层是地面段基础设施,网关天线、射频前端、核心网对接软件,这一层原文只提到 0.9 米天线,没有点名供应商,但无论哪条 D2D 路线胜出,地面站数量都会增加;第三层是终端芯片,原文没有点名厂商,按行业格局看 Qualcomm、MediaTek 这类已经在做 NTN 基带的芯片公司会是联合测试的天然参与者,不过这是我的延展,不是原文内容。

至于原文提到的自主巡检机器人和安全无人机,我倾向于把它当成对机器人板块和 edge AI 板块的一个弱信号:它说明运营商开始把"机器人在无地面覆盖区域保持连接"当成需要正式验证的场景,但文章没有给出任何具体客户、设备型号或部署规模,目前更像测试清单而不是订单。现在还早,值得跟踪的是两件事:一是 Málaga 中心之后有没有公布具体参与测试的芯片和手机厂商;二是 Vodafone 在欧洲推出 AST 商用 D2D 服务的时间表,以及它和 PPDR 频段测试能否转化成公共安全领域的采购。
