## ADDED Requirements

### Requirement: 核心 Prompt 技巧掌握
学习者 SHALL 掌握 Few-shot、Chain of Thought、结构化输出等核心 Prompt 技巧，并能针对不同场景选择合适的策略。

#### Scenario: 使用 Few-shot 引导输出格式
- **WHEN** 学习者需要 Claude 按特定格式输出
- **THEN** 能在 Prompt 中提供 2-3 个示例，引导 Claude 生成符合格式要求的输出

#### Scenario: 使用 Chain of Thought 提升推理质量
- **WHEN** 学习者面对需要多步推理的复杂任务
- **THEN** 能设计引导 Claude 分步思考的 Prompt，显著提升推理准确性

#### Scenario: 获取结构化 JSON 输出
- **WHEN** 学习者需要 Claude 返回可解析的结构化数据
- **THEN** 能通过 Prompt 设计或 Tool Use 获取稳定的 JSON 格式输出

### Requirement: Claude 特有 Prompt 技巧
学习者 SHALL 掌握 Claude 独有的 Prompt 优化技巧，包括 XML 标签结构化、Prefill 和 Extended Thinking。

#### Scenario: 使用 XML 标签组织 Prompt
- **WHEN** 学习者编写复杂的多部分 Prompt
- **THEN** 能使用 `<tag>` 结构化组织输入内容，提升 Claude 对不同部分的理解和区分

#### Scenario: 使用 Prefill 控制输出开头
- **WHEN** 学习者需要精确控制 Claude 输出的格式或方向
- **THEN** 能预填充 Assistant 消息的开头部分，引导 Claude 从指定位置继续生成

#### Scenario: 使用 Extended Thinking
- **WHEN** 学习者面对高复杂度推理任务
- **THEN** 能启用 Extended Thinking 功能，让 Claude 在输出前进行深度思考，提升复杂任务的准确性

### Requirement: Prompt 管理与评估
学习者 SHALL 能建立 Prompt 版本管理和效果评估体系，实现 Prompt 的持续迭代优化。

#### Scenario: Prompt 版本管理
- **WHEN** 学习者需要迭代优化某个场景的 Prompt
- **THEN** 能对 Prompt 进行版本化管理，记录每次修改和效果变化

#### Scenario: Prompt 效果评估
- **WHEN** 学习者需要比较两个 Prompt 版本的效果
- **THEN** 能设计评估用例集，通过对比测试量化 Prompt 效果差异
