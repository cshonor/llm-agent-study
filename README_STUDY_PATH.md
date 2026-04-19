# LLM 学习路线：全书 **12 章** 与仓库路径

《图解大语言模型》类体系：**共 12 章**。下面按章节列出**推荐落笔/落代码的位置**（**文件夹名均为英文**）。

| 章 | 主题（与书对应） | 仓库路径 |
|---:|------------------|----------|
| 1 | 大语言模型简介 | `01_foundations/01_llm_intro.md` |
| 2 | 词元与嵌入 | `01_foundations/02_tokens_embeddings.md` |
| 3 | LLM 内部机制 / Transformer | `01_foundations/03_transformer_internals.md` |
| 4 | 文本分类等 | `02_applications/04_text_classification/` |
| 5 | 聚类与主题建模等 | `02_applications/05_topic_clustering/` |
| 6 | 提示工程 | `02_applications/06_prompt_engineering/` |
| 7 | LangChain 与 Agent 等 | `02_applications/07_langchain_agent/` |
| 8 | 语义搜索与 RAG | `02_applications/08_rag/` |
| 9 | 多模态 LLM | `02_applications/09_multimodal/` |
| 10 | 构建文本嵌入模型 | `03_finetuning/10_embedding_training/` |
| 11 | 分类任务微调等 | `03_finetuning/11_classification_finetuning/` |
| 12 | 生成模型微调（LoRA、DPO 等） | `03_finetuning/12_generation_lora_dpo/` |

**代码实验（跨章）**：`04_code_lab/`（例如 `bow_demo.py` 对应第 2 章词袋、`prompt_demo.py` 对应第 6 章等）。  
**资料与截图**：`05_resources/`。

按章节推进时：优先在对应 `.md` 或章节目录里记要点，在 `04_code_lab` 里放最小可运行示例。
