# AI 学习路径 - 阶段进度看板

> **当前聚焦**: 阶段 1 - Python + FastAPI 基础
> **总体进度**: 0/5 阶段完成 (0%)

---

## 🎯 阶段概览

| 阶段 | 名称 | 进度 | 状态 | 核心产出 |
|------|------|------|------|----------|
| 1 | Python + FastAPI 基础 | [░░░░░░░░░░] 0% | 🟢 进行中 | FastAPI CRUD + SSE 流式 |
| 2 | Claude API 对接 | [░░░░░░░░░░] 0% | ⚪ 未开始 | AI 聊天应用 |
| 3 | Prompt 工程 | [░░░░░░░░░░] 0% | ⚪ 未开始 | 数据提取工具 |
| 4 | RAG 系统 | [░░░░░░░░░░] 0% | ⚪ 未开始 | 知识库问答系统 |
| 5 | Agent 工作流 | [░░░░░░░░░░] 0% | ⚪ 未开始 | 多 Agent 应用 |

---

## 📊 阶段 1: Python + FastAPI 基础

**进度**: 0/15 任务完成 (0%)
**知识沉淀**: `specs/python-fastapi-foundation/spec.md`

### 核心里程碑
- [ ] Python 环境搭建（uv 工具链）
- [ ] Pydantic 数据模型掌握
- [ ] FastAPI 基础路由实现
- [ ] 异步编程深入理解
- [ ] SSE 流式输出实现
- [ ] Vue3 前后端联调完成

---

## 📊 阶段 2: LLM API 对接与本地部署

**进度**: 0/15 任务完成 (0%)
**知识沉淀**: `specs/llm-api-integration/spec.md`

### 核心里程碑
- [ ] OpenAI API 标准接口掌握
- [ ] 流式响应与多轮对话
- [ ] Claude API 高级特性（Tool Use、Vision）
- [ ] Ollama 本地模型部署
- [ ] 模型切换与统一接口封装
- [ ] 阶段产出：支持云端+本地的 AI 聊天应用

---

## 📊 阶段 3: Prompt 工程与上下文管理

**进度**: 0/10 任务完成 (0%)
**知识沉淀**: `specs/prompt-engineering/spec.md`

### 核心里程碑
- [ ] Few-shot & CoT 核心技巧
- [ ] 结构化输出（JSON、Pydantic）
- [ ] Claude 特有技巧（XML、Prefill）
- [ ] 上下文窗口管理与截断策略
- [ ] RAG Prompt 设计（上下文拼接）
- [ ] 阶段产出：RAG 专用 Prompt 模板

---

## 📊 阶段 4: RAG 系统核心技术

**进度**: 0/18 任务完成 (0%)
**知识沉淀**: `specs/rag-system/spec.md`

### 核心里程碑
- [ ] Embedding 与向量检索原理
- [ ] 文档解析（PDF、Markdown、HTML）
- [ ] 文本分块策略与优化
- [ ] 向量数据库（Chroma）集成
- [ ] 基础 RAG 流程实现
- [ ] 检索优化（HyDE、Rerank）
- [ ] 引用溯源与元数据管理
- [ ] 阶段产出：完整的知识库问答 API

---

## 📊 阶段 5: LangChain 实战与应用集成

**进度**: 0/15 任务完成 (0%)
**知识沉淀**: `specs/langchain-application/spec.md`

### 核心里程碑
- [ ] LangChain 核心概念（LCEL、Chain）
- [ ] LangChain + Claude API 集成
- [ ] 使用 LangChain 重构 RAG 系统
- [ ] 对话历史管理（Memory）
- [ ] Agent + Tool 集成
- [ ] Streamlit UI 构建
- [ ] 知识库管理功能
- [ ] 阶段产出：LangChain 驱动的知识库应用

---

## 🏆 最终冲刺：Langchain-Chatchat MVP

### 项目目标
**构建一个类似 Langchain-Chatchat 的本地知识库问答系统**

### 核心功能
- ✅ 文档上传与解析（PDF、Markdown、TXT）
- ✅ 知识库管理（创建、删除、切换）
- ✅ 智能问答（基于 RAG）
- ✅ 多轮对话（上下文记忆）
- ✅ 引用溯源（显示来源文档）
- ✅ Streamlit Web UI

### 技术架构
```
前端: Streamlit (简单快速)
后端: FastAPI (API 服务)
LLM: Claude API (替代 ChatGLM)
框架: LangChain (RAG 编排)
向量库: Chroma (本地存储)
Embedding: Voyage AI (云端) 或 本地模型
```

### 实战任务
- [ ] 完成需求文档和架构设计
- [ ] 实现文档处理模块
- [ ] 实现知识库管理模块
- [ ] 实现 RAG 问答核心
- [ ] 实现多轮对话功能
- [ ] 构建 Streamlit UI
- [ ] 完整测试与优化
- [ ] 编写部署文档

### ✅ 最终完成标志
- [ ] 完成一个可演示的知识库问答系统
- [ ] 支持多种文档格式上传
- [ ] 问答效果良好，引用准确
- [ ] UI 美观易用
- [ ] 代码规范，文档完善
