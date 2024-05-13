def split_list(lst):
    if len(lst) == 0:
        return [[], []]
    elif len(lst) % 2 == 0:
        midpoint = len(lst) // 2
        return [lst[:midpoint], lst[midpoint:]]
    else:
        midpoint = len(lst) // 2 + 1
        return [lst[:midpoint], lst[midpoint:]]


my_list = [1, 2, 3, 4, 5, 6, 7]
print("Початковий список:", my_list)
result = split_list(my_list)
print("Результат:", result)
