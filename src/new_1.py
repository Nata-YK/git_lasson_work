

print(42)
print("Hi")

def is_even(x):
    return x % 2 == 0

result_filter = list(filter(is_even, range(20)))

def dup(x):
    return [x, x]
# Функция map() применяет функцию dup ко всему списку: result_filter, т.е. синтаксис map(функция, список)
result_map = list((map(dup, result_filter)))

# Далее развернем последовательность, список result_filter в один список, сечас он [[]] какбы список в списке
# для этого вызовем метод chain
from itertools import chain

result_chain = list(chain(*result_map))

print(result_chain)

num = [1,2,3,4,5,6]
filter_num = list(filter(lambda x: x % 2 == 0, num))
print(filter_num)


# Получить список числел которые делятся на 3 или на 5 в диапазоне от 1 до 100
# создадим диапазон, до 101, т.к. последний не берется в расчет, а первое число означает начало списка, т.к. 0 не нужен.
number = range(1,101)

result_num = [x for x in number if x % 3 == 0 or x % 5 == 0]

print(result_num)

result_number = [x for num in range(20) for x in [num, num] if num % 2 == 0]

print(result_number)

