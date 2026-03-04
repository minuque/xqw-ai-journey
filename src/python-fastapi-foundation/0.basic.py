"""
Python 基础语法练习 - 1.2 阶段
渐进式学习：从基础到进阶
"""

# ==================== 第一部分：基础类型与 None/True/False ====================
# 难度：⭐ (最简单)
# JS 对比：理解 Python 和 JavaScript 的类型差异


import email
import re


def exercise_1_basic_types():
    """练习1：基础类型与 None/True/False"""

    # 1.1 None vs null/undefined
    # JS: let value = null; let value2 = undefined;
    value = None

    # 练习题：判断变量是否为 None
    # TODO: 实现一个函数，如果输入是 None 返回 "empty"，否则返回值本身
    def check_none(val):
        # if val is None:
        #     return "empty"
        # return val

        # 简化后
        return "empty" if val is None else val

    # 测试
    assert check_none(None) == "empty"
    assert check_none("hello") == "hello"

    # 1.2 True/False vs true/false
    # JS: const isValid = true; const isEmpty = false;
    is_valid = True
    is_empty = False

    # 练习题：布尔值判断
    # TODO: 实现一个函数，判断列表是否为空
    # JS 实现: const isEmpty = (arr) => arr.length === 0
    def is_list_empty(lst):
        return len(lst) == 0

    # 测试
    assert is_list_empty([]) == True
    assert is_list_empty([1, 2]) == False

    # 1.3 Falsy 值对比
    # JS: if (!value) {} // 0, "", null, undefined, false, NaN
    # Python: if not value: # None, False, 0, "", [], {}, ()

    # 练习题：实现一个函数，返回参数是否为"假值"
    def is_falsy(val):
        return not val

    # 测试
    assert is_falsy(None) == True
    assert is_falsy(0) == True
    assert is_falsy("") == True
    assert is_falsy([]) == True
    assert is_falsy("hello") == False


# ==================== 第二部分：Type Hints 基础 ====================
# 难度：⭐⭐
# JS 对比：类似 TypeScript 的类型注解


def exercise_2_type_hints():
    """练习2：Type Hints 基础"""

    # 2.1 函数参数和返回值类型注解
    # TS: function greet(name: string): string { return `Hello, ${name}`; }
    def greet(name: str) -> str:
        return f"Hello, {name}"

    # 练习题：添加类型注解
    # TODO: 为以下函数添加类型注解
    # 要求：接收两个整数，返回它们的和
    def add(a: int, b: int):  # 请添加类型注解
        return a + b

    # 2.2 变量类型注解
    # TS: const age: number = 18;
    age: int = 18
    name: str = "Alice"
    scores: list[int] = [90, 85, 88]

    # 练习题：声明带类型注解的变量
    # TODO: 声明以下变量并添加类型注解
    # - email: 字符串类型
    # - is_active: 布尔类型
    # - tags: 字符串列表
    email: str = "xqw@qq.com"
    is_active: bool = False
    tags: list[str] = ["xqw1", "xqw2"]

    # 2.3 可选类型 Optional
    # TS: function findUser(id: number): User | null { }
    from typing import Optional

    def find_user(user_id: int) -> Optional[str]:
        """返回用户名，如果找不到返回 None"""
        if user_id == 1:
            return "Alice"
        return None

    # 练习题：实现带可选返回值的函数
    # TODO: 实现一个函数，在列表中查找元素，找到返回索引，找不到返回 None
    # JS 实现: const findIndex = (arr, target) => { const idx = arr.indexOf(target); return idx >= 0 ? idx : null; }
    def find_index(
        lst: list[int], target: int
    ) -> Optional[int]:  # 请添加返回值类型注解
        for i in range(len(lst)):  # i 是索引 0, 1, 2...
            if lst[i] == target:
                return i
        return None

    # 或更 Pythonic
    # def find_index(lst: list[int], target: int) -> Optional[int]:
    #     try:
    #         return lst.index(target)
    #     except ValueError:
    #         return None


# ==================== 第三部分：列表/字典推导式 ====================
# 难度：⭐⭐⭐
# JS 对比：类似 map/filter/reduce，但语法更简洁


def exercise_3_comprehensions():
    """练习3：列表推导式与字典推导式"""

    # 3.1 列表推导式基础
    # JS: const squares = numbers.map(x => x ** 2)
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]

    # 练习题：使用列表推导式
    # TODO: 将列表中所有字符串转为大写
    # JS 实现: const upper = words.map(w => w.toUpperCase())
    words = ["hello", "world", "python"]
    upper_words = []  # 请使用列表推导式实现

    # 3.2 带条件的列表推导式
    # JS: const evens = numbers.filter(x => x % 2 === 0)
    evens = [x for x in numbers if x % 2 == 0]

    # 练习题：筛选并转换
    # TODO: 获取所有大于10的数字的平方
    # JS 实现: const result = numbers.filter(x => x > 10).map(x => x ** 2)
    nums = [5, 12, 8, 20, 3, 15]
    result = []  # 请使用列表推导式实现

    # 3.3 字典推导式
    # JS: const obj = Object.fromEntries(arr.map(x => [x, x ** 2]))
    square_dict = {x: x**2 for x in numbers}

    # 练习题：字典推导式
    # TODO: 创建一个字典，key 是单词，value 是单词长度
    # JS 实现: const lengths = Object.fromEntries(words.map(w => [w, w.length]))
    words = ["apple", "banana", "cherry"]
    word_lengths = {}  # 请使用字典推导式实现

    # 3.4 嵌套推导式
    # JS: const matrix = Array.from({length: 3}, (_, i) => Array.from({length: 3}, (_, j) => i * 3 + j))
    matrix = [[i * 3 + j for j in range(3)] for i in range(3)]

    # 练习题：展平嵌套列表
    # TODO: 将二维列表展平为一维
    # JS 实现: const flat = matrix.flat() 或 matrix.reduce((acc, row) => [...acc, ...row], [])
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = []  # 请使用列表推导式实现


# ==================== 第四部分：Type Hints 进阶 - 泛型 ====================
# 难度：⭐⭐⭐⭐
# JS 对比：类似 TypeScript 的泛型


def exercise_4_generics():
    """练习4：泛型类型注解"""

    from typing import List, Dict, Tuple, Union

    # 4.1 泛型列表和字典
    # TS: function getFirst<T>(arr: T[]): T | undefined { return arr[0]; }
    def get_first(items: List[str]) -> Optional[str]:
        return items[0] if items else None

    # 练习题：泛型函数
    # TODO: 实现一个函数，返回字典的所有键
    # TS 实现: function getKeys<K, V>(obj: Record<K, V>): K[] { return Object.keys(obj); }
    def get_keys(d: Dict[str, int]):  # 请添加返回值类型注解
        pass  # 请实现

    # 4.2 Union 类型
    # TS: type ID = string | number;
    from typing import Union

    def process_id(id_val: Union[int, str]) -> str:
        return str(id_val)

    # 练习题：Union 类型处理
    # TODO: 实现一个函数，接收字符串或列表，返回其长度
    # TS 实现: function getLength(val: string | any[]): number { return val.length; }
    def get_length(val):  # 请添加类型注解
        pass  # 请实现

    # 4.3 Tuple 元组类型
    # TS: type Point = [number, number];
    def get_point() -> Tuple[int, int]:
        return (10, 20)

    # 练习题：元组解包
    # TODO: 实现一个函数，接收元组 (name, age)，返回格式化字符串
    def format_person(person: Tuple[str, int]):  # 请添加返回值类型注解
        pass  # 请实现，返回 "Name: xxx, Age: xxx"


# ==================== 第五部分：dataclass ====================
# 难度：⭐⭐⭐⭐
# JS 对比：类似 TypeScript 的 class


def exercise_5_dataclass():
    """练习5：dataclass - Python 的数据类"""

    from dataclasses import dataclass
    from typing import Optional

    # 5.1 基础 dataclass
    # TS: class User { constructor(public name: string, public age: number) {} }
    @dataclass
    class User:
        name: str
        age: int

    user = User(name="Alice", age=18)
    print(user.name)  # Alice

    # 练习题：定义 dataclass
    # TODO: 定义一个 Product 数据类
    # 包含字段：name (str), price (float), in_stock (bool)
    # TS 对比: class Product { constructor(public name: string, public price: number, public inStock: boolean) {} }

    # 5.2 带默认值的 dataclass
    @dataclass
    class Config:
        host: str = "localhost"
        port: int = 8000
        debug: bool = False

    config = Config()  # 使用默认值
    config2 = Config(host="127.0.0.1")  # 部分覆盖

    # 练习题：带默认值的类
    # TODO: 定义一个 BlogPost 类
    # 字段：title (str), content (str), published (bool, 默认 False), views (int, 默认 0)

    # 5.3 dataclass 方法
    @dataclass
    class Rectangle:
        width: float
        height: float

        def area(self) -> float:
            return self.width * self.height

        def perimeter(self) -> float:
            return 2 * (self.width + self.height)

    # 练习题：实现带方法的 dataclass
    # TODO: 定义一个 Circle 类
    # 字段：radius (float)
    # 方法：area() -> float, circumference() -> float
    # 提示：π 可以用 3.14 或 import math; math.pi


# ==================== 第六部分：装饰器 ====================
# 难度：⭐⭐⭐⭐⭐ (最难)
# JS 对比：类似 JS Decorator 提案 (实验性特性)


def exercise_6_decorators():
    """练习6：装饰器原理"""

    # 6.1 基础装饰器
    # JS 类比:
    # function log(target, name, descriptor) {
    #     const original = descriptor.value;
    #     descriptor.value = function(...args) {
    #         console.log(`Calling ${name}`);
    #         return original.apply(this, args);
    #     }
    # }

    def log_call(func):
        """装饰器：打印函数调用"""

        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    @log_call
    def greet(name: str) -> str:
        return f"Hello, {name}"

    # greet("Alice")  # 输出: Calling greet \n Hello, Alice

    # 练习题：实现计时装饰器
    # TODO: 实现一个装饰器，打印函数执行时间
    # 提示：使用 time.time() 获取时间戳
    import time

    def timer(func):
        """装饰器：计算函数执行时间"""
        pass  # 请实现

    # @timer
    # def slow_function():
    #     time.sleep(1)
    #     return "Done"

    # 6.2 带参数的装饰器
    def repeat(times: int):
        """装饰器工厂：重复执行函数 n 次"""

        def decorator(func):
            def wrapper(*args, **kwargs):
                results = []
                for _ in range(times):
                    results.append(func(*args, **kwargs))
                return results

            return wrapper

        return decorator

    @repeat(3)
    def say_hello():
        return "Hello!"

    # say_hello()  # 返回: ["Hello!", "Hello!", "Hello!"]

    # 练习题：实现缓存装饰器
    # TODO: 实现一个简单的缓存装饰器，避免重复计算
    # 提示：使用字典存储已计算的结果
    def cache(func):
        """装饰器：缓存函数结果"""
        pass  # 请实现

    # @cache
    # def fibonacci(n: int) -> int:
    #     if n < 2:
    #         return n
    #     return fibonacci(n - 1) + fibonacci(n - 2)

    # 6.3 类装饰器
    @dataclass
    class Counter:
        """使用装饰器的类"""

        count: int = 0

        def increment(self):
            self.count += 1
            return self.count

    # 练习题：为类添加装饰器
    # TODO: 实现一个装饰器，为类自动添加 __repr__ 方法


# ==================== 综合练习：组合运用 ====================


def final_exercise():
    """综合练习：组合使用所学知识"""

    from dataclasses import dataclass
    from typing import List, Optional

    # TODO: 实现一个简单的任务管理系统
    # 要求：
    # 1. 定义 Task dataclass，包含：id (int), title (str), completed (bool, 默认 False)
    # 2. 定义 TaskManager 类，包含方法：
    #    - add_task(title: str) -> Task
    #    - complete_task(task_id: int) -> bool
    #    - get_pending_tasks() -> List[Task]  (使用列表推导式)
    #    - get_completed_tasks() -> List[Task]  (使用列表推导式)
    # 3. 为 add_task 方法添加日志装饰器

    # 参考 JS 实现：
    # class TaskManager {
    #   constructor() { this.tasks = []; this.nextId = 1; }
    #   addTask(title) {
    #     const task = { id: this.nextId++, title, completed: false };
    #     this.tasks.push(task);
    #     return task;
    #   }
    #   getPendingTasks() { return this.tasks.filter(t => !t.completed); }
    # }

    pass  # 请实现


def main():
    """主函数：运行所有练习"""
    print("=== Python 基础语法练习 ===\n")

    # 取消注释以运行各个练习
    exercise_1_basic_types()
    # exercise_2_type_hints()
    # exercise_3_comprehensions()
    # exercise_4_generics()
    # exercise_5_dataclass()
    # exercise_6_decorators()
    # final_exercise()

    print("\n完成所有练习后，请运行测试验证结果！")


if __name__ == "__main__":
    main()
