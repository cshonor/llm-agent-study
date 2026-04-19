# LLM 学习路线：全书 **12 章**（三大模块）与仓库路径

定位：**从零入门大语言模型**，按 **原理 → 预训练模型应用 → 微调训练** 递进。下面先给**全书结构**，再给**章 ↔ 英文路径**速查表（文件夹名均为英文）。

---

## 第一部分：理解语言模型（底层原理）

**对应仓库：** `01_foundations/`

### 第 1 章 大语言模型简介

- 语言 AI 发展脉络、词向量与向量表征、Transformer 与注意力
- 编码器 / 解码器、LLM 定义与范式、应用与安全交互

**笔记文件：** `01_foundations/01_llm_intro.md`

### 第 2 章 词元与嵌入

- 分词、词嵌入与文本嵌入、Word2Vec
- 与推荐系统等「向量化表示」的衔接

**笔记文件：** `01_foundations/02_tokens_embeddings.md`  
**示例代码：** `04_code_lab/bow_demo.py`（词袋等朴素向量化）

### 第 3 章 LLM 的内部机制

- Transformer 整体结构、注意力机制、位置编码（如 RoPE）、架构演进

**笔记文件：** `01_foundations/03_transformer_internals.md`

---

## 第二部分：使用预训练语言模型（落地实战）

**对应仓库：** `02_applications/`

### 第 4 章 文本分类

- 情感分析、预训练模型做分类、零样本 / 少样本、工程化落地思路

**目录：** `02_applications/04_text_classification/`

### 第 5 章 文本聚类与主题建模

- 基于文本嵌入的聚类、BERTopic、无监督语义归纳

**目录：** `02_applications/05_topic_clustering/`

### 第 6 章 提示工程

- 基础 Prompt、思维链 CoT、上下文学习、格式与约束、输出校验

**目录：** `02_applications/06_prompt_engineering/`  
**示例代码：** `04_code_lab/prompt_demo.py`

### 第 7 章 高级文本生成技术与工具

- LangChain 链路、能力扩展、对话记忆、Agent

**目录：** `02_applications/07_langchain_agent/`

### 第 8 章 语义检索与 RAG

- RAG 全流程、本地知识库问答、效果评估

**目录：** `02_applications/08_rag/`  
**示例代码：** `04_code_lab/rag_demo.py`

### 第 9 章 多模态 LLM

- CLIP 等跨模态嵌入、图文理解、多模态链路概览

**目录：** `02_applications/09_multimodal/`

---

## 第三部分：训练与微调语言模型（进阶）

**对应仓库：** `03_finetuning/`

### 第 10 章 构建文本嵌入模型

- 对比学习、SBERT、无监督预训练、嵌入模型微调

**目录：** `03_finetuning/10_embedding_training/`

### 第 11 章 分类任务微调表示模型

- 监督分类、少样本、NER 等下游任务微调

**目录：** `03_finetuning/11_classification_finetuning/`

### 第 12 章 微调生成模型

- 预训练 + 微调范式、QLoRA、对齐与 DPO、偏见与安全

**目录：** `03_finetuning/12_generation_lora_dpo/`  
**示例代码：** `04_code_lab/finetune_lora.py`

---

## 章节目录与路径速查表

| 章 | 主题 | 仓库路径 |
|---:|------|----------|
| 1 | 大语言模型简介 | `01_foundations/01_llm_intro.md` |
| 2 | 词元与嵌入 | `01_foundations/02_tokens_embeddings.md` |
| 3 | LLM 内部机制 / Transformer | `01_foundations/03_transformer_internals.md` |
| 4 | 文本分类 | `02_applications/04_text_classification/` |
| 5 | 聚类与主题建模 | `02_applications/05_topic_clustering/` |
| 6 | 提示工程 | `02_applications/06_prompt_engineering/` |
| 7 | LangChain 与 Agent | `02_applications/07_langchain_agent/` |
| 8 | 语义检索与 RAG | `02_applications/08_rag/` |
| 9 | 多模态 LLM | `02_applications/09_multimodal/` |
| 10 | 构建文本嵌入模型 | `03_finetuning/10_embedding_training/` |
| 11 | 分类任务微调 | `03_finetuning/11_classification_finetuning/` |
| 12 | 生成模型微调 | `03_finetuning/12_generation_lora_dpo/` |

**跨章代码实验：** `04_code_lab/`  
**资料与截图：** `05_resources/`

---

## 与先修知识的衔接（可选）

若你已熟悉**梯度下降、损失函数、学习率**等，第 3 章里与优化、表示相关的推导会更容易连贯；其后按 **嵌入 → 提示工程 → RAG → Agent** 进入应用，再落到 **LoRA / 对齐** 等微调，形成从表示到系统再到训练的闭环。

---

## 使用方式

按章在对应 `.md` 或章节目录里记要点，在 `04_code_lab` 里为每一小段配最小可运行示例，便于对照书本图表与公式。
