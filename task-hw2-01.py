#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

import common

# consts:

WARN_NAN = 'Некорректный ввод: введено нечисловое значение. Пожалуйста попробуйте снова.'


# # methods:

# def float_to_completed_integer(real_number: float) -> int:
#     magnitude = int(1)
#     temp = float(real_number)
#     while not temp.is_integer():
#         magnitude *= 10
#         temp = real_number * magnitude
#     return int(temp)


# def get_digits_sum(any_number):
#     no_point_number = float_to_completed_integer(any_number)
#     no_point_number = abs(no_point_number)
#     sum = 0
#     while no_point_number > 0:
#         sum += no_point_number % 10
#         no_point_number //= 10
#     return sum


# # main flow:

# user_answer = True

# while(user_answer):
#     common.Console.clear()
#     common.print_title('Сумма цифр вещественного числа')

#     fnum = common.get_user_input_float(
#         'Введите любое число: ', None, lambda _: True)

#     dsum = get_digits_sum(fnum)

#     print(f'\nСумма цифр числа {fnum} = {dsum}')
#     print()

#     user_answer = common.ask_for_repeat()

### =========================================================
### FILTER, MAP И LAMBDA ВМЕСТО ФУНКЦИЙ ПРЕОБРАЗОВАНИЯ ЧИСЛА:
### =========================================================
user_answer = True

while(user_answer):
    common.Console.clear()
    common.print_title('Сумма цифр вещественного числа')

    num_str = ''.join(filter(lambda c: c.isdigit() or c == '.', input('Введите любое число: ').replace(',', '.')))

    dsum = sum(map(int, filter(str.isdigit, num_str)))

    print(f'\nСумма цифр числа {num_str} = {dsum}')
    print()

    user_answer = common.ask_for_repeat()
