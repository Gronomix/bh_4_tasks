"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Дана функция resolve_equation, которая принимает 3 аргумента, которые
являются коэффициентами квадратного уравнения:
    - a
    - b
    - c

Нужно отредактировать функцию таким образом, чтобы она возвращала 4 значения:
    - Дискриминант
    - Количество корней
    - Первый корень или None, если его не существует
    - Второй корень или None, если его не существует

Квадратное уравнение имеет вид:
ax2 + bx + c = 0

При его решении сначала вычисляют дискриминант по формуле:
d = b2 - 4ac, где b2 - это b**2

В зависимости от значения дискриминанта:
    - d > 0, то квадратное уравнение имеет два корня
    - d = 0, то 1 корень
    - d < 0, то корней нет

Формула поиска корней:
var1 = (-b + кв.корень(d))/2a
var2 = (-b - кв.корень(d))/2a
Когда d = 0, можно использовать любую из этих формул — получится
одно и то же число, которое и будет ответом, поэтому вычисляем только var1,
а var2 должен быть None

ПРИМЕРЫ
--------------------------------------------------------------------------------
- resolve_equation(1, -2, -3) -> (16, 2, 3, -1)
- resolve_equation(-1, -2, 15) -> (64, 2, -5, 3)
- resolve_equation(1, 12, 36) -> (0, 1, -6, None)
"""


def resolve_equation(a: float, b: float, c: float) -> tuple:
    """Решает квадратное уравнение, возвращает дискриминант и корни уравнения

    d - дискриминант
    n_var - количество корней
    var1 - первый корень
    var2 - второй корень

    :return: tuple(значение дискриминанта, количество корней,
     первый корень, второй корень)
    :rtype: tuple
    """
    d = (b_val ** 2) - (4 * (a_val * c_val))
    print(d)
    if d > 0:
        n_var = 2
        var1 = (- b_val + (0.5 ** d)) / 2 * a
        var2 = (- b_val - (0.5 ** d)) / 2 * a
    elif d == 0:
        n_var = 1
        var2 = var1 = (- b_val + (0.5 ** d)) / 2 * a
    else:
        n_var = var1 = var2 = None


    return d, n_var, var1, var2


if __name__ == '__main__':
    print('Решатель квадратных уравнений: ax2 + bx + c = 0')
    a_val = float(input('Введите a: '))
    b_val = float(input('Введите b: '))
    c_val = float(input('Введите c: '))
    print(f'Дискриминант, кол-во корней, 1 корень, 2 корень: '
          f'{resolve_equation(a_val, b_val, c_val)}')
