# class_study.py

class Human:
    # 定义属性（类属性）
    message = "这是类属性"

    # 构造方法
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age
        print("这是构造方法")

    def __str__(self):
        return f"Name:{self.name},Age:{self.age}"

    # 实例方法
    def study(self, course):
        print(f"{self.name}正在学习{course}")

    @staticmethod
    def eat():
        pass

    @classmethod
    def sleep(cls):
        pass


# 实例化对象
person = Human("哈利波特", 12)

# 通过实例访问类属性
print(person.message)

# 通过实例访问实例属性
print(person.name)
print(person.age)

print(person)

person.study("魔法")

person1 = Human("王二牛", 48)
print(person1)

person1.study("耕田")

Human.eat()
Human.sleep()
