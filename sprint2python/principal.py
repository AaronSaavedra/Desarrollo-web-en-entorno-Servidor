from re import A
from factorial import factorial
from factorial2 import func_factorial2
print('MENU')
print('a) primer algoritmo')
print('b) segundo algoritmo')
op = input('Teclea una opción: ')
if op == 'a':
    numero=int(input ("Teclea un número: "))
    print(factorial(numero))
elif op == 'b':
    numero=int(input ("Teclea un número: "))
    print(func_factorial2(numero))
else:
    print('La opción tecleada es inválida.')