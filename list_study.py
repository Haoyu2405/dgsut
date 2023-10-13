# # 1、通过构造函数创建
# li1 = list()  # 空列表
# print(li1)
# li1 = list('hogwarts')  # 字符串
# print(li1)
# li1 = list((1, 2, 3))  # 元组
# print(li1)
# li1 = list({4, 5, 6})  # 集合
# print(li1)
# li1 = list({'a': 7, 'b': 8})  # 字典
# print(type(li1), li1)
#
# # 2、字面量创建并填充元素
# li2 = []  # 空列表
# print(li2)
# li2 = [1, 2, 3]  # 直接填充对象
# print(type(li2), li2)
#
# print("*" * 30)
#
# # 1、重复
# li = [1] * 5
# print(li)  # 打印[1, 1, 1, 1, 1]
#
# # 2、合并
# li1 = [1, 2, 3]
# li2 = [99, 100]
# print(li1 + li2)  # 打印[1, 2, 3, 99, 100]
# li1.extend(li2)
# print(li1)
#
# print("*" * 30)
#
# lisa = [1, 2, 3, 4]
# lisa.append("2")
# print(lisa)
# lisa.append(["a","b"])
# print(lisa)
# lisa.insert(2,"abcd")
# print(lisa)
#
# print("*" * 30)
#
# li = ['h', 'o', 'g', 'w', 'a', 'r', 't', 's']
# print(len(li))  # 打印 8
#
# # 1、删除指定元素'h'
# li.remove('h')
# print(li)  # 打印 ['o', 'g', 'w', 'a', 'r', 't', 's']
# print(len(li))  # 打印 7
#
# # 2、移除第一个2
# li = [1, 2, 3, 2, 1]
# li.remove(2)
# print(li)  # 打印 [1, 3, 2, 1]
#
# # 3、删除不存在的元素，会报ValueError错误
# li = [1, 2, 3]
# li.remove(100)

print("*" * 30)

nums = [2, 4, 3, 1, 5]

# 1、不传参数，默认升序，数字从小到大排列
nums.sort()
print(nums)  # 打印 [1, 2, 3, 4, 5]

# 2、指定key=len，按元素的长度排序
words = ['Python', 'Java', 'R', 'Go']
words.sort(key=len)
print(words)  # 打印 ['R', 'Go', 'Java', 'Python']

# 3、指定reverse=True，降序
nums = [2, 4, 3, 1, 5]
nums.sort(reverse=True)
print(nums)  # 打印 [5, 4, 3, 2, 1]