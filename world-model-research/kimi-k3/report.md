# Kimi-K3 evaluation result

- Status: Completed
- Model: kimi-k3
- Output shown by Playground: 31.0K tokens

## Raw assistant answer

# 实时互动视频生成 / 世界模型：头部人物研究梳理（投资视角）

---

## 0. 方法与核实边界（务必先读）

在给出结论前，先明确本报告的信息边界，这直接关系到"事实与判断区分"的要求：

- 【事实标注规则】本文用三种标签：**【事实】**= 公开可查、多源印证的信息；**【判断】**= 我的分析推测；**【待核实】**= 我无法在当前条件下确认的信息。
- 【重要局限】**本次研究无法实时联网检索**，内容基于我训练数据中截至 **2025 年初** 的公开信息（arXiv、机构博客、媒体报道、个人主页等）。arXiv 论文编号是稳定标识符，可信度最高；个人主页域名、X/LinkedIn 账号我无法逐一验证，凡不确定处均明确标注，**未编造任何链接**。
- 该领域 2025 年内演进极快（如 Genie 后续版本、Sora 迭代、Decart 新产品、World Labs 产品化等很可能晚于我的知识截止），**第 6 节列出必须自行复核的动态清单**。

---

## 1. 执行摘要（核心判断）

**【判断】**

1. 该赛道已分化为三条技术路线：①**视频帧预测派**（动作条件化的扩散/自回归视频模型，代表：Genie 系、GameNGen、Oasis、DIAMOND）；②**规模化视频生成派**（DiT scaling 涌现"模拟器性质"，代表：Sora）；③**3D 原生空间派**（生成+显式 3D 表示，代表：World Labs）。2025–2026 年的分水岭指标是**实时性（fps）、可交互性（动作→帧的闭环）、长时记忆/持久性**。
2. 五位最值得跟踪的对象恰好覆盖上述路线与"学术—大厂—创业"全谱系：**Tim Rocktäschel**（DeepMind/UCL，Genie 系）、**Bill Peebles**（OpenAI，Sora/DiT）、**Tim Brooks**（OpenAI Sora 前 co-lead → DeepMind）、**李飞飞**（Stanford/World Labs）、**Dean Leitersdorf**（Decart，Oasis 实时世界模型）。
3. 人才流动本身是最强信号：Brooks 2024 年 10 月从 OpenAI 跳槽 DeepMind"做视频生成与世界模拟器"，说明两大厂正在把"视频生成"与"交互世界模型"两条线合并押注。
4. 资本密度最高的节点：World Labs（2.3 亿美元融资）与 Decart（实时可玩世界模型唯一开源标杆），分别代表"3D 资产平台"与"流式内容引擎"两种商业假说。

---

## 2. 赛道界定与技术路线地图

**范围界定**：本报告所称"世界模型"= 能根据用户输入（动作、文本、图像）**生成可交互视觉状态**的生成模型，面向游戏、虚拟世界、内容生成；**排除**机器人/自动驾驶/具身智能方向（故 Danijar Hafner 的 Dreamer 系、NVIDIA Cosmos 等仅作边界说明）。

### 里程碑成果谱系（均为【事实】，arXiv 链接可信度高）

| 时间 | 成果 | 团队 | 一句话定位 | 链接 |
| --- | --- | --- | --- | --- |
| 2018 | World Models | David Ha & Schmidhuber | 概念源头（VAE+RNN 学环境） | [arXiv:1803.10122](https://arxiv.org/abs/1803.10122) |
| 2022 | VPT | OpenAI (Bowen Baker 等) | Minecraft 视频预训练+动作反推 | [arXiv:2206.11795](https://arxiv.org/abs/2206.11795) |
| 2022 | DiT | Peebles & Xie | 视频世界模型的架构底座 | [arXiv:2212.09748](https://arxiv.org/abs/2212.09748) |
| 2023.10 | UniSim | UC Berkeley + Google DeepMind | "通用交互模拟器"早期范式 | [arXiv:2310.06114](https://arxiv.org/abs/2310.06114) |
| 2024.02 | **Genie** | Google DeepMind | 无标注视频学潜在动作，图生可玩环境 | [arXiv:2402.15391](https://arxiv.org/abs/2402.15391) |
| 2024.02 | **Sora** | OpenAI | "视频生成模型即世界模拟器" | [arXiv:2402.17177](https://arxiv.org/abs/2402.17177) |
| 2024.05 | DIAMOND | 日内瓦大学等 | 扩散世界模型，Atari/CS:GO 可玩 | [arXiv:2405.12399](https://arxiv.org/abs/2405.12399) |
| 2024.06 | Pandora | UCSD 等 | 自然语言动作的通用世界模型 | [arXiv:2406.09455](https://arxiv.org/abs/2406.09455) |
| 2024.08 | **GameNGen** | Google | 首个 20fps 实时神经游戏引擎（DOOM） | [arXiv:2408.14837](https://arxiv.org/abs/2408.14837) |
| 2024.10/11 | **Oasis** | Decart × Etched | 首个公开可玩、开源权重的实时 AI 游戏 | decart.ai（见 3.5 节） |
| 2024.12 | **Genie 2** | Google DeepMind | 单图生可玩 3D 世界 | [DeepMind 官方博客](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/) |
| 2024.12 | Sora 公开发布 / World Labs 3D demo | OpenAI / World Labs | 产品化与 3D 路线落地 | openai.com / worldlabs.ai |
| 2025.01 | Cosmos | NVIDIA | 偏物理 AI，作边界参照 | [arXiv:2501.03575](https://arxiv.org/abs/2501.03575) |

---

## 3. 五位头部人物深描

### 3.1 Tim Rocktäschel —— 交互式世界模型的学术旗手（Genie 系）

**机构与背景【事实】**：伦敦大学学院（UCL）人工智能教授，同时任 Google DeepMind 研究科学家（伦敦）；UCL 博士出身，早期做可微推理/知识表示，后转向开放式强化学习与世界模型，是 UCL DARK Lab 的核心负责人之一。

**入选理由【判断】**：DeepMind 旗舰世界模型项目 **Genie（ICML 2024）与 Genie 2** 的资深负责人；兼具顶级教职（人才管道）与大厂资源（算力+数据），是"生成式交互环境"路线最确定的学术锚点。

**代表成果与解读**：

- **Genie**（[arXiv:2402.15391](https://arxiv.org/abs/2402.15391)）：核心创新是 **latent action model**——从无动作标注的 2D 平台跳跃游戏视频中反推出 8 个离散"潜在动作"，再训练自回归动力学模型，使**任意一张图（照片、草图、AI 生成图）都能变成逐帧可玩的环境**。【判断】这把世界模型从"像素预测"升级为"可交互环境生成"，且不依赖动作标注，数据可扩展性强；短板是 2D 域、非实时、长时记忆缺失。
- **Genie 2**（[DeepMind 博客](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/)，2024.12）：从单张图像生成**可用键鼠游玩的 3D 世界**，一致性可达约一分钟，展示物体恒存、NPC、流体/光照等效果。【判断】未开放权重、论文细节有限，信息透明度低；其真正的跨代版本动向（见第 6 节）是 1–2 年内最重要的单一跟踪点。

**公开账号**：个人主页疑似 rockt.ai【待核实】；X 账号未确认；[Google Scholar 检索入口](https://scholar.google.com/scholar?q=%22Tim+Rockt%C3%A4schel%22)；LinkedIn 建议按姓名检索（不提供未核实链接）。

**投资含义【判断】**：跟踪他≈跟踪 DeepMind 世界模型战略的公开窗口；其"开放式学习（open-endedness）"纲领若与 Genie 合流，是通往"无限内容生成"的关键叙事。

---

### 3.2 Bill Peebles —— DiT 之父、Sora 研究负责人（规模化路线）

**机构与背景【事实】**：OpenAI 研究员，**Sora 联合负责人**；UC Berkeley 博士（导师 Alyosha Efros）【较可信，建议以其主页为准】。

**入选理由【判断】**：他 2022 年的 **DiT** 已成为当今几乎所有视频世界模型（Sora、Oasis 及多数开源视频模型）的架构底座；Sora 官方定位"world simulators"，他是"scaling 出模拟器性质"这一路线的旗手。

**代表成果与解读**：

- **DiT**（[arXiv:2212.09748](https://arxiv.org/abs/2212.09748)，ICCV 2023）：用 Transformer 替换扩散模型的 U-Net，并证明 FID 随算力/参数稳定改善——扩散模型 scaling law 的早期硬证据。【判断】投资含义：架构护城河弱化，竞争要素转向算力、数据工程与推理成本，结构性利好大厂。
- **Sora 技术报告**（[arXiv:2402.17177](https://arxiv.org/abs/2402.17177)）：时空 patch + DiT 大规模训练，涌现出 3D 一致性、长程连贯、物体恒存、简单交互（如画笔留痕）乃至 Minecraft 式的数字世界模拟。【判断】局限同样明显：非实时、产品形态非交互、物理错误；但 2024.12 Sora 公开发布标志其从研究转入产品周期。

**公开账号**：个人主页 [wpeebles.com](https://www.wpeebles.com/)【较可信】；X/LinkedIn 未确认；[Scholar 检索](https://scholar.google.com/scholar?q=%22Bill+Peebles%22)。

**投资含义【判断】**：跟踪点在于 Sora 是否从"视频工具"演进为"交互模拟器"（API、动作控制、实时化）——这将决定 OpenAI 在游戏/虚拟世界市场的入场方式。

---

### 3.3 Tim Brooks —— 连接"视频生成"与"交互世界模型"的关键节点

**机构与背景【事实】**：UC Berkeley 博士（导师 Alyosha Efros）→ OpenAI（Sora 联合负责人）→ **2024 年 10 月加入 Google DeepMind，公开表示将从事"视频生成与世界模拟器"研究**（其本人 X 公告，多家科技媒体报道）。

**入选理由【判断】**：①Sora co-lead 的一线规模化视频经验；②InstructPix2Pix 奠定的"自然语言指令可控生成"范式，恰好补上"多模态可控视频"维度；③他的跳槽是两大厂路线合并的标志性人才信号。

**代表成果与解读**：

- **InstructPix2Pix**（[arXiv:2211.09800](https://arxiv.org/abs/2211.09800)，CVPR 2023）：用 GPT-3 + Stable Diffusion 合成配对训练数据，实现"用自然语言指令编辑图像"。【判断】指令可控性是交互式视频/世界模型人机接口的范式原型。
- **Sora**（同上 arXiv:2402.17177）：作为研究负责人主导。

**公开账号**：个人主页 [timothybrooks.com](https://www.timothybrooks.com/)【较可信】；X 账号 @_tim_brooks【较可信，建议点开核实】；LinkedIn 未确认；[Scholar 检索](https://scholar.google.com/scholar?q=%22Tim+Brooks%22+video)。

**投资含义【判断】**：他在 DeepMind 的具体分工未公开【待核实】，合理推测处于 Veo（视频生成）× Genie（交互世界模型）的交汇点；若下一代 DeepMind 世界模型由视频团队与 Genie 团队合流产出，他大概率是枢纽人物。其公开演讲与 X 动态是低成本高价值的情报源。

---

### 3.4 李飞飞（Fei-Fei Li）—— 3D 原生"空间智能"路线定义者

**机构与背景【事实】**：斯坦福大学计算机科学教授、斯坦福 HAI 联合主任；ImageNet 发起人；曾任 Google Cloud AI 首席科学家（2017–2018）、Twitter 董事会成员（2020–2022）；2024 年联合创立 **World Labs**（[worldlabs.ai](https://www.worldlabs.ai/)）并任 CEO，联创包括 NeRF 一作 **Ben Mildenhall**、Justin Johnson、Christoph Lassner；2024 年 9 月宣布 **2.3 亿美元融资**（a16z、NEA、Radical Ventures 等，据报道估值超 10 亿美元；Jeff Dean、Geoffrey Hinton 个人参投见诸报道【以当时报道为准】）。

**入选理由【判断】**：她定义的"Large World Model / 空间智能"是区别于视频帧预测的第三条路线；World Labs 是 3D 世界生成人才密度最高的团队（NeRF 创造者+斯坦福系），资本与学术双制高点。

**代表成果与解读**：

- **ImageNet / ILSVRC**（[arXiv:1409.0575](https://arxiv.org/abs/1409.0575)）【历史锚点】：数据规模驱动范式的奠基作。【判断】类比：World Labs 正在试图构建"空间智能时代"的数据—模型飞轮。
- **World Labs 单图生 3D 世界 demo**（2024.12，worldlabs.ai）：输入单张图像 → 浏览器内**实时可探索的 3D 场景**（自由相机、景深、推拉变焦），强调 3D 一致性与持久性——恰好命中视频世界模型的"记忆/持久性"痛点。【判断】技术路线推测为生成式先验 + 显式/半显式 3D 表示（NeRF/Gaussian Splatting 谱系），产出"可持久、可编辑、可进引擎的世界资产"，与纯视频路线形成对冲；短板是当前交互限于"漫游"，尚无动作物理与动态演化。

**公开账号**：[斯坦福官方主页](https://profiles.stanford.edu/fei-fei-li)【可信】；X @drfeifei【较可信】；LinkedIn 按姓名检索（不提供未核实链接）；[Scholar 检索](https://scholar.google.com/scholar?q=%22Fei-Fei+Li%22)。

**投资含义【判断】**：跟踪 World Labs 的首个产品形态（3D 世界资产管线？创作者平台？）与对游戏引擎/影视管线的渗透；这是"世界模型→可交易资产"商业假说的最大赌注。

---

### 3.5 Dean Leitersdorf（Decart）—— 实时可玩世界模型的创业标杆

**机构与背景【事实】**：Decart 联合创始人兼 CEO（2023 年创立，特拉维夫，联创 Moshe Shalev）；以色列理工学院（Technion）博士【院系与导师未核实】；2024 年 12 月宣布 2100 万美元 A 轮（Sequoia 领投，Zeev Ventures 等；含此前种子轮累计约 3200 万美元【以媒体报道为准】）。

**入选理由【判断】**：**"实时"是交互世界模型的分水岭指标**，Decart 的 Oasis 是首个公开可玩（约 20fps、浏览器即用）、且开放权重的 AI 生成游戏世界（Minecraft 风格，2024 年 10 月底–11 月发布，与芯片公司 Etched 合作）。【事实标注】其成果以公司博客/开源仓库/媒体为主，**缺乏同行评审论文**，需以工程证据替代学术证据——这本身是"世界模型研究重心向工业界转移"的注脚。

**代表成果与解读**：

- **Oasis**（decart.ai 官网及官方博客；开源权重与代码托管于 Hugging Face/GitHub，组织名【待核实】）：技术栈为 ViT VAE + DiT 扩散、键鼠动作条件、少步去噪、自回归逐帧生成；在 H100 上实时运行，并演示于 Etched Sohu 专用 ASIC。【判断】官方承认存在幻觉、物体持久性差、分辨率低等短板；但"可玩性>画质"的取舍符合游戏/直播场景的需求弹性，而软硬协同（Sohu）展示了世界模型推理成本曲线的下探路径——这是实时世界模型商业化的核心变量。

**公开账号**：公司官网 [decart.ai](https://decart.ai/)【可信】；个人主页未见；X/LinkedIn 未确认（建议按全名检索）；GitHub 组织【待核实】。

**投资含义【判断】**：Decart 是"世界模型即流式内容引擎"假说的最纯标的；跟踪其新一代模型（记忆、分辨率）与实时视频类新产品的商业化落地，以及专用芯片带来的单位经济改善。

---

## 4. 横向对比表

| 维度 | Rocktäschel | Peebles | Brooks | 李飞飞 | Leitersdorf |
| --- | --- | --- | --- | --- | --- |
| 角色 | 学术+大厂双栖 | 大厂研究负责人 | 大厂研究负责人（2024 转会） | 学术+创业 CEO | 创业 CEO |
| 技术路线 | 潜在动作+自回归生成（Genie 系） | DiT 规模化视频扩散（Sora 系） | 视频扩散+指令可控生成 | 3D 原生空间生成（LWM） | 动作条件 DiT+实时推理 |
| 交互性【判断】 | 高（逐帧可玩） | 低（产品非交互，仅展示模拟能力） | 中（Sora 非交互；DeepMind 新职面向交互） | 中（3D 漫游，无动作物理） | 高（20fps 可玩） |
| 实时性【判断】 | 低（研究原型） | 低 | 低–中 | 中（浏览器实时渲染） | 高（约 20fps） |
| 开放性 | 有论文，无权重 | 技术报告 | 论文+技术报告 | Demo | **开源权重** |
| 与实时互动世界模型相关性 | ★★★★★（范式定义） | ★★★★（架构底座） | ★★★★（路线枢纽） | ★★★★（3D 对冲路线） | ★★★★★（实时标杆） |
| 产业价值 | DeepMind 生态与人才管道 | OpenAI 多模态旗舰（Sora 产品） | 两大厂竞逐的关键节点 | 融资 2.3 亿美元，3D 资产平台假说 | 融资约 3200 万美元，流式内容引擎假说 |
| 未来 1–2 年跟踪点 | Genie 跨代版本、权重开放策略 | Sora 交互化/API 化、scaling 论文 | Veo×Genie 合流的产出、公开演讲 | 首个产品、技术披露、引擎/影视合作 | 新模型记忆/画质、实时视频新品、芯片成本曲线 |

---

## 5. 第二梯队与边界说明（均为【事实】+简要【判断】）

- **Jake Bruce**（DeepMind，Genie 一作）：Genie 落地的关键执行者；公开账号稀少，跟踪价值高但情报成本高。
- **Dan Valevski / Yaniv Leviathan / Shlomi Fruchter**（Google，GameNGen，[arXiv:2408.14837](https://arxiv.org/abs/2408.14837)，项目页 gamengen.github.io【较可信】）：实时性标杆（单 TPU 20fps 模拟 DOOM），"扩散即游戏引擎"的最强证据。
- **Zhiting Hu**（UCSD，Pandora，[arXiv:2406.09455](https://arxiv.org/abs/2406.09455)）：自然语言作为动作的通用世界模型；主页 zhiting.ucsd.edu【较可信】。学术开放路线代表。
- **Sherry Yang / Yilun Du 等**（UniSim，[arXiv:2310.06114](https://arxiv.org/abs/2310.06114)，项目页 universal-simulator.github.io【较可信】）：通用模拟器思想源头之一。
- **François Fleuret / Eloi Alonso**（日内瓦大学，DIAMOND，[arXiv:2405.12399](https://arxiv.org/abs/2405.12399)，项目页 diamond-wm.github.io【较可信】）：扩散世界模型的视觉保真与可玩 CS:GO demo。
- **Anastasis Germanidis**（Runway CTO，Gen-1 论文 [arXiv:2302.03011](https://arxiv.org/abs/2302.03011)）：可控视频生成旗舰，已公开"General World Models"路线；X @agermanidis【较可信】。
- **边界排除说明**：Danijar Hafner（DreamerV3，[arXiv:2301.04104](https://arxiv.org/abs/2301.04104)）与 David Ha（现 Sakana AI）属智能体/历史谱系；NVIDIA Cosmos 偏物理 AI；Jim Fan、Bowen Baker 属 Minecraft 智能体线——均因范围界定未列入前五，但其技术（动作反推、潜在动力学）持续向本赛道溢出。

---

## 6. 未来 1–2 年跟踪信号清单

**【判断+待核实】以下动态很可能发生于我的知识截止（2025 年初）之后，务必逐项复核：**

1. **DeepMind**：Genie 跨代版本（交互时长、帧率、权重/API 开放）；Veo 与 Genie 团队合流的公开证据；Brooks 的演讲/论文署名动向。
2. **OpenAI**：Sora 是否出现动作控制/实时/游戏化接口；Peebles 团队是否发布 scaling 或交互性论文。
3. **World Labs**：首个产品形态与定价；是否发布 LWM 技术论文；与游戏引擎/影视制作管线合作。
4. **Decart**：Oasis 后继模型（记忆与持久性改进）；实时 AI 视频新产品的延迟与成本数据；Sohu 芯片量产节奏。
5. **领域级技术变量**：实时化方法（因果/少步蒸馏、流式生成，如 Diffusion Forcing [arXiv:2407.01392](https://arxiv.org/abs/2407.01392) 一脉）、长时记忆架构、交互数据（键鼠+视频）资产争夺、评测基准、游戏 IP 训练数据的版权风险。

---

## 7. 核实状态汇总与风险提示

- **高可信**：全部 arXiv 链接（稳定标识符）；Genie 2 / Sora / World Labs / Decart 官方页面；各人机构归属与融资事件（以 Reuters/TechCrunch 等当时报道为准）。
- **较可信但建议点开复核**：timothybrooks.com、wpeebles.com、profiles.stanford.edu/fei-fei-li；X 账号 @drfeifei、@_tim_brooks、@agermanidis。
- **未确认（未编造，需自行检索）**：Rocktäschel 个人主页与 X 账号、Peebles 与 Leitersdorf 的 X/LinkedIn、Decart 的 GitHub 组织名、Leitersdorf 的博士院系信息；所有 LinkedIn 链接一律未提供。
- **最大风险**：本报告无法覆盖 2025 年内的新发布（该领域以月为周期演进）；建议将第 6 节清单作为尽调复核的起点，并直接查阅各人的 Google Scholar 与机构页面获取最新署名成果。

*说明：本报告为研究梳理而非投资建议；所有【判断】均为基于公开信息的分析推测，不构成事实陈述。*
