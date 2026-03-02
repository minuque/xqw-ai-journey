## Context

学习者背景：5 年 Vue 前端开发经验，具备 Java 后端开发经验，TypeScript 熟练。目标是转型 AI 应用开发（非算法/模型训练方向），以 Python 作为主力后端语言，优先对接 Claude API（Anthropic）。

当前状态：零 Python 基础、零 AI 应用开发经验，但具备强大的可迁移技能（前端工程化、API 对接、异步编程、状态管理）。

约束条件：每天可投入 2-3 小时学习，在职状态，需要高效利用时间。

## Goals / Non-Goals

**Goals:**

- 建立从 Java/JS 到 Python 的快速迁移路径，避免重复学习已掌握的通用编程概念
- 以 Claude API 为核心 LLM 接口，同时设计为可适配多模型
- 每个阶段产出可运行的 demo 项目，确保学习效果可验证
- 掌握 RAG 全链路，从文档处理到检索优化到评估
- 掌握 LangGraph 状态机式 Agent 工作流设计
- 充分利用 Vue3 前端优势，在实战项目中构建优质 AI 交互界面

**Non-Goals:**

- 不学习模型训练、微调、算法原理（非算法方向）
- 不深入机器学习/深度学习理论
- 不追求 Python 语言专家水平，够用即可
- 暂不考虑 TypeScript AI 生态（LangChain.js / Vercel AI SDK），后期再补强
- 不涉及模型部署/推理服务搭建（使用云端 API）

## Decisions

### 1. Python 包管理选择 uv 而非 pip/poetry

**决定**：使用 `uv` 作为 Python 包管理和环境管理工具。

**理由**：
- 速度极快（Rust 编写），对标 pnpm 的体验
- 统一管理虚拟环境 + 包安装 + 脚本运行
- 对前端工程师来说概念最接近 pnpm/bun

**备选**：pip + venv（太原始）、poetry（较慢、配置复杂）、conda（偏数据科学）

### 2. Web 框架选择 FastAPI 而非 Django/Flask

**决定**：使用 FastAPI 作为后端框架。

**理由**：
- 原生 async/await，与 JS 异步模型一致
- 自动生成 OpenAPI 文档
- Pydantic 类型系统类比 TypeScript interface
- SSE 流式输出支持好（AI 对话必备）
- 学习曲线低，写法接近 Express/Spring Boot

**备选**：Flask（太简陋、无类型）、Django（太重、不适合 API-first）

### 3. LLM API 优先 Claude 而非 OpenAI

**决定**：以 Claude API（Anthropic SDK）为主要 LLM 接口。

**理由**：
- 用户明确指定
- API 设计简洁，Tool Use 原生支持
- 长上下文支持好，适合 RAG 场景
- 代码能力强，适合 Agent 场景

**适配策略**：抽象 LLM 调用层，便于后期接入其他模型（OpenAI、本地模型等）

### 4. 向量数据库分阶段选择

**决定**：学习阶段用 Chroma（轻量），生产级项目用 Qdrant。

**理由**：
- Chroma：纯 Python、零配置、适合快速原型
- Qdrant：性能好、API 友好、Docker 部署简单
- 分阶段降低认知负荷

**备选**：Milvus（太重）、Pinecone（云服务、有成本）、Weaviate（复杂）

### 5. 阶段式渐进学习而非项目驱动一步到位

**决定**：5 个阶段渐进式学习，每阶段有独立产出物。

**理由**：
- 避免一开始就面对过多新概念
- 每阶段产出物可独立验证学习效果
- 前一阶段的产出物可作为后一阶段的基础
- 适合在职每天 2-3 小时的碎片化学习节奏

## Risks / Trade-offs

- **[Python 深度不足]** → 只学 AI 应用开发所需的 Python 子集，可能在调试复杂问题时遇到困难。缓解：遇到时再按需深入，不提前过度学习。

- **[Claude API 单一依赖]** → 只学 Claude API 可能限制就业选择。缓解：设计抽象层，后期补充 OpenAI API 对接（差异很小）。

- **[学习周期可能延长]** → 16-20 周是理想估计，实际可能因工作繁忙而延长。缓解：每阶段独立可用，即使中断也有阶段性成果。

- **[技术栈快速迭代]** → AI 工具链变化很快，学习内容可能过时。缓解：重点学习核心概念（RAG 原理、Agent 模式），而非特定框架 API。
