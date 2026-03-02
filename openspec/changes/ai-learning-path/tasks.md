## 1. Python 环境搭建与语法基础（第 1 周）

- [ ] 1.1 安装 Python 3.12+ 和 uv 包管理工具，配置开发环境（VS Code + Python 插件）
- [ ] 1.2 使用 uv init 创建第一个 Python 项目，熟悉 pyproject.toml、uv.lock、虚拟环境结构
- [ ] 1.3 练习 Python 核心语法差异：Type Hints、列表推导式、装饰器、dataclass
- [ ] 1.4 练习 Pydantic BaseModel：定义数据模型、字段验证、嵌套模型、模型序列化
- [ ] 1.5 练习 Python 异步编程：async/await、asyncio 基础、与 JS 异步模型对比

## 2. FastAPI Web 服务开发（第 2 周）

- [ ] 2.1 创建 FastAPI 项目，实现基础 CRUD API（GET/POST/PUT/DELETE）
- [ ] 2.2 掌握 FastAPI 依赖注入（Depends）、中间件、CORS 配置
- [ ] 2.3 实现 SSE 流式输出端点（StreamingResponse），为 AI 对话做准备
- [ ] 2.4 搭建 Vue3 前端项目，实现与 FastAPI 后端的跨域通信

## 3. Claude API 对接（第 3 周）

- [ ] 3.1 注册 Anthropic API，安装 anthropic Python SDK，完成基础 Messages API 调用
- [ ] 3.2 实现 Claude Streaming 流式调用，通过 FastAPI SSE 转发到前端
- [ ] 3.3 实现多轮对话上下文管理（messages 数组维护）
- [ ] 3.4 实现 Claude Tool Use：定义工具 schema、处理 tool_use/tool_result 消息循环
- [ ] 3.5 实现 Claude Vision：图片上传 + base64 编码 + 多模态对话
- [ ] 3.6 **阶段产出**：完成带流式输出的 AI 聊天应用（Vue3 + FastAPI + Claude）

## 4. Prompt 工程核心技巧（第 4-5 周）

- [ ] 4.1 练习 Few-shot prompting：设计多个场景的示例引导 Prompt
- [ ] 4.2 练习 Chain of Thought：设计分步推理 Prompt，对比有无 CoT 的效果差异
- [ ] 4.3 练习结构化输出：通过 Prompt 设计和 Tool Use 两种方式获取稳定 JSON 输出
- [ ] 4.4 练习 Claude 特有技巧：XML 标签结构化、Prefill 预填充、Extended Thinking
- [ ] 4.5 实践 System Prompt 设计：角色设定、行为边界、输出格式控制

## 5. Prompt 管理与评估（第 6 周）

- [ ] 5.1 设计 Prompt 版本管理方案，记录 Prompt 迭代历史
- [ ] 5.2 设计评估用例集，建立 Prompt 效果对比测试流程
- [ ] 5.3 **阶段产出**：基于 Tool Use 的结构化数据提取工具，或 Prompt 管理小工具

## 6. RAG 基础：Embedding 与向量数据库（第 7-8 周）

- [ ] 6.1 学习 Embedding 原理，调用 Voyage AI（或 OpenAI）Embedding API 将文本向量化
- [ ] 6.2 安装 Chroma，完成向量数据的增删改查和相似性搜索操作
- [ ] 6.3 使用 Unstructured/PyMuPDF 解析 PDF 文档，提取结构化文本
- [ ] 6.4 实现递归分块策略，控制块大小和重叠，处理 Markdown/HTML 格式文档

## 7. RAG 进阶：检索优化（第 9-10 周）

- [ ] 7.1 实现 Query 改写与扩展：使用 Claude 改写用户查询以提升检索效果
- [ ] 7.2 实现 HyDE（假设性文档嵌入）：生成假设性回答用于向量检索
- [ ] 7.3 实现混合检索：向量检索 + BM25 关键词检索结果融合
- [ ] 7.4 集成 Cohere/Voyage Rerank 实现检索结果重排序
- [ ] 7.5 实现上下文组装：Token 预算管理 + 引用来源标注

## 8. RAG 系统整合与评估（第 11-12 周）

- [ ] 8.1 使用 RAGAS 框架评估 RAG 系统：检索准确率、召回率、答案忠实度
- [ ] 8.2 基于评估结果调优分块策略和检索参数
- [ ] 8.3 构建完整的 RAG 前端界面：文档上传、问答交互、引用溯源高亮
- [ ] 8.4 **阶段产出**：完整的知识库问答系统（Vue3 + FastAPI + Chroma + Claude）

## 9. LangChain 基础与 Tool 集成（第 13-14 周）

- [ ] 9.1 学习 LangChain 核心抽象：LCEL 管道操作符、Prompt Template、Output Parser
- [ ] 9.2 集成 Claude 到 LangChain：配置 ChatAnthropic，使用 Tool Use 和 Streaming
- [ ] 9.3 使用 @tool 装饰器定义自定义工具，实现工具描述和类型化输入
- [ ] 9.4 构建基础 ReAct Agent：LLM 思考 → 选择工具 → 执行 → 观察循环

## 10. LangGraph 状态图核心（第 15-16 周）

- [ ] 10.1 学习 LangGraph 核心概念：StateGraph、节点、边、状态定义
- [ ] 10.2 构建基础状态图：定义状态类型、实现节点函数、配置边和条件路由
- [ ] 10.3 实现条件路由：根据 LLM 输出动态决定下一步操作节点
- [ ] 10.4 实现子图（Subgraph）：将复杂工作流分解为可复用的子流程

## 11. LangGraph 高级模式（第 17-18 周）

- [ ] 11.1 实现多 Agent 协作：设计多个专业 Agent，通过 LangGraph 编排协作
- [ ] 11.2 实现 Human-in-the-loop：在工作流关键节点插入人工审核，支持暂停/恢复
- [ ] 11.3 配置 Checkpointer 实现状态持久化和中断恢复
- [ ] 11.4 集成 LangSmith 监控追踪：调用链可视化、Token 用量统计、问题定位

## 12. 综合实战项目（第 19-20 周+）

- [ ] 12.1 确定实战项目方向（智能文档助手 / 代码 Review 助手 / 数据分析 Agent / 知识管理系统）
- [ ] 12.2 完成项目架构设计和技术选型
- [ ] 12.3 实现核心功能 MVP
- [ ] 12.4 实现前端交互界面（发挥 Vue3 优势）
- [ ] 12.5 测试、优化、完善文档
- [ ] 12.6 **最终产出**：一个完整可演示的 AI 应用项目
