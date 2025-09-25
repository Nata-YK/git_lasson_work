from itertools import chain

from src.new import result
from src.new_1 import result_filter, result_chain


def calc_avg(my_list):
    if sum(my_list) > 0:
        return sum(my_list) / len(my_list)
    else:
        return 0

if __name__ == '__main__':
    assert calc_avg([1, 2, 3, 4]) == 2.5

    assert calc_avg([]) == 0

def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

for value in simple_generator():
    print(value)
# Задача 5
# Объедините несколько списков в один список, учитывая возможные дубликаты элементов.

list1 = [1]
list2 = [1,2]
list3 = [1,2,3]
list4 = [1,2,3,4,5,6]

result_chain = set(list(chain(list1,list2, list3,list4)))
print(result_chain)


# Задача 6
# Дан список словарей. Отфильтруйте его по ключу age и значению 30.


people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]


result_filter_list = list(filter(lambda x: x["age"] == 30,people))
print(result_filter_list)

def f():
    print('Initializing...')
    yield ('one')
    print('Continue...')
    yield ('two')
    print('Stopping...')
    yield ('three')

i = f()
print(next(i))
print(next(i))
print(next(i))
# print(next(i))
