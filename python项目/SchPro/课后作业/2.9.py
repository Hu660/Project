import math


def calculate_circle_properties():
    # 获取用户输入的圆半径
    radius = float(input("请输入圆的半径: "))

    # 计算圆的面积
    area = math.pi * radius ** 2

    # 计算圆的直径
    diameter = 2 * radius

    # 输出结果
    print(f"圆的直径是: {diameter:.2f}")
    print(f"圆的面积是: {area:.2f}")


def calculate_remaining_trips():
    # 定义煤场剩余的煤量、大车和小车的载重
    total_coal = 29.5
    big_truck_capacity = 4
    small_truck_capacity = 2.5
    big_truck_trips = 3

    # 计算大车运走的煤量
    coal_taken_by_big_truck = big_truck_capacity * big_truck_trips

    # 计算剩余的煤量
    remaining_coal = total_coal - coal_taken_by_big_truck

    # 计算还需要小车运送几次
    remaining_trips = -(-remaining_coal // small_truck_capacity)  # 使用负负得正的方式实现向上取整

    # 输出结果
    print(f"大车运送了{big_truck_trips}次，每次载重{big_truck_capacity}t，总共运送了{coal_taken_by_big_truck}t煤。")
    print(f"剩余{remaining_coal:.2f}t煤需要用小车运送。")
    print(f"小车每次载重{small_truck_capacity}t，还需要运送{remaining_trips}次才能送完。")


# 调用函数

# 调用函数
calculate_circle_properties()

calculate_remaining_trips()
