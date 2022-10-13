# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

import common

# consts:

WARN_OUT_OF_RANGE = 'Ошибка: Требуется неотрицательное целое число! ' + \
    common.PLEASE_REPEAT


# # methods:

# def form_fibo_list_symmetrical(number):
#     number = abs(number)

#     # shared part for n = 1 [fib-1, fib0, fib1]:
#     fibo_list = [1, 0, 1]

#     # fill positive (common fibonacci) items:
#     # fib0 <- fibo_list[1], fib1 <- fibo_list[2]
#     for i in range(3, number+2):
#         fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

#     # fill negative (negofibonacci) items
#     for i in range(2, number+1):
#         fibo_list.insert(0, fibo_list[1] - fibo_list[0])

#     return fibo_list


# # main flow:

# user_answer = True

# while(user_answer):
#     common.Console.clear()
#     common.print_title(
#         'Объединённый симметрично список чисел Негафибоначчи\u2014Фибоначчи')

#     n = common.get_user_input_int('\nЗадайте целое число отличное от нуля: ',
#                                   WARN_OUT_OF_RANGE, lambda a: a != 0)

#     fib_lst = form_fibo_list_symmetrical(n)

#     print('Вывод:\n ', fib_lst)
#     print()

#     user_answer = common.ask_for_repeat()

# ===========================================================================
# ФОРМИРОВАНИЕ НЕГАФИБОНАЧЧИ + ФИБОНАЧЧИ ТОЛЬКО С ПОМОЩЬЮ LIST COMPREHENSION:
# ===========================================================================
user_answer = True

while(user_answer):
    common.Console.clear()
    common.print_title(
        'Объединённый симметрично список чисел Негафибоначчи\u2014Фибоначчи')

    n = common.get_user_input_int('\nЗадайте целое число отличное от нуля: ',
                                  WARN_OUT_OF_RANGE, lambda a: a != 0)
    prev = 1
    prev_prev = -1
    next = 0
    next_next = 1
    fib_lst = [(next := next_next - (next_next := next)) for _ in range(n)][::-1] + \
        [(prev := prev_prev + (prev_prev := prev)) for _ in range(n+1)]

    print('Вывод:\n ', fib_lst)
    print()

    user_answer = common.ask_for_repeat()
