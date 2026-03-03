# 学习任务清单

> 💡 **使用说明**
> - 按阶段顺序推进，完成一个阶段再开始下一个
> - 每个任务独立可完成，可以跳着做（标注依赖的除外）
> - 完成任务后打勾，并记录到当天的学习日记中

---

## 🚀 阶段 1: Python + FastAPI 基础

**目标**: 建立 Python 开发能力，掌握 FastAPI Web 服务开发

### 1.1 Python 环境与工具链

- [ ] 安装 Python 3.12+ 和 uv 包管理工具
- [ ] 使用 `uv init` 创建第一个项目，理解项目结构
- [ ] 理解 pyproject.toml、uv.lock、虚拟环境的作用
- [ ] 配置 VS Code Python 开发环境（插件、格式化、类型检查）

### 1.2 Python 语法快速上手

- [ ] 练习 Type Hints：函数注解、变量注解、泛型
- [ ] 练习列表推导式、字典推导式（对比 JS map/filter）
- [ ] 理解装饰器原理（对比 JS Decorator 提案）
- [ ] 学习 dataclass（对比 TypeScript class）
- [ ] 理解 Python 的 None、True/False（对比 JS null/undefined）

### 1.3 Pydantic 数据模型

- [ ] 定义第一个 BaseModel，理解运行时校验
- [ ] 练习字段类型、默认值、可选字段
- [ ] 练习嵌套模型、模型继承
- [ ] 练习自定义 Validator（字段校验逻辑）
- [ ] 练习模型序列化：model_dump()、model_dump_json()
- [ ] 对比 Pydantic 与 TypeScript Zod

### 1.4 Python 异步编程

- [ ] 理解 async/await 语法（对比 JS Promise）
- [ ] 练习 asyncio.gather()（对比 Promise.all）
- [ ] 理解事件循环机制（对比 JS Event Loop）
- [ ] 练习异步上下文管理器（async with）
- [ ] 对比 Python asyncio 与 JS async 的差异

### 1.5 FastAPI 基础开发

- [ ] 创建第一个 FastAPI 应用（Hello World）
- [ ] 实现 GET 路由：路径参数、查询参数
- [ ] 实现 POST 路由：请求体、Pydantic 模型校验
- [ ] 实现 PUT/DELETE 路由，完成完整 CRUD
- [ ] 理解 FastAPI 自动生成的 OpenAPI 文档（/docs）
- [ ] 配置 CORS 中间件，允许前端跨域请求

### 1.6 FastAPI 进阶特性

- [ ] 学习依赖注入（Depends）：数据库连接、认证依赖
- [ ] 学习 FastAPI 中间件：请求日志、异常处理
- [ ] 实现文件上传接口（UploadFile）
- [ ] 实现 SSE 流式输出（StreamingResponse）
- [ ] 实现 WebSocket 端点（可选，了解即可）

### 1.7 前后端联调

- [ ] 创建 Vue3 + Vite + TypeScript 前端项目
- [ ] 配置 Axios，实现与 FastAPI 后端的跨域通信
- [ ] 前端实现 TODO 列表界面，调用后端 CRUD API
- [ ] 测试 SSE 流式接口的前端接收（EventSource）

### ✅ 阶段 1 完成标志

- [ ] 完成一个完整的 FastAPI + Vue3 TODO 应用
- [ ] 包含 CRUD 操作、SSE 流式输出
- [ ] 代码规范、类型完整、文档清晰
- [ ] 沉淀学习笔记到 `specs/python-fastapi-foundation/spec.md`

---

## 🤖 阶段 2: Claude API 对接

**目标**: 掌握 Claude API 完整使用，实现 AI 对话应用

### 2.1 Claude API 基础

- [ ] 注册 Anthropic 账号，获取 API Key
- [ ] 安装 `anthropic` Python SDK
- [ ] 实现第一个 Messages API 调用（同步）
- [ ] 理解 Claude 的 messages 数组结构（role、content）
- [ ] 练习 system prompt 设计（角色、约束）
- [ ] 测试不同模型（claude-3-5-sonnet、claude-3-5-haiku）

### 2.2 流式响应

- [ ] 理解 Streaming 工作原理（SSE 协议）
- [ ] 实现 Claude Streaming API 调用
- [ ] 通过 FastAPI StreamingResponse 转发流式响应
- [ ] 前端使用 EventSource 接收流式响应
- [ ] 实现打字机效果的 AI 回复界面

### 2.3 多轮对话

- [ ] 设计对话历史存储结构（messages 数组）
- [ ] 实现多轮对话上下文管理（累积 messages）
- [ ] 实现对话历史截断策略（Token 预算管理）
- [ ] 实现对话重置、删除功能
- [ ] 前端实现对话列表、对话切换

### 2.4 Tool Use (函数调用)

- [ ] 学习 Claude Tool Use 工作原理（tool_use / tool_result）
- [ ] 定义第一个工具 schema（get_weather）
- [ ] 实现工具调用循环：LLM 请求 → 执行工具 → 返回结果 → LLM 继续
- [ ] 实现多个工具（搜索、计算器、数据查询）
- [ ] 实现工具调用的前端可视化（显示工具调用过程）

### 2.5 Vision 多模态

- [ ] 学习 Claude Vision 的 content 数组结构
- [ ] 实现图片上传接口（base64 编码）
- [ ] 实现图片 + 文本的多模态对话
- [ ] 测试图片理解、OCR、图表分析场景
- [ ] 前端实现图片上传与预览

### ✅ 阶段 2 完成标志

- [ ] 完成一个功能完整的 AI 聊天应用
- [ ] 支持流式输出、多轮对话、Tool Use、Vision
- [ ] 前端界面美观、交互流畅
- [ ] 沉淀学习笔记到 `specs/claude-api-integration/spec.md`

---

## 🎨 阶段 3: Prompt 工程

**目标**: 系统掌握 Prompt 设计技巧，提升 AI 输出质量

### 3.1 核心 Prompt 技巧

- [ ] 练习 Zero-shot：清晰指令设计
- [ ] 练习 Few-shot：提供示例引导输出
- [ ] 练习 Chain of Thought (CoT)：分步推理
- [ ] 练习角色扮演：通过 system prompt 设定角色
- [ ] 练习输出格式控制：Markdown、JSON、表格

### 3.2 结构化输出

- [ ] 通过 Prompt 设计获取 JSON 输出
- [ ] 通过 Tool Use 强制结构化输出
- [ ] 使用 Pydantic 模型定义输出结构
- [ ] 实现输出校验与重试机制
- [ ] 对比两种方式的优劣

### 3.3 Claude 特有技巧

- [ ] 学习 XML 标签结构化（&lt;document&gt;、&lt;thinking&gt;）
- [ ] 学习 Prefill 技巧（assistant 消息预填充）
- [ ] 学习 Extended Thinking（长思维链）
- [ ] 学习 Claude 的上下文缓存机制
- [ ] 测试不同技巧的效果差异

### 3.4 Prompt 管理

- [ ] 设计 Prompt 模板管理方案（文件、数据库）
- [ ] 实现 Prompt 变量替换（Jinja2 或自定义）
- [ ] 设计 Prompt 版本管理方案
- [ ] 建立 Prompt 效果评估流程
- [ ] 记录 Prompt 迭代历史

### 3.5 实战练习

- [ ] 实现一个数据提取工具（从非结构化文本提取结构化数据）
- [ ] 实现一个文本分类工具（情感分析、意图识别）
- [ ] 实现一个文本生成工具（邮件、文章、代码注释）
- [ ] 对比不同 Prompt 设计的效果差异

### ✅ 阶段 3 完成标志

- [ ] 完成一个 Prompt 管理工具或数据提取工具
- [ ] 掌握 Few-shot、CoT、结构化输出等核心技巧
- [ ] 建立 Prompt 迭代与评估的方法论
- [ ] 沉淀学习笔记到 `specs/prompt-engineering/spec.md`

---

## 📚 阶段 4: RAG 系统

**目标**: 从零搭建完整 RAG 系统，掌握知识库问答

### 4.1 Embedding 与向量检索

- [ ] 学习 Embedding 原理（向量化表示）
- [ ] 注册 Voyage AI，获取 API Key
- [ ] 使用 Voyage Embedding API 将文本向量化
- [ ] 安装 Chroma 向量数据库
- [ ] 实现向量的增删改查操作
- [ ] 实现基于余弦相似度的向量检索

### 4.2 文档处理

- [ ] 安装 Unstructured/PyMuPDF 文档解析库
- [ ] 实现 PDF 文档解析，提取文本
- [ ] 实现 Markdown/HTML 文档解析
- [ ] 实现文档上传接口（批量处理）
- [ ] 设计文档元数据存储结构（标题、作者、时间）

### 4.3 分块策略

- [ ] 理解分块的重要性（检索粒度、上下文完整性）
- [ ] 实现固定长度分块（Character Splitter）
- [ ] 实现递归分块（Recursive Splitter）
- [ ] 实现语义分块（Semantic Splitter）
- [ ] 实现分块重叠策略（Overlap）
- [ ] 对比不同分块策略的效果

### 4.4 基础 RAG 实现

- [ ] 实现基础 RAG 流程：用户提问 → 向量检索 → 拼接上下文 → LLM 生成
- [ ] 实现 Token 预算管理（控制上下文长度）
- [ ] 实现引用来源标注（返回 chunk 来源文档）
- [ ] 前端实现引用溯源高亮显示
- [ ] 测试基础 RAG 的效果

### 4.5 检索优化

- [ ] 实现 Query 改写（使用 Claude 优化用户查询）
- [ ] 实现 HyDE（生成假设性文档用于检索）
- [ ] 实现混合检索（向量检索 + BM25 关键词检索）
- [ ] 集成 Cohere/Voyage Rerank 重排序
- [ ] 对比优化前后的检索效果

### 4.6 RAG 评估

- [ ] 安装 RAGAS 评估框架
- [ ] 设计评估数据集（问题、参考答案、参考上下文）
- [ ] 评估检索准确率、召回率
- [ ] 评估答案忠实度、相关性
- [ ] 基于评估结果调优参数

### 4.7 向量数据库升级

- [ ] 安装 Qdrant（Docker 部署）
- [ ] 迁移 Chroma 数据到 Qdrant
- [ ] 学习 Qdrant 的高级特性（过滤、分组）
- [ ] 对比 Chroma 与 Qdrant 的性能差异

### ✅ 阶段 4 完成标志

- [ ] 完成一个功能完整的知识库问答系统
- [ ] 支持文档上传、向量检索、引用溯源
- [ ] 实现检索优化（Query 改写、Rerank）
- [ ] 建立 RAG 评估方法论
- [ ] 沉淀学习笔记到 `specs/rag-system/spec.md`

---

## 🤖 阶段 5: Agent 工作流

**目标**: 掌握 LangChain/LangGraph，构建复杂 Agent 系统

### 5.1 LangChain 基础

- [ ] 安装 LangChain 和 LangChain-Anthropic
- [ ] 学习 LCEL（管道操作符 `|`）
- [ ] 学习 Prompt Template（模板变量）
- [ ] 学习 Output Parser（结构化输出解析）
- [ ] 实现第一个 LCEL 链：Prompt → LLM → Parser

### 5.2 LangChain Tool 集成

- [ ] 使用 `@tool` 装饰器定义自定义工具
- [ ] 实现工具描述、类型化输入输出
- [ ] 集成 Claude 的 Tool Use 到 LangChain
- [ ] 实现 ReAct Agent（思考 → 行动 → 观察循环）
- [ ] 测试多工具场景（搜索、计算、数据库查询）

### 5.3 LangGraph 核心概念

- [ ] 学习 LangGraph 的状态图模型（StateGraph）
- [ ] 定义状态类型（TypedDict / Pydantic）
- [ ] 实现节点函数（处理状态转换）
- [ ] 实现边（连接节点）
- [ ] 实现条件路由（根据状态决定下一步）

### 5.4 LangGraph 高级模式

- [ ] 实现子图（Subgraph）：将复杂流程分解
- [ ] 实现循环节点（Loop）：重试、多轮优化
- [ ] 实现并行节点（Parallel）：同时执行多个任务
- [ ] 实现 Human-in-the-loop：人工审核节点
- [ ] 配置 Checkpointer 实现状态持久化

### 5.5 多 Agent 协作

- [ ] 设计多 Agent 架构（Researcher、Writer、Reviewer）
- [ ] 实现 Agent 间通信（共享状态）
- [ ] 实现 Agent 路由（Supervisor Agent）
- [ ] 实现 Agent 协作流程（分工、汇总）
- [ ] 测试多 Agent 协作的效果

### 5.6 监控与调试

- [ ] 注册 LangSmith，配置 API Key
- [ ] 集成 LangSmith 追踪（自动记录调用链）
- [ ] 学习 LangSmith 可视化界面（调用链、Token 用量）
- [ ] 使用 LangSmith 调试 Agent 问题
- [ ] 建立 Agent 性能监控方案

### ✅ 阶段 5 完成标志

- [ ] 完成一个复杂的 Agent 工作流应用
- [ ] 实现多 Agent 协作或 Human-in-the-loop
- [ ] 使用 LangSmith 监控与调试
- [ ] 沉淀学习笔记到 `specs/agent-workflow/spec.md`

---

## 🏆 最终冲刺：综合实战项目

### 项目方向选择

从以下方向中选择 1 个，综合运用所有学到的技能：

**选项 A: 智能文档助手**
- 功能：文档上传、知识库问答、文档摘要、多文档对比
- 技术：RAG + Tool Use + 流式输出

**选项 B: 代码 Review 助手**
- 功能：代码分析、问题检测、优化建议、测试生成
- 技术：Claude Code 能力 + Prompt 工程 + Agent 工作流

**选项 C: 数据分析 Agent**
- 功能：自然语言查询数据库、生成图表、数据洞察
- 技术：Tool Use + LangGraph + 数据可视化

**选项 D: 个人知识管理系统**
- 功能：笔记管理、知识图谱、智能推荐、双向链接
- 技术：RAG + Embedding + Graph + Claude

### 实战任务

- [ ] 确定项目方向，输出需求文档
- [ ] 完成架构设计和技术选型
- [ ] 实现核心功能 MVP
- [ ] 实现完整的前端交互界面（发挥 Vue3 优势）
- [ ] 测试、优化、完善文档
- [ ] 部署上线（可选）

### ✅ 最终完成标志

- [ ] 完成一个可演示、可落地的 AI 应用
- [ ] 代码质量高、文档完善
- [ ] 总结学习历程，输出学习报告
