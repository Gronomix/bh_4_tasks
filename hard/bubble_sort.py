"""
СОРТИРОВКА ПУЗЫРЬКОМ

Сначала сравниваются первые два элемента списка. Если первый элемент больше,
они меняются местами. Если они уже в нужном порядке, оставляем их как есть.
Затем переходим к следующей паре элементов, сравниваем их значения и меняем местами
при необходимости. Этот процесс продолжается до последней пары элементов в списке.

При достижении конца списка процесс повторяется заново для каждого элемента.
Это крайне неэффективно, если в массиве нужно сделать, например, только один обмен.
Алгоритм повторяется n² раз, даже если список уже отсортирован.

Для оптимизации алгоритма нужно знать, когда его остановить,
то есть когда список отсортирован.

Чтобы остановить алгоритм по окончании сортировки, нужно ввести переменную-флаг.
Когда значения меняются местами, устанавливаем флаг в значение True, чтобы повторить
процесс сортировки. Если перестановок не произошло,
флаг остаётся False и алгоритм останавливается.

Алгоритм работает в цикле while и прерывается,
когда элементы ни разу не меняются местами.
Вначале присваиваем swapped значение True,
чтобы алгоритм запустился хотя бы один раз.

ВРЕМЯ СОРТИРОВКИ: самый худший случай (изначально список отсортирован по убыванию),
затраты времени будут равны O(n²), где n — количество элементов списка.
"""
from random import randint

def bubble_sort(array: list) -> list:

    run = True
    while run:
        run = False
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index], array[index + 1]
                run = True
    return array



if __name__ == '__main__':
    assert bubble_sort([2, 1, 5, 4, 7]) == [1, 2, 4, 5, 7]
    assert bubble_sort([2, -5, -3, 3, 1, 2]) == [-5, -3, 1, 2, 2, 3]
    print('Решено!')
