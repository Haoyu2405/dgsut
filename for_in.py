# # 使用for 循环遍历列表中的元素
# for i in [1, 2, 3]:
#     print(i)
#
# for i in range(1, 101):
#     print(i)
#
# # for 循环结合 range函数
# for i in range(1, 100, 2):
#     print(i)


for a in range(3):
    for b in range(5):
        print("*", end='')
    print()

list_demo = [1, 2, 3, 4, 5, 6]
# 循环遍历列表
for i in list_demo:
    # 如果i 等于三，那么跳出整个for循环
    # 不再打印后面的4、5、6
    print(i)
    if i == 3:
        break

list_demo = [1, 2, 3, 4, 5, 6]
# 循环遍历列表
for i in list_demo:
    # 如果i 等于三，那么跳过当前的循环操作
    # 继续后边打印后面的4、5、6
    if i == 3:
        continue
    print(i)
print("*" * 30)

for a in range(1, 10):
    for b in range(1, a + 1):
        print(f"{a}x{b}={a * b}", end='\t')
    print()
