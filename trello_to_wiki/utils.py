def replace_leading_spaces_with_asterisks(string):
    stripped_str = string.lstrip()
    leading_space_cnt = len(string) - len(stripped_str)
    return f"{'*' * (leading_space_cnt // 2)}{stripped_str}"
