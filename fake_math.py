def division(first, second):
    if second == 0:
        return 'Ошибка'
    return first / second

result1 = division(69, 3)
result2 = division(3, 0)
print(result1)
print(result2)