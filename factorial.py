def factorial(n):
    """
    Calculamos el factorial de n

    returns n!
    """
    if n == 1:
        return 1
    
    return n * factorial(n -1)

n = int(input('Escriba un número entero: '))

print(factorial(n))