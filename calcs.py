# 加
a = 1 + 1
print(a)
# 减
b = 2 - 1
print(a)
# 变量之间也可以做运算
c = 4
d = 3
e = c - d
print(e)
# 乘
f = 1 * 2
print(f)
# 除
g = 3 / 2
print(g)
# 取模（取余）
h = 5 % 2
print(h)
# 幂
i = 2 ** 3
print(i)
# 取整除
j = 3 // 2
print(j)

print("*" * 30)

n = 1
m = 2
print(n == m)
print(n != m)
print(n > m)
print(n < m)
print(n <= m)
print(n >= m)

print("*" * 30)

# 简单赋值
a = 1
# 多个变量赋值
a, b = 1, 2
# 加法运算
# a = a+1
# 加法赋值运算
a += 1
print(a)

print("*" * 30)

a, b = True, False
print(a and b)
print(a or b)
print(not a)
print(not b)

print("*" * 30)

list_a = ["a", "b", "c"]
list_b = ["a", "b", "c"]

print(id(list_a)) # 使用id查看变量的内存地址
print(id(list_b))
print(list_a is list_b)
print(list_a == list_b)