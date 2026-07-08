基于对公开信息的系统梳理，以下是"实时互动视频生成 / 世界模型"（聚焦可交互视频生成、游戏/虚拟世界生成、实时内容生成、多模态可控视频，排除机器人/自动驾驶/具身智能等物理执行场景）方向的5位头部学者研究梳理。

---

# 实时互动视频生成 / 世界模型领域头部学者研究梳理

## 一、领域界定与筛选逻辑

本梳理聚焦的"世界模型"特指：**以视频生成为核心载体，支持用户实时交互、可控生成虚拟环境或游戏世界的AI系统**。核心能力包括：
- 逐帧或流式实时生成（≥20 FPS）
- 基于用户动作（键盘/鼠标/文本）的条件控制
- 长时序一致性与物理合理性
- 从互联网视频或游戏数据中学习世界动态

排除：以机器人控制、自动驾驶仿真、具身智能训练为主要目标的物理世界模型（如NVIDIA Cosmos主要面向Physical AI的部分）。

---

## 二、5位头部学者详细梳理

### 1. Jack Parker-Holder｜Google DeepMind

**入选理由**：Genie系列（Genie 1/2/3）的核心领导者，Genie 1获ICML 2024最佳论文奖，Genie 2是首个大规模基础世界模型，Genie 3是首个支持实时交互（24 FPS、720p）的通用世界模型。其工作定义了"视频世界模型"这一研究方向的基本范式。

**代表论文**：
| 论文 | 链接 | 解读 |
|------|------|------|
| **Genie: Generative Interactive Environments** (ICML 2024 Best Paper) | https://arxiv.org/abs/2402.15391 | 11B参数，首个从无标签互联网视频无监督训练的生成式交互环境。由时空视频分词器、自回归动态模型和隐空间动作模型组成，支持逐帧动作控制，无需ground-truth动作标签。 |
| **Genie 2: A large-scale foundation world model** (DeepMind Blog 2024) | https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/ | 自回归隐扩散模型，使用因果mask的Transformer动态模型，支持键盘鼠标输入生成一致性虚拟世界，可实时游玩蒸馏版本。 |
| **Genie 3: A new frontier for world models** (DeepMind Blog 2025) | https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ | 首个实时交互世界模型，文本提示生成720p、24FPS动态世界，数分钟一致性，支持导航探索。 |

**研究方向**：大规模世界模型训练、互联网规模视频数据学习、开放式环境生成、智能体训练环境。

**所属机构与经历**：
- 现任Google DeepMind Research Scientist，Open-Endedness Team
- 牛津大学机器学习DPhil（博士），导师Stephen Roberts
- 哥伦比亚大学MA QMSS
- 曾任J.P. Morgan量化研究员/ETF交易员（7年）
- UCL Honorary Lecturer

**社交/学术链接**：
- 个人主页：https://jparkerholder.github.io/
- Google Scholar：https://scholar.google.com/citations?user=2O_ESc4AAAAJ
- LinkedIn：https://www.linkedin.com/in/jparkerholder
- X/Twitter：https://x.com/jparkerholder

---

### 2. Shlomi Fruchter｜Google DeepMind

**入选理由**：DeepMind Research Director，Genie 3联合负责人，同时主导Google Veo（视频生成）和Imagen 3（图像生成）等旗舰项目。作为GameNGen的共同作者，其工作横跨交互式世界模型与视频生成两大核心方向。

**代表论文**：
| 论文 | 链接 | 解读 |
|------|------|------|
| **Diffusion Models Are Real-Time Game Engines (GameNGen)** (ICLR 2025) | https://arxiv.org/abs/2408.14837 | 首个完全由神经模型驱动的游戏引擎，基于Stable Diffusion v1.4，以20 FPS实时模拟DOOM游戏。两阶段训练：RL智能体采集数据→扩散模型条件生成下一帧。PSNR 29.4，接近有损JPEG压缩。 |
| **Genie 3: A new frontier for world models** (2025) | https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ | 与Jack Parker-Holder共同领导，实现文本到可交互3D世界的实时生成。 |
| **Google Veo / Imagen 3** | Google I/O发布 | 前沿文生视频与文生图模型，体现对视频物理动态的深刻理解。 |

**研究方向**：大规模生成模型、视频生成（Veo）、图像生成（Imagen）、交互式世界模型（Genie）、神经游戏引擎（GameNGen）。

**所属机构与经历**：
- 现任Google DeepMind Research Director
- 特拉维夫大学背景
- 领导多个Google I/O主题演讲项目

**社交/学术链接**：
- 个人主页：https://shlomifruchter.github.io/
- Google Scholar：https://scholar.google.com/citations?user=YkQGEqsAAAAJ
- LinkedIn：https://ch.linkedin.com/in/shlomifruchter
- X/Twitter：https://x.com/shlomifruchter

---

### 3. Anastasis Germanidis｜Runway

**入选理由**：Runway联合创始人兼CTO（现Co-CEO），主导GWM-1通用世界模型发布。GWM-1是业界首个明确以"General World Model"命名的产品级世界模型，包含GWM Worlds（可探索环境）、GWM Avatars（对话角色）、GWM Robotics三个变体，其中GWM Worlds直接面向游戏/VR/沉浸式体验场景。

**代表论文/产品**：
| 论文/产品 | 链接 | 解读 |
|------|------|------|
| **GWM-1: General World Model** (Runway 2025.12) | https://runwayml.com/research/introducing-runway-gwm-1 | 基于Gen-4.5的自回归模型，逐帧生成、实时运行、支持动作控制（相机位姿、机器人指令、音频）。GWM Worlds支持从静态场景生成无限可探索空间，保持空间一致性，支持物理定义。 |
| **Structure and content-guided video synthesis with diffusion models** (CVPR) | Google Scholar | 早期视频合成工作，为后续世界模型奠定基础。 |
| **Runway: Adding AI capabilities to design platforms** (NeurIPS 2018) | Google Scholar | 公司创立初期的系统性工作。 |

**研究方向**：通用世界模型、视频生成、实时交互环境、多模态可控生成。

**所属机构与经历**：
- Runway联合创始人兼CTO/Co-CEO（2018至今）
- 纽约大学MPS，Interactive Telecommunications Program
- 希腊AI研究者、软件工程师、艺术家

**社交/学术链接**：
- Google Scholar：https://scholar.google.com/citations?user=YVVKiFgAAAAJ
- LinkedIn：https://www.linkedin.com/in/agermanidis
- X/Twitter：https://x.com/agermanidis

---

### 4. Dani Valevski｜Google Research

**入选理由**：GameNGen第一作者，实现了"扩散模型即实时游戏引擎"的突破性验证。该工作首次证明神经模型可以完全替代传统游戏引擎，以20 FPS在单TPU上实时模拟复杂游戏（DOOM），且人类评估者难以区分真实游戏与模拟。

**代表论文**：
| 论文 | 链接 | 解读 |
|------|------|------|
| **Diffusion Models Are Real-Time Game Engines (GameNGen)** (ICLR 2025) | https://arxiv.org/abs/2408.14837 | 两阶段训练：(1) RL智能体玩游戏并记录轨迹；(2) 扩散模型基于历史帧和动作生成下一帧。通过条件增强（训练时对编码帧加高斯噪声）解决自回归漂移问题，实现长时序稳定生成。微调latent decoder提升细节保真度。 |
| **Text-driven image editing by fine-tuning diffusion model on single image** | Google Scholar | 单图像文本驱动编辑，早期扩散模型应用工作。 |

**研究方向**：扩散模型、实时游戏模拟、神经游戏引擎、条件视频生成。

**所属机构与经历**：
- Google Research Research Scientist
- GameNGen项目核心开发者，负责代码库开发、参数调优、autoencoder微调、智能体训练等

**社交/学术链接**：
- Google Scholar：https://scholar.google.com/citations?user=ECKZ08wAAAAJ
- 个人主页/LinkedIn：未找到公开确认信息

---

### 5. Dean Leitersdorf｜Decart

**入选理由**：Decart联合创始人兼CEO，主导Oasis系列实时交互世界模型。Oasis是首个面向公众的实时交互式生成式AI视频模型（Minecraft风格），支持从单张截图生成可游玩的3D世界。2026年5月完成3亿美元融资（NVIDIA、Amazon参投），估值达独角兽级别。Oasis 3进一步扩展至自动驾驶仿真等场景。

**代表论文/产品**：
| 论文/产品 | 链接 | 解读 |
|------|------|------|
| **Oasis: A Universe in a Transformer** (Decart 2024) | https://decart.ai/research | 首个实时交互式生成式AI视频模型，从Minecraft游戏视频和键盘输入训练，无需传统游戏引擎。支持上传截图即时生成可游玩世界。 |
| **Oasis 3** (Decart 2026.6) | https://decart.ai/oasis | 实时交互世界模型，生成逼真、可控、多视角仿真环境，支持机器人训练和自动驾驶仿真。 |

**研究方向**：实时世界模型、高效推理优化、交互式视频生成、游戏/虚拟世界模拟。

**所属机构与经历**：
- Decart联合创始人兼CEO（2023至今）
- 以色列Technion计算机科学博士（23岁毕业，曾为最年轻博士）
- Unit 8200（以色列精英网络部队）背景
- 2026年5月完成3亿美元融资

**社交/学术链接**：
- LinkedIn：https://www.linkedin.com/in/dean-leitersdorf
- X/Twitter：未找到公开确认的个人账号
- 公司主页：https://decart.ai/

---

## 三、横向比较表

| 维度 | Jack Parker-Holder (DeepMind) | Shlomi Fruchter (DeepMind) | Anastasis Germanidis (Runway) | Dani Valevski (Google) | Dean Leitersdorf (Decart) |
|------|------|------|------|------|------|
| **技术路线** | 隐空间自回归+时空Transformer+隐动作模型；从互联网视频无监督学习 | 扩散模型+条件生成+RL数据采集；多模态生成（视频/图像/世界） | 自回归逐帧生成+动作条件控制；基于Gen-4.5视频基座 | 扩散模型+RL智能体数据+条件增强；单TPU实时推理 | 自回归Transformer+高效推理优化；从游戏视频+动作训练 |
| **实时性** | Genie 3: 24 FPS, 720p | GameNGen: 20 FPS (单TPU) | GWM-1: 实时（具体FPS未公开） | GameNGen: 20 FPS | Oasis: 实时（具体FPS未公开，宣称最快） |
| **交互控制** | 键盘/鼠标/文本；隐空间动作 | 键盘/鼠标动作条件 | 相机位姿/机器人指令/音频 | 键盘/鼠标动作 | 键盘/鼠标；单图输入 |
| **与本领域相关性** | ★★★★★ 定义性贡献 | ★★★★★ 横跨世界模型+视频生成 | ★★★★☆ 产品级世界模型 | ★★★★★ 神经游戏引擎开创 | ★★★★☆ 实时交互世界模型先驱 |
| **产业价值** | 学术研究为主，为AGI训练环境奠基 | 学术+产品（Veo/Imagen商业化） | 极高：GWM-1已API商业化，面向游戏/VR/教育 | 学术验证，技术可迁移至游戏引擎 | 极高：3亿美元融资，Oasis已公开演示，面向游戏/仿真 |
| **未来1-2年跟踪原因** | Genie 4预期；世界模型规模定律验证 | Veo 4/Genie 4迭代；多模态统一 | GWM-1产品迭代；开源可能性；与游戏公司合作 | 神经游戏引擎扩展至更多游戏类型 | Oasis 3商业化落地；自动驾驶仿真拓展；IPO预期 |
| **关键风险** | DeepMind研究转向；商业化路径不清晰 | 与Genie团队资源竞争 | 视频生成竞争激烈（Sora/Veo/Kling） | Google内部优先级变化 | 技术壁垒可持续性；大厂竞争 |

---

## 四、关键事实与分析判断区分说明

**已验证事实**（附来源链接）：
- Genie 1获ICML 2024最佳论文奖
- Genie 2由Jack Parker-Holder领导
- Genie 3支持24 FPS、720p实时交互
- GameNGen在单TPU上以20 FPS模拟DOOM
- GWM-1于2025年12月11日发布
- Decart于2026年5月完成3亿美元融资
- Dean Leitersdorf为Technion最年轻博士（23岁）

**分析判断**（基于公开信息推断）：
- Jack Parker-Holder和Shlomi Fruchter在DeepMind内部存在资源协同与竞争关系
- Runway GWM-1的产业化路径最清晰，直接面向游戏/VR市场
- Decart的Oasis在实时性优化方面可能具有独特优势（高效推理内核）
- GameNGen的技术路线（扩散模型+RL数据）可能被更多游戏公司采用
- 未来1-2年，世界模型领域将出现更多开源竞争

---

## 五、补充说明

1. **未纳入但值得关注的学者/项目**：
   - **Jiwen Yu (HKU)**：Video World Model活跃研究者，组织CVPR 2026 Video World Models Workshop，但为PhD学生
   - **Xianglong He (Skywork AI/Tsinghua)**：Matrix-Game 2.0第一作者，开源实时交互世界模型，但为硕士生
   - **Jinwei Gu (NVIDIA Cosmos)**：主导Cosmos世界模型平台，但主要面向Physical AI（机器人/自动驾驶），与本梳理排除范围有重叠

2. **信息来源限制**：部分学者（如Dani Valevski、Dean Leitersdorf）的LinkedIn/X账号未找到公开确认信息，已明确标注。

3. **时效性**：本梳理基于2026年7月前的公开信息，该领域迭代极快，建议持续跟踪上述学者的最新发表和公司动态。
