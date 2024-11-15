import circle
import square


figs = ['circle', 'square'] #Список фигур
funcs = ['perimeter', 'area'] #Список функций
sizes = {} #Словарь для хранения аргументов

def calc(fig, func, size):
	'''Функция для вычисления периметра или площади заданной фигуры
	Параметры:
	fig - имя фигуры
	func - функция для выполнения
	size - список размеров'''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



