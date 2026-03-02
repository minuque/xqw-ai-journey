## ADDED Requirements

### Requirement: 文档处理与分块 Pipeline
学习者 SHALL 能构建完整的文档处理流水线，将 PDF/Markdown/网页等格式转换为可检索的文本块。

#### Scenario: 解析多种文档格式
- **WHEN** 学习者输入 PDF、Markdown 或 HTML 格式的文档
- **THEN** 能使用 Unstructured/PyMuPDF 等工具提取纯文本内容，保留必要的结构信息

#### Scenario: 实现智能分块策略
- **WHEN** 学习者需要将长文档切分为检索单元
- **THEN** 能实现递归分块和语义分块策略，控制块大小和重叠，保持语义完整性

### Requirement: Embedding 与向量存储
学习者 SHALL 能使用 Embedding 模型将文本向量化，并存储到向量数据库中进行相似性检索。

#### Scenario: 文本向量化
- **WHEN** 学习者需要将文本块转换为向量
- **THEN** 能调用 Voyage AI 或 OpenAI Embedding API 生成向量表示，理解向量维度和相似度计算原理

#### Scenario: 向量数据库 CRUD 操作
- **WHEN** 学习者需要存储和检索向量数据
- **THEN** 能使用 Chroma（入门）或 Qdrant（生产）完成向量的增删改查和相似性搜索

### Requirement: 检索优化策略
学习者 SHALL 掌握多种检索优化策略，显著提升 RAG 系统的检索质量。

#### Scenario: Query 改写与扩展
- **WHEN** 用户查询过于简短或模糊
- **THEN** 能使用 LLM 改写或扩展查询，生成更利于检索的查询版本

#### Scenario: 混合检索（向量 + BM25）
- **WHEN** 单一向量检索无法覆盖所有相关结果
- **THEN** 能实现向量检索与关键词检索（BM25）的混合策略，融合两种检索结果

#### Scenario: HyDE（假设性文档嵌入）
- **WHEN** 用户查询与文档表述风格差异大
- **THEN** 能使用 LLM 生成假设性回答，用该回答的向量去检索相关文档

### Requirement: Reranking 与上下文组装
学习者 SHALL 能对检索结果进行重排序，并将最优结果组装为 LLM 的上下文。

#### Scenario: 使用 Cross-encoder 重排序
- **WHEN** 初步检索返回 Top-K 结果
- **THEN** 能使用 Cohere Rerank 或 Voyage Rerank 对结果进行精排，提升相关性排序质量

#### Scenario: 上下文组装与引用溯源
- **WHEN** 重排序后的结果需要传给 LLM 生成回答
- **THEN** 能合理组装上下文（控制 Token 预算），生成的回答 MUST 包含引用来源信息

### Requirement: RAG 系统评估
学习者 SHALL 能使用评估框架量化 RAG 系统的检索和生成质量。

#### Scenario: 使用 RAGAS 评估框架
- **WHEN** 学习者需要量化 RAG 系统效果
- **THEN** 能使用 RAGAS 评估检索准确率、召回率、答案忠实度和答案相关性等指标
