# Q.security Launches With $11.5 Million From Castle Island Ventures, New York Life Ventures and Coinbase Ventures
https://thequantuminsider.com/2026/11/23/q-security-launches-with-11-5-million-from-castle-island-ventures-new-york-life-ventures-and-coinbase-ventures/

(说明:原文是 Q.security 的公司新闻稿,The Quantum Insider 以 PRESS RELEASE 形式转载,SiliconANGLE 同日也做了内容基本一致的报道。平台能力和"更快、更低成本降低风险"之类的说法都来自公司自述,未经独立验证。)

这篇新闻稿背后更大的命题是:量子计算对产业最先产生的"真实需求",可能并不是量子计算机本身,而是为了防御量子计算机而必须进行的密码迁移。量子计算机什么时候能真正破解 RSA 和椭圆曲线密码(所谓 Q-Day)目前没有人能给出确定答案,但"先收集、后解密"(harvest-now, decrypt-later)意味着攻击者今天就可以截获加密数据、等将来再解密,所以对持有长期敏感数据的金融机构来说,迁移的截止时间其实已经被提前到了现在。

文章指出,Q.security 以 1150 万美元种子轮走出隐身状态,由 Castle Island Ventures 领投,New York Life Ventures 和 Coinbase Ventures 参投,其他投资方还包括 Fin Capital、SBI US Gateway Fund(SBI Holdings 与 Plug and Play 的合资基金)和 Ground Up Ventures。它的定位是"业务优先"的后量子密码(PQC)修复平台,而不是又一个扫描工具。文章提出的核心痛点是:企业做完密码资产盘点之后会得到大量发现项,但时间和人力有限,不知道先修哪个。Q.security 的做法可以拆成四步:第一是把企业的业务结构和应用系统建成一张地图,把密码盘点结果挂到这张地图上,让风险最高的资产排在最前面;第二是用对话式 AI 界面让安全团队调查暴露面、推进修复;第三是和企业现有的网络安全与基础设施工具集成,通过 AI 引导的 runbook、工单和自动化把修复做完;第四是验证修复确实生效,并在标准和威胁变化时持续监控密码态势。

创始团队背景是这家公司最有信息量的部分。文章提到,CEO Guy Peer 联合创办了 Unbound Security,并带领研发一直到 2021 年被 Coinbase 收购;另一位创始人 Nir Steinherz 曾任 Coinbase 产品总监、Unbound Security 战略与产品副总裁,以及花旗安全创新中心高级副总裁。两人据称主导过一次保护数千亿美元资产的密码迁移。投资方里同时出现保险公司(New York Life)和加密货币交易所(Coinbase)的风投部门,本身就说明了买单方是谁:持有长期敏感数据和高价值数字资产的金融机构。

和今天早些时候写的 [Microsoft builds Israeli team to help companies prepare for quantum threats](2026-11-23-microsoft-builds-israeli-team-to-help-companies-prepare-for-quantum-threats.md) 放在一起看,PQC 迁移服务这个赛道同一天就出现了一家巨头和一家初创公司。再往前,[Securities regulators warn that slow progress on quantum security is a mistake](2026-11-19-securities-regulators-warn-that-slow-progress-on-quantum-security-is-a-mistake.md) 讲的是监管层在催进度,而 [NEC and IBM Japan demonstrate integrated QKD and PQC communications](2026-11-17-nec-and-ibm-japan-demonstrate-integrated-qkd-and-pqc-communications.md) 和 [Hybrid QKD and PQC network connects Chicago and Europe across 8,000 km](2026-11-18-hybrid-qkd-and-pqc-network-connects-chicago-and-europe-across-8-000-km.md) 讲的是网络层的技术方案。

个人看法:我会把量子安全这条线拆成三层来看。第一层是算法和标准,NIST 已经发布了 PQC 标准,这一层基本是公共品,不太产生商业壁垒;第二层是网络与硬件层,QKD 设备、支持 PQC 的网络设备和 HSM,这一层有硬件收入但部署慢;第三层是迁移执行层,也就是 Q.security 所在的位置。按"先找瓶颈再找解决瓶颈的那一层"的逻辑,现在真正卡住企业的不是没有算法,而是不知道自己有多少密码资产、先改哪个、改完怎么证明改好了——这本质上是一个组织和工程问题,所以迁移执行层反而是最先有现金流的。这对量子计算板块是一个间接但重要的信号:量子硬件还没有大规模商业化,但"量子威胁"已经开始让企业花钱了,这部分预算主要流向网络安全公司(比如 Palo Alto Networks、Cloudflare、Thales 这类已经在做 PQC 的厂商),而不是量子硬件公司。同时也和 AI 板块有一点关系,因为这些平台都把 AI agent 作为执行修复的手段,算是 agentic AI 在安全运维里的一个落地场景,但这一点只能算加分项。1150 万美元种子轮规模不大,而且同一天就看到微软入场,初创公司的护城河主要是团队经验和渠道,能不能撑住还要看后面能不能拿到大型金融机构的落地客户。值得跟踪的信号是:监管机构是否给出明确的 PQC 迁移时间表,一旦有强制截止日期,这一层的需求会从"可选"变成"必须"。
