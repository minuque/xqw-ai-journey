# AI 应用开发学习路径 - 探索讨论记录

> 日期：2026-03-02
> 背景：5年 Vue 前端经验 + Java 后端经验，转型 AI 应用开发（非算法方向）

## 个人定位

- **前端**：Vue3（主场不变）
- **后端**：Python + FastAPI（主力语言）
- **AI API**：Claude API 优先（Anthropic SDK）
- **学习节奏**：每天 2-3h，在职学习

## 已有能力迁移分析

| 已有能力 | 可迁移到 |
|---------|---------|
| Vue 5年（组件化思维、状态管理、API 对接） | AI 应用前端、Agent 状态机设计 |
| Java 后端（OOP、REST API、数据库） | Python 快速上手、FastAPI 开发 |
| 前端工程化（构建工具、包管理） | Python 项目管理（uv/poetry） |
| TypeScript 类型系统 | Python Type Hints、Pydantic |
| async/await 异步编程 | Python asyncio（几乎一致） |

## 学习路径总览（5 个阶段）

```
阶段1              阶段2              阶段3              阶段4              阶段5
Python 快速上手    Prompt 工程        RAG 系统           Agent 工作流       综合实战项目
(2-3周)           (2-3周)           (5-6周)            (5-6周)           (持续)
    │                 │                 │                  │                 │
    ▼                 ▼                 ▼                  ▼                 ▼
 能调 Claude API   能写出稳定可靠    能搭建完整         能设计多步骤       落地一个完整
 能写 FastAPI 服务  的 Prompt 体系    的知识问答系统      Agent 系统        AI 应用
```

---

## 阶段 1：Python + Claude API 快速上手（3 周）

### 第 1 周：Python 核心差异速通

重点抓 Java/JS → Python 的差异点：

| Java/JS 概念 | Python 对应 | 重点关注 |
|-------------|------------|---------|
| `npm/pnpm` | `uv`（推荐） | `uv init`、`uv add`、`uv run` |
| `node_modules` | `venv` 虚拟环境 | `uv venv` 自动管理 |
| `interface/type` | Type Hints | `def foo(name: str) -> dict:` |
| `class` | `dataclass` / `Pydantic` | Pydantic 在 AI 开发中极其重要 |
| `map/filter` | 列表推导式 | `[x for x in items if x > 0]` |
| `async/await` | `asyncio` | 语法几乎一样，概念直接迁移 |
| `try/catch` | `try/except` | 异常处理 |
| `装饰器(@)` | `decorator` | FastAPI 路由大量使用 |

### 第 2 周：FastAPI 核心

重点掌握：
- 路由、请求/响应模型（Pydantic）
- 依赖注入（FastAPI 的 `Depends`）
- 中间件、CORS 配置
- SSE 流式输出（AI 对话必备）

### 第 3 周：Claude API 实操

```
┌──────────┐   SSE Stream    ┌──────────────┐   Anthropic SDK  ┌───────────┐
│  Vue3    │ ◄─────────────► │  FastAPI     │ ◄──────────────► │ Claude    │
│  前端    │                 │  后端        │                  │ API       │
└──────────┘                 └──────────────┘                  └───────────┘
```

核心要掌握的 Claude API 特性：
- Messages API：基础对话
- Streaming：流式输出
- Tool Use：Function Calling（Agent 的基础）
- System Prompt：系统提示词设计
- Vision：图片理解能力

**产出物：一个带流式输出的 AI 聊天应用（Vue3 + FastAPI + Claude）**

---

## 阶段 2：Prompt 工程（2-3 周）

### 第 1 周：核心技巧

- System / User / Assistant 角色设计
- Few-shot prompting（给示例）
- Chain of Thought（引导推理）
- 结构化输出（JSON mode、Tool Use）

Claude 特有技巧：
- XML 标签结构化（Claude 对 `<tag>` 格式响应特别好）
- Prefill 技巧（预填充 Assistant 消息控制输出格式）
- Extended Thinking（利用思考过程提升复杂推理质量）

### 第 2 周：Tool Use 深入

连接 Prompt 工程和 Agent 开发的桥梁。

### 第 3 周：Prompt 管理实践

- Prompt 版本管理
- 评估体系
- 多场景适配

---

## 阶段 3：RAG 系统（5-6 周）

### 技术选型

| 组件 | 推荐方案 | 备选 |
|------|---------|------|
| Embedding | Voyage AI（Anthropic 推荐） | OpenAI Embedding |
| 向量数据库 | Chroma（入门）→ Qdrant（生产） | Milvus |
| 文档解析 | Unstructured / PyMuPDF | LlamaParse |
| 分块策略 | 语义分块 + 递归分块 | - |
| Reranking | Cohere Rerank / Voyage Rerank | - |
| LLM | Claude Sonnet（性价比）| Claude Opus（复杂场景）|

### 周计划

| 周次 | 主题 | 目标 |
|------|------|------|
| Week 1 | Embedding + 向量数据库基础 | 能把文档存进 Chroma 并检索 |
| Week 2 | 文档处理 pipeline | PDF/Markdown/网页 → 清洗 → 分块 → 向量化 |
| Week 3 | 检索优化（重点） | Query 改写、HyDE、混合检索（向量 + BM25） |
| Week 4 | Reranking + 上下文组装 | 重排序、上下文窗口管理、引用溯源 |
| Week 5 | 评估与调优 | RAGAS 框架、检索准确率/召回率评估 |
| Week 6 | 完整系统整合 | 端到端 RAG 应用 + 前端交互 |

**产出物：完整的知识库问答系统**

---

## 阶段 4：LangChain / LangGraph Agent 工作流（5-6 周）

### 核心概念

LangGraph 的状态机模型类比 Vue Router 导航守卫 + Vuex 状态管理：
- 每个节点是一个处理函数
- 边是条件路由

### 周计划

| 周次 | 主题 | 要点 |
|------|------|------|
| Week 1 | LangChain 基础 | LCEL 表达式、Prompt Template、Output Parser |
| Week 2 | Tool + Claude 集成 | 自定义工具、Claude Tool Use 在 LangChain 中的使用 |
| Week 3 | LangGraph 核心 | StateGraph、节点、边、条件路由、状态管理 |
| Week 4 | 高级模式 | 多 Agent 协作、子图、Human-in-the-loop |
| Week 5 | 持久化 + Memory | Checkpointer、长期记忆、对话历史管理 |
| Week 6 | 生产化 | LangSmith 追踪、错误处理、流式输出、部署 |

---

## 阶段 5：落地项目建议

### 项目 1（首推）：智能文档助手

- 场景：上传文档，基于文档内容问答
- 技术栈：Vue3 + FastAPI + Chroma + Claude
- 亮点：文档上传/预览/标注 UI + 引用溯源高亮
- 难度：⭐⭐⭐

### 项目 2：AI 代码 Review 助手

- 场景：接入 GitHub，自动 Review PR
- 技术栈：FastAPI + LangChain + GitHub API
- 亮点：解决日常工作痛点，可加入团队代码规范作为 RAG 知识库
- 难度：⭐⭐⭐⭐

### 项目 3：多步骤数据分析 Agent

- 场景：自然语言 → SQL 查询 → 图表 → 分析报告
- 技术栈：Vue3 + LangGraph + 数据库 + ECharts
- 亮点：前端可视化强项 + LangGraph 多步骤工作流
- 难度：⭐⭐⭐⭐⭐

### 项目 4：个人知识管理系统

- 场景：笔记/网页/PDF 自动整理、语义搜索、智能问答
- 技术栈：Vue3 + FastAPI + RAG + Agent
- 亮点：自己用得上，持续迭代动力强
- 难度：⭐⭐⭐⭐⭐

---

## 推荐资源

| 资源 | 用途 |
|------|------|
| [Anthropic Docs](https://docs.anthropic.com) | Claude API 官方文档，必读 |
| [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) | 官方示例代码库 |
| [LangChain 官方教程](https://python.langchain.com/docs/tutorials/) | LangChain/LangGraph 学习 |
| FastAPI 官方文档 | 写得非常好，推荐直接读 |
