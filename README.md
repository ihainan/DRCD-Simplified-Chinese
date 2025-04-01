# DRCD 简体中文版

本项目是在 [台达电子 DRCD（Delta Reading Comprehension Dataset）](https://github.com/DRCKnowledgeTeam/DRCD) 的基础上，进行的扩展版本。我们做了以下两项主要修改：

1. **将原始繁体中文内容全部转换为简体中文**
2. **基于 DRCD 的 QA 数据构建适用于信息检索任务的数据格式，包括维基百科原文（corpus）、查询（queries）和关联关系（qrels）**

---

## 数据说明

原始问答数据集的**简体中文翻译版本** 基于 zhconv 转换得到，具体实现脚本参见 convert_to_simplified.py。

数据集也可从 [Hugging Face](https://huggingface.co/datasets/ihainan/DRCD-Simplified-Chinese) 获取。

此外还额外生成适用于 IR 任务的完整长文档检索数据集，基于 wikipediaapi 和 zhconv 实现。这些文件可用于训练和评估信息检索系统（例如向量检索、BM25、dense retriever 等）。格式参考 [LongEmbed Benchmark](https://github.com/dwzhu-pku/LongEmbed) 提供的的数据集，也可以通过简单转换使用在 [BEIR Benchmark](https://github.com/beir-cellar/beir) 中。

数据集较大，请跳转 [Hugging Face](https://huggingface.co/datasets/ihainan/DRCD-for-Document-Retrieval-Task) 获取。

具体数据规模如下（Token 数基于 Qwen2.5-7B-Instruct 的 tokenizer 统计得到）：

- 训练集

| #Queries | # Docs | Avg Tokens/Query | Avg Tokens/Doc | Max Tokens in Docs |
| ----------- | ----------- | ----------- | ----------- | ----------- | 
| 3524 | 383 | 29 | 8831 | 61881 |

- 测试集

| #Queries | # Docs | Avg Tokens/Query | Avg Tokens/Doc | Max Tokens in Docs |
| ----------- | ----------- | ----------- | ----------- | ----------- | 
| 26920 | 1958 | 26 | 8000 | 79189 |

## 协议与署名

本项目基于原始的 DRCD 数据集进行构建，原始数据版权归 台达电子 DRCD 项目 所有，并使用 CC BY-SA 3.0 协议 发布。
