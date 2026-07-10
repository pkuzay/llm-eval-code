下面按你指定的型号对比，时间口径为 **2026 年 7 月 10 日**。所有价格均按 **每 100 万 tokens** 计算；美元价格按 **1 美元≈6.8 元人民币** 粗略换算。([[中国银行](https://www.boc.cn/sourcedb/whpj/enindex_1619.html?utm_source=chatgpt.com)][1])

## 一、API 价格对比

| 模型                               |          上下文窗口 |              输入价 |            缓存命中价 |             输出价 | 价格说明                                                                                         |
| -------------------------------- | -------------: | ---------------: | ---------------: | --------------: | -------------------------------------------------------------------------------------------- |
| **GPT-5.5**                      |        约 105 万 | **≤272K：$5≈¥34** |       $0.50≈¥3.4 |    **$30≈¥204** | 单次请求超过 272K 后，输入 $10、缓存 $1、输出 $45；Batch/Flex 约半价。([[OpenAI平台](https://platform.openai.com/docs/pricing)][2])                             |
| **DeepSeek V4 Flash**            |          100 万 |  **$0.14≈¥0.95** |   $0.0028≈¥0.019 | **$0.28≈¥1.90** | 定位高吞吐、低延迟版本，支持思考、工具调用和 384K 最大输出。([[DeepSeek API Docs](https://api-docs.deepseek.com/quick_start/pricing)][3])                                    |
| **DeepSeek V4 Pro**              |          100 万 | **$0.435≈¥2.96** | $0.003625≈¥0.025 | **$0.87≈¥5.92** | V4 系列较高能力版本，价格仍明显低于其他国际旗舰模型。([[DeepSeek API Docs](https://api-docs.deepseek.com/quick_start/pricing)][3])                                         |
| **Claude Opus 4.7**              |          100 万 |       **$5≈¥34** |       $0.50≈¥3.4 |    **$25≈¥170** | Batch 为 $2.5/$12.5；缓存写入另收费。网上常见的 $30/$150 是 Fast Mode，不是标准 API 价。([[Claude Platform Docs](https://docs.anthropic.com/en/docs/about-claude/pricing)][4]) |
| **Kimi K2.6**                    |           256K |         **¥6.5** |             ¥1.1 |         **¥27** | 价格采用腾讯云 TokenHub 当前公开报价；支持文字、图片、视频输入及思考、工具调用。([[腾讯云](https://cloud.tencent.com/document/product/1823/130055)][5])                                      |
| **Hy3 Preview：0–16K**            | 256K，最大输入约192K |         **¥1.2** |             ¥0.4 |          **¥4** | 按单次请求输入长度分档。([[腾讯云](https://cloud.tencent.com/document/product/1823/130055)][5])                                                                       |
| **Hy3 Preview：16–32K**           |             同上 |         **¥1.6** |             ¥0.6 |        **¥6.4** | 长提示词成本上升。([[腾讯云](https://cloud.tencent.com/document/product/1823/130055)][5])                                                                          |
| **Hy3 Preview：32K以上**            |             同上 |           **¥2** |             ¥0.8 |          **¥8** | 即使进入最高档，价格仍较低。([[腾讯云](https://cloud.tencent.com/document/product/1823/130055)][5])                                                                     |
| **Gemini 3.1 Pro Preview：≤200K** |  100 万输入、64K输出 |     **$2≈¥13.6** |      $0.20≈¥1.36 |   **$12≈¥81.6** | 输出价包含模型使用的 thinking tokens；Batch/Flex 为 $1/$6。([[Google AI for Developers](https://ai.google.dev/gemini-api/docs/pricing)][6])                |
| **Gemini 3.1 Pro Preview：>200K** |             同上 |     **$4≈¥27.2** |      $0.40≈¥2.72 |  **$18≈¥122.4** | 超过 200K 后进入长上下文档。([[Google AI for Developers](https://ai.google.dev/gemini-api/docs/pricing)][6])                                             |

> 不同厂商对“缓存”的定义不完全一致。Claude 还区分缓存读取、5 分钟写入和 1 小时写入；Gemini 可能另收缓存存储费，不能只看命中单价。

---

## 二、典型使用成本

假设一项业务累计消耗：

* 输入：100 万 tokens
* 输出：20 万 tokens
* 不使用缓存
* 多次请求累计，且都位于对应价格档位

| 模型                        |             估算费用 | 相对成本 |
| ------------------------- | ---------------: | ---: |
| **DeepSeek V4 Flash**     |      **约 ¥1.33** |   最低 |
| **Hy3 Preview**           | **约 ¥2.00～3.60** |   极低 |
| **DeepSeek V4 Pro**       |      **约 ¥4.14** |   极低 |
| **Kimi K2.6**             |     **约 ¥11.90** |   较低 |
| **Gemini 3.1 Pro ≤200K档** |     **约 ¥29.92** |   中等 |
| **Gemini 3.1 Pro >200K档** |     **约 ¥51.68** |   中高 |
| **Claude Opus 4.7**       |     **约 ¥68.00** |    高 |
| **GPT-5.5 ≤272K档**        |     **约 ¥74.80** |    高 |
| **GPT-5.5 >272K档**        |    **约 ¥129.20** |   很高 |

单看 token 价格，DeepSeek V4 Flash 的典型账单大约只有 GPT-5.5 标准短上下文档的 **1/56**。但这只是成本差距，不代表两者在复杂任务中的实际效果也相差相同比例。

---

## 三、各模型性价比分析

### 1. DeepSeek V4 Flash：批量业务的价格屠夫

**性价比：★★★★★**

最突出的优势就是便宜。输入、输出和缓存价格都远低于其他模型，并且有 100 万上下文和工具调用能力。

比较适合：

* 海量文本分类、抽取、改写和审核
* 搜索结果整理、RAG 问答
* 对话机器人和高并发 Agent
* 可以接受偶尔重试或二次校验的业务

它的问题不在价格，而在于你需要结合自己的任务测试：复杂编程、长链条 Agent、极高指令遵循要求下，是否能达到昂贵旗舰模型的稳定性。

**结论：只要实际效果达到业务及格线，它通常就是成本最优解。**

---

### 2. DeepSeek V4 Pro：综合成本性价比最强

**性价比：★★★★★**

Pro 比 Flash 贵约 3 倍，但放到整个市场里依然极便宜。按照官方规格，它同时提供 100 万上下文、超长输出、思考模式和工具调用。

适合：

* 复杂分析与研究
* 代码生成和代码库理解
* 多步骤 Agent
* 对质量要求高，但无法承受 Claude/GPT 成本的产品

相较 Flash，Pro 更适合作为主模型；Flash 则可以承担预处理、路由、摘要等外围任务。

**结论：如果要兼顾模型能力和大规模调用成本，V4 Pro 是这一组里最值得优先压测的型号。**

---

### 3. Hy3 Preview：国内企业应用的低成本选择

**性价比：★★★★☆**

其价格介于 DeepSeek Flash 和 Pro 附近，人民币直接计费，国内云服务采购、结算和企业接入通常更方便。

优势：

* 输出最高档也只有 ¥8/百万 tokens
* 中文业务和国内企业接入友好
* 支持工具调用、结构化输出和交错思考
* 256K 上下文已经足够多数企业场景

不足是价格按输入长度分档；同一批 100 万 tokens，如果由大量长提示词请求组成，费用会比短请求更高。另外它仍带有 Preview 标签，生产环境需要关注版本升级和行为变化。

值得注意的是，腾讯云现在还提供 **Hy3 正式版**，公开价格约为输入 ¥1、缓存 ¥0.25、输出 ¥4，不要求 Preview 特性的情况下，正式版反而更便宜。([[腾讯云](https://cloud.tencent.com/document/product/1823/130055)][5])

---

### 4. Kimi K2.6：中文编码与 Agent 的均衡档

**性价比：★★★★☆**

它比 DeepSeek、Hy3 贵，但依然显著低于 Gemini、Claude 和 GPT。Kimi K2.6 的卖点不只是语言模型，还包括多模态输入、思考模式和工具调用。

比较适合：

* 中文代码助手
* 产品研究和复杂资料分析
* 图片、视频、文档混合输入
* 国内 Agent 产品
* 对模型一致性要求高于“极致省钱”的场景

其 256K 上下文低于 GPT、Claude、Gemini 和 DeepSeek V4 的百万级上下文，不过多数常规 Agent 和代码任务并不会真正用满 100 万。

**结论：不追求最低成本，重视中文、多模态和 Agent 综合体验时，Kimi K2.6 是较稳妥的中间选择。**

---

### 5. Gemini 3.1 Pro：国际旗舰里的价格均衡型

**性价比：★★★★☆**

在国际旗舰模型中，它明显比 GPT-5.5 和 Claude Opus 4.7 便宜。尤其是短于 200K 的请求，标准价格只有 $2/$12；Batch/Flex 进一步降至 $1/$6。

适合：

* 图片、视频、音频、文档等原生多模态任务
* 超长文档处理
* Google Cloud 或 Vertex AI 技术栈
* 可以使用批处理降低成本的离线业务
* 需要较强能力，又不愿承担 GPT/Claude 价格

需要留意两个隐性成本：

1. thinking tokens 会计入输出 tokens；
2. 超过 200K 后，输入和输出价格都会提升。

**结论：对于多模态、长上下文和批量处理，它是国际模型中性价比较突出的一档。**

---

### 6. Claude Opus 4.7：贵，但适合高价值任务

**成本性价比：★★★☆☆
高价值任务性价比：★★★★☆**

Claude 的输出价比 GPT-5.5 低一些，并且 100 万上下文内没有 GPT 那种 272K 长上下文阶梯涨价。它更适合单次任务价值高、失败和返工成本高的场景。

适合：

* 大型代码库理解与修改
* 高难度 Agent
* 长文档写作、分析与编辑
* 对指令遵循和输出风格稳定性要求较高的场景

不过 Claude Opus 4.7 使用了新 tokenizer，同一段文本可能比旧版 Claude 产生更多 tokens，官方提示大约可能增加 30%，所以真实账单不能只依据表面单价判断。([[Claude Platform Docs](https://docs.anthropic.com/en/docs/about-claude/pricing)][4])

此外，**Fast Mode 的 $30/$150 是加速服务价格**，不要将它误认为 Opus 4.7 的普通 API 定价。

**结论：不适合跑廉价批量任务，但在复杂代码和高价值知识工作里，少返工一次就可能覆盖模型价差。**

---

### 7. GPT-5.5：生态与能力优先，成本不占优势

**成本性价比：★★★☆☆
综合生产力性价比：★★★★☆**

GPT-5.5 与 Claude 输入价格相同，但输出价格更高；单次上下文超过 272K 后还会明显涨价。因此它不适合作为无差别的全量底座模型。

优势主要在于：

* OpenAI API 和工具生态完整
* 约 105 万上下文、128K 最大输出
* 适合复杂工具调用、代码和专业分析
* 企业已有 OpenAI 技术栈时，迁移成本较低

适合：

* 单次请求价值高
* 对 OpenAI 工具链和兼容性有依赖
* 模型质量和稳定性比 token 成本更重要
* 可以通过路由机制只让少量困难任务进入 GPT-5.5

**结论：它的优势不是便宜，而是能力、工具生态和现有系统兼容性。高并发产品若全量使用，成本压力会很明显。**

---

## 四、最终选型建议

| 业务目标            | 优先选择                            | 备选              |
| --------------- | ------------------------------- | --------------- |
| 极致低成本、高并发       | **DeepSeek V4 Flash**           | Hy3 Preview     |
| 复杂推理但预算有限       | **DeepSeek V4 Pro**             | Kimi K2.6       |
| 国内企业采购、中文业务     | **Hy3 / Kimi K2.6**             | DeepSeek V4 Pro |
| 中文编码和 Agent     | **Kimi K2.6 / DeepSeek V4 Pro** | Claude Opus 4.7 |
| 原生多模态、视频和长文档    | **Gemini 3.1 Pro**              | Kimi K2.6       |
| 大型代码库、高难度 Agent | **Claude Opus 4.7**             | GPT-5.5         |
| OpenAI 工具生态兼容   | **GPT-5.5**                     | Gemini 3.1 Pro  |
| 离线批处理           | **Gemini Batch / GPT Batch**    | DeepSeek V4     |

### 综合判断

按**纯成本**排序：

> DeepSeek V4 Flash ＜ Hy3 Preview ＜ DeepSeek V4 Pro ＜ Kimi K2.6 ＜ Gemini 3.1 Pro ＜ Claude Opus 4.7 ≈ GPT-5.5

按**单位价格与官方规格的综合性价比**：

> **DeepSeek V4 Pro > DeepSeek V4 Flash ≈ Hy3 Preview > Kimi K2.6 ≈ Gemini 3.1 Pro > Claude Opus 4.7 ≈ GPT-5.5**

实际产品里，更合理的方案通常不是只选一个模型，而是：

* Flash/Hy3 负责分类、抽取、摘要和简单问答；
* DeepSeek Pro/Kimi/Gemini 负责中高难度任务；
* Claude/GPT 仅处理低频、高价值、前级模型失败的任务。

这种三级模型路由，往往能把整体 API 成本降低一个数量级，同时保留旗舰模型处理困难任务的能力。

这些价格变化较快，也可设置每月检查六家官方定价并在价格调整时提醒。

[1]: https://www.boc.cn/sourcedb/whpj/enindex_1619.html?utm_source=chatgpt.com "BOC EXCHANGE RATE(new)"
[2]: https://platform.openai.com/docs/pricing "
  Pricing | OpenAI API
"
[3]: https://api-docs.deepseek.com/quick_start/pricing "Models & Pricing | DeepSeek API Docs"
[4]: https://docs.anthropic.com/en/docs/about-claude/pricing "Pricing - Claude Platform Docs"
[5]: https://cloud.tencent.com/document/product/1823/130055 "大模型服务平台 TokenHub 模型价格_腾讯云"
[6]: https://ai.google.dev/gemini-api/docs/pricing "Gemini Developer API pricing  |  Gemini API  |  Google AI for Developers"
