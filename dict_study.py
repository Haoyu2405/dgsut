# """字典使用：创建"""
# # 1、使用大括号填充键值对
# dc = {'name': 'Harry Potter', 'age': 18}
# print(type(dc), dc)
#
# # 2、使用字典构造方法
# dc1 = dict()  # 空字典
# dc2 = dict(name="Harry Potter", age=18)  # 关键字参数赋值
# print(type(dc2), dc2)
# dc3 = dict([("name", "Harry Potter"), ("age", 18)])
# print(type(dc3), dc3)
#
# print("*" * 30)
#
# """字典使用：访问元素"""
# dc = {"name": "Harry Potter", "age": 18}
# # 1、访问存在的key
# print(dc["name"])
# print(dc["age"])
#
# # 2、访问不存在的key，会报KeyError错误
# print(dc['hobby'])
#
# print("*" * 30)

"""字典使用：操作元素"""
dc = {"name": "Harry Potter", "age": 18}
# 1、修改年龄，改为20
dc['age'] = 20
print(dc)

# 2、新增hobby字段
dc['hobby'] = 'Magic'
print(dc)

print("*" * 30)

"""字典方法 keys()"""
dc = {"name": "Harry Potter", "age": 18}
keys = dc.keys()
print(type(keys), keys)

# 1、遍历查看所有的键
for key in keys:
    print(key)

# 2、将视图对象转成列表
print(list(keys))

print("*" * 30)

"""字典方法 values()"""
dc = {"name": "Harry Potter", "age": 18}
values = dc.values()
print(type(values), values)

# 1、遍历查看所有的值
for value in values:
    print(value)

# 2、将视图对象转成列表
print(list(values))

print("*" * 30)

"""字典方法 items()"""
dc = {"name": "Harry Potter", "age": 18}
items = dc.items()
print(type(items), items)

# 1、遍历查看所有的项
for item in items:
    print(item)

# 2、将视图对象转成列表
print(list(items))

for k, v in items:
    print(f"字典的键{k}的值为{v}")

print("*" * 30)

"""字典方法 get()"""
dc = {"name": "Harry Potter", "age": 18}

# 1、访问存在的key
name = dc['name']
print(name)

# 2、访问不存在的key
hobby = dc.get('hobby', {}).get("age")
print(hobby)

a = dc.pop("age")
print(a)
print(dc)

print("*" * 30)

new_dic = dict()
new_dic["str_key"] = "hogwarts"
new_dic["list_key"] = ["hogwarts", "harry", 12]
new_dic["int_key"] = 27
new_dic["dict_key"] = {"age": 18, "name": "harry"}
new_dic["rm_key"] = "will delete"
print(new_dic)
new_dic.pop("rm_key")
print(new_dic)
print(new_dic.get("dict_key", {}).get("age"))

print("*" * 30)
