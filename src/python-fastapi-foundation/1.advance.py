"""
Python 进阶语法练习 - 1.3 + 1.4 阶段
渐进式学习：Pydantic 数据模型 + 异步编程
"""

# ==================== 第一部分：Pydantic 数据模型 ====================
# 难度：⭐⭐ (基础)
# JS 对比：类似 TypeScript Zod

import random
from typing import Any, Optional

from pydantic import Field


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

    class Person(BaseModel):
        name: str
        email: str
        age: int = 0

    p = Person(name="xqw", email="xqw@qq.com")
    print(p)

    # 1.2 模型实例化与字段访问
    # Zod 对比: const user = User.parse({ name: "Bob", age: 25 })
    user2 = User.model_validate({"name": "Bob", "age": 25})

    # 练习题：模型字段操作
    # TODO: 创建 Person 实例并访问其字段
    # p = p.model_validate({"name": "xqw1", "email": "xqw@gamil.com"}) # 不推荐用实例的model_validate
    p = Person.model_validate({"name": "xqw1", "email": "xqw@gmail.com"})
    print(f"p name= {p.name}, email= {p.email}")

    # 1.3 模型序列化
    # Zod 对比: JSON.stringify(user.toJSON())
    user_dict = user.model_dump()  # 转 dict
    user_json = user.model_dump_json()  # 转 JSON 字符串

    # 练习题：序列化练习
    # TODO: 将 Person 实例转为 JSON 字符串
    p_dict = p.model_dump()
    p_json = p.model_dump_json()
    print("p => dict=> ", p_dict["name"], p_dict["email"])
    print("p => json=", p_json)


def exercise_2_pydantic_fields():
    """练习2：Pydantic 字段类型、默认值、可选字段"""

    from typing import Optional

    from pydantic import BaseModel

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

    class Book(BaseModel):
        title: str
        author: str = "未知作者"
        pages: int = 0

    book = Book(title="book")
    print(book.author, book.title)

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
    # @dataclass
    class Product(BaseModel):
        name: str
        price: float
        description: Optional[str] = None

    product = Product(name="xqw product", price=float("18.0"))
    print(product)

    # 2.3 必填字段与默认值对比
    # Zod: 必填 = z.string()，可选 = z.string().optional() 或 .default()

    # 练习题：字段验证
    # TODO: 定义一个 RegisterModel
    # - username: str（必填，最少 3 个字符）
    # - password: str（必填，最少 6 个字符）
    # - email: str | None（可选）
    from pydantic import Field

    class RegisterModel(BaseModel):
        username: str = Field(min_length=3)
        password: str = Field(min_length=6)
        email: str | None = None

    # 测试
    r1 = RegisterModel(username="xqw", password="123456")
    print(r1)  # username='xqw' password='123456' email=None


def exercise_3_pydantic_nested():
    """练习3：嵌套模型、模型继承"""

    from typing import List

    from pydantic import BaseModel

    # 3.1 嵌套模型
    # Zod 对比: const Address = z.object({ city: z.string() }); const User = z.object({ address: Address })
    class Address(BaseModel):
        city: str
        country: str = "China"

    class User(BaseModel):
        name: str
        address: Address  # 嵌套 Address 模型

    user = User(name="Alice", address=Address(city="Beijing"))
    print(user.address.city)  # Beijing

    # 练习题：嵌套模型
    # TODO: 定义一个 Company 模型，包含：
    # - name: str
    # - address: Address（嵌套）
    # - employees: List[User]（用户列表）
    class Company(BaseModel):
        name: str
        address: Address
        employees: List[User]

    # 3.2 列表字段
    # Zod 对比: const Post = z.object({ tags: z.array(z.string()) })
    class Post(BaseModel):
        title: str
        tags: List[str]  # 或 list[str] (Python 3.9+)

    post = Post(title="Hello", tags=["python", "fastapi"])

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
    class BaseEmployee(BaseModel):  # 或 Person
        name: str
        email: str

    class Employee(BaseEmployee):
        salary: int

    e = Employee(name="xqw", email="xqw@qq.com", salary=10)
    print(e)


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

    # u1 = User(name='xqw', age=-11)
    # print(u1)  # Value error, 年龄不能为负数 [type=value_error, input_value=-11, input_type=int]
    u2 = User(name="xqw", age=10)
    print(u2)  # name='xqw' age=10

    # 练习题：字段校验器
    # TODO: 定义一个 Person 模型
    # - name: str（长度 1-50）
    # - email: str（必须是邮箱格式，包含 @）
    # 提示：用 field_validator 校验

    # 4.2 多个字段联合校验
    # Zod 对比: const Password = z.object({ password: z.string(), confirm: z.string() }).refine()
    class Person(BaseModel):
        name: str = Field(min_length=1, max_length=50)
        email: str

        @field_validator("email")
        @classmethod
        def validate_email(cls, v):
            if "@" not in v:
                raise ValueError("必须是邮箱格式，包含 @")
            return v

    # 测试正常情况
    p = Person(name="xqw", email="xqw@qq.com")
    print(p)  # name='xqw' email='xqw@qq.com'

    # 测试验证失败（会抛出 ValidationError）
    # from pydantic import ValidationError
    # try:
    #     p_invalid = Person(name="xqw", email="xqwqq.com")
    # except ValidationError as e:
    #     print(f"验证失败: {e}")

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

    class LoginForm(BaseModel):
        username: str
        password: str = Field(min_length=6)
        confirm_password: str

        @field_validator("confirm_password")
        @classmethod
        def validate(cls, value: Any, info):
            if "password" not in info.data or value != info.data["password"]:
                raise ValueError("confirm_password 必须与 password 相同")
            return value

    # 测试正常情况
    loginform = LoginForm(
        username="xqw", password="sk-1234", confirm_password="sk-1234"
    )
    print(loginform)  # username='xqw' password='sk-1234' confirm_password='sk-1234'

    # 测试验证失败（会抛出 ValidationError）
    # from pydantic import ValidationError
    # try:
    #     loginform_invalid = LoginForm(username="xqw", password="sk-1234", confirm_password="sk-123")
    # except ValidationError as e:
    #     print(f"验证失败: {e}")


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
    class Product(BaseModel):
        name: str
        price: int

    p = Product(name="xqw", price=18)

    p_dict = p.model_dump()
    p_dict_json = p.model_dump_json()
    p_new = Product.model_validate(p_dict)
    print("p_dict", p_dict)
    print("p_dict_json", p_dict_json)
    print(p_new)


# ==================== 第二部分：Python 异步编程 ====================
# 难度：⭐⭐⭐⭐ (较难)
# JS 对比：类似 JavaScript Promise/async-await


def exercise_6_async_basic():
    """练习6：async/await 基础"""

    import asyncio

    # ==================== 核心：async 定义协程 ====================
    # JS: async function fn() { return 1; }  → 返回 Promise
    # Python: async def fn(): return 1       → 返回协程对象（coroutine）
    #
    # 关键区别：
    # - JS: async 函数自动执行，返回 Promise
    # - Python: async 函数调用后返回协程对象，需要用 asyncio.run() 或 await 来执行

    # 6.1 定义异步函数
    async def fetch_data():
        print("fetch_data 开始执行")
        return "data"

    # JS 对比:
    # async function fetchData() {
    #     console.log("fetchData 开始执行");
    #     return "data";
    # }

    # 调用 async 函数会发生什么？
    coro = fetch_data()  # 这里只是创建协程对象，函数体还没执行！
    print(f"协程对象: {coro}")  # <coroutine object fetch_data at 0x...>
    coro.close()  # 关闭未执行的协程，避免警告
    # JS 对比: JS 中调用 async 函数会立即执行，返回 Promise

    # 要执行协程，必须用 asyncio.run() 或 await
    result = asyncio.run(fetch_data())  # 现在才真正执行
    print(f"执行结果: {result}")

    # ==================== 练习1：第一个 async 函数 ====================
    # TODO: 定义一个异步函数 greet(name: str) -> str
    # 返回 "Hello, {name}!"
    # 要求：用 asyncio.run() 执行并打印结果

    async def greet(name: str) -> str:
        return f"Hello, {name}!"

    # 测试
    print(asyncio.run(greet("xqw")))  # Hello, xqw!

    # ==================== 6.2 await 等待异步结果 ====================
    # await 只能在 async 函数内部使用
    # JS 对比: const data = await fetchData();

    async def fetch_user():
        return {"name": "Alice", "age": 18}

    async def main():
        # await 会暂停当前函数，等待协程完成
        user = await fetch_user()  # 等待 fetch_user 完成
        print(f"用户: {user}")
        return user

    asyncio.run(main())

    # ==================== 练习2：await 链式调用 ====================
    # TODO: 实现以下两个函数，模拟获取用户信息流程
    # 1. async def get_user_id() -> int: 返回用户ID 1001
    # 2. async def get_user_profile(user_id: int) -> dict: 返回 {"id": user_id, "name": "Alice"}
    # 3. 在 main 中先 await get_user_id()，再 await get_user_profile(user_id)

    async def get_user_id() -> int:
        return 1001

    async def get_user_profile(user_id: int) -> dict:
        return {"id": user_id, "name": "Alice"}

    async def main2():
        user_id = await get_user_id()
        profile = await get_user_profile(user_id)
        print(f"用户资料: {profile}")

    asyncio.run(main2())


def exercise_7_async_sleep():
    """练习7：asyncio.sleep() 模拟异步延迟与并发"""

    import asyncio
    import time

    # ==================== 核心：异步延迟 ====================
    # JS: await new Promise(r => setTimeout(r, 1000))
    # Python: await asyncio.sleep(1)
    #
    # 区别：
    # - JS setTimeout 单位是毫秒
    # - Python asyncio.sleep 单位是秒

    # 7.1 基础延迟
    async def delayed_hello():
        print("开始等待...")
        await asyncio.sleep(1)  # 等待 1 秒
        return "Hello after 1 second!"

    # JS 对比:
    # async function delayedHello() {
    #     console.log("开始等待...");
    #     await new Promise(r => setTimeout(r, 1000)); // 毫秒
    #     return "Hello after 1 second!";
    # }

    async def main():
        result = await delayed_hello()
        print(result)

    asyncio.run(main())

    # ==================== 练习1：带参数的延迟函数 ====================
    # TODO: 实现一个通用的延迟函数
    # async def wait_and_return(msg: str, seconds: float) -> str
    # 等待指定秒数后返回消息
    async def wait_and_return(msg: str, seconds: float) -> str:
        await asyncio.sleep(delay=seconds)
        return msg

    # ==================== 7.2 并发执行：asyncio.gather ====================
    # JS 对比: Promise.all([task1(), task2()])
    # Python: asyncio.gather(task1(), task2())
    #
    # 关键区别：
    # - JS: Promise.all() 接收 Promise 数组
    # - Python: asyncio.gather() 接收协程对象（注意：是协程，不是协程函数）

    async def task1():
        print("task1 开始")
        await asyncio.sleep(1)
        print("task1 结束")
        return "Task 1 done"

    async def task2():
        print("task2 开始")
        await asyncio.sleep(2)
        print("task2 结束")
        return "Task 2 done"

    async def main_parallel():
        start = time.time()
        # 并发执行：两个任务同时开始，总耗时约 2 秒（取最长的）
        results = await asyncio.gather(task1(), task2())
        elapsed = time.time() - start
        print(f"结果: {results}")
        print(f"总耗时: {elapsed:.1f}秒（并发执行）")

    # asyncio.run(main_parallel())

    # JS 对比:
    # async function mainParallel() {
    #     const start = Date.now();
    #     const results = await Promise.all([task1(), task2()]);
    #     console.log(`总耗时: ${(Date.now() - start) / 1000}秒`);
    # }

    # ==================== 7.3 顺序执行 vs 并发执行 ====================
    async def demo_sequential_vs_parallel():
        async def fetch(name: str, delay: float):
            await asyncio.sleep(delay)
            return f"{name} fetched"

        # 顺序执行：总耗时 = 1 + 2 + 3 = 6秒
        start = time.time()
        r1 = await fetch("A", 1)
        r2 = await fetch("B", 2)
        r3 = await fetch("C", 3)
        sequential_time = time.time() - start
        print(f"顺序执行: {sequential_time:.1f}秒")

        # 并发执行：总耗时 ≈ 3秒（取最长的）
        start = time.time()
        results = await asyncio.gather(fetch("A", 1), fetch("B", 2), fetch("C", 3))
        parallel_time = time.time() - start
        print(f"并发执行: {parallel_time:.1f}秒")
        print(f"性能提升: {sequential_time / parallel_time:.1f}x")

    # asyncio.run(demo_sequential_vs_parallel())

    # ==================== 练习2：模拟 API 并发请求 ====================
    # TODO: 实现以下功能
    # 1. async def fetch_user(user_id: int) -> dict: 模拟获取用户，延迟 1 秒
    # 2. async def fetch_posts(user_id: int) -> list: 模拟获取帖子，延迟 2 秒
    # 3. async def get_user_data(user_id: int): 并发获取用户和帖子
    #    期望：总耗时约 2 秒（不是 3 秒）
    async def fetch_user(user_id: int) -> dict:
        await asyncio.sleep(delay=1)
        return {"name": "xqw", "age": 18}

    async def fetch_posts(user_id: int) -> list:
        await asyncio.sleep(delay=2)
        return [{"content": "i am contenrt"}]

    async def get_user_data(user_id: int) -> Any:
        res = await asyncio.gather(fetch_user(user_id), fetch_posts(user_id))
        return res

    print(asyncio.run(get_user_data(1)))


def exercise_8_async_event_loop():
    """练习8：事件循环与任务调度"""

    import asyncio

    # ==================== 核心：事件循环 ====================
    # JS: 事件循环由浏览器/Node.js 自动管理
    # Python: 需要用 asyncio.run() 显式启动事件循环
    #
    # 关键概念：
    # 1. 事件循环是单线程的（和 JS 一样）
    # 2. await 会"让出控制权"，允许其他任务执行
    # 3. asyncio.gather() 让多个任务"交替"执行

    # 8.1 理解 await 的"让出控制权"
    async def demo_yield_control():
        async def count(name: str, n: int):
            for i in range(n):
                print(f"{name}: {i}")
                await asyncio.sleep(0)  # 让出控制权，允许其他任务执行

        # 两个任务交替执行
        await asyncio.gather(count("A", 3), count("B", 3))

    # asyncio.run(demo_yield_control()) # 补充:在这里就是 第一个并任务执行完到await后让给另一个并向任务继续执行
    # 输出: A:0, B:0, A:1, B:1, A:2, B:2（交替）

    # ==================== 8.2 asyncio.create_task ====================
    # JS 对比: const task = asyncFn(); // JS 中直接调用就创建了 Promise
    # Python: task = asyncio.create_task(coro) // 需要显式创建任务

    async def demo_create_task():
        async def background_task(name: str):
            print(f"{name} 开始")
            await asyncio.sleep(1)
            print(f"{name} 完成")
            return f"{name} result"

        # 创建任务（立即开始执行）
        task1 = asyncio.create_task(background_task("Task1"))
        task2 = asyncio.create_task(background_task("Task2"))

        print("任务已创建，等待完成...")
        # 可以在这里做其他事情
        await asyncio.sleep(0.5)
        print("做了其他事情...")

        # 等待所有任务完成
        results = await asyncio.gather(task1, task2)
        print(f"结果: {results}")

    asyncio.run(demo_create_task())

    # ==================== 练习1：任务调度 ====================
    # TODO: 实现一个任务调度器
    # 1. 创建 3 个任务，分别延迟 1、2、3 秒后打印 "Task X done"
    # 2. 使用 create_task 创建任务
    # 3. 主任务在等待期间打印 "等待中..."
    # 4. 最后等待所有任务完成

    async def task_schedule():
        async def demo_task(seconds: float):
            await asyncio.sleep(seconds)
            return f"Task {seconds} done"

        task1 = asyncio.create_task(demo_task(1))
        task2 = asyncio.create_task(demo_task(2))
        task3 = asyncio.create_task(demo_task(3))

        print("等待中...")

        return await asyncio.gather(task1, task2, task3)

    print("task_schedule 已完成结果=> ", asyncio.run(task_schedule()))

    # ==================== 8.3 超时处理 ====================
    # JS 对比: Promise.race([task(), timeout()])
    # Python: asyncio.wait_for(coro, timeout) 或 asyncio.timeout()

    async def demo_timeout():
        async def slow_operation():
            await asyncio.sleep(5)
            return "完成"

        try:
            # 设置 2 秒超时
            result = await asyncio.wait_for(slow_operation(), timeout=2.0)
            print(result)
        except asyncio.TimeoutError:
            print("操作超时！")

    asyncio.run(demo_timeout())  # 操作超时！

    # JS 对比:
    # async function withTimeout(promise, ms) {
    #     return Promise.race([
    #         promise,
    #         new Promise((_, reject) =>
    #             setTimeout(() => reject(new Error('Timeout')), ms)
    #         )
    #     ]);
    # }


def exercise_9_async_context_manager():
    """练习9：异步上下文管理器"""

    import asyncio

    # ==================== 核心：async with ====================
    # JS 对比: 没有直接对应的概念，但可以类比：
    # - try { await acquire(); ... } finally { await release(); }
    # - 或使用 AbortController 管理资源
    #
    # Python 的 async with 会自动调用 __aenter__ 和 __aexit__

    # 9.1 定义异步上下文管理器
    class AsyncTimer:
        """异步计时器：自动记录代码块执行时间"""

        def __init__(self, name: str):
            self.name = name
            self.start_time = None

        async def __aenter__(self):
            print(f"[{self.name}] 开始...")
            self.start_time = asyncio.get_event_loop().time()
            return self  # 返回 self，可以通过 as 捕获

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            elapsed = asyncio.get_event_loop().time() - self.start_time  # type: ignore
            print(f"[{self.name}] 结束，耗时: {elapsed:.2f}秒")
            return False  # 不抑制异常

    async def demo_timer():
        async with AsyncTimer("数据获取"):
            await asyncio.sleep(1)
            print("正在处理数据...")

    asyncio.run(demo_timer())

    # JS 模拟（没有原生支持）:
    # async function withTimer(name, fn) {
    #     console.log(`[${name}] 开始...`);
    #     const start = Date.now();
    #     try {
    #         await fn();
    #     } finally {
    #         console.log(`[${name}] 结束，耗时: ${(Date.now() - start) / 1000}秒`);
    #     }
    # }

    # ==================== 9.2 实际应用：模拟数据库连接 ====================
    class AsyncDBConnection:
        """模拟异步数据库连接"""

        def __init__(self, db_name: str):
            self.db_name = db_name
            self.connected = False

        async def __aenter__(self):
            print(f"连接数据库: {self.db_name}")
            await asyncio.sleep(0.5)  # 模拟连接延迟
            self.connected = True
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            print(f"断开数据库: {self.db_name}")
            await asyncio.sleep(0.1)  # 模拟断开延迟
            self.connected = False
            return False

        async def query(self, sql: str):
            if not self.connected:
                raise RuntimeError("数据库未连接")
            await asyncio.sleep(0.2)  # 模拟查询
            return f"[{self.db_name}] Result: {sql}"

    async def demo_db():
        async with AsyncDBConnection("mydb") as db:
            result = await db.query("SELECT * FROM users")
            print(result)

    asyncio.run(demo_db())

    # ==================== 练习1：异步文件处理器 ====================
    # TODO: 实现一个 AsyncFileHandler 类
    # - __init__(self, filename: str)
    # - async def __aenter__(self): 打印 "打开文件: {filename}"，延迟 0.1 秒
    # - async def __aexit__(self, ...): 打印 "关闭文件: {filename}"
    # - async def read(self) -> str: 延迟 0.2 秒，返回 "content of {filename}"

    class AsyncFileHandler:
        def __init__(self, filename):
            self.filename = filename

        async def __aenter__(self):
            await asyncio.sleep(0.1)
            print(f"打开文件: {self.filename}，延迟 0.1 秒")
            return self

        async def __aexit__(self, exc_type, exc, tb):
            print(f"关闭文件: {self.filename}")
            return False

        async def read(
            self,
        ):
            await asyncio.sleep(0.2)
            return f"content of {self.filename}"

    # 测试：
    async def test_file_handler():
        async with AsyncFileHandler("test.txt") as f:
            content = await f.read()
            print(content)

    asyncio.run(test_file_handler())


def exercise_10_async_vs_sync():
    """练习10：Python async vs JS async 完整对比"""

    import asyncio

    # ==================== 完整对比表 ====================
    # | 场景                  | JavaScript                          | Python                              |
    # |----------------------|-------------------------------------|-------------------------------------|
    # | 定义异步函数           | async function fn() {}              | async def fn():                     |
    # | 调用异步函数           | const p = fn(); // 自动执行          | coro = fn(); // 返回协程对象          |
    # | 等待结果              | await promise                       | await coroutine                     |
    # | 运行入口              | 自动运行                             | asyncio.run(main())                 |
    # | 并发执行              | Promise.all([...])                  | asyncio.gather(...)                 |
    # | 创建任务              | 直接调用（自动开始）                   | asyncio.create_task(coro)           |
    # | 延迟                  | setTimeout(fn, ms)                  | await asyncio.sleep(seconds)        |
    # | 超时                  | Promise.race([...])                 | asyncio.wait_for(coro, timeout)     |
    # | 错误处理              | try/catch 或 .catch()               | try/except                          |
    # | 上下文管理            | 无原生支持                           | async with                          |

    # ==================== 实战对比 ====================

    # 场景1：并发请求
    # JS:
    # const users = await Promise.all([
    #     fetch('/user/1'),
    #     fetch('/user/2'),
    #     fetch('/user/3')
    # ]);

    # Python:
    async def fetch_user(user_id: int):
        await asyncio.sleep(1)  # 模拟网络请求
        return {"id": user_id, "name": f"User{user_id}"}

    async def demo_concurrent():
        users = await asyncio.gather(fetch_user(1), fetch_user(2), fetch_user(3))
        print(f"获取到 {len(users)} 个用户")

    # asyncio.run(demo_concurrent())

    # 场景2：错误处理
    # JS:
    # try {
    #     const result = await riskyOperation();
    # } catch (error) {
    #     console.error(error);
    # }

    # Python:
    async def risky_operation():
        await asyncio.sleep(0.5)
        raise ValueError("出错了！")

    async def demo_error():
        try:
            result = await risky_operation()
        except ValueError as e:
            print(f"捕获错误: {e}")

    # asyncio.run(demo_error())

    # ==================== 综合练习 ====================
    # TODO: 将以下 JS 代码转换为 Python asyncio
    #
    # JS 代码：
    # async function fetchWithRetry(url, maxRetries = 3) {
    #     for (let i = 0; i < maxRetries; i++) {
    #         try {
    #             const response = await fetch(url);
    #             return response.json();
    #         } catch (error) {
    #             if (i === maxRetries - 1) throw error;
    #             await new Promise(r => setTimeout(r, 1000 * (i + 1)));
    #         }
    #     }
    # }
    #
    # 要求：
    # 1. 实现 async def fetch_with_retry(url: str, max_retries: int = 3) -> dict
    # 2. 模拟 fetch：随机成功或失败
    # 3. 失败后等待 1 秒重试，最多重试 max_retries 次
    async def random_fetch(url: str) -> str:
        if random.randint(0, 1) > 0:
            print(f"fetch {url} success")
            return "fetch success"
        raise ValueError("fetch error")

    async def fetch_with_retry(url: str, max_retries: int = 3) -> Optional[dict]:
        for i in range(max_retries):
            try:
                res = await random_fetch(url)
                return {"result": res}
            except ValueError as e:
                await asyncio.sleep(1)  # 失败后等待 1 秒重试
                print(f"捕获错误: {e}")

    print(asyncio.run(fetch_with_retry("xqw.com", 3)))


def exercise_11_async_queue():
    """练习11：异步队列与生产者-消费者模式（新增）"""

    import asyncio

    # ==================== 核心：asyncio.Queue ====================
    # JS 对比: 没有内置的异步队列，通常用数组 + 事件模拟
    # Python: asyncio.Queue 提供线程安全的异步队列
    #
    # 应用场景：
    # - 任务队列
    # - 生产者-消费者模式
    # - 限流处理

    # 11.1 基础队列操作
    async def demo_queue():
        queue = asyncio.Queue()

        # 放入数据
        await queue.put("task1")
        await queue.put("task2")
        await queue.put("task3")

        # 取出数据
        while not queue.empty():
            item = await queue.get()
            print(f"处理: {item}")
            queue.task_done()  # 标记任务完成

    # asyncio.run(demo_queue())

    # ==================== 11.2 生产者-消费者模式 ====================
    async def producer(queue: asyncio.Queue, name: str, count: int):
        """生产者：生成任务"""
        for i in range(count):
            item = f"{name}-item-{i}"
            await queue.put(item)
            print(f"[生产者 {name}] 产生: {item}")
            await asyncio.sleep(0.5)

    async def consumer(queue: asyncio.Queue, name: str):
        """消费者：处理任务"""
        while True:
            item = await queue.get()
            print(f"[消费者 {name}] 处理: {item}")
            await asyncio.sleep(1)  # 模拟处理
            queue.task_done()

    async def demo_producer_consumer():
        queue = asyncio.Queue(maxsize=5)  # 限制队列大小

        # 启动生产者
        producers = [
            asyncio.create_task(producer(queue, "P1", 3)),
            asyncio.create_task(producer(queue, "P2", 3)),
        ]

        # 启动消费者
        consumers = [
            asyncio.create_task(consumer(queue, "C1")),
            asyncio.create_task(consumer(queue, "C2")),
        ]

        # 等待生产者完成
        await asyncio.gather(*producers)

        # 等待队列清空
        await queue.join()

        # 取消消费者（它们在无限循环中）
        for c in consumers:
            c.cancel()

    # asyncio.run(demo_producer_consumer())

    # ==================== 练习：异步任务队列 ====================
    # TODO: 实现一个异步任务处理系统
    # 1. async def worker(queue: Queue, worker_id: int): 从队列取任务并处理
    # 2. async def submit_task(queue: Queue, task: str): 提交任务到队列
    # 3. 使用 3 个 worker 并发处理 10 个任务


# ==================== 综合练习 ====================


def final_pydantic_exercise():
    """综合练习：使用 Pydantic 构建 API 模型"""

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
    exercise_10_async_vs_sync()
    # exercise_11_async_queue()

    print("\n请按顺序完成练习！")


if __name__ == "__main__":
    main()
