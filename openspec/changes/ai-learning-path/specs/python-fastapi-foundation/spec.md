## ADDED Requirements

### Requirement: Python 环境搭建与包管理
学习者 SHALL 使用 uv 完成 Python 项目初始化、虚拟环境管理和包安装，能独立管理项目依赖。

#### Scenario: 初始化 Python 项目
- **WHEN** 学习者执行 `uv init` 创建新项目
- **THEN** 生成 `pyproject.toml` 和虚拟环境，学习者能用 `uv add` 安装依赖并用 `uv run` 执行脚本

#### Scenario: 管理项目依赖
- **WHEN** 学习者需要添加/移除/更新依赖包
- **THEN** 能通过 `uv add`/`uv remove` 管理依赖，并理解 `uv.lock` 的作用（类比 package-lock.json）

### Requirement: Python 核心语法掌握（基于 JS/Java 迁移）
学习者 SHALL 掌握 Python 与 JS/Java 的核心语法差异，包括类型提示、列表推导式、装饰器、异常处理和异步编程。

#### Scenario: 使用 Type Hints 编写类型安全代码
- **WHEN** 学习者编写 Python 函数和类
- **THEN** 能正确使用类型提示（如 `def foo(name: str) -> dict:`），理解其与 TypeScript 类型注解的异同

#### Scenario: 使用 Python 异步编程
- **WHEN** 学习者需要处理并发 I/O 操作
- **THEN** 能使用 `async/await` 和 `asyncio` 编写异步代码，理解事件循环机制与 JS 的异同

#### Scenario: 使用 Pydantic 定义数据模型
- **WHEN** 学习者需要定义请求/响应数据结构
- **THEN** 能使用 Pydantic BaseModel 定义带验证的数据模型（类比 TypeScript interface + 运行时验证）

### Requirement: FastAPI Web 服务开发
学习者 SHALL 能使用 FastAPI 构建完整的 RESTful API 服务，包括路由、数据验证、依赖注入、中间件和 CORS 配置。

#### Scenario: 创建基础 API 路由
- **WHEN** 学习者需要创建 REST API 端点
- **THEN** 能定义 GET/POST/PUT/DELETE 路由，使用 Pydantic 模型做请求/响应验证，自动生成 OpenAPI 文档

#### Scenario: 实现 SSE 流式输出
- **WHEN** 学习者需要实现 AI 对话的流式响应
- **THEN** 能使用 FastAPI 的 `StreamingResponse` 实现 Server-Sent Events，前端能实时接收并渲染流式内容

#### Scenario: 配置 CORS 和中间件
- **WHEN** 学习者的 Vue 前端需要跨域请求 FastAPI 后端
- **THEN** 能正确配置 CORS 中间件，允许前端跨域访问
