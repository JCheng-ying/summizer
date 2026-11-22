# Securing the turbine is only half the battle: the emissions monitoring path to data center power
https://www.datacenterdynamics.com/en/opinions/securing-the-turbine-is-only-half-the-battle-the-emissions-monitoring-path-to-data-center-power/

先说明:这是 DCD 的一篇观点专栏,从内容看作者来自排放监测(CEMS)行业,文中对"选对供应商"的强调带有明显的行业立场,相关判断应结合这一点看。

这篇文章想说的是,AI 数据中心的电力瓶颈不只是"能不能买到燃气轮机",而是买到之后还有一条无法压缩的合规链条。如果这个判断成立,那么表后燃气发电的项目时间表里,真正的关键路径可能不是设备交付,而是许可、排放监测和第三方认证。

文章指出,AI 和云需求把开发商推向表后发电,主要是燃气轮机和往复式发动机。2025 年全球燃气轮机订单达到 846 台、100.3 吉瓦,是前一年的两倍多,新的重型机组交付周期约三年,交付档期已排到 2030 年。但文章认为这只是一半的故事:买涡轮是"排队等"的采购问题,而空气许可、排放监测和外部认证是固定的监管步骤,决定机组什么时候能合法运行。文章引用一位 GE Vernova 高管的说法,即便订单排到 2028 年,涡轮也不是拖慢数据中心建设的关键因素。按美国数据中心能耗报告,到 2028 年数据中心可能占美国总用电量的 7% 到 12%,其中每一点来自现场燃烧发电的增长都带来新的许可和监测义务。连续排放监测系统(CEMS)包括采样接口、气体调理、分析仪和数据采集处理系统,它必须在调试和外部排放测试之前就装好并正常运行。大型固定式燃气轮机可能适用 EPA 40 CFR Part 60 的新源性能标准,州和地方还会加码,所以两个类似的项目可能因为选址不同而有不同的监测要求。认证顺序是固定的:七天校准漂移测试、线性检查、循环时间测试、数据采集系统验证,最后由第三方测试公司做相对准确度审核(RATA),这些都有最短时长,加人也压缩不了。文章建议把 RATA 当作和涡轮交付同等重要的里程碑写进总进度表,并尽早锁定集成商,因为原本按稳定需求配置的集成商产能是有限的。

这和 [Anthropic signs $3.4bn gas generator deal to support 1.7GW of data center power](2026-11-09-anthropic-signs-3-4bn-gas-generator-deal-to-support-1-7gw-of-data-center-power.md)、[SoftBank’s billion-dollar loss may have put a cap on AI’s natural gas ambitions](2026-11-12-softbank-s-billion-dollar-loss-may-have-put-a-cap-on-ai-s-natural-gas-ambitions.md) 是一条线:AI 公司正在大规模转向现场燃气发电,而这篇补充的是这条路上容易被忽视的监管环节。

个人看法:我觉得这篇文章的价值在于把"能源瓶颈"再拆细了一层。之前我们把数据中心拆成计算、电力、散热、基础设施四大系统,电力这一块又可以拆成:第一是发电设备本身(燃气轮机、往复式发动机、燃料电池),交付周期三年;第二是并网或许可,表后发电绕开了电网排队,却换来了空气许可;第三是排放监测和认证,是一条固定时长、不能并行压缩的流程;第四是燃料供应,也就是天然气管道接入。按"谁在解决具体瓶颈"来看,能源板块里受益的层次会是:第一层仍然是燃气轮机厂商(GE Vernova、Siemens Energy、Mitsubishi Power),订单已经排到 2030 年;第二层是往复式发动机和燃料电池(Caterpillar、Wärtsilä、Bloom Energy),它们交付更快,可以填补涡轮的空档;第三层是这篇文章点出的、规模小但确定性高的环节——排放分析仪和环境监测设备(Thermo Fisher、Emerson、ABB、Teledyne 等都有相关业务),以及第三方测试和 EPC 集成商,需求是被监管强制拉动的。需要提醒的是,随着各地对数据中心环境影响的审查趋严([Meta 刚因为排放创纪录重新评估净零时间表](2026-11-20-meta-to-reevaluate-net-zero-timeline-on-the-back-of-record-emissions.md)),排放限值可能还会收紧,这会让监测环节更重要,也可能让部分燃气项目成本上升。这是一篇行业观点,不是新的数据,值得跟踪的是有没有大型表后燃气项目因为许可或认证环节公开延期。
