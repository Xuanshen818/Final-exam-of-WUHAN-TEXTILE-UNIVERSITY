'''
2.Python-循环结构-02(M)
【问题描述】输入正整数n，然后再输入n个整数，求n个整数的平均值并输出
精确到小数点后 4 位
【样例输入】
5
15
2
3
50
30
【样例输出】
20.0000
'''

#使用for循环

# 输入正整数 n
n = int(input("请输入正整数n: "))

# 输入 n 个整数，并计算它们的总和
total = 0
for _ in range(n):
    num = int(input("请输入一个整数: "))
    total += num

# 计算平均值
if n == 0:
    average = 0.0
else:
    average = total / n

# 输出平均值，精确到小数点后 4 位
print(f"{average:.4f}")
