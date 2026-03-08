# 🚀 AI 学习之旅

> 专为前端开发者设计的 Python + AI 开发学习路径

## 📖 简介

这是一份系统化的 AI 开发学习计划，从 Python 基础到完整的知识库应用，帮助前端开发者快速掌握 AI 开发技术栈。

## 🎯 学习路径

1. **阶段 1**: Python + FastAPI 基础
2. **阶段 2**: LLM API 对接
3. **阶段 3**: Prompt 工程
4. **阶段 4**: RAG 系统
5. **阶段 5**: Agent 工作流

## 🛠️ 技术栈

- **Python**: 3.11+
- **Web 框架**: FastAPI
- **数据验证**: Pydantic
- **LLM**: Claude API / OpenAI API / Ollama 本地模型
- **向量库**: Chroma
- **AI 框架**: LangChain
- **UI**: Streamlit

## 📁 项目结构

```
xqw-ai-journey/
├── docs/                          # 学习日记
├── src/                           # 练习代码
│   └── python-fastapi-foundation/ # 阶段1
├── openspec/                      # 学习计划
│   └── changes/ai-learning-path/
│       ├── tasks.md               # 详细任务清单
│       ├── stages.md              # 进度看板
│       └── specs/                 # 知识沉淀
└── README.md
```

## 🚀 快速开始

```bash
# 1. 克隆项目
git clone <repo-url>
cd xqw-ai-journey

# 2. 安装依赖
uv sync

# 3. 运行示例代码
uv run python src/python-fastapi-foundation/0.basic.py

# 4. 查看学习任务
cat openspec/changes/ai-learning-path/tasks.md
```

## 📊 学习进度

查看当前学习进度和任务清单：

- **详细任务**: [tasks.md](openspec/changes/ai-learning-path/tasks.md)
- **阶段进度**: [stages.md](openspec/changes/ai-learning-path/stages.md)

## 📝 代码风格

练习代码中包含 **JS/TS 对比注释**，帮助前端开发者理解：

```python
# JS: const value = null;
value = None

# TS: function greet(name: string): string
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## 📚 阶段产出

- ✅ **阶段 1**: FastAPI CRUD API + SSE 流式输出
- 🔄 **阶段 2**: AI 聊天应用（支持云端+本地模型）
- 🔄 **阶段 3**: RAG Prompt 模板库
- 🔄 **阶段 4**: 知识库问答 API
- 🔄 **阶段 5**: LangChain 驱动的知识库应用

## 🤝 贡献

欢迎分享学习心得、提交代码优化或发现的问题！

## 📄 许可证

MIT
