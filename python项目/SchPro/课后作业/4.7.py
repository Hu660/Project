s = 'AbcDeFGhIJ'
lowercase_count = sum(1 for c in s if c.islower())
print(f"字符串小写字母的数量为{lowercase_count}")

original_string = 'life is short.I use python'
substring_to_check = 'python'
new_substring = 'Python'
if substring_to_check in original_string:
    new_string = original_string.replace(substring_to_check,new_substring)
    print(f'替换后的字符串为:{new_string}')
else:
    print(f'源字符中不包含{substring_to_check}')