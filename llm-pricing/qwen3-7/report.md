基于已收集的公开信息，我为您整理"实时互动视频生成 / 世界模型"方向最值得关注的5位头部学者。需要说明的是，由于部分学者的社交媒体账号未公开或无法确认，我会在相应位置明确标注。

---

## 一、五位头部学者深度梳理

### 1. **Xun Huang（黄勋）**
**现任职位**：Roblox Technical Director，负责 Roblox Reality 混合生成式AI架构 

**入选理由**：
Xun Huang 是实时互动视频生成领域的关键产业界领军人物。他提出的 **Self Forcing** 训练范式解决了自回归视频扩散模型中长期存在的曝光偏差（exposure bias）问题，实现了在单张RTX 4090 GPU上**亚秒级延迟的实时流式视频生成** 。此外，他联合主导的 **MotionStream** 项目实现了29 FPS的流式生成，比传统方法快两个数量级 。他的研究直接连接了学术前沿与产业应用（Roblox游戏平台），是推动"可交互视频生成"从实验室走向消费级产品的核心人物。

**代表论文**：
- **Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion** (2025)
  - 论文链接：https://arxiv.org/abs/2506.08009
  - 核心贡献：首次在训练阶段模拟推理时的自回归展开，通过KV缓存机制实现视频级整体损失监督，解决了传统方法依赖逐帧损失导致的分布偏移问题。实验表明可在单GPU上实现实时流式生成，质量匹敌非因果扩散模型 

- **MotionStream: Real-Time Video Generation with Interactive Motion Controls** (ICLR 2026 Oral, 1.13%录取率)
  - 论文链接：https://arxiv.org/abs/2511.01266
  - 核心贡献：通过将双向教师模型蒸馏为因果学生模型，结合滑动窗口因果注意力与attention sinks，实现无限长度视频的恒定速度生成。用户可通过绘制轨迹、控制相机或迁移运动来实时交互 

- **CausVid: From Slow Bidirectional to Fast Autoregressive Video Diffusion Models** (2025)
  - 论文链接：https://arxiv.org/abs/2412.07772

**研究方向**：自回归视频扩散模型、实时流式生成、交互式运动控制、模型蒸馏加速

**经历背景**：
- 康奈尔大学CS博士（2020），导师Serge Belongie
- 博士期间发明AdaIN，成为StyleGAN和早期扩散模型的基础组件
- 曾任Adobe Research Research Scientist、NVIDIA Research Scientist、CMU兼职教授
- 创办Morpheus AI后被Roblox收购
- 研究被引用超过19,000次，主导项目引用超14,000次 

**公开联系方式**：
- 个人主页：https://www.xunhuang.me/
- GitHub：未在搜索结果中确认
- LinkedIn/X/Twitter：未在搜索结果中确认

---

### 2. **Gordon Wetzstein**
**现任职位**：斯坦福大学副教授，计算成像与显示实验室负责人 

**入选理由**：
Gordon Wetzstein 是**视频世界模型与3D几何结合**方向的顶尖学者。他团队近期在NeurIPS 2025发表的 **Video World Models with Long-term Spatial Memory** 首次将几何基础的空间记忆机制引入视频世界模型，解决了模型在长期交互中"遗忘"已生成场景的核心问题 。此外，他在ICCV 2025发表的 **Long-Context State-Space Video World Models** 利用状态空间模型（SSM）扩展时序记忆，在保持交互速度的同时实现长程一致性 。他的研究特色是将计算成像、3D几何与生成模型深度融合，为构建"可持久化"的虚拟世界提供了技术基础。

**代表论文**：
- **Video World Models with Long-term Spatial Memory** (NeurIPS 2025)
  - 论文链接：https://arxiv.org/abs/2506.05284
  - 项目页面：https://spmem.github.io/
  - 核心贡献：受人类记忆机制启发，设计了空间记忆（3D点云图）和情景记忆（稀疏历史帧）双机制。空间记忆自动提取静态场景部分并融合，情景记忆保存视觉细节和身份特征，显著改善视频世界模型的长期一致性 

- **Long-Context State-Space Video World Models** (ICCV 2025)
  - 论文链接：https://arxiv.org/abs/2505.20171
  - 核心贡献：首次充分利用状态空间模型（SSM）在因果序列建模中的固有优势，通过块级SSM扫描策略平衡空间一致性与扩展时序记忆，结合密集局部注意力确保帧间连贯性。在Memory Maze和Minecraft数据集上验证了长程空间检索和推理能力 

- **CameraCtrl: Enabling Camera Control for Text-to-Video Generation** (ICLR 2025)
  - 论文链接：https://arxiv.org/abs/2404.02101

**研究方向**：视频世界模型、长程空间记忆、状态空间模型、3D几何感知生成、计算成像

**经历背景**：
- 斯坦福大学计算成像实验室负责人
- 研究领域横跨神经渲染、全息显示、计算显微镜与生成模型
- 指导学生发表多篇CVPR/ICCV/NeurIPS/SIGGRAPH论文
- 2025年指导学生在CVPR获得Outstanding Reviewer (top 5%) 

**公开联系方式**：
- 个人主页：https://stanford.edu/~gordonwz/
- Google Scholar：可通过个人主页访问
- LinkedIn/X/Twitter：未在搜索结果中确认

---

### 3. **Saining Xie（谢赛宁）**
**现任职位**：纽约大学（NYU）助理教授；AMI Labs联合创始人兼首席科学官（CSO）

**入选理由**：
Saining Xie 是**扩散Transformer（DiT）架构的共同发明者**，该架构已成为Sora等主流视频生成系统的技术基础 。2026年，他联合图灵奖得主Yann LeCun创立AMI Labs，获得**10.3亿美元种子轮融资，投前估值35亿美元** 。AMI的核心方向是构建JEPA（联合嵌入预测架构）世界模型，而非生成式模型。2026年3月，他团队发布了**Solaris——全球首个多人视频世界模型**，基于Matrix-Game2.0架构引入"多人自注意力层"，实现多玩家在同一虚拟空间中的实时交互和视觉一致性 。他的学术影响力（引用超90,000次）与产业资源（顶级融资、NVIDIA合作）使其成为该领域最具系统影响力的学者之一。

**代表论文**：
- **Scalable Diffusion Models with Transformers (DiT)** (ICCV 2023)
  - 论文链接：https://arxiv.org/abs/2212.09748
  - 核心贡献：首次将Transformer架构系统性地引入扩散模型，替代传统卷积骨干，实现生成模型的可扩展性。该架构已成为Sora、Stable Diffusion 3等系统的核心组件 

- **Solaris: Multi-person Video World Model** (2026年3月发布)
  - 核心贡献：基于Matrix-Game2.0开源方案，引入多人自注意力层实现实时信息交换。在Minecraft测试场景中解决了建筑一致性和视觉对齐问题，支持多玩家在同一空间交互而不发生视觉崩溃 

- **Cambrian-1: 开源多模态模型** (2024)
  - 论文链接：可通过其主页获取

**研究方向**：扩散Transformer架构、世界模型（JEPA范式）、多模态理解、多人交互视频生成

**经历背景**：
- 上海交通大学本科（2013），UC San Diego博士（2018）
- 曾任Meta FAIR（4年）、Google DeepMind研究科学家
- 2023年起NYU助理教授，2026年春/夏学期休假专注AMI 
- 获Marr Prize Honorable Mention、NSF CAREER Award、PAMI Young Researcher Award等

**公开联系方式**：
- 个人主页：https://www.sainingxie.com/
- Google Scholar：可通过主页访问
- LinkedIn/X/Twitter：未在搜索结果中确认具体账号
- AMI Labs信息：公司总部巴黎，Yann LeCun任总部负责人 

---

### 4. **Jaesik Park**
**现任职位**：首尔国立大学（SNU）助理教授，视觉与几何智能实验室（VGI Lab）负责人 

**入选理由**：
Jaesik Park 是**实时交互视频生成的关键推动者**，其团队与Adobe Research、CMU合作开发的 **MotionStream** 实现了29 FPS的实时交互式视频生成（ICLR 2026 Oral）。他的研究特色是将**3D几何感知与生成模型结合**，在视频编辑、运动控制和场景一致性方面取得突破。此外，他在图像编辑领域提出的**Layer-wise Memory**机制（ICCV 2025）为迭代式交互生成提供了新范式 。作为SNU的PI，他培养了多名进入顶尖机构（Adobe Research、Microsoft Research Asia）的学生，形成了活跃的学术网络。

**代表论文**：
- **MotionStream: Real-Time Video Generation with Interactive Motion Controls** (ICLR 2026 Oral, 1.13%录取率)
  - 论文链接：https://arxiv.org/abs/2511.01266
  - 核心贡献：作为合作作者，参与设计了通过Self Forcing和Distribution Matching Distillation将双向教师模型蒸馏为因果学生模型的方法，实现亚秒级延迟和无限长度视频生成。项目由Adobe Research主导，SNU提供学术支持 

- **Improving Editability in Image Generation with Layer-wise Memory** (ICCV 2025)
  - 论文链接：https://arxiv.org/abs/2505.01079
  - 核心贡献：提出层-wise记忆机制存储先前编辑的潜在表示和提示嵌入，通过背景一致性引导和多查询解耦实现多次顺序编辑的场景连贯性，为交互式内容创作提供了新工具 

- **InstantDrag: Improving Interactivity in Drag-based Image Editing** (SIGGRAPH Asia 2024)
  - 核心贡献：提升拖拽式图像编辑的交互性

**研究方向**：实时视频生成、交互式运动控制、3D几何感知生成、迭代图像/视频编辑、扩散模型

**经历背景**：
- KAIST电气工程博士（2015），导师In So Kweon
- 曾任Intel Intelligent Systems Lab Staff Research Scientist（2015-2019），Manager: Vladlen Koltun
- 共同创建Open3D库（GitHub 10.8k+ stars）
- POSTECH助理教授（2019-2023）、副教授（2022-2023）
- SNU助理教授（2023至今），指导约20名硕士/博士生 

**公开联系方式**：
- 个人主页：https://jaesik.info/
- Google Scholar：https://jaesik.info/publications 或搜索"Jaesik Park SNU"
- LinkedIn/X/Twitter：未在搜索结果中确认具体账号
- 邮箱：jaesik.park@snu.ac.kr

---

### 5. **Jun-Yan Zhu（朱俊彦）**
**现任职位**：卡内基梅隆大学（CMU）助理教授 

**入选理由**：
Jun-Yan Zhu 是**生成模型与视觉理解交叉领域**的顶尖学者，其研究涵盖GAN、扩散模型和神经渲染。他与Adobe Research、SNU等合作参与**MotionStream**项目（ICLR 2026 Oral），为实时交互视频生成贡献了对因果注意力机制和模型蒸馏的理论分析 。他早期在**CycleGAN**（ICCV 2017最佳论文）和**GAN Dissection**（CVPR 2019）的工作为可控生成奠定了基础。近期他团队在学生指导下开发了**InstantDrag**等交互式编辑工具，持续推动生成模型向用户友好方向发展。

**代表论文**：
- **MotionStream: Real-Time Video Generation with Interactive Motion Controls** (ICLR 2026 Oral)
  - 论文链接：https://arxiv.org/abs/2511.01266
  - 核心贡献：作为合作作者（来自CMU），参与设计了滑动窗口因果注意力和attention sinks机制，解决无限长度视频生成中的误差累积和上下文窗口计算成本增长问题 

- **CycleGAN: Unpaired Image-to-Image Translation** (ICCV 2017, Best Paper)
  - 论文链接：https://arxiv.org/abs/1703.10593
  - 核心贡献：开创性实现无需配对数据的图像到图像转换，为后续可控生成奠定基础

- **GAN Dissection: Visualizing and Understanding Generative Adversarial Networks** (CVPR 2019 Oral)
  - 论文链接：https://arxiv.org/abs/1801.03101
  - 核心贡献：首次系统性地可视化和理解GAN内部表示，揭示生成器学到的对象概念

**研究方向**：可控图像/视频生成、神经渲染、生成模型可解释性、交互式视觉编辑

**经历背景**：
- 清华大学本科，CMU博士（导师：Alexei Efros）
- MIT博士后
- 2019年起CMU助理教授
- 获SIGGRAPH杰出博士论文奖、Adobe Research Fellowship等

**公开联系方式**：
- 个人主页：https://www.cs.cmu.edu/~junyanz/
- GitHub：https://github.com/junyanz
- Google Scholar：可通过主页访问
- LinkedIn/X/Twitter：未在搜索结果中确认具体账号

---

## 二、横向比较表

| 维度 | **Xun Huang** | **Gordon Wetzstein** | **Saining Xie** | **Jaesik Park** | **Jun-Yan Zhu** |
|------|---------------|----------------------|-----------------|-----------------|-----------------|
| **核心技术路线** | 自回归视频扩散蒸馏（Self Forcing）、实时流式生成、交互运动控制 | 视频世界模型+3D几何记忆、状态空间模型（SSM）、神经渲染 | JEPA世界模型、DiT架构、多人交互视频生成 | 3D几何感知生成、实时交互视频、迭代编辑记忆 | 可控生成、GAN/扩散模型、因果注意力机制 |
| **与实时互动视频/世界模型的相关性** | ⭐⭐⭐⭐⭐ 直接实现单GPU实时流式生成（29 FPS），产业落地最成熟 | ⭐⭐⭐⭐⭐ 解决世界模型长期一致性核心问题，几何记忆机制是关键基础设施 | ⭐⭐⭐⭐⭐ 架构层面定义行业标准（DiT），多人交互是前沿方向，但JEPA与生成式路线有差异 | ⭐⭐⭐⭐☆ 实时交互视频生成（MotionStream），但更多作为合作者参与 | ⭐⭐⭐★☆ 主要贡献在可控生成基础理论，实时交互为近期合作方向 |
| **产业价值** | ⭐⭐⭐⭐⭐ Roblox平台直接落地，影响数亿用户游戏体验；技术可泛化至所有实时交互场景 | ⭐⭐⭐⭐☆ 技术可赋能游戏、VR/AR、数字孪生；但偏学术，需产业伙伴转化 | ⭐⭐⭐⭐⭐ AMI Labs融资10.3亿美元，估值35亿美元；Solaris可直接服务游戏/VR产业 | ⭐⭐★☆☆ 学术导向，通过学生培养和技术授权产生间接产业影响 | ⭐⭐⭐☆☆ 学术影响力大，产业转化主要通过合作（Adobe）和学生创业 |
| **未来1-2年跟踪价值** | **最高优先级**：实时生成技术从"可用"到"好用"的关键节点；关注其在Roblox的落地进度和开源计划 | **高优先级**：长期记忆是世界模型的瓶颈问题；关注其记忆机制与商业模型的整合 | **高优先级**：AMI的产品化进程、JEPA vs 生成式路线的竞争结果、Solaris开源生态 | **中高优先级**：关注SNU VGI Lab独立成果（Layer-wise Memory等）及与产业合作深化 | **中优先级**：关注其在因果生成和交互编辑方面的独立贡献 |
| **机构/资源** | Roblox（游戏平台） | 斯坦福大学（学术） | AMI Labs + NYU（学术+创业） | 首尔国立大学（学术） | CMU（学术） |
| **技术成熟度** | 已有开源代码（GitHub）和演示 | 论文+项目页面，部分代码开源 | 公司预产品阶段，部分开源（Cambrian-1） | 论文发表，部分项目代码待开源 | 论文+部分开源代码 |

---

## 三、投资研究视角的关键判断

### 已验证事实
1. **Xun Huang** 的 Self Forcing 和 MotionStream 已实现单GPU实时流式视频生成，论文经同行评审（ICLR 2026 Oral），代码部分开源 
2. **Gordon Wetzstein** 团队的空间记忆机制（NeurIPS 2025）和状态空间模型（ICCV 2025）经同行评审，项目页面已上线 
3. **Saining Xie** 的 AMI Labs 获得10.3亿美元种子轮融资，Solaris模型已发布，Yann LeCun参与创立 
4. **Jaesik Park** 和 **Jun-Yan Zhu** 均为MotionStream的共同作者，该论文为ICLR 2026 Oral（1.13%录取率）

### 分析判断
1. **技术路线分化**：Xun Huang和Jaesik Park走"生成式扩散模型+蒸馏加速"路线，追求实时性；Saining Xie/AMI走JEPA（联合嵌入预测）路线，强调理解和规划能力而非像素生成。两种路线在未来1-2年将形成直接竞争。
2. **产业落地时序**：Xun Huang（Roblox）> Saining Xie（AMI）> Gordon Wetzstein（需转化）> Jaesik Park/Jun-Yan Zhu（学术为主）。实时互动视频生成的商业化窗口期可能在2026-2027年。
3. **关键瓶颈**：长期一致性（Gordon Wetzstein的研究方向）和多人交互一致性（Saining Xie的Solaris）是世界模型从"演示"走向"产品"的两大技术门槛。
4. **地缘因素**：Jaesik Park（韩国）和Saining Xie（中国背景+巴黎总部）的分布反映了该领域人才的全球化流动，但也带来合作网络的地缘复杂性。

---

**免责声明**：以上信息基于2025-2026年公开可查的论文、机构主页和媒体报道。部分学者的社交媒体账号未在公开搜索结果中确认，已明确标注。投资研究应结合更多一手尽职调查。
