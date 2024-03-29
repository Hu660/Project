import shutil


# 第一个功能：读取文件并打印除以#开头的行之外的所有行
def print_lines_without_comments(filename):
    with open(filename, 'r') as file:
        for line in file:
            if not line.lstrip().startswith('#'):
                print(line, end='')

            # 第二个功能：实现文件备份的功能


def backup_file(source_filename, backup_filename):
    shutil.copy2(source_filename, backup_filename)
    print(f"文件已成功备份为 '{backup_filename}'\n")


# 第三个功能：读取存储数字的文件，排序后输出
def sort_numbers_in_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            # 假设每行只有一个数字，并且没有额外的空格或字符
            number = float(line.strip())  # 使用float可以处理整数和浮点数
            numbers.append(number)
    sorted_numbers = sorted(numbers)
    for number in sorted_numbers:
        print(number, end=' ')

    # 示例使用


# 读取文件并打印除以#开头的行之外的所有行
print_lines_without_comments('input2.txt')

# 备份文件
backup_file('input.txt', 'input_backup.txt')

# 读取存储数字的文件，排序后输出
sort_numbers_in_file('numbers.txt')
