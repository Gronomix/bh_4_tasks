"""
Написать функцию odd_sum, которая принимает список, который может состоять
из различных элементов.
Если все элементы списка целые числа, то функция должна посчитать сумму
нечетных чисел.
Если хотя бы один элемент не является целым числом, то выкинуть ошибку
TypeError с сообщением "Все элементы списка должны быть целыми числами"
Задачу стоит выполнить с помощью одного цикла

Написать блок if __name__ == '__main__', в котором
нужно описать обработку исключения try-except-else-finally
"""


def odd_sum(int_list: list) -> int:
    summ = 0
    for number in int_list:
        if isinstance(number, int):
            if number % 2 == 1:
                summ += number

        #else:
            #raise TypeError("Все элементы списка должны быть целыми числами")

    return summ



if __name__ == '__main__':
    assert odd_sum([1, 2, 3, 4, 5]) == 9
    print('В первом списке все числа целые')
    assert odd_sum([1, 2, 3, 'asd']) != int
    print('Решено!')

    try:
        odd_sum != int

    except TypeError:
        odd_sum = None


    finally:
        print('Во втором списке не все значения в списке целые числа')




