figs = ['circle', 'square', 'triangle']  # Список фигур
funcs = ['perimeter', 'area']  # Список функций
sizes = {"area-circle": 1,
         "perimeter-circle": 1,
         "area-square": 1,
         "perimeter-square": 1,
         "perimeter-triangle": 3,
         "area-triangle": 3
         }  # Словарь для хранения аргументов


def calc(fig, func, size):
    '''Функция для вычисления периметра или площади заданной фигуры
    Параметры:
    fig - имя фигуры
    func - функция для выполнения
    size - список размеров'''
    if fig not in figs:
        raise ValueError(f"Invalid figure: {fig}. Available figures: {figs}.")
    if func not in funcs:
        raise ValueError(f"Invalid function: {func}. Available functions: {funcs}.")
    expected_size_cnt = sizes.get(f"{func}-{fig}", 1)
    if len(size) != expected_size_cnt:
        raise ValueError(f"Expected {expected_size_cnt} size(s) for {fig}-{func}, but got {len(size)}.")
    if any(s < 0 for s in size):
        raise ValueError("Sizes must be non-negative.")

    result = eval(f'{fig}.{func}(*{size})')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}: \n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}: \n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    calc(fig, func, size)
