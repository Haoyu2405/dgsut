# s = "Hogwarts"
# print(s)
# print(type(s))
# print(s[3])
#
# print("*" * 30)
#
# s = "Hello" + " " + "Hogwarts"
# print(s)
#
# print("*" * 30)
#
# s = "Hogwarts" * 5
# print(s)
#
# print("*" * 30)
#
str_d = "abcdefg"
print(str_d[0])
# x>=1
print(str_d[1:])
# 前闭后开原则，1<=x<5
print(str_d[1:5])
# 步长，
print(str_d[1:5:2])
print(str_d[1::2])

print(str_d[::-1])

print("*" * 30)

print("hogwarts %s" % "测试学院")
print("hogwarts %d" % 1)

print("*" * 30)
# 不设置指定位置，按默认顺序
print("{} {}".format("hogwarts", "ad"))
# 设置指定位置
print("{1} {0}".format("hogwarts", "ad"))
# 通过名称传递变量
print("{name}测试开发".format(name="霍格沃兹"))

print("*" * 30)

name = "Bob"
school = "hogwarts"
# 通过 f"{变量名}"
print(f"我的名字叫做{name}, 毕业于{school}")
print("*" * 30)

# 在Hogwarts 中查找 war 是否存在
print("Hogwarts".find("war"))

# 在Hogwarts 中查找 War 是否存在
print("Hogwarts".find("War"))

print("*" * 30)

# 在Hogwarts 中查找 war 是否存在
print("war" in "Hogwarts")

# 在Hogwarts 中查找 War 是否存在
print("War" in "Hogwarts")

print("*" * 30)

# 将原字符串中的school替换为top school
s = "hogwarts school"
print(s.replace("school", "top school"))
# 注意:字符串的所有操作都会新生成一个字符串,不会影响原字符串
print(s)

print("*" * 30)

a = ["h", "o", "g", "w", "a", "r", "t", "s"]
# 将列表中的每一个元素拼接起来
print("".join(a))

print("*" * 30)

# 根据split内的内容将字符串进行切分
demo = "hogwarts school"
print(demo.split(" "))

print("*" * 30)

demo = "hogwarts school "
print(demo)
print(demo.strip())