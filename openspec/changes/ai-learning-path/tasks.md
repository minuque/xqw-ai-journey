# 学习任务清单

> 💡 **使用说明**
> - 按阶段顺序推进，完成一个阶段再开始下一个
> - 每个任务独立可完成，可以跳着做（标注依赖的除外）
> - 完成任务后打勾，并记录到当天的学习日记中

---

## 🚀 阶段 1: Python + FastAPI 基础

**目标**: 建立 Python 开发能力，掌握 FastAPI Web 服务开发

### 1.1 Python 环境与工具链

- [x] 安装 Python 3.12+ 和 uv 包管理工具
- [x] 使用 `uv init` 创建第一个项目，理解项目结构
- [x] 理解 pyproject.toml、uv.lock、虚拟环境的作用
- [x] 配置 VS Code Python 开发环境（插件、格式化、类型检查）

### 1.2 Python 语法快速上手

- [x] 练习 Type Hints：函数注解、变量注解、泛型
- [x] 练习列表推导式、字典推导式（对比 JS map/filter）
- [x] 理解装饰器原理（对比 JS Decorator 提案）
- [x] 学习 dataclass（对比 TypeScript class）
- [x] 理解 Python 的 None、True/False（对比 JS null/undefined）

### 1.3 Pydantic 数据模型

- [x] 定义第一个 BaseModel，理解运行时校验
- [x] 练习字段类型、默认值、可选字段
- [x] 练习嵌套模型、模型继承
- [x] 练习自定义 Validator（字段校验逻辑）
- [x] 练习模型序列化：model_dump()、model_dump_json()
- [x] 对比 Pydantic 与 TypeScript Zod

### 1.4 Python 异步编程

- [x] 理解 async/await 语法（对比 JS Promise）
- [x] 练习 asyncio.gather()（对比 Promise.all）
- [x] 理解事件循环机制（对比 JS Event Loop）
- [x] 练习异步上下文管理器（async with）
- [x] 对比 Python asyncio 与 JS async 的差异

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

## 🤖 阶段 2: LLM API 对接与本地部署

**目标**: 掌握通用 LLM API，实现云端+本地模型的灵活切换

### 2.1 OpenAI API 标准接口

- [ ] 注册 OpenAI 账号，获取 API Key（或使用第三方兼容服务）
- [ ] 安装 `openai` Python SDK
- [ ] 理解 OpenAI API 的标准结构（Chat Completions）
- [ ] 实现第一个 Chat API 调用（同步）
- [ ] 理解 messages 数组结构（role: system/user/assistant）
- [ ] 练习 system prompt 设计
- [ ] 测试不同模型（gpt-4o-mini、gpt-4o）

### 2.2 流式响应与多轮对话

- [ ] 理解 Streaming 工作原理（SSE 协议）
- [ ] 实现 OpenAI Streaming API 调用（stream=True）
- [ ] 通过 FastAPI StreamingResponse 转发流式响应
- [ ] 前端使用 EventSource 接收流式响应
- [ ] 实现打字机效果的 AI 回复界面
- [ ] 设计对话历史存储结构（messages 数组）
- [ ] 实现多轮对话上下文管理（累积 messages）
- [ ] 实现对话历史截断策略（Token 预算管理）

### 2.3 Claude API 高级特性

- [ ] 注册 Anthropic 账号，获取 API Key
- [ ] 安装 `anthropic` Python SDK
- [ ] 对比 Claude API 与 OpenAI API 的差异
- [ ] 学习 Claude Tool Use（函数调用）
- [ ] 定义工具 schema，实现工具调用循环
- [ ] 学习 Claude Vision（多模态）
- [ ] 实现图片上传与多模态对话
- [ ] 测试 Claude 特有功能（Extended Thinking、Prefill）

### 2.4 Ollama 本地模型部署

- [ ] 安装 Ollama（官方下载或 Docker）
- [ ] 理解 Ollama 工作原理（本地模型服务）
- [ ] 下载并运行第一个模型（qwen2.5:7b 或 llama3.2:3b）
- [ ] 学习 Ollama CLI 命令（ollama run、ollama list、ollama pull）
- [ ] 理解 Ollama 的 OpenAI 兼容接口
- [ ] 通过 OpenAI SDK 调用 Ollama 本地模型
- [ ] 测试不同本地模型（Qwen、Llama、Mistral）
- [ ] 对比本地模型与云端模型的效果和速度

### 2.5 模型切换与统一接口封装

- [ ] 设计统一的 LLM 调用接口（抽象层）
- [ ] 实现配置化的模型切换（配置文件或环境变量）
- [ ] 封装 OpenAI、Claude、Ollama 三种后端
- [ ] 实现统一的流式响应处理
- [ ] 实现统一的错误处理和重试机制
- [ ] 前端实现模型选择器（下拉菜单）
- [ ] 测试模型切换的无缝性

### 2.6 本地端到端联调

- [ ] 完整测试：Vue3 前端 → FastAPI 后端 → Ollama 本地模型
- [ ] 验证流式输出在本地模型下的表现
- [ ] 验证多轮对话在本地模型下的表现
- [ ] 优化本地模型的响应速度（GPU 加速、量化模型）
- [ ] 实现本地模型的健康检查（自动启动/重连）
- [ ] 编写本地部署文档（环境要求、启动步骤）

### ✅ 阶段 2 完成标志

- [ ] 完成一个支持云端+本地的 AI 聊天应用
- [ ] 支持 OpenAI、Claude、Ollama 三种后端
- [ ] 支持流式输出、多轮对话、模型切换
- [ ] 实现完整的本地端到端联调
- [ ] 沉淀学习笔记到 `specs/llm-api-integration/spec.md`

---

## 🎨 阶段 3: Prompt 工程与上下文管理

**目标**: 掌握实用 Prompt 技巧，为 RAG 系统做准备

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
- [ ] 学习 Claude 的上下文缓存机制（降低成本）
- [ ] 测试不同技巧的效果差异

### 3.4 上下文窗口管理

- [ ] 理解 Token 计算与限制
- [ ] 实现上下文长度估算（tiktoken 或 Claude API）
- [ ] 实现上下文截断策略（保留最新/最相关）
- [ ] 实现滑动窗口对话历史管理
- [ ] 测试不同截断策略对对话质量的影响

### 3.5 RAG Prompt 设计

- [ ] 学习 RAG Prompt 结构（系统提示 + 检索上下文 + 用户问题）
- [ ] 设计上下文拼接模板（文档来源标注）
- [ ] 实现"基于上下文回答"的提示工程
- [ ] 处理检索内容不足的情况（承认不知道）
- [ ] 实现引用来源的 Prompt 引导

### ✅ 阶段 3 完成标志

- [ ] 完成一个 RAG Prompt 模板库
- [ ] 掌握 Few-shot、CoT、结构化输出等核心技巧
- [ ] 理解上下文窗口管理策略
- [ ] 沉淀学习笔记到 `specs/prompt-engineering/spec.md`

---

## 📚 阶段 4: RAG 系统核心技术

**目标**: 从零搭建完整 RAG 系统，掌握知识库问答核心能力

### 4.1 Embedding 与向量检索基础

- [ ] 学习 Embedding 原理（文本向量化表示）
- [ ] 注册 Voyage AI，获取 API Key
- [ ] 使用 Voyage Embedding API 将文本向量化
- [ ] 理解余弦相似度计算原理
- [ ] 手写一个简单的向量检索（NumPy 实现）

### 4.2 Chroma 向量数据库

- [ ] 安装 Chroma 向量数据库
- [ ] 理解 Collection 概念（类比数据库表）
- [ ] 实现向量的增删改查操作
- [ ] 实现基于相似度的向量检索（top k）
- [ ] 学习元数据过滤（metadata filter）
- [ ] 实现持久化存储（本地文件）

### 4.3 文档处理与解析

- [ ] 安装 PyMuPDF（PDF 解析）
- [ ] 实现 PDF 文档解析，提取文本
- [ ] 实现 Markdown 文档解析
- [ ] 实现 TXT 文档解析
- [ ] 设计文档元数据结构（文件名、页码、时间戳）
- [ ] 实现文档上传接口（FastAPI）

### 4.4 文本分块策略

- [ ] 理解分块的重要性（检索粒度 vs 上下文完整性）
- [ ] 实现固定长度分块（Character Splitter）
- [ ] 实现递归分块（Recursive Splitter，按段落/句子）
- [ ] 实现分块重叠策略（Overlap，保证上下文连续）
- [ ] 为每个 chunk 添加元数据（来源文档、页码）
- [ ] 对比不同分块策略的效果

### 4.5 基础 RAG 流程实现

- [ ] 实现文档上传 → 分块 → 向量化 → 存储流程
- [ ] 实现用户提问 → 向量检索 → 获取 top k chunks
- [ ] 实现上下文拼接（chunk 内容 + 来源信息）
- [ ] 实现 Token 预算管理（控制上下文总长度）
- [ ] 将上下文 + 问题发送给 Claude 生成答案
- [ ] 测试基础 RAG 效果

### 4.6 引用溯源

- [ ] 在 RAG 响应中返回 chunk 来源信息
- [ ] 实现引用来源的格式化输出（文档名、页码）
- [ ] 通过 Prompt 引导 Claude 标注引用
- [ ] 前端实现引用高亮显示（可选）
- [ ] 测试引用准确性

### 4.7 检索优化

- [ ] 实现 Query 改写（使用 Claude 优化用户查询）
- [ ] 实现 HyDE（生成假设性答案用于检索）
- [ ] 集成 Voyage Rerank 重排序（提升检索精度）
- [ ] 实现多路检索（同时检索多个知识库）
- [ ] 对比优化前后的检索效果

### 4.8 知识库管理

- [ ] 设计知识库结构（一个知识库 = 一个 Collection）
- [ ] 实现知识库创建、删除、列表查询
- [ ] 实现知识库文档管理（添加、删除文档）
- [ ] 实现知识库统计（文档数、chunk 数）
- [ ] 前端实现知识库切换功能

### ✅ 阶段 4 完成标志

- [ ] 完成一个功能完整的知识库问答 API
- [ ] 支持文档上传、向量检索、引用溯源
- [ ] 实现至少一种检索优化技术
- [ ] 具备知识库管理能力
- [ ] 沉淀学习笔记到 `specs/rag-system/spec.md`

---

## 🤖 阶段 5: LangChain 实战与应用集成

**目标**: 使用 LangChain 重构 RAG 系统，构建完整知识库应用

### 5.1 LangChain 核心概念

- [ ] 安装 LangChain 和 LangChain-Anthropic
- [ ] 理解 LangChain 架构（Chain、LLM、Memory）
- [ ] 学习 LCEL（管道操作符 `|`）
- [ ] 学习 Prompt Template（模板变量）
- [ ] 实现第一个 LCEL 链：Prompt → LLM → Output

### 5.2 LangChain + Claude 集成

- [ ] 使用 ChatAnthropic 封装 Claude API
- [ ] 实现流式输出（LangChain Streaming）
- [ ] 集成 Prompt Template 与 Claude
- [ ] 实现结构化输出解析（Output Parser）
- [ ] 测试与原生 API 的对比

### 5.3 使用 LangChain 重构 RAG

- [ ] 使用 LangChain 的 VectorStore 封装 Chroma
- [ ] 使用 LangChain 的 Embeddings 封装 Voyage
- [ ] 使用 LangChain 的 Document Loader 加载文档
- [ ] 使用 LangChain 的 Text Splitter 分块
- [ ] 使用 RetrievalQA Chain 实现 RAG
- [ ] 对比手写 RAG 与 LangChain RAG 的差异

### 5.4 对话历史管理（Memory）

- [ ] 学习 LangChain Memory 概念
- [ ] 实现 ConversationBufferMemory（缓存所有历史）
- [ ] 实现 ConversationBufferWindowMemory（滑动窗口）
- [ ] 实现 ConversationSummaryMemory（摘要压缩）
- [ ] 集成 Memory 到 RAG Chain
- [ ] 实现多轮对话的知识库问答

### 5.5 Agent 与 Tool 集成

- [ ] 学习 LangChain Agent 概念（ReAct）
- [ ] 使用 `@tool` 装饰器定义自定义工具
- [ ] 定义"知识库检索"工具
- [ ] 定义"网络搜索"工具（可选）
- [ ] 定义"计算器"工具（可选）
- [ ] 创建 Agent 实现多工具调用
- [ ] 测试 Agent 在复杂问答中的表现

### 5.6 Streamlit UI 构建

- [ ] 安装 Streamlit
- [ ] 创建基本的 Streamlit 应用框架
- [ ] 实现文档上传界面
- [ ] 实现知识库选择/切换界面
- [ ] 实现聊天界面（st.chat_message）
- [ ] 实现流式输出显示
- [ ] 实现引用来源展示
- [ ] 优化 UI 美观度

### 5.7 知识库管理功能

- [ ] 实现知识库创建界面
- [ ] 实现知识库删除功能
- [ ] 实现知识库文档列表展示
- [ ] 实现文档删除功能
- [ ] 实现知识库统计信息展示
- [ ] 实现知识库导出/导入（可选）

### 5.8 系统优化与完善

- [ ] 实现错误处理和用户友好提示
- [ ] 实现 Loading 状态展示
- [ ] 优化长文档处理性能
- [ ] 实现配置文件管理（API Key、模型选择）
- [ ] 编写部署文档（本地运行指南）

### ✅ 阶段 5 完成标志

- [ ] 完成一个 LangChain 驱动的知识库应用
- [ ] 具备完整的 Streamlit UI
- [ ] 支持多轮对话和知识库管理
- [ ] 代码结构清晰、易于维护
- [ ] 沉淀学习笔记到 `specs/langchain-application/spec.md`

---

## 🏆 最终冲刺：Langchain-Chatchat MVP

**目标**：构建一个类似 Langchain-Chatchat 的本地知识库问答系统

### 项目规划

- [ ] 确定项目名称和定位
- [ ] 编写项目需求文档（功能清单、技术栈）
- [ ] 设计系统架构图
- [ ] 设计数据库 Schema（如需要）
- [ ] 规划开发里程碑

### 核心功能实现

- [ ] 完善文档处理模块（支持更多格式）
- [ ] 完善知识库管理模块（权限、分类）
- [ ] 优化 RAG 效果（调优参数、A/B 测试）
- [ ] 实现高级功能：对话导出、搜索历史
- [ ] 实现配置管理：模型切换、参数调整

### UI/UX 优化

- [ ] 设计统一的 UI 风格
- [ ] 优化响应速度（异步处理）
- [ ] 实现移动端适配（响应式设计）
- [ ] 增加用户引导和帮助文档
- [ ] 实现暗色主题（可选）

### 测试与优化

- [ ] 准备测试数据集（不同类型文档）
- [ ] 进行端到端测试
- [ ] 性能优化（大文档、高并发）
- [ ] 修复 Bug 和边界情况
- [ ] 收集用户反馈并改进

### 文档与部署

- [ ] 编写 README（项目介绍、快速开始）
- [ ] 编写开发文档（架构说明、API 文档）
- [ ] 编写部署文档（环境要求、配置说明）
- [ ] 录制 Demo 视频（可选）
- [ ] 发布到 GitHub（开源）

### ✅ 最终完成标志

- [ ] 完成一个可演示、可落地的知识库问答系统
- [ ] 功能完整：文档上传、知识库管理、智能问答、引用溯源
- [ ] UI 美观易用，响应流畅
- [ ] 代码质量高，文档完善
- [ ] 成功部署并可供他人使用
- [ ] 总结学习历程，输出学习报告
