## ADDED Requirements

### Requirement: LangChain 基础链式调用
学习者 SHALL 掌握 LangChain 的核心抽象（LCEL、Prompt Template、Output Parser），能构建基础链式调用。

#### Scenario: 使用 LCEL 构建调用链
- **WHEN** 学习者需要将多个处理步骤串联
- **THEN** 能使用 LCEL（LangChain Expression Language）的管道操作符 `|` 组合 Prompt → LLM → Parser 链

#### Scenario: 集成 Claude 作为 LLM
- **WHEN** 学习者在 LangChain 中使用 Claude
- **THEN** 能正确配置 ChatAnthropic，使用 Claude 的 Tool Use 和 Streaming 能力

### Requirement: LangChain Tool 集成
学习者 SHALL 能定义自定义工具并集成到 LangChain Agent 中，实现 AI 与外部系统的交互。

#### Scenario: 定义自定义工具
- **WHEN** 学习者需要让 Agent 访问外部系统（数据库、API 等）
- **THEN** 能使用 `@tool` 装饰器定义工具，包含清晰的描述和类型化的输入 schema

#### Scenario: 工具编排与错误处理
- **WHEN** Agent 执行工具调用
- **THEN** 工具执行结果能正确返回给 LLM，工具执行异常能被捕获并优雅处理

### Requirement: LangGraph 状态图核心
学习者 SHALL 掌握 LangGraph 的 StateGraph 模型，能设计和实现基于状态机的 Agent 工作流。

#### Scenario: 构建基础状态图
- **WHEN** 学习者需要实现多步骤 Agent 工作流
- **THEN** 能定义 StateGraph（状态、节点、边），实现节点间的数据流转和条件路由

#### Scenario: 实现条件路由
- **WHEN** Agent 需要根据当前状态决定下一步操作
- **THEN** 能使用条件边（conditional edges）实现动态路由，类比 Vue Router 的导航守卫

### Requirement: 多 Agent 协作与 Human-in-the-loop
学习者 SHALL 能设计多 Agent 协作工作流，并在关键节点加入人工审核环节。

#### Scenario: 多 Agent 协作
- **WHEN** 复杂任务需要多个专业 Agent 协同完成
- **THEN** 能使用 LangGraph 子图设计多 Agent 系统，每个 Agent 有独立的工具集和职责

#### Scenario: Human-in-the-loop 审核
- **WHEN** Agent 工作流中的关键决策需要人工确认
- **THEN** 能在工作流中插入人工审核节点，暂停执行等待人工输入后继续

### Requirement: Agent 持久化与生产化
学习者 SHALL 能实现 Agent 状态的持久化、对话记忆管理，并使用 LangSmith 进行监控追踪。

#### Scenario: 状态持久化（Checkpointer）
- **WHEN** Agent 工作流需要支持中断恢复
- **THEN** 能配置 Checkpointer 实现状态持久化，Agent 可从任意检查点恢复执行

#### Scenario: LangSmith 监控追踪
- **WHEN** 学习者需要调试和监控 Agent 执行过程
- **THEN** 能集成 LangSmith，追踪每次 LLM 调用的输入/输出/耗时/Token 用量，定位问题节点
