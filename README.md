# LLM Eval Code

AI 大模型代码生成能力评测仓库。收集不同模型对同一题目的代码输出，用于横向对比分析。

## 目录结构

```
llm-eval-code/
├── 3d-globe/                  # 题目：3D 数据可视化地球仪
│   ├── hunyuan3/index.html    # 混元 3 输出
│   ├── glm5-2/index.html      # GLM 5.2 输出
│   └── qwen3-7/               # Qwen 3.7 Plus 输出
├── thread-safe-queue/         # 题目：线程安全的泛型有界阻塞队列
│   ├── hunyuan3/queue.py
│   ├── glm5-2/queue.py
│   └── qwen3-7/queue.py
└── README.md
```

## 评测说明

- 每道题目的文件夹包含不同模型的完整代码输出
- 代码保持模型原始输出，不做任何修改

## 模型列表

| 模型 | 厂商 | 类型 |
|------|------|------|
| Hunyuan 3 | 腾讯 | 闭源 |
| GLM 5.2 | 智谱 | 闭源 |
| Qwen 3.7 Plus | 阿里 | 开源 |
