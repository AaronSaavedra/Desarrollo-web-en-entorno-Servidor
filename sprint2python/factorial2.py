def func_factorial2(n):
    f = 1
    while (n > 0):
        f = f*n
        n = n-1
    return f

numero=int(input ("Teclea un número: "))
print(func_factorial2(numero))