## ADDED Requirements

### Requirement: Claude Messages API 基础对话
学习者 SHALL 能使用 Anthropic Python SDK 调用 Claude Messages API，完成基础对话功能。

#### Scenario: 发送单轮对话请求
- **WHEN** 学习者调用 Claude Messages API 并传入用户消息
- **THEN** 能获取 Claude 的文本响应，正确处理 API 返回的 JSON 结构

#### Scenario: 管理多轮对话上下文
- **WHEN** 学习者需要实现多轮对话
- **THEN** 能正确维护 messages 数组（交替 user/assistant 消息），实现连续对话体验

### Requirement: Claude Streaming 流式输出
学习者 SHALL 能实现 Claude API 的流式输出，并通过 FastAPI SSE 传递到 Vue 前端实时渲染。

#### Scenario: 实现后端流式调用
- **WHEN** 学习者调用 Claude API 的 stream 模式
- **THEN** 能逐 token 接收响应，并通过 FastAPI SSE 转发给前端

#### Scenario: 前端流式渲染
- **WHEN** Vue 前端通过 EventSource 或 fetch 接收 SSE 流
- **THEN** 能实时渲染 Markdown 格式的 AI 响应，提供打字机效果的用户体验

### Requirement: Claude Tool Use（Function Calling）
学习者 SHALL 能定义工具 schema 并让 Claude 自动选择调用工具，实现 AI 与外部系统的交互。

#### Scenario: 定义并注册工具
- **WHEN** 学习者定义一组工具（含 name、description、input_schema）
- **THEN** Claude 能根据对话上下文自动决定是否调用工具，返回 tool_use 类型的 content block

#### Scenario: 处理工具调用结果
- **WHEN** Claude 返回 tool_use 请求
- **THEN** 学习者的代码能执行对应工具函数，将结果以 tool_result 消息返回 Claude 继续对话

### Requirement: Claude System Prompt 与多模态
学习者 SHALL 能设计有效的 System Prompt 控制 Claude 行为，并使用 Vision 能力处理图片输入。

#### Scenario: 设计 System Prompt
- **WHEN** 学习者需要 Claude 扮演特定角色或遵循特定规则
- **THEN** 能编写结构化的 System Prompt，有效控制 Claude 的输出风格、格式和行为边界

#### Scenario: 使用 Vision 能力
- **WHEN** 学习者需要让 Claude 理解图片内容
- **THEN** 能将图片（base64 或 URL）作为消息内容传入，获取 Claude 对图片的分析结果
