# 判断偶数
def isevenNum():
    num = 0

    # 使用while循环
    while num <= 100:
        if num % 2 == 0:
            print(num)
        num += 1


# 判断数
def gudgmentNum():
    num = float(input("\n请输入一个数字: "))

    # 判断并输出
    if num > 0:
        print("这是一个正数")
    elif num < 0:
        print("这是一个负数")
    else:
        print("这是零")


# 定义一个函数来检查一个数是否为质数
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 判断100以内的质数
def prime():
    for num in range(2, 101):
        if is_prime(num):
            print(num)

# isevenNum()
# gudgmentNum()
# is_prime(2)
prime()