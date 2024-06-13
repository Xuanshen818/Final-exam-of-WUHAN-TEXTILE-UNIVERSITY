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

#使用函数

def calculate_average(n, numbers):
    if n == 0:
        return 0.0
    average = sum(numbers) / n
    return round(average, 4)

# 输入正整数 n
n = int(input("请输入正整数n: "))

# 输入 n 个整数
numbers = []
for _ in range(n):
    num = int(input("请输入一个整数: "))
    numbers.append(num)

# 计算平均值
average = calculate_average(n, numbers)

# 输出平均值
print(f"{average:.4f}")

