#Example Basic
def decorador(func):
    def wraper():
        print('iniciando funcion')
        func()
        print('terminando funcion')

    return wraper

@decorador
def other_function():
    print('funcion del medio')

other_function()


#example 2

import time

# Crea el decorator
def calc_ex(func):
    def wrapper():
        # Calcula el tiempo de ejecución.
        start = time.time()
        func()
        end = time.time()


        print(f'tiempo total de ejecución: {str(end - start)}')


    return wrapper

# Decora la funcion main() con el decorator @calc_ex que calcula el tiempo de ejecución
@calc_ex
def main():
    for n in range(0, 100000000):
        pass

# ejecuta la funcion decorada
main()
