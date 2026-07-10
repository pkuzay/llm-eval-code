[![Genie 3: An Infinite World Model with Shlomi Fruchter and Jack Parker ...](https://tse1.mm.bing.net/th/id/OIP.pKlx72djTlMKGiTl-RDeGwHaHa?r=0\&pid=Api)](https://www.audible.com/es_US/podcast/Genie-3-An-Infinite-World-Model-with-Shlomi-Fruchter-and-Jack-Parker-Holder/B0FND872B4?utm_source=chatgpt.com)

# 实时互动视频生成 / 世界模型：5 位头部研究者跟踪清单

**研究时点：2026 年 7 月 10 日**

## 一、研究口径与结论

本报告采用较严格的“互动世界模型”定义：模型不仅生成一段看起来合理的视频，还需要让**用户动作、镜头控制、文字指令或其他交互信号持续影响后续世界状态**。近期综述将该方向的核心瓶颈归纳为：动作可控性、长时交互与记忆，以及实时响应能力。([[arXiv](https://arxiv.org/abs/2606.01164?utm_source=chatgpt.com)][1])

因此，本次筛选：

* 不将普通文生视频、单次视频编辑直接等同于世界模型；
* 不讨论以机器人、自动驾驶和物理执行为主要落地目标的研究；
* 但保留可服务于游戏、虚拟世界、AR/VR、互动内容和实时视频生成的物理模拟或 3D 表示方法；
* “学者”按广义口径处理，包括高校教授和产业研究负责人。

这不是按 Google Scholar 引用量排列的榜单，而是综合考察了三个维度：**对互动视频核心技术的直接贡献、持续项目领导力，以及未来产业化杠杆**。

综合判断，最值得持续跟踪的 5 位分别为：

1. **Shlomi Fruchter**：Google DeepMind 实时生成世界与大型生成模型负责人
2. **Jack Parker-Holder**：Genie 路线的核心发起人与世界模型团队负责人
3. **Tim Brooks**：Sora 共同负责人，当前 Meta 多模态生成核心研究者
4. **Yangguang Li（李阳光）**：Matrix-Game 开源实时世界模型项目负责人
5. **Jiajun Wu（吴佳俊）**：显式 3D、物理模拟与视频生成混合路线代表

其中，前三位更接近大厂的“基础模型规模化路线”；Yangguang Li 代表开放权重、实时部署路线；Jiajun Wu 则是对纯像素自回归路线的重要架构对冲。

---

# 二、重点研究者

## 1. Shlomi Fruchter

### 已验证事实

Shlomi Fruchter 目前是 **Google DeepMind Research Director**，个人主页显示其主要从事大型生成模型研究，曾领导或参与 Veo、Imagen 3、Magic Editor 等项目。Genie 3 官方发布文章由他与 Jack Parker-Holder 共同署名，公开访谈和个人账号将其列为 Genie 3 的共同负责人。([[shlomifruchter.github.io](https://shlomifruchter.github.io/)][2])

他的独特之处在于，研究轨迹横跨了：

**通用视频生成 Veo → 神经游戏引擎 GameNGen → 通用实时互动世界 Genie 3。**

这使他同时掌握高质量视频基础模型与实时闭环生成两端，而不只是某一个局部模块。

**公开账号：**
[[个人主页](https://shlomifruchter.github.io/)](https://shlomifruchter.github.io/)｜[[Google Scholar](https://scholar.google.com/citations?hl=en&user=YkQGEqsAAAAJ)](https://scholar.google.com/citations?hl=en&user=YkQGEqsAAAAJ)｜[[LinkedIn](https://ch.linkedin.com/in/shlomifruchter)](https://ch.linkedin.com/in/shlomifruchter)｜[[X/Twitter](https://x.com/shlomifruchter)](https://x.com/shlomifruchter)

### 代表成果一：GameNGen

**论文：** [[Diffusion Models Are Real-Time Game Engines](https://arxiv.org/abs/2408.14837)](https://arxiv.org/abs/2408.14837)
**项目页：** [[GameNGen](https://gamengen.github.io/)](https://gamengen.github.io/)

GameNGen 用神经网络完整替代了传统《DOOM》游戏的状态更新和像素渲染过程。系统先训练强化学习智能体游玩游戏并收集带动作的轨迹，再训练扩散模型，根据历史画面和用户动作预测下一帧；在单个 TPU 上达到超过 20 FPS。([[arXiv](https://arxiv.org/html/2408.14837v1)][3])

**论文解读：**

它的重要性不在于“AI 能模仿《DOOM》画面”，而在于首次较有说服力地证明：**游戏引擎的主循环可以被动作条件视频模型近似替代**。也就是说，程序员不再明确编写每一个状态转移与渲染规则，模型可以从交互轨迹中学习“按下某个键后世界应如何变化”。

但其边界也很明确：训练和评估集中在单一游戏，画面空间高度受限，记忆能力有限。作者也明确表示，进一步扩展到复杂软件和更长记忆仍是未来工作。([[arXiv](https://arxiv.org/html/2408.14837v1)][3])

### 代表成果二：Genie 3

**官方技术介绍：** [[Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)

Google DeepMind 披露，Genie 3 可从文本提示生成可实时导航的动态世界，输出为 720p、24 FPS，并能在数分钟内保持一定一致性。它逐帧响应用户动作，而不是预先一次性生成完整视频。([[Google DeepMind](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)][4])

**论文解读：**

Genie 3 标志着路线从“复刻一个现有游戏”转向“根据自然语言即时生成新世界”。其潜在价值也从游戏模拟器扩展到互动娱乐、虚拟拍摄、可探索教育内容和生成式 UGC。

需要注意，Genie 3 当前主要以官方技术介绍和产品演示形式披露，**完整模型结构、训练数据、推理成本与系统实现并未公开**。因此，24 FPS 和数分钟一致性是官方演示条件下的数据，不能直接等同于任意场景、任意硬件上的稳定表现。

### 入选理由与投资判断

**入选理由：** Shlomi Fruchter 是目前少数同时实际领导过高质量视频模型、神经游戏引擎和通用互动世界模型的人。

**投资判断：** 他是判断 Google 是否能把 Veo 的视觉质量、Genie 的互动性和 Gemini 的多模态理解融合成统一“生成式世界平台”的关键人物。

未来 1—2 年重点看：

* Genie 是否开放稳定 API 或开发者平台；
* 动作空间是否从行走、转向扩大到对象操作和复杂事件；
* 世界记忆能否从分钟级提升至小时级或持久化；
* Genie 与 Veo、Flow、Gemini 的底层模型是否进一步合并。

---

## 2. Jack Parker-Holder

### 已验证事实

Jack Parker-Holder 是 Genie 项目的核心发起人。其个人主页显示，他在 Google DeepMind 从事开放式学习与世界模型研究，并兼任 UCL 荣誉讲师；他在牛津大学完成博士训练，此前曾在 Meta FAIR 实习，并有约七年的量化研究和摩根大通 ETF 交易经历。([[jparkerholder.github.io](https://jparkerholder.github.io/)][5])

公开职位信息存在轻微不一致：其个人主页仍标注为 **Research Scientist**，而目前 X 主页标注为 **Research Director, scaling world models at Google DeepMind**。可以确认的是，他持续负责 DeepMind 世界模型路线并共同领导 Genie 3，但不宜强行统一其具体职级名称。([[X (formerly Twitter)](https://x.com/jparkerholder?lang=en&utm_source=chatgpt.com)][6])

**公开账号：**
[[个人主页](https://jparkerholder.github.io/)](https://jparkerholder.github.io/)｜[[Google Scholar](https://scholar.google.com/citations?hl=en&user=2O_ESc4AAAAJ)](https://scholar.google.com/citations?hl=en&user=2O_ESc4AAAAJ)｜[[LinkedIn](https://uk.linkedin.com/in/jparkerholder)](https://uk.linkedin.com/in/jparkerholder)｜[[X/Twitter](https://x.com/jparkerholder)](https://x.com/jparkerholder)

### 代表论文：Genie

**论文：** [[Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391)](https://arxiv.org/abs/2402.15391)
**项目页：** [[Genie 2024](https://sites.google.com/view/genie-2024/home)](https://sites.google.com/view/genie-2024/home)

Genie 是一个约 110 亿参数的生成式互动环境模型，由时空视频 tokenizer、自回归动力学模型和潜在动作模型组成。最关键的突破是：模型可以从**没有动作标签的互联网视频**中学习潜在动作空间，之后让用户逐帧控制生成环境。([[arXiv](https://arxiv.org/abs/2402.15391?utm_source=chatgpt.com)][7])

### 论文解读

传统动作条件世界模型面临明显的数据瓶颈：视频很多，但同时包含准确键盘、鼠标或控制器动作的视频很少。

Genie 的潜在动作模型尝试从连续视频中反推出“两个画面之间发生了什么动作”。因此，模型不必预先知道某个离散标签是“向左走”还是“跳跃”，而是先学习一组能解释状态变化的动作编码。

这条路线的战略意义在于，它有机会把互联网视频转化为世界模型训练数据，形成类似大语言模型利用互联网文本的数据扩张逻辑。其局限则是潜在动作未必具有人类可理解的语义，也可能把镜头变化、对象运动和真正的用户动作混在一起。

### Genie 2 与 Genie 3 的延伸

Genie 2 将该路线扩展到可通过键鼠控制的 3D 环境；Genie 3 又进一步实现 720p、24 FPS 的实时互动，并延长了世界一致性时间。([[Google DeepMind](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/?utm_source=chatgpt.com)][8])

尽管 Jack 的公开研究目标也包括为智能体提供训练环境，本报告将其列入的原因仅限于：**他在无标注视频学习、生成式游戏世界及实时互动内容方面的贡献**，而非机器人应用。

### 入选理由与投资判断

**入选理由：** 如果 Shlomi 更像“大型生成系统与实时化负责人”，Jack 的差异化价值则是**世界模型的数据学习范式和动作表示**。

**投资判断：** 潜在动作能否真正规模化，是世界模型能否复制 LLM 预训练飞轮的关键变量之一。

未来 1—2 年重点看：

* 潜在动作能否跨游戏、跨场景形成统一动作词表；
* 是否能够把无标注真实视频转化为稳定可控的交互数据；
* 世界模型能否从“生成可走动环境”升级到“生成有目标、规则和游戏机制的环境”；
* Genie 是否形成面向开发者和创作者的数据反馈飞轮。

---

## 3. Tim Brooks

### 已验证事实

Tim Brooks 目前在 **Meta Superintelligence Labs** 从事多模态生成模型研究。此前他在 Google DeepMind 从事世界模型和多模态生成研究，再此前在 OpenAI 共同创建并领导 Sora；他在 UC Berkeley 获得人工智能方向博士学位。([[Timothy Brooks](https://www.timothybrooks.com/?utm_source=chatgpt.com)][9])

需要严格区分的是：Tim Brooks 对大规模视频世界模型的影响非常大，但截至目前，Meta 尚未公开由他负责的、类似 Genie 3 或 Matrix-Game 的实时互动世界模型。因此，他的入选更多基于**底层视频模型路线与组织信号**，而不是已经发布的 Meta 互动产品。

**公开账号：**
[[个人主页](https://www.timothybrooks.com/)](https://www.timothybrooks.com/)｜[[Google Scholar](https://scholar.google.com/citations?hl=en&user=l9iNFaMAAAAJ)](https://scholar.google.com/citations?hl=en&user=l9iNFaMAAAAJ)｜[[LinkedIn](https://www.linkedin.com/in/timothyebrooks)](https://www.linkedin.com/in/timothyebrooks)｜[[X/Twitter](https://x.com/_tim_brooks)](https://x.com/_tim_brooks)

### 代表论文一：长视频动态建模

**论文：** [[Generating Long Videos of Dynamic Scenes](https://arxiv.org/abs/2206.03429)](https://arxiv.org/abs/2206.03429)

该论文针对早期视频模型容易陷入“画面不变化”或“长时间后内容变形”的问题，重新设计时间潜变量，并采用长视频低分辨率训练和短视频高分辨率训练相结合的两阶段策略。([[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2022/hash/ce208d95d020b023cba9e64031db2584-Abstract-Conference.html?utm_source=chatgpt.com)][10])

**论文解读：**

这是 Tim Brooks 后续 Sora 路线的重要前身。其核心思想是：视频模型不能只是给图像生成器增加一个弱时间维度，而要把**长时动态、对象持续存在和镜头移动**作为主要建模目标。

它还不是互动世界模型，因为没有实时动作输入，但解决的是互动世界模型的必要前置问题——世界不能在几秒后失去对象身份或退化成静态背景。

### 代表成果二：Sora 技术报告

**技术报告：** [[Video generation models as world simulators](https://openai.com/index/video-generation-models-as-world-simulators/)](https://openai.com/index/video-generation-models-as-world-simulators/)

Sora 将不同长度、分辨率和长宽比的图片及视频压缩到潜空间，切分为统一的时空 patch，再使用扩散 Transformer 建模。OpenAI 披露其最大模型能够生成约一分钟高保真视频，并观察到一定程度的三维一致性、对象持续存在和数字世界模拟能力。([[OpenAI](https://openai.com/index/video-generation-models-as-world-simulators/?utm_source=chatgpt.com)][11])

**论文解读：**

Sora 的核心主张是：扩大视频生成模型的规模，本身可能产生一定的世界模拟能力。这一路线相信，足够强的视频预测模型能够通过海量视觉数据隐式学习空间、运动和物理规律。

但 Sora 并非成熟的互动世界模型：它主要接受生成前给定的条件，不能像 Genie 或 Matrix-Game 一样持续接受用户动作并低延迟生成下一状态。技术报告也明确没有公开完整模型和实现细节。([[Latent Labs](https://www.latentlabs.com/video-generation-models-as-world-simulators/?utm_source=chatgpt.com)][12])

独立研究还表明，视频模型可能只是对训练分布进行“相似案例匹配”，在分布外物理规律泛化方面依然较弱。因此，“生成逼真视频”和“真正学习世界规则”不能画等号。([[arXiv](https://arxiv.org/abs/2411.02385?utm_source=chatgpt.com)][13])

### 入选理由与投资判断

**入选理由：** Tim Brooks 是“把视频基础模型扩展为世界模拟器”路线最具代表性的研究领导者之一，而且其人才流动横跨 OpenAI、Google DeepMind 与 Meta。

**投资判断：** 他加入 Meta 后，可能帮助 Meta 建立区别于传统 JEPA 表征学习路线的像素级、多模态生成能力。但 Meta 是否真的将其资源投入实时互动世界模型，目前仍属于分析推断，不能视为已公布事实。

未来 1—2 年重点看：

* Meta 是否发布新的大型视频或世界生成基础模型；
* 是否把 Instagram、Quest、游戏和社交内容数据转化为多模态生成优势；
* 是否出现低延迟、动作条件或可交互生成能力；
* 视频模型与 Meta 的 AR/VR、虚拟角色和社交产品是否形成闭环。

---

## 4. Yangguang Li（李阳光）

### 已验证事实

Yangguang Li 的个人主页显示，他自 2021 年起担任上海人工智能实验室高级顾问，2023 年 4 月至 2025 年 4 月担任 VAST Research Director，此前为商汤科技 Research Leader；其博士毕业于香港中文大学，目前研究重点为世界模型和 3D 生成。([[yg256li.github.io](https://yg256li.github.io/)][14])

在 Matrix-Game 2.0 论文中，他被列为项目负责人及通信联系人之一；其个人主页连续列出了 Matrix-Game 1.0、2.0、3.0 和 Matrix-3D 等项目，呈现出较为完整的“互动视频—实时推理—长期记忆—显式 3D 世界”布局。([[arXiv](https://arxiv.org/html/2508.13009v4)][15])

**公开账号：**
[[个人主页](https://yg256li.github.io/)](https://yg256li.github.io/)｜[[Google Scholar](https://scholar.google.com/citations?hl=zh-CN&user=a7AMvgkAAAAJ)](https://scholar.google.com/citations?hl=zh-CN&user=a7AMvgkAAAAJ)｜[[X/Twitter](https://x.com/ygLi212175)](https://x.com/ygLi212175)｜[[Matrix-Game GitHub](https://github.com/SkyworkAI/Matrix-Game)](https://github.com/SkyworkAI/Matrix-Game)

**LinkedIn：** 未找到能够可靠确认属于本人的 LinkedIn 页面。检索到的主要同名账号是 Google AI Studio 前端工程师，与其公开履历明显不符，因此不列入。

### 代表论文一：Matrix-Game 2.0

**论文：** [[Matrix-Game 2.0](https://arxiv.org/abs/2508.13009)](https://arxiv.org/abs/2508.13009)
**代码：** [[SkyworkAI/Matrix-Game](https://github.com/SkyworkAI/Matrix-Game)](https://github.com/SkyworkAI/Matrix-Game)

Matrix-Game 2.0 使用约 1,200 小时 Unreal Engine 和 GTA5 环境数据，加入逐帧键盘及鼠标动作控制，并通过少步扩散蒸馏、因果自回归架构和 KV cache 实现流式生成。论文报告其在单张 H100 上达到约 25 FPS，并支持分钟级生成。([[arXiv](https://arxiv.org/html/2508.13009v4)][15])

**论文解读：**

其工程路线非常清晰：

1. 用游戏引擎批量生产带精确动作标签的数据；
2. 在视频 DiT 中注入键鼠动作；
3. 将多步扩散蒸馏成三至四步；
4. 使用因果架构和缓存避免每次重新处理完整视频。

这条路线牺牲了一部分通用性，以换取部署速度、动作精度和开源可复现性。论文也披露了明显局限：2.0 的输出约为 352×640，在分布外场景中可能出现过饱和、退化或长时间移动后的画面崩坏。([[arXiv](https://arxiv.org/html/2508.13009v4)][15])

### 代表论文二：Matrix-Game 3.0

**论文：** [[Matrix-Game 3.0](https://arxiv.org/abs/2604.08995)](https://arxiv.org/abs/2604.08995)
**项目页：** [[Matrix-Game 3.0](https://matrix-game-v3.github.io/)](https://matrix-game-v3.github.io/)

Matrix-Game 3.0 增加了基于摄像机状态的记忆检索与注入、生成误差再注入训练、DMD 多段自回归蒸馏、量化和 VAE 剪枝。论文报告 5B 模型可在 720p 下达到最高 40 FPS，并在分钟级序列中维持较稳定的记忆；更大的 2×14B 版本用于提高质量和泛化。([[arXiv](https://arxiv.org/abs/2604.08995?utm_source=chatgpt.com)][16])

官方 GitHub 同时提供 1.0、2.0 和 3.0 的实现，并采用 MIT License。([[GitHub](https://github.com/SkyworkAI/Matrix-Game?utm_source=chatgpt.com)][17])

**论文解读：**

Matrix-Game 3.0 处理的是实时世界模型最现实的矛盾：模型必须快速逐帧生成，但短上下文又会导致走过的地点被遗忘。其解决方案不是无限扩大注意力窗口，而是建立外部记忆并按相机位置检索相关历史。

不过，40 FPS、分钟级稳定性等结果目前主要来自作者报告。其评测基准、硬件设置、实际交互延迟以及复杂场景表现，仍需更多第三方复现。另外，使用 GTA、AAA 游戏采集训练数据可能涉及数据许可和商业使用边界，投资尽调时应单独核查。

### 入选理由与投资判断

**入选理由：** 他是目前开源社区中少数持续推进“高帧率、流式生成、动作控制、长期记忆和开放权重”完整工程链条的研究负责人。

**投资判断：** 相较闭源大模型，Matrix-Game 未必在通用性和视觉质量上领先，但更可能率先形成开发者可改造、可私有部署的技术栈。

未来 1—2 年重点看：

* 第三方是否能复现论文公布的帧率和长时稳定性；
* 社区是否围绕 Matrix-Game 形成微调、游戏插件和应用生态；
* 训练能否摆脱特定游戏数据，泛化到真人、动画和影视场景；
* 推理成本能否下降到消费级 GPU 或端侧硬件；
* 开源模型是否形成实际商业客户，而非停留在演示阶段。

---

## 5. Jiajun Wu（吴佳俊）

### 已验证事实

Jiajun Wu 是斯坦福大学计算机科学系助理教授，并兼任心理学系教职；此前曾在 Google Research 担任访问教师研究员。他在 MIT 完成博士学位，导师包括 William T. Freeman 与 Josh Tenenbaum，本科就读于清华大学。([[Jiajun Wu](https://jiajunwu.com/)][18])

其研究长期围绕物理场景理解、3D/4D 表示、视觉生成和结构化世界建模。虽然研究组合中也包含机器人应用，本报告关注的是其在**可生成、可探索、可施加动作的视觉世界**方面的成果。

**公开账号：**
[[个人主页](https://jiajunwu.com/)](https://jiajunwu.com/)｜[[Google Scholar](https://scholar.google.com/citations?hl=en&user=2efgcS0AAAAJ)](https://scholar.google.com/citations?hl=en&user=2efgcS0AAAAJ)｜[[LinkedIn](https://www.linkedin.com/in/jiajunwu)](https://www.linkedin.com/in/jiajunwu)｜[[X/Twitter](https://x.com/jiajunwu_cs)](https://x.com/jiajunwu_cs)

### 代表论文一：WonderWorld

**论文：** [[WonderWorld: Interactive 3D Scene Generation from a Single Image](https://arxiv.org/abs/2406.09394)](https://arxiv.org/abs/2406.09394)
**项目页：** [[WonderWorld](https://kovenyu.com/wonderworld/)](https://kovenyu.com/wonderworld/)

WonderWorld 使用 Fast Layered Gaussian Surfels 和引导式深度扩散，从单张图像生成可连接的 3D 场景。论文报告，在单张 A6000 GPU 上生成新场景区域耗时不到 10 秒，生成后可实时渲染和探索。([[arXiv](https://arxiv.org/abs/2406.09394?utm_source=chatgpt.com)][19])

**论文解读：**

它与 Genie、Matrix-Game 的差异非常关键：

* Genie 和 Matrix-Game 主要生成下一段像素或视频 latent；
* WonderWorld 先构建显式、可渲染的 3D 场景表示。

显式 3D 路线更适合镜头自由移动、空间编辑、资产导出和传统游戏引擎集成；不足是生成新区域仍存在秒级等待，动态对象和复杂交互能力最初也较弱。

### 代表论文二：RealWonder

**论文：** [[RealWonder: Real-Time Physical Action-Conditioned Video Generation](https://arxiv.org/abs/2603.05449)](https://arxiv.org/abs/2603.05449)

RealWonder 从单张图片重建 3D 场景，使用物理模拟器计算动作后果，将光流和粗略 RGB 渲染作为中间控制信号，再交给经蒸馏的四步视频生成器进行真实感渲染。论文报告其达到 480×832 分辨率、最高 13.2 FPS，可处理相机控制、外力、刚体、流体、柔性和颗粒材料。([[arXiv](https://arxiv.org/abs/2603.05449?utm_source=chatgpt.com)][20])

### 论文解读

RealWonder 没有要求视频模型直接理解抽象的连续三维力和复杂动作，而是让传统物理模拟器先把动作翻译成模型熟悉的视觉信号。

这形成了一条不同于纯端到端世界模型的路线：

> **结构化 3D 状态负责可控性和因果约束，视频扩散模型负责真实感。**

与纯像素模型相比，它更容易控制具体对象、力的方向和材质变化，也能显式保留世界状态；代价则是系统复杂、需要可靠的单图 3D 重建和材质估计，而且目前 13.2 FPS 仍低于主流游戏需要的 30—60 FPS。

### 入选理由与投资判断

**入选理由：** Jiajun Wu 团队提供了对“只靠规模化视频预测即可形成世界模型”这一假设的重要替代方案，并已从 WonderWorld 的静态可探索场景推进到 RealWonder 的实时动作条件视频。

**投资判断：** 当产业需求从“看起来像真的”转向“镜头可控、对象可编辑、状态可保存、结果可重复”时，显式 3D 与视频模型结合可能比纯像素生成更适合专业内容生产。

未来 1—2 年重点看：

* RealWonder 能否提升至 30 FPS 以上；
* 显式物理状态和生成视频能否长期双向同步；
* 单图重建错误是否会在交互中累积；
* 系统是否能接入 Unity、Unreal、Blender 和虚拟拍摄工作流；
* 该路线能否支持角色、剧情与大规模开放世界，而不只是一小块物理场景。

---

# 三、五位研究者横向比较

> **说明：** 技术路线和公开成果属于已验证事实；“产业价值”“未来跟踪原因”和相关性评级属于研究判断。

| 研究者                    | 核心技术路线                                   | 与实时互动视频 / 世界模型的相关性                     | 潜在产业价值（分析判断）                           | 未来 1—2 年最值得跟踪的原因                                       |
| ---------------------- | ---------------------------------------- | -------------------------------------- | -------------------------------------- | ------------------------------------------------------ |
| **Shlomi Fruchter**    | 动作条件扩散、自回归视频生成、大规模多模态生成；GameNGen→Genie 3 | **极高**：已直接实现神经游戏引擎和 720p/24 FPS 通用互动世界 | 可能形成 Google 体系内的生成式游戏、互动影视、教育内容及世界模型平台 | 能否将 Veo 的画质、Genie 的交互和 Gemini 的理解能力统一；是否开放 API 与持久化世界  |
| **Jack Parker-Holder** | 无标注互联网视频预训练、潜在动作学习、自回归世界动力学              | **极高**：Genie 核心发起人，解决动作标签和训练数据扩张问题     | 可能建立世界模型的数据飞轮，使海量公开视频变为可交互环境训练数据       | 潜在动作能否跨场景形成统一表示；Genie 是否从“可探索”升级为“有规则、任务和机制”           |
| **Tim Brooks**         | 大规模视频扩散 Transformer、时空 patch、长视频和多模态预训练  | **高，但偏基础层**：Sora 展示世界模拟潜力，尚非持续动作闭环模型   | Meta 拥有社交、视频和 AR/VR 分发渠道，若完成实时化，商业杠杆极大 | Meta 是否发布动作条件或实时生成模型；视频基础模型是否与 Quest、Instagram 和虚拟角色结合 |
| **Yangguang Li**       | 少步自回归扩散、键鼠动作注入、KV cache、DMD 蒸馏、外部长期记忆    | **极高**：直接针对实时帧率、动作控制和分钟级一致性            | 最可能形成开放、可微调、可私有部署的互动视频技术栈              | 第三方复现、开发者采用、消费级 GPU 部署，以及训练数据许可与商业化能力                  |
| **Jiajun Wu**          | Gaussian/显式 3D 表示、物理模拟器、光流控制与视频扩散混合      | **高**：不完全依赖纯视频自回归，但已实现实时动作条件视频         | 对游戏资产、AR/VR、虚拟拍摄和专业可控内容生产更有优势          | 能否达到游戏级帧率，并把显式世界状态、物理逻辑和生成画面长期统一                       |

---

# 四、科技投资视角下的核心判断

## 1. 当前赛道还不是传统游戏引擎的直接替代品

目前最先进模型已经能做到实时或接近实时的视觉反馈，但在精确状态管理、复杂对象交互、多人同步、可重复运行、关卡规则和长时存档方面，仍明显弱于 Unity、Unreal 等确定性引擎。

近期研究也指出，多数互动世界模型仍主要支持导航动作，真正针对对象的持续操作、状态改变与因果记忆仍处于早期阶段。([[arXiv](https://arxiv.org/abs/2606.17730?utm_source=chatgpt.com)][21])

因此，未来一段时间更现实的产品形态可能不是“完全抛弃传统引擎”，而是：

**生成模型负责即时外观、内容扩展和未预制场景；传统引擎或结构化状态层负责规则、碰撞、角色状态和多人一致性。**

## 2. 未来壁垒不只在模型参数，而在交互数据

普通网络视频缺少精确动作标签。GameNGen 通过智能体收集，Matrix-Game 通过游戏引擎和 GTA5 自动采集，Genie 则尝试从无标签视频中学习潜在动作。这三种方法实际上对应三种数据战略。([[arXiv](https://arxiv.org/html/2408.14837v1)][3])

从投资角度看，值得重点考察的不是企业拥有多少普通视频，而是是否拥有：

* 带键鼠、控制器、镜头和对象状态的交互轨迹；
* 可合法使用的游戏、虚拟世界或创作软件数据；
* 用户实时操作产生的数据回流；
* 可自动扩展的数据引擎及评测环境。

## 3. “纯像素模型”与“结构化世界模型”很可能长期并存

Shlomi、Jack、Tim 和 Yangguang 更接近“让模型直接预测未来视觉状态”的路线；Jiajun Wu 则用显式 3D、物理模拟和视频生成组合世界。

前者扩展性强、视觉表现好，但容易产生状态漂移和因果幻觉；后者更可控、更容易编辑和接入传统内容工具，但系统复杂度更高。

现阶段尚无法断言某一路线会全面胜出。更可能的终局是：

> **视频基础模型提供世界先验和真实感，显式状态、记忆系统或可执行程序负责长期一致性与精确控制。**

## 4. 五人中不同风险偏好的跟踪选择

* **押注闭源技术上限：** Shlomi Fruchter、Jack Parker-Holder
* **押注大平台重新洗牌：** Tim Brooks
* **押注开源与低成本部署：** Yangguang Li
* **押注专业内容生产和可编辑世界：** Jiajun Wu

从“与本报告主题的直接程度”看，Shlomi、Jack、Yangguang 处于第一梯队；从未来产业平台影响力看，Tim Brooks 不应因为当前缺少公开互动产品而被忽视；从架构差异化和风险对冲看，Jiajun Wu 是最值得保留的非纯视频路线研究者。

这个赛道更新极快；可设置一份月度监测，持续追踪这 5 人的新论文、职位变化、GitHub 更新和项目发布。

[1]: https://arxiv.org/abs/2606.01164?utm_source=chatgpt.com "Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends"
[2]: https://shlomifruchter.github.io/ " Shlomi Fruchter "
[3]: https://arxiv.org/html/2408.14837v1 "Diffusion Models Are Real-Time Game Engines"
[4]: https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ "Genie 3: A new frontier for world models — Google DeepMind"
[5]: https://jparkerholder.github.io/ "Jack Parker-Holder"
[6]: https://x.com/jparkerholder?lang=en&utm_source=chatgpt.com "Jack Parker-Holder (@jparkerholder) / Posts / X"
[7]: https://arxiv.org/abs/2402.15391?utm_source=chatgpt.com "Genie: Generative Interactive Environments"
[8]: https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/?utm_source=chatgpt.com "Genie 2: A large-scale foundation world model"
[9]: https://www.timothybrooks.com/?utm_source=chatgpt.com "Tim Brooks"
[10]: https://proceedings.neurips.cc/paper_files/paper/2022/hash/ce208d95d020b023cba9e64031db2584-Abstract-Conference.html?utm_source=chatgpt.com "Generating Long Videos of Dynamic Scenes"
[11]: https://openai.com/index/video-generation-models-as-world-simulators/?utm_source=chatgpt.com "Video generation models as world simulators"
[12]: https://www.latentlabs.com/video-generation-models-as-world-simulators/?utm_source=chatgpt.com "Video generation models as world simulators"
[13]: https://arxiv.org/abs/2411.02385?utm_source=chatgpt.com "How Far is Video Generation from World Model: A Physical Law Perspective"
[14]: https://yg256li.github.io/ "Yangguang Li"
[15]: https://arxiv.org/html/2508.13009v4 "Matrix-game 2.0: An open-source real-time and streaming interactive world model"
[16]: https://arxiv.org/abs/2604.08995?utm_source=chatgpt.com "Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory"
[17]: https://github.com/SkyworkAI/Matrix-Game?utm_source=chatgpt.com "Matrix-Game - Skywork AI"
[18]: https://jiajunwu.com/ "Jiajun Wu"
[19]: https://arxiv.org/abs/2406.09394?utm_source=chatgpt.com "WonderWorld: Interactive 3D Scene Generation from a Single Image"
[20]: https://arxiv.org/abs/2603.05449?utm_source=chatgpt.com "RealWonder: Real-Time Physical Action-Conditioned Video Generation"
[21]: https://arxiv.org/abs/2606.17730?utm_source=chatgpt.com "ActWorld: From Explorable to Interactive World Model via Action-Aware Memory"
