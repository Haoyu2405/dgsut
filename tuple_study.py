# 1、直接使用逗号分隔
t = 1, 2, 3
print(type(t))

# 2、通过小括号填充元素
t = (1, 2, 3)
print(t)
print(type(t))
t4 = ('a', 'b', 'c', 1)
print(t4)

# 3、通过构造函数tuple()
t = tuple()
print(type(t))
t = tuple([1, 2, 3])
print(t)
print(type(t))

t = tuple(range(1, 6))

# 正向索引
print(t[2])

# 反向索引
print(t[-1])

a = 1, 2, 3, 4, 5
print(a[1:3])

print("*" * 30)

# 切片的使用
t = (1, 2, 3, 4, 5, 6)

print(t[:])
print(t[:-2])
print(t[2:4])
print(t[2:5:2])

# 特殊的切片写法：逆序
print(t[::-1])

print("*" * 30)
t = (1, 3, 2, 3, 2)
print(t.index(3))
print(t.count(3))

t = ('h', 'o', 'g', 'w', 'a', 'r', 't', 's', 'a')
print(t.index('a'))
print(t.count('a'))
