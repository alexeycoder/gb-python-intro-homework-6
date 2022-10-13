# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import prod
import common

# consts:

WARN_OUT_OF_RANGE = 'Ошибка: Число должно быть натуральным! Пожалуйста попробуйте снова.'

# # methods:

# def calc_fact(number):
#     if number == 0:
#         return 1
#     fact = 1
#     i = 2
#     while i <= number:
#         fact *= i
#         i += 1
#     return fact


# # main flow:

# user_answer = True

# while(user_answer):
#     common.Console.clear()
#     common.print_title('Формирование списка произведений чисел от 1 до N')

#     n = common.get_user_input_int(
#         'Введите натуральное число N: ', WARN_OUT_OF_RANGE, lambda x: x > 0)

#     lst = [calc_fact(i) for i in range(1, n+1)]

#     print(f'\nВывод: {n} -> {lst}')

#     print()
#     user_answer = common.ask_for_repeat()

### ==========================================
### MAP И LAMBDA ВМЕСТО ИСПОЛЬЗОВАНИЯ ФУНКЦИИ:
### ==========================================
user_answer = True

while(user_answer):
    common.Console.clear()
    common.print_title('Формирование списка произведений чисел от 1 до N')

    n = common.get_user_input_int(
        'Введите натуральное число N: ', WARN_OUT_OF_RANGE, lambda x: x > 0)

    lst = list(map(lambda i: prod(range(1, i+1)), range(1, n+1)))

    print(f'\nВывод: {n} -> {lst}')

    print()
    user_answer = common.ask_for_repeat()
