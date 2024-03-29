print("------------------类-----开始----------")


def testa():
    age = int(input("输入您的年龄:"))
    if age < 18:
        print("您是未成年")
    elif age < 66:
        print("您是青年人")
    elif age < 80:
        print("您是青年人")
    elif age < 100:
        print("您是青年人")
    else:
        print("您是长寿老人")


if __name__ == '__main__':
    print("------------__main__------开始------------")
    testa()
    print("------------------------结束--------------")
