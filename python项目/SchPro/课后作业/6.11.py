# 1. 编写函数，输出1~100中偶数之和
def sum_of_even_numbers():
    return sum(i for i in range(1, 101) if i % 2 == 0)


# 2. 编写函数，计算20*19*18*...*3的结果
def factorial_product(n):
    result = 1
    for i in range(n, 2, -1):
        result *= i
    return result


# 3. 编写函数，判断用户输入的整数是否为回文数
def is_palindrome(num):
    return str(num) == str(num)[::-1]


# 4. 编写函数，判断用户输入的三个数字是否能构成三角形的三条边
def can_form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


# 5. 编写函数，求2个正整数的最小公倍数
def lcm(a, b):
    # 计算最大公约数
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)


# 测试上述函数

# 1. 测试偶数之和函数
print("1~100中偶数之和:", sum_of_even_numbers())

# 2. 测试计算20*19*...*3的函数
print("20*19*...*3的结果:", factorial_product(20))

# 3. 测试回文数判断函数
num = int(input("请输入一个整数："))
print(num, "是否是回文数：", is_palindrome(num))

# 4. 测试三角形构成判断函数
a = int(input("请输入第一条边的长度："))
b = int(input("请输入第二条边的长度："))
c = int(input("请输入第三条边的长度："))
print("是否能构成三角形：", can_form_triangle(a, b, c))

# 5. 测试最小公倍数函数
num1 = int(input("请输入第一个正整数："))
num2 = int(input("请输入第二个正整数："))
print("两个数的最小公倍数：", lcm(num1, num2))