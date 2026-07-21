# 实时互动视频生成 / 世界模型方向——头部学者研究梳理

> **研究范围界定**：本报告聚焦"可交互视频生成、游戏/虚拟世界生成、实时内容生成、多模态可控视频"方向的世界模型研究，**不包含**机器人控制、自动驾驶、具身智能等物理执行场景。
>
> **信息截止日期**：2026年7月21日。所有事实性信息均标注来源；分析判断以"【分析】"标注。

---

## 一、领域背景速览

2024–2026年，"视频生成→世界模型"成为生成式AI最核心的演进方向之一。从OpenAI Sora提出"视频生成模型即世界模拟器"[[5]]，到DeepMind Genie系列实现实时可交互3D环境生成[[21]][[31]]，再到Self Forcing将自回归视频扩散模型推至单GPU 17 FPS实时推理[[252]]，该领域正从"离线视频合成"快速迈向"实时、可交互、持续生成"的范式。CVPR 2025已设立"From Video Generation to World Model"专题Tutorial[[3]]，NeurIPS 2025收录多篇互动视频世界模型论文[[2]][[146]]，标志着学术社区对该方向的高度认可。

---

## 二、5位头部学者详细档案

---

### 1. Jake Bruce — DeepMind｜Genie系列世界模型核心领导者

| 维度 | 内容 |
|------|------|
| **现任职位** | Research Scientist（后升任Staff Research Scientist），Google DeepMind，伦敦 [[98]][[277]] |
| **教育背景** | PhD — 昆士兰科技大学（QUT）机器人与自主系统；MSc — 西蒙弗雷泽大学（SFU）计算机科学；BCS — Acadia大学计算机科学 [[101]] |
| **个人主页** | https://jakebruce.ca/ [[101]] |
| **Google Scholar** | https://scholar.google.com/citations?user=RGNVBKMAAAAJ [[97]] |
| **LinkedIn** | https://uk.linkedin.com/in/jake-bruce-877b4739 [[98]] |
| **Twitter/X** | ⚠️ 未找到经本人确认的公开X/Twitter账号，不做编造 |

#### 入选理由

Jake Bruce是DeepMind **Genie 1 → Genie 2 → Genie 3** 三代世界模型的项目领导者（project leadership）[[100]]。Genie是业界首个从无标注互联网视频中无监督训练的生成式交互环境[[89]]；Genie 2扩展为大规模基础世界模型，可生成可操控的3D环境[[92]]；Genie 3（2025年8月发布）进一步实现从文本描述实时生成照片级可交互环境[[21]][[31]]，被DeepMind定位为"通用世界模型的新前沿"[[27]]。Bruce在Genie论文中负责视频tokenizer、动作模型、动力学模型、scaling等核心模块[[100]]，是该方向学术影响力最大的单一研究者之一（Genie论文被引831次[[89]]）。

#### 代表论文解读

**论文：Genie: Generative Interactive Environments (ICML 2024)**
- 链接：https://arxiv.org/abs/2402.15391 [[89]]
- 解读：Genie提出了一种三组件架构——**Latent Action Model**（从未标注视频中无监督推断离散动作空间）、**Video Tokenizer**（将视频帧压缩为离散token）、**Dynamics Model**（基于MaskGIT的自回归Transformer，根据前一帧+动作预测下一帧）。其核心突破在于：**无需任何动作标签**即可从互联网视频中学习可交互环境，用户可通过推断出的潜动作实时"游玩"生成的世界。这为后续Genie 2/3的规模化奠定了基础。

**论文/博客：Genie 2: A Large-Scale Foundation World Model (2024)**
- 链接：https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/ [[92]]
- 解读：Genie 2将Genie扩展为可生成多样化3D环境的基础世界模型，支持键盘/鼠标动作控制，环境具有一致性和持久性，可用于训练和评估AI智能体。

**Genie 3 (2025)**
- 链接：https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ [[21]]
- 解读：Genie 3实现从简单文本描述生成照片级实时可交互环境，具备物理属性建模、自然世界模拟、动画与虚构场景生成等能力[[296]]，并拥有约1分钟的环境记忆[[301]]。

#### 研究方向
生成式交互环境、基础世界模型、视频tokenizer、无监督动作发现、大规模环境生成与实时交互。

---

### 2. Eloi Alonso — General Intuition联合创始人｜扩散世界模型先驱

| 维度 | 内容 |
|------|------|
| **现任职位** | Co-Founder & Researcher，General Intuition [[77]][[133]] |
| **教育背景** | PhD — 日内瓦大学（University of Geneva），师从François Fleuret教授，研究方向为强化学习与世界模型 [[73]][[77]] |
| **个人主页** | https://eloialonso.github.io/ [[77]] |
| **Google Scholar** | https://scholar.google.com/citations?user=Ya4KugcAAAAJ [[74]] |
| **LinkedIn** | https://ch.linkedin.com/in/eloialonso [[227]] |
| **Twitter/X** | https://x.com/EloiAlonso1 [[136]] |

#### 入选理由

Eloi Alonso是**扩散模型用于世界建模**这一技术路线的开创者之一。其博士期间主导的**DIAMOND**（NeurIPS 2024 Spotlight，被引326次[[48]]）首次证明扩散模型可以作为高保真世界模型来训练RL智能体，在Atari 100k基准上取得当时纯世界模型训练的最佳成绩[[78]]。此前的**IRIS**（ICLR 2023 Oral）和**Δ-IRIS**（ICML 2024）则奠定了Transformer世界模型的基础范式[[135]]。

更具产业意义的是，Alonso于2025年联合创立**General Intuition**，该公司于2026年6月完成**3.2亿美元A轮融资**，估值约23亿美元[[134]][[230]]，并发布了**MIRA**——一个可实时运行的多人在线世界模型（20 FPS），与Epic Games合作[[136]][[224]]。这使他成为该方向从学术到产业转化的标志性人物。

#### 代表论文解读

**论文：Diffusion for World Modeling: Visual Details Matter in Atari (DIAMOND, NeurIPS 2024 Spotlight)**
- 链接：https://arxiv.org/abs/2405.12399 [[48]]
- 代码：https://github.com/eloialonso/diamond [[50]]
- 解读：DIAMOND首次将**扩散模型**（而非传统的RSSM或Transformer）用作RL智能体的完整世界模型。智能体完全在扩散世界模型生成的"梦境"中训练，无需真实环境交互。关键发现是：扩散模型生成的**视觉细节**（而非仅抽象特征）对策略学习至关重要。在Atari 100k基准上达到1.46的人类标准化均分，刷新了纯世界模型训练的记录[[78]]。该工作还扩展到了CS:GO等更复杂的游戏环境[[135]]。

**论文：Transformers are Sample-Efficient World Models (IRIS, ICLR 2023 Oral)**
- 链接：https://eloialonso.github.io/ 中列出 [[135]]
- 解读：IRIS将世界建模转化为序列建模问题——用VQ-VAE将观测编码为离散token，再用自回归Transformer预测未来token序列。在Atari 100k上展示了Transformer作为世界模型的高样本效率，获DRLW 2022最佳论文奖[[135]]。

**MIRA (2026, General Intuition)**
- 来源：https://x.com/EloiAlonso1 [[136]][[225]]
- 解读：MIRA是一个**可游玩的多人世界模型**，基于1万小时游戏数据训练，实时运行于20 FPS，与Epic Games合作开发。它代表了世界模型从单人Atari级别向多人、复杂游戏环境跃迁的关键一步。

#### 研究方向
扩散世界模型、强化学习中的模型预测、实时多人世界模型、游戏数据驱动的AI训练。

---

### 3. Dani Valevski — Google Research｜实时神经游戏引擎开创者

| 维度 | 内容 |
|------|------|
| **现任职位** | Senior Staff Researcher，Google Research [[199]][[242]] |
| **教育背景** | 特拉维夫大学（Tel Aviv University），2006–2009年学习数学 [[242]] |
| **个人主页** | ⚠️ 未找到独立个人学术主页 |
| **Google Scholar** | https://scholar.google.com/citations?user=ECKZ08wAAAAJ [[82]] |
| **LinkedIn** | https://il.linkedin.com/in/dani-valevski-a3b5936 [[242]] |
| **Twitter/X** | https://x.com/daniva [[246]] |

#### 入选理由

Dani Valevski是**GameNGen**的第一作者和核心开发者[[81]]。GameNGen（2024年8月发布，被引273次[[70]]）是**业界首个完全由神经模型驱动的实时游戏引擎**，以20 FPS实时模拟DOOM游戏，无需任何传统游戏引擎代码[[40]][[66]]。该工作直接证明了"扩散模型即游戏引擎"的可行性，对游戏产业和实时内容生成产生了深远影响。此外，Valevski还主导了**Dreamix**（视频扩散模型用于通用视频编辑）[[196]]和**Generative UI**（LLM驱动的交互式UI生成）[[199]][[322]]等项目，展现了从视频生成到交互式内容生成的完整技术布局。

#### 代表论文解读

**论文：Diffusion Models Are Real-Time Game Engines (GameNGen, ICLR 2025)**
- 链接：https://arxiv.org/abs/2408.14837 [[87]]
- 项目页：https://gamengen.github.io/ [[40]]
- 解读：GameNGen基于Stable Diffusion微调，将游戏引擎完全替换为神经扩散模型。系统接收玩家键盘/鼠标输入和前一帧画面，实时生成下一帧游戏画面，达到20 FPS、PSNR与真实DOOM引擎几乎无法区分的质量[[66]]。训练流程分两阶段：(1) 用RL智能体收集游戏数据并训练奖励模型；(2) 在收集的数据上微调扩散模型，并加入噪声增强以缓解自回归误差累积。该工作的核心意义在于：**首次证明复杂游戏的完整渲染和物理逻辑可以被神经网络端到端学习**，为"AI原生游戏引擎"开辟了新范式。

**Generative UI: LLMs are Effective UI Generators (2026)**
- 链接：https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/ [[199]]
- 解读：该工作让AI模型根据任意prompt生成富交互式UI体验和工具/模拟器，将生成式AI从内容生成扩展到**交互式应用生成**，与实时互动内容生成方向高度相关。

#### 研究方向
实时神经游戏引擎、视频扩散模型、视频编辑、生成式UI、交互式内容生成。

---

### 4. 车浩轩（Haoxuan Che）— 独立研究者｜互动游戏世界模型与Agentic World Modeling

| 维度 | 内容 |
|------|------|
| **现任职位** | 独立研究者（Independent Researcher），此前为华为香港研究中心AI Lab首席研究员（Principal Researcher），领导20+人视觉生成与世界模型团队 [[112]][[124]] |
| **教育背景** | PhD — 香港科技大学（HKUST）计算机科学与工程；B.Eng. — 西北工业大学（NWPU），荣誉毕业 [[112]] |
| **个人主页** | https://chehx.github.io/ [[112]] |
| **Google Scholar** | https://scholar.google.com/citations?user=rCvK7tcAAAAJ [[123]] |
| **LinkedIn** | https://hk.linkedin.com/in/hche [[219]] |
| **Twitter/X** | ⚠️ 未找到经本人确认的公开X/Twitter账号，不做编造 |

#### 入选理由

车浩轩是**GameGen-X**的第一作者和项目领导者[[109]]。GameGen-X（ICLR 2025，被引121次[[36]]）是**首个专为开放世界游戏视频生成与交互控制设计的扩散Transformer模型**[[34]]，实现了游戏环境生成与角色/环境交互控制的统一。此后，他领导了**Agentic World Modeling**（2026年4月发布，Hugging Face Daily Papers #1[[214]][[303]]），系统性地提出了从被动预测到主动世界建模的能力路线图，覆盖70+世界建模系统[[308]]。他还领导了**Capybara**——首个统一视觉创作模型[[214]]。在华为期间，他领导了20+人的研发工程团队，将前沿模型研究与大规模系统开发、数据管线、评估和产品部署相衔接[[112]]。其研究被引1367次[[223]]。

#### 代表论文解读

**论文：GameGen-X: Interactive Open-world Game Video Generation (ICLR 2025)**
- 链接：https://arxiv.org/abs/2411.00769 [[111]]
- 项目页：https://gamegen-x.github.io/ [[35]]
- 代码：https://github.com/GameGen-X/GameGen-X [[109]]
- 解读：GameGen-X采用**两阶段训练策略**：第一阶段在大规模开放世界游戏视频上训练视频生成能力；第二阶段引入交互控制模块，支持通过键盘/鼠标动作实时控制游戏环境和角色[[38]][[110]]。其核心创新在于将Diffusion Transformer（DiT）架构与游戏交互控制相结合，实现了**生成质量与交互性的统一**。该工作被量子位、机器之心等中文科技媒体广泛报道[[214]]。

**论文：Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond (2026)**
- 链接：https://arxiv.org/abs/2604.22748 [[303]]
- 解读：这是一篇系统性综述与路线图论文，提出了世界模型的**能力层级分类**（从被动下一步预测到主动Agentic世界建模），梳理了2018–2026年间70+代表性世界建模系统[[308]]，并提出了连接此前孤立社区（视频生成、RL、游戏AI等）的统一框架。该论文在Hugging Face Daily Papers登顶#1[[214]]，反映了社区对世界模型统一理论框架的强烈需求。

#### 研究方向
互动游戏视频生成、世界模型、多模态生成模型、AI智能体、统一视觉创作、模型泛化。

---

### 5. 黄勋（Xun Huang）— Roblox Technical Director｜实时视频生成架构奠基人

| 维度 | 内容 |
|------|------|
| **现任职位** | Technical Director，Roblox（负责Roblox Reality——混合生成式AI架构，驱动下一代多人照片级游戏体验）[[262]][[287]] |
| **此前经历** | Morpheus AI创始人兼CEO（被Roblox收购）→ Adobe Research研究科学家 → NVIDIA研究科学家 → CMU兼职教授 [[262]][[317]] |
| **教育背景** | PhD — 康奈尔大学（Cornell）计算机科学，导师Serge Belongie（2020年）[[262]] |
| **个人主页** | https://www.xunhuang.me/ [[262]] |
| **Google Scholar** | https://scholar.google.com/citations?user=1XGC4GsAAAAJ [[266]] |
| **LinkedIn** | https://www.linkedin.com/in/xunhuang1995 [[313]] |
| **Twitter/X** | https://x.com/xxunhuang [[290]] |

#### 入选理由

黄勋是**实时自回归视频生成**技术路线的核心奠基人。他发明的**Self Forcing**（NeurIPS 2025 Spotlight，被引383次[[252]]）解决了自回归视频扩散模型长期存在的**训练-测试分布不匹配（exposure bias）**问题，使模型在单张RTX 4090上实现17 FPS实时流式视频生成[[253]][[263]]。此前的**CausVid**（CVPR 2025）首次实现了从慢速双向扩散到快速自回归视频扩散的转换[[267]]；**MotionStream**（ICLR 2026 Oral）进一步实现了带交互运动控制的实时视频生成，达29 FPS[[155]][[161]]。

更早期的**AdaIN**（ICCV 2017 Oral）成为StyleGAN的基础组件，并在几乎所有现代扩散模型中广泛使用[[262]]。其研究总被引超过19,000次[[262]]。

2026年，他创立的Morpheus AI被Roblox收购，他加入Roblox担任Technical Director，主导**Roblox Reality**——将视频世界模型直接应用于多人在线游戏平台的实时生成[[287]][[317]]。这使他成为该方向**学术→创业→产业落地**路径最完整的华人研究者。

#### 代表论文解读

**论文：Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion (NeurIPS 2025 Spotlight)**
- 链接：https://arxiv.org/abs/2506.08009 [[252]]
- 项目页：https://self-forcing.github.io/ [[184]]
- 解读：自回归视频扩散模型在训练时使用teacher forcing（以真实前帧为条件），但推理时使用自身生成的前帧，导致**误差累积**和长视频质量退化。Self Forcing通过在训练时模拟推理过程（自回归rollout + KV caching），让模型在训练阶段就"看到"自己的预测误差，从而消除train-test gap[[253]][[257]]。结果：480P视频初始延迟约0.8秒，之后以约16 FPS流式生成[[184]]，质量匹配甚至超越双向教师模型。该工作被公认为实时视频生成的里程碑。

**论文：From Slow Bidirectional to Fast Autoregressive Video Diffusion Models (CausVid, CVPR 2025)**
- 链接：https://arxiv.org/abs/2412.07772 [[267]]
- 解读：CausVid提出将预训练的双向视频扩散模型"因果化"为自回归模型的方法，结合分布匹配蒸馏（DMD），实现单GPU 9.4 FPS的高质量流式视频生成[[267]]。这是Self Forcing的前置工作，奠定了"双向→自回归"转换的技术基础。

**论文：MotionStream: Real-Time Video Generation with Interactive Motion Controls (ICLR 2026 Oral)**
- 链接：https://arxiv.org/abs/2511.01266 [[161]]
- 解读：MotionStream在Self Forcing基础上增加了**交互式运动控制**——用户可以实时绘制轨迹、控制相机、迁移运动，并即时看到生成结果[[155]][[165]]。达到亚秒延迟、29 FPS流式生成[[155]]。该工作将"实时视频生成"从被动播放推进到**实时交互创作**。

#### 研究方向
实时自回归视频扩散、视频世界模型、交互式运动控制视频生成、生成式AI架构（AdaIN/Style Transfer）、3D生成。

---

## 三、横向比较总表

| 维度 | **Jake Bruce** | **Eloi Alonso** | **Dani Valevski** | **车浩轩 (Haoxuan Che)** | **黄勋 (Xun Huang)** |
|------|---------------|-----------------|-------------------|------------------------|---------------------|
| **所属机构** | Google DeepMind（伦敦）[[98]] | General Intuition（联合创始人）[[77]] | Google Research（以色列）[[242]] | 独立研究者（前华为HK）[[112]] | Roblox（Technical Director）[[262]] |
| **核心技术路线** | 无监督动作发现 + 自回归Transformer世界模型 + 大规模scaling [[100]] | 扩散模型世界模型 + RL训练 + 多人实时世界模型 [[48]][[136]] | 扩散模型实时游戏引擎 + 视频编辑 + 生成式UI [[87]][[199]] | DiT互动游戏生成 + Agentic世界建模 + 统一视觉创作 [[35]][[303]] | 自回归视频扩散 + Self Forcing实时化 + 交互运动控制 [[252]][[161]] |
| **与"实时互动视频/世界模型"的相关性** | ★★★★★ 直接定义该方向（Genie 1/2/3） | ★★★★★ 扩散世界模型→实时多人世界模型（MIRA） | ★★★★★ 首个神经实时游戏引擎（GameNGen） | ★★★★☆ 互动游戏视频生成+世界模型理论框架 | ★★★★★ 实时视频生成架构奠基（Self Forcing/CausVid） |
| **代表工作被引量** | Genie: 831次 [[89]] | DIAMOND: 326次 [[48]] | GameNGen: 273次 [[70]] | GameGen-X: 121次 [[36]] | Self Forcing: 383次 [[252]] |
| **产业价值与落地** | 【分析】Genie 3已集成至Google Project Genie产品原型[[29]]，潜在应用于游戏、教育、模拟；但尚未独立商业化 | 【分析】General Intuition估值$2.3B[[230]]，MIRA与Epic Games合作[[136]]，游戏数据→AI训练路径清晰 | 【分析】GameNGen验证"AI原生游戏引擎"可行性；Generative UI指向交互式应用生成，Google内部产品化潜力大 | 【分析】GameGen-X/Capybara在华为/字节/快手等有产品化经验[[112]]；Agentic World Modeling提供行业路线图 | 【分析】Roblox Reality直接面向2亿+月活用户平台[[287]]，Self Forcing已产品化为实时生成架构，产业落地最直接 |
| **未来1-2年跟踪理由** | Genie 3→Genie 4的scaling路径；Project Genie产品化进展；是否开源 | MIRA多人世界模型的迭代；General Intuition $320M资金的使用方向；与Epic合作深度 | Google是否将GameNGen范式扩展至更多游戏/交互场景；Generative UI的产品化 | Agentic World Modeling框架的社区影响力；下一代的互动世界模型系统；是否加入新机构/创业 | Roblox Reality的公开技术进展；Self Forcing++分钟级生成[[268]]；MonarchRT高效注意力架构[[262]]；对游戏UGC生态的影响 |
| **个人主页** | ✅ jakebruce.ca [[101]] | ✅ eloialonso.github.io [[77]] | ❌ 未找到 | ✅ chehx.github.io [[112]] | ✅ xunhuang.me [[262]] |
| **Google Scholar** | ✅ [[97]] | ✅ [[74]] | ✅ [[82]] | ✅ [[123]] | ✅ [[266]] |
| **LinkedIn** | ✅ [[98]] | ✅ [[227]] | ✅ [[242]] | ✅ [[219]] | ✅ [[313]] |
| **Twitter/X** | ⚠️ 未确认 | ✅ @EloiAlonso1 [[136]] | ✅ @daniva [[246]] | ⚠️ 未确认 | ✅ @xxunhuang [[290]] |

---

## 四、技术路线图谱与分析判断

### 4.1 三条主要技术路线

根据上述5位学者的工作，当前"实时互动视频生成/世界模型"方向可归纳为**三条主要技术路线**：

| 路线 | 代表 | 核心思路 | 优势 | 挑战 |
|------|------|---------|------|------|
| **自回归Transformer世界模型** | Jake Bruce (Genie) | 离散token + 自回归预测 + 无监督动作发现 | 天然支持交互、scaling law明确 | 长程一致性、实时性受限于序列长度 |
| **扩散模型世界模型** | Eloi Alonso (DIAMOND/MIRA)、Dani Valevski (GameNGen)、车浩轩 (GameGen-X) | 扩散去噪生成帧/视频 + 动作条件注入 | 视觉保真度高、训练稳定 | 实时性需额外蒸馏/加速、误差累积 |
| **自回归视频扩散（混合路线）** | 黄勋 (Self Forcing/CausVid/MotionStream) | 将双向扩散模型因果化 + 自回归流式生成 + 蒸馏加速 | 兼顾质量与实时性（17-29 FPS） | 分钟级长视频一致性、多模态控制 |

【分析】这三条路线正在**加速融合**：Genie 3已引入扩散组件提升视觉质量[[296]]；Self Forcing本质上是将扩散模型自回归化[[252]]；GameGen-X使用DiT架构（扩散+Transformer的融合）[[35]]。未来1-2年，"自回归 + 扩散 + 实时蒸馏"的混合架构可能成为主流。

### 4.2 产业格局判断

【分析】从产业落地速度看：
- **最快落地**：黄勋（Roblox Reality，直接面向2亿+月活平台[[287]]）> Eloi Alonso（General Intuition，$320M资金+ Epic合作[[230]]）
- **最大平台潜力**：Jake Bruce（Google/DeepMind生态[[29]]）、Dani Valevski（Google Research + Generative UI[[199]]）
- **最灵活/独立**：车浩轩（独立研究者，跨华为/字节/快手等多平台经验[[112]]，Agentic World Modeling提供行业理论框架[[303]]）

### 4.3 关键不确定性

【分析】
1. **实时性 vs 质量的权衡**：当前最先进系统（Genie 3、MIRA、Self Forcing）在720P/480P下实现实时，但4K实时仍需1-2年；
2. **长程一致性**：Genie 3记忆约1分钟[[301]]，Self Forcing++正在攻克分钟级生成[[268]]，但"无限时长"一致性仍是开放问题；
3. **商业模式**：世界模型是作为"游戏引擎替代品"还是"新型内容平台"尚不明确，Roblox和General Intuition代表了两种不同路径。

---

## 五、信息来源汇总

| 编号 | 来源 | 链接 |
|------|------|------|
| 1 | Genie论文 (arXiv) | https://arxiv.org/abs/2402.15391 |
| 2 | Genie 2博客 (DeepMind) | https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/ |
| 3 | Genie 3博客 (DeepMind) | https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ |
| 4 | DIAMOND论文 (arXiv) | https://arxiv.org/abs/2405.12399 |
| 5 | GameNGen论文 (arXiv) | https://arxiv.org/abs/2408.14837 |
| 6 | GameGen-X论文 (arXiv) | https://arxiv.org/abs/2411.00769 |
| 7 | Self Forcing论文 (arXiv) | https://arxiv.org/abs/2506.08009 |
| 8 | MotionStream论文 (arXiv) | https://arxiv.org/abs/2511.01266 |
| 9 | Agentic World Modeling (arXiv) | https://arxiv.org/abs/2604.22748 |
| 10 | Jake Bruce主页 | https://jakebruce.ca/ |
| 11 | Eloi Alonso主页 | https://eloialonso.github.io/ |
| 12 | 车浩轩主页 | https://chehx.github.io/ |
| 13 | 黄勋主页 | https://www.xunhuang.me/ |
| 14 | General Intuition融资 (TechCrunch) | https://techcrunch.com/2026/06/25/general-intuitions-2-3b-bet-that-video-games-can-train-ai-agents-for-the-real-world/ |
| 15 | Roblox收购Morpheus AI | https://about.roblox.com/newsroom/2026/06/pioneering-ai-founders-join-to-accelerate-roblox-reality-vision |
| 16 | CVPR 2025 World Model Tutorial | https://world-model-tutorial.github.io/ |

---

> **免责声明**：本报告基于公开信息整理，所有事实性信息已标注来源。标注"【分析】"的内容为研究者基于公开信息的判断，不构成投资建议。部分研究者的社交媒体账号可能因隐私设置或平台变更而不可访问，已如实标注"未确认"。