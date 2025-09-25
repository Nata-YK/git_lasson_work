# Генераторные выражения тема 11.1 пунк 5
# Пример создадим генераторное выражение и вызовем его в функции print6()

def print6(xs):
    for i, x in enumerate(xs):
        print(x)
        if i == 5:
            break


i = (x*x for x in range(10))

print6(i)

print('#'*5)
print6(i)

# Пример создать генераторное выражение от 1 до 100, отфильтровать четные числа, возведем эти числа в квадрат и суммируем их


result = (x*x for x in range(1, 101) if x % 2 == 0)
print(sum(result))

# Напишите генераторное выражение, которое возвращает кубы четных чисел от 0 до 10. cubes = (x**3 for x in range(11) if x % 2 == 0)
cube_even = (x**3 for x in range(11) if x % 2 == 0)

print(list(cube_even))

# Задача 2
# Напишите функцию, которая принимает список чисел и возвращает сумму квадратов положительных чисел в этом списке.
# Используйте для этого генераторное выражение.    def sum_of_squares(lst):
#                                                       return sum(x**2 for x in lst if x > 0)

list_num = [1,2,-1,-3,0,-5,7,8,9]

result_positive = (x*x for x in list_num if x > 0)
print(sum(result_positive))

# Задача 3
# Напишите генераторное выражение, которое возвращает буквы строки "hello", но только если они являются гласными.
# Решение vowels = (x for x in "hello" if x in ['a', 'e', 'i', 'o', 'u'])
vowels = "aeoui"
letter_list = (l for l in "hello" if l.isalpha() and l in vowels)

print(list(letter_list))

# Задача 4
# Найдите среднее арифметическое всех чисел, кратных 3 или 5, в диапазоне от 1 до 100 включительно.

multiple_num = list((num for num in range(1, 101) if num % 3 == 0 or num % 5 == 0))
print(sum(multiple_num) / len(multiple_num))
# НЕ ЗАБЫВАЕМ ОБОРАЧИВАТЬ В LIST  ИНАЧЕ не sum не len не будут работать
numbers = range(1, 101)
filtered_numbers = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers))
average = sum(filtered_numbers) / len(filtered_numbers)
print(average)


