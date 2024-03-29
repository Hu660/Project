"""
用python编写
已知列表li——num1 = [4，5，2，7] 和 li_num2 = [3,6] ,
请将这两个列表合并为一个列表，并将合并后的列表中的元素按降序排列

已知元组 tu_num1 = ('p','y','t',['o','n']) 请向元组的最后一个列表中添加新元素’h‘

已知字符串 str = 'skdaskerkjsalkj' 请统计该字符串中个字母出现的次数

已知列表li_one = [1,2,1,2,3,5,4,3,5,7,4,7,8],请删除列表li_one中的重复数据
"""

# 问题一：合并列表并按降序排列
li_num1 = [4, 5, 2, 7]
li_num2 = [3, 6]
merged_list = li_num1 + li_num2
sorted_list = sorted(merged_list, reverse=True)
print("合并后的列表并按降序排列:", sorted_list)

# 问题二：向元组的最后一个列表中添加元素
tu_num1 = ('p', 'y', 't', ['o', 'n'])
new_inner_list = tu_num1[-1] + ['h']
new_tuple = tu_num1[:-1] + (new_inner_list,)
print("向元组的最后一个列表中添加元素后的元组:", new_tuple)

# 问题三：统计字符串中各个字母出现的次数
str_text = 'skdaskerkjsalkj'
letter_counts = {}
for letter in str_text:
    if letter.isalpha():
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
print("字符串中各个字母出现的次数:", letter_counts)

# 问题四：删除列表中的重复数据
from collections import OrderedDict
li_one = [1, 2, 1, 2, 3, 5, 4, 3, 5, 7, 4, 7, 8]
li_one_unique_ordered = list(OrderedDict.fromkeys(li_one))
print("删除列表中的重复数据后的列表:", li_one_unique_ordered)