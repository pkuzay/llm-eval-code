# Kimi-K3 evaluation result

- Status: Partially satisfied
- Model: kimi-k3
- Evaluation note: The response covers all requested models with a structured price table and scenario analysis. Most core prices align with official sources, but GPT-5.5 now uses short/long-context price tiers rather than the single launch-price figure shown here. Several benchmark scores, price-change claims, and self-hosting break-even figures also lack source links.

## Raw assistant answer

我来帮你调研这几个模型的 API 价格。这些都是较新的模型，我先搜索最新的官方定价信息。
已找到大部分数据，还缺 HY3 preview 的信息，另外需要核实 Gemini 3.1 Pro 的官方定价（两个来源有出入）。继续搜索：
调研完成。以下数据来自各厂商官方定价页及第三方价格追踪站（截至 2026-07-19/20），单位统一为**每百万 tokens**。

## 一、API 价格总表

| 模型 | 输入 | 输出 | 缓存输入 | 上下文窗口 | 发布/状态 |
|---|---|---|---|---|---|
| **GPT-5.5**（OpenAI） | $5.00 | $30.00 | $0.50 | ~105 万 | 2026-04-24 发布 |
| ├ GPT-5.5 Pro | $30.00 | $180.00 | — | ~105 万 | 顶配档，价格为标准版 6 倍 |
| **Claude Opus 4.7**（Anthropic） | $5.00 | $25.00 | $0.50 | 100 万 | 2026-04-16 发布 |
| **DeepSeek V4 Pro** | $0.435 | $0.87 | $0.0036 | 100 万 | 2026-04-24 发布 |
| ├ DeepSeek V4 Flash | $0.14 | $0.28 | $0.0028 | 100 万 | 第三方渠道低至 $0.09/$0.18 |
| **Kimi K2.6**（Moonshot） | $0.95 | $4.00 | $0.16 | 26.2 万 | 开源，可自部署 |
| **HY3 Preview**（腾讯混元） | ¥2.00（≈$0.28） | ¥8.00（≈$1.11） | ¥0.80 | 26.2 万 | 腾讯云官方价 |
| **Gemini 3.1 Pro**（Google，≤20 万 tokens） | $2.00 | $12.00 | $0.20 | 100 万 | 2026-02-19 发布 |
| └ Gemini 3.1 Pro（>20 万 tokens） | $4.00 | $18.00 | $0.40 | — | 长上下文整体跳档 |

**补充说明：**

- **HY3 值得单独注意**：正式版 Hy3 定价已降至 ¥1/¥4（缓存 ¥0.25），比 Preview 版还便宜一半，且官方限时免费到 **2026 年 7 月 22 日**（后天截止）；第三方渠道（GMICloud/OpenRouter）上 Hy3 Preview 甚至只要 $0.063/$0.21。
- **各家折扣机制**：OpenAI、Anthropic、DeepSeek 均有 Batch API 半价；Google 的 Batch/Flex 档为 $1/$6，Priority 档则高达 $3.6/$21.6；Anthropic 缓存写入为 1.25 倍输入价、读取约 1 折。
- **同门更新款**：GPT-5.6 系列（Sol $5/$30、Terra $2.5/$15、Luna $1/$6）已于 7 月 9 日 GA；Claude Opus 4.8 已发布且与 4.7 同价（$5/$25）；Gemini 3.5 Flash（$1.5/$9）是 Google 当前主推。如果你还没锁定版本，这些同价或低价的新款也值得纳入评估。

## 二、性价比分析

用「综合能力指数（第三方基准，满分~50）÷ 混合成本（按 3:1 输入输出比估算）」做粗略的性价比标尺：

| 模型 | 综合智能分（百分位） | 混合成本/百万 tokens | 性价比评级 | 特点 |
|---|---|---|---|---|
| **Gemini 3.1 Pro** | 46.5（99%），GPQA 94.1 | ~$4.5 | ★★★★☆ | 六者中能力最强，价格却只有 GPT/Claude 一半 |
| **Claude Opus 4.7** | 42.7（97%），GPQA 88.5 | ~$10 | ★★★☆☆ | 能力强但贵；同价可上更新的 Opus 4.8 |
| **GPT-5.5** | 35.4（91%），GPQA 76.8 | ~$11.25 | ★★☆☆☆ | 价格最高档而跑分不占优，胜在生态和工具链 |
| **HY3 Preview** | 33.6（86%），GPQA 86.7 | ~¥3.5（≈$0.49） | ★★★★★ | 官方价仅为 GPT-5.5 的 ~1/20，GPQA 反超 GPT-5.5 |
| **DeepSeek V4 Pro** | 31.2（82%），GPQA 71.7 | ~$0.54 | ★★★★★ | 缓存命中价几乎为零，高并发成本最低 |
| **Kimi K2.6** | 基准站无同口径分数 | ~$1.71 | ★★★★☆ | Agentic 编码和长程任务是强项，工具调用表现突出 |

**分场景建议：**

1. **追求极致能力、预算不敏感**：Gemini 3.1 Pro 是当前「能力/价格」双优的选择——能力分最高，价格却只有 Opus 4.7 的 40%、GPT-5.5 的 40%。注意 prompt 超 20 万 tokens 会整体涨价一倍。
2. **大规模生产调用、成本敏感**：DeepSeek V4 Pro 和 HY3 是第一梯队。V4 Pro 输出仅 $0.87/百万，缓存命中价 $0.0036 几乎免费；HY3 正式版 ¥1/¥4 且这两天还限免，中文场景和国产生态对接更顺。
3. **Agent / 编码场景**：Kimi K2.6 开源可自部署，API 价 $0.95/$4 在编码类模型中很便宜；按官方测算，日调用 50K 次以内用 API 比自建划算（自托管盈亏平衡点约 3.26 亿 tokens/天）。Claude Opus 系列在指令遵循和长上下文工程任务上口碑最好，但需接受 5-10 倍溢价。
4. **GPT-5.5 的定位略显尴尬**：价格对标旗舰、跑分已被 Gemini 3.1 Pro 和 Opus 4.7 压制，除非是深度绑定 OpenAI 生态（Assistants API、工具链），否则纯按性价比不推荐；同门的 GPT-5.6 Terra（$2.5/$15）是更理性的选择。

**几个容易踩的坑**：推理类模型的「思考 tokens」按输出价计费，复杂任务 output 可能膨胀 30% 以上；Google 长文本超 200K 整单跳档而非只对超出部分加价；价格变动极快（DeepSeek V4 Pro 三个月内降价 75%），签约前务必以官方页面实时价格为准。
