"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import random
import timeit


def bubble_sort(lst):
    """
    Сортировка пузырьком
    Сложность алгоритма O(n^2)
    """

    n = 1

    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

        n += 1

    return lst


def bubble_sort_opt(lst):
    """
    Сортировка пузырьком (оптимизированная)
    Сложность алгоритма O(n^2)
    """

    n = 1

    while n < len(lst):

        need_continue = False

        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                need_continue = True

        if not need_continue:
            return lst

        n += 1

    return lst


lst = random.sample(range(-100, 100), 200)
print(lst)
print(bubble_sort(lst))
print('bubble_sort', timeit.timeit('bubble_sort(lst[:])', globals=globals(), number=1000))

lst = random.sample(range(-100, 100), 200)
print(lst)
print(bubble_sort(lst))
print('bubble_sort_opt', timeit.timeit('bubble_sort_opt(lst[:])', globals=globals(), number=1000))

"""
Результаты замеров:

bubble_sort 1.5173649
bubble_sort_opt 0.015223699999999951

Как мы видим, доработка значительно уменьшила время выполнение сортировки, так как оптимизация избавила от
бесполезных проходов, когда массив уже отсортирован
"""
