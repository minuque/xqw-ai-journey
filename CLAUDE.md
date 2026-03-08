# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 📚 项目概述

AI 学习之旅项目，帮助前端开发者系统学习 Python 和 AI 开发技术栈。当前处于 **阶段 1: Python + FastAPI 基础**（76% 完成度）。

### 五个学习阶段
1. **Python + FastAPI 基础** - 环境搭建、Pydantic、异步编程、FastAPI CRUD
2. **LLM API 对接** - OpenAI/Claude API、流式响应、Ollama 本地模型
3. **Prompt 工程** - Few-shot、CoT、结构化输出、上下文管理
4. **RAG 系统** - Embedding、向量数据库、文档处理、检索优化
5. **Agent 工作流** - LangChain、多 Agent 应用、Streamlit UI

## 🛠️ 开发命令

### 环境管理
```bash
uv sync                    # 安装/同步依赖
uv add <package>           # 添加生产依赖
uv add --dev <package>     # 添加开发依赖
uv run python <file>       # 运行 Python 脚本
```

### 代码质量
```bash
uv run ruff check .        # Lint 检查
uv run ruff check --fix .  # 自动修复问题
uv run ruff format .       # 格式化代码
```

## 📁 项目结构

```
xqw-ai-journey/
├── docs/                          # 每日学习日记
├── src/
│   └── python-fastapi-foundation/ # 阶段1代码
│       ├── 0.basic.py             # Python 基础语法
│       └── 1.advance.py           # Pydantic + 异步编程
├── openspec/changes/ai-learning-path/
│   ├── tasks.md                   # 详细任务清单
│   ├── stages.md                  # 阶段进度看板
│   └── specs/                     # 各阶段知识沉淀
└── pyproject.toml                 # 项目配置
```

## 🎯 当前任务（阶段 1 剩余工作）

- [ ] 实现 FastAPI 基础路由（GET/POST/PUT/DELETE）
- [ ] 实现 SSE 流式输出
- [ ] 配置 CORS 中间件
- [ ] 创建 Vue3 前端项目并联调

查看完整任务列表：`openspec/changes/ai-learning-path/tasks.md`

## 💻 代码风格

- Python 3.11+
- 使用 Type Hints（参数和返回值类型注解）
- 练习代码包含 JS/TS 对比注释，格式如下：
  ```python
  # JS: const value = null;
  value = None

  # TS: function greet(name: string): string
  def greet(name: str) -> str:
      ...
  ```

## 📝 学习工作流

1. 编写练习代码到 `src/` 对应目录
2. 记录学习笔记到 `docs/YYYY-MM-DD.md`
3. 更新 `tasks.md` 和 `stages.md`