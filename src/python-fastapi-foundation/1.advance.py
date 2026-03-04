"""
Python 进阶语法练习 - 1.3 + 1.4 阶段
渐进式学习：Pydantic 数据模型 + 异步编程
"""

# ==================== 第一部分：Pydantic 数据模型 ====================
# 难度：⭐⭐ (基础)
# JS 对比：类似 TypeScript Zod

def exercise_1_pydantic_basics():
    """练习1：Pydantic 基础 - 定义第一个 BaseModel"""

    from pydantic import BaseModel

    # 1.1 基础模型定义
    # Zod 对比: const User = z.object({ name: z.string(), age: z.number() })
    class User(BaseModel):
        name: str
        age: int

    user = User(name="Alice", age=18)
    print(user)  # User(name='Alice', age=18)

    # 练习题：定义一个 User 模型
    # TODO: 定义一个 Person 模型，包含：
    # - name: str
    # - email: str
    # - age: int（可选，默认 0）
    # Zod 对比: const Person = z.object({ name: z.string(), email: z.string(), age: z.number().default(0) })

    # 1.2 模型实例化与字段访问
    # Zod 对比: const user = User.parse({ name: "Bob", age: 25 })
    user2 = User.model_validate({"name": "Bob", "age": 25})

    # 练习题：模型字段操作
    # TODO: 创建 Person 实例并访问其字段

    # 1.3 模型序列化
    # Zod 对比: JSON.stringify(user.toJSON())
    user_dict = user.model_dump()  # 转 dict
    user_json = user.model_dump_json()  # 转 JSON 字符串

    # 练习题：序列化练习
    # TODO: 将 Person 实例转为 JSON 字符串


def exercise_2_pydantic_fields():
    """练习2：Pydantic 字段类型、默认值、可选字段"""

    from pydantic import BaseModel
    from typing import Optional

    # 2.1 默认值字段
    # Zod 对比: const Config = z.object({ host: z.string().default("localhost") })
    class Config(BaseModel):
        host: str = "localhost"
        port: int = 8080

    config = Config()
    print(config.host)  # localhost

    # 练习题：带默认值的模型
    # TODO: 定义一个 Book 模型
    # - title: str（必填）
    # - author: str（默认 "未知作者"）
    # - pages: int（默认 0）

    # 2.2 可选字段
    # Zod 对比: const Profile = z.object({ bio: z.string().optional() })
    class Profile(BaseModel):
        bio: Optional[str] = None  # 或使用 str | None (Python 3.10+)
        avatar: str | None = None  # Python 3.10+ 语法

    # 练习题：可选字段
    # TODO: 定义一个 Product 模型
    # - name: str（必填）
    # - description: str | None（可选）
    # - price: float（必填）

    # 2.3 必填字段与默认值对比
    # Zod: 必填 = z.string()，可选 = z.string().optional() 或 .default()

    # 练习题：字段验证
    # TODO: 定义一个 RegisterModel
    # - username: str（必填，最少 3 个字符）
    # - password: str（必填，最少 6 个字符）
    # - email: str | None（可选）


def exercise_3_pydantic_nested():
    """练习3：嵌套模型、模型继承"""

    from pydantic import BaseModel
    from typing import List, Optional

    # 3.1 嵌套模型
    # Zod 对比: const Address = z.object({ city: z.string() }); const User = z.object({ address: Address })
    class Address(BaseModel):
        city: str
        country: str = "China"

    class User(BaseModel):
        name: str
        address: Address  # 嵌套 Address 模型

    user = User(
        name="Alice",
        address={"city": "Beijing", "country": "China"}
    )
    print(user.address.city)  # Beijing

    # 练习题：嵌套模型
    # TODO: 定义一个 Company 模型，包含：
    # - name: str
    # - address: Address（嵌套）
    # - employees: List[User]（用户列表）

    # 3.2 列表字段
    # Zod 对比: const Post = z.object({ tags: z.array(z.string()) })
    class Post(BaseModel):
        title: str
        tags: List[str]  # 或 list[str] (Python 3.9+)

    post = Post(title="Hello", tags=["python", "fastapi"])

    # 练习题：列表字段
    # TODO: 定义一个 TodoList 模型
    # - name: str
    # - items: List[str]

    # 3.3 模型继承
    # Zod 对比: 使用 .extend() 或 .merge()
    class BasePerson(BaseModel):
        name: str

    class Student(BasePerson):
        grade: int

    # 练习题：模型继承
    # TODO: 定义 BaseModel，然后创建 Employee 继承它
    # - Base: name, email
    # - Employee 额外字段: salary


def exercise_4_pydantic_validator():
    """练习4：自定义 Validator"""

    from pydantic import BaseModel, field_validator

    # 4.1 字段校验器
    # Zod 对比: const User = z.object({ age: z.number().min(0).max(150) })
    class User(BaseModel):
        name: str
        age: int

        @field_validator("age")
        @classmethod
        def validate_age(cls, v):
            if v < 0:
                raise ValueError("年龄不能为负数")
            if v > 150:
                raise ValueError("年龄超出合理范围")
            return v

    # 练习题：字段校验器
    # TODO: 定义一个 Person 模型
    # - name: str（长度 1-50）
    # - email: str（必须是邮箱格式，包含 @）
    # 提示：用 field_validator 校验

    # 4.2 多个字段联合校验
    # Zod 对比: const Password = z.object({ password: z.string(), confirm: z.string() }).refine()

    class RegisterForm(BaseModel):
        password: str
        confirm: str

        @field_validator("confirm")
        @classmethod
        def validate_match(cls, v, info):
            # info.data 可以访问同一条记录的其他字段
            if "password" in info.data and v != info.data["password"]:
                raise ValueError("两次密码不一致")
            return v

    # 练习题：联合校验
    # TODO: 定义一个 LoginForm 模型
    # - username: str（不能为空）
    # - password: str（长度 >= 6）
    # - confirm_password: str（必须与 password 相同）


def exercise_5_pydantic_serialization():
    """练习5：模型序列化"""

    from pydantic import BaseModel

    # 5.1 model_dump() - 转字典
    # Zod 对比: JSON.parse(JSON.stringify(zodObj))
    class User(BaseModel):
        name: str
        age: int

    user = User(name="Alice", age=18)
    user_dict = user.model_dump()
    print(user_dict)  # {'name': 'Alice', 'age': 18}

    # 5.2 model_dump_json() - 转 JSON 字符串
    user_json = user.model_dump_json()
    print(user_json)  # {"name":"Alice","age":18}

    # 5.3 model_validate() - 从字典创建模型
    data = {"name": "Bob", "age": 20}
    user2 = User.model_validate(data)

    # 练习题：序列化练习
    # TODO: 定义一个 Product 模型，包含 name, price
    # - 创建实例
    # - 转为 dict
    # - 转为 JSON
    # - 从 dict 重建实例


# ==================== 第二部分：Python 异步编程 ====================
# 难度：⭐⭐⭐⭐ (较难)
# JS 对比：类似 JavaScript Promise/async-await

def exercise_6_async_basic():
    """练习6：async/await 基础"""

    import asyncio

    # 6.1 定义异步函数
    # JS 对比: async function fetchData() { return "data"; }
    async def fetch_data():
        return "data"

    # 6.2 await 等待异步结果
    # JS 对比: const data = await fetchData();
    async def main():
        result = await fetch_data()
        print(result)  # data

    # 运行异步函数
    asyncio.run(main())

    # 练习题：异步函数
    # TODO: 定义一个异步函数 greet(name: str) -> str
    # 返回 "Hello, {name}!"

    # 6.3 async with 异步上下文管理器
    # JS 对比: await using (await openFile()) { ... }

    # 练习题：async with
    # TODO: 模拟一个异步上下文管理器
    # 提示：定义 __aenter__ 和 __aexit__ 方法的类


def exercise_7_async_sleep():
    """练习7：asyncio.sleep() 模拟异步延迟"""

    import asyncio

    # 7.1 asyncio.sleep() - 异步延迟
    # JS 对比: await new Promise(r => setTimeout(r, 1000))
    async def delayed_hello():
        await asyncio.sleep(1)  # 等待 1 秒
        return "Hello after 1 second!"

    async def main():
        result = await delayed_hello()
        print(result)

    # asyncio.run(main())

    # 练习题：异步延迟
    # TODO: 定义一个异步函数 wait_and_return(msg: str, seconds: float)
    # 等待指定秒数后返回消息

    # 7.2 并发执行 - 同时等待多个异步任务
    # JS 对比: const [result1, result2] = await Promise.all([task1(), task2()])

    async def task1():
        await asyncio.sleep(1)
        return "Task 1 done"

    async def task2():
        await asyncio.sleep(2)
        return "Task 2 done"

    async def main_parallel():
        # 并发执行，两个任务同时运行
        results = await asyncio.gather(task1(), task2())
        print(results)  # ['Task 1 done', 'Task 2 done']

    # asyncio.run(main_parallel())

    # 练习题：asyncio.gather
    # TODO: 定义三个异步函数，分别等待 1、2、3 秒
    # 使用 gather 并发执行，总耗时应该是 3 秒（而不是 6 秒）


def exercise_8_async_event_loop():
    """练习8：事件循环机制"""

    import asyncio

    # 8.1 事件循环理解
    # JS 对比: JS 事件循环在浏览器中运行，Python 事件循环在 asyncio 中运行

    # 练习题：事件循环观察
    # TODO: 创建多个异步任务，观察执行顺序
    # 提示：打印开始和结束时间戳

    async def print_nums():
        for i in range(5):
            print(i)
            await asyncio.sleep(0.1)

    async def print_letters():
        for letter in "abcde":
            print(letter)
            await asyncio.sleep(0.1)

    async def main():
        # 顺序执行
        await print_nums()
        await print_letters()
        print("---")
        # 并发执行
        await asyncio.gather(print_nums(), print_letters())

    # asyncio.run(main())

    # 练习题：执行顺序分析
    # TODO: 预测以下代码的输出顺序
    async def a(): print("a start"); await asyncio.sleep(0); print("a end")
    async def b(): print("b start"); await asyncio.sleep(0); print("b end")
    async def c(): print("c start"); print("c end")  # 同步执行

    # asyncio.run(asyncio.gather(a(), b(), c()))


def exercise_9_async_context_manager():
    """练习9：异步上下文管理器"""

    import asyncio

    # 9.1 定义异步上下文管理器
    # JS 对比: 类比 using 语句（.NET）或 async with
    class AsyncConnection:
        async def __aenter__(self):
            print("Connecting...")
            await asyncio.sleep(0.5)  # 模拟连接延迟
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            print("Disconnecting...")
            await asyncio.sleep(0.1)  # 模拟断开延迟
            return False

        async def query(self, sql: str):
            await asyncio.sleep(0.2)  # 模拟查询
            return f"Result: {sql}"

    async def main():
        async with AsyncConnection() as conn:
            result = await conn.query("SELECT * FROM users")
            print(result)

    # asyncio.run(main())

    # 练习题：异步上下文管理器
    # TODO: 定义一个 AsyncFile 类，实现异步文件操作
    # - __aenter__ / __aexit__
    # - async read() / async write()


def exercise_10_async_vs_sync():
    """练习10：对比 Python async 与 JS async 差异"""

    import asyncio

    # 10.1 语法差异
    # JS: async/await 是原生语法
    # Python: async/await 也是原生语法（Python 3.5+）

    # 10.2 事件循环差异
    # JS: 浏览器事件循环 / Node.js 事件循环
    # Python: asyncio 事件循环（单线程）

    # 10.3 Promise.all vs asyncio.gather
    # JS: Promise.all([promise1, promise2])
    # Python: asyncio.gather(coro1, coro2)

    # 练习题：对比练习
    # TODO: 用 Python asyncio 实现 JS 的效果
    # JS: Promise.all([delay(1000, "a"), delay(2000, "b")]).then(console.log)

    async def delay(ms: int, msg: str):
        await asyncio.sleep(ms / 1000)
        return msg

    async def main():
        # 请用 asyncio.gather 实现相同效果
        pass  # 请实现

    # asyncio.run(main())  # 期望输出: ['a', 'b']


# ==================== 综合练习 ====================

def final_pydantic_exercise():
    """综合练习：使用 Pydantic 构建 API 模型"""

    from pydantic import BaseModel, field_validator
    from typing import List, Optional

    # TODO: 实现一个 TODO 应用的数据模型
    # 需求：
    # 1. TodoItem: id, title, completed(bool), created_at
    # 2. TodoCreate: title（必填，1-100字符）
    # 3. TodoUpdate: title（可选）, completed（可选）
    # 4. TodoList: items(List[TodoItem]), total(int)

    # 参考 Zod 实现：
    # const TodoItem = z.object({
    #   id: z.number(),
    #   title: z.string(),
    #   completed: z.boolean(),
    #   createdAt: z.string()
    # })
    pass


def final_async_exercise():
    """综合练习：异步任务调度"""

    import asyncio
    from typing import List

    # TODO: 实现一个异步任务调度器
    # 需求：
    # 1. 定义 async def fetch_url(url: str) -> str，模拟网络请求
    # 2. 定义 async def fetch_all(urls: List[str]) -> List[str]
    #    - 使用 asyncio.gather 并发获取所有 URL
    #    - 返回所有结果
    # 3. 测试：并发获取 3 个 URL，总耗时应接近最慢的那个

    # JS 参考实现：
    # async function fetchAll(urls) {
    #   return Promise.all(urls.map(url => fetch(url)));
    # }

    pass


def main():
    """主函数"""
    print("=== Python 进阶语法练习 (1.3 + 1.4) ===\n")

    # 取消注释运行各个练习
    # exercise_1_pydantic_basics()
    # exercise_2_pydantic_fields()
    # exercise_3_pydantic_nested()
    # exercise_4_pydantic_validator()
    # exercise_5_pydantic_serialization()
    # exercise_6_async_basic()
    # exercise_7_async_sleep()
    # exercise_8_async_event_loop()
    # exercise_9_async_context_manager()
    # exercise_10_async_vs_sync()

    print("\n请按顺序完成练习！")


if __name__ == "__main__":
    main()
