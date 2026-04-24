# 02 Transformer编码器深度拆解

## 一、编码器整体结构

编码器由 N 个重复编码层堆叠（Transformer Base 常见为 6 层）。每层结构相同：

多头自注意力 -> 残差连接 + 层归一化 -> 前馈神经网络（FFN）-> 残差连接 + 层归一化

## 二、编码器核心模块详解

### 1) 词嵌入 + 位置编码

- 词嵌入：将 token 映射为固定维度向量（Base 常见 `d_model=512`）
- 位置编码：补充位置信息，常见正弦/余弦形式

`PE(pos,2i)=sin(pos/10000^(2i/d_model))`

`PE(pos,2i+1)=cos(pos/10000^(2i/d_model))`

最终输入是：词嵌入向量 + 位置编码向量

### 2) 多头自注意力（编码器核心）

- 输入：词向量序列
- 流程：线性映射得到 Q/K/V -> 分头并行注意力 -> 拼接 -> 线性映射
- 特点：编码器是全局自注意力（无因果掩码）

### 3) 残差连接与层归一化

- 残差：缓解深层网络训练困难，保留底层信息
- 层归一化：稳定训练分布、加速收敛

常见写法：`LayerNorm(x + SubLayer(x))`

### 4) 前馈神经网络（FFN）

每个位置独立执行同构两层感知机：

1. `d_model (512) -> 4*d_model (2048) + 激活`
2. `4*d_model (2048) -> d_model (512)`

作用：对注意力输出做非线性变换，提升特征表达能力。

## 三、编码器输出与句向量提取

编码器输出通常是：`序列长度 x d_model` 的上下文向量序列。

### 1) [CLS] 向量

- 在输入前加 `[CLS]`
- 取其输出向量作为句向量
- 优点：计算简单、推理快，适合实时意图判断

### 2) Mean Pooling（平均词向量）

- 对所有 token 向量做平均
- 常见公式：`sent = (1/N) * sum(token_i)`
- 优点：稳定、覆盖语义更全面，常用于检索/相似度

### 3) 两种方式建议

- `[CLS]`：低延迟分类与路由
- Mean Pooling：RAG 检索、向量匹配、语义相似度

## 四、平均词向量代码（可直接复用）

```python
from typing import Sequence
import numpy as np


def mean_pooling(token_embeddings: np.ndarray, attention_mask: Sequence[int]) -> np.ndarray:
    """
    token_embeddings: shape [seq_len, hidden_size]
    attention_mask:   shape [seq_len], 1 表示有效 token，0 表示 padding
    """
    mask = np.asarray(attention_mask, dtype=np.float32).reshape(-1, 1)  # [seq_len, 1]
    masked = token_embeddings * mask
    denom = np.clip(mask.sum(axis=0), 1e-9, None)
    return masked.sum(axis=0) / denom
```

> 若使用 Hugging Face，可将 `last_hidden_state` 与 `attention_mask` 传入同样逻辑。

## 五、编码器常见参数（Base）

- `d_model = 512`
- `num_heads = 8`
- `d_ff = 2048`
- `num_layers = 6`

