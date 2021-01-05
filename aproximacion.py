objetivo = int(input('Escriba un número: '))
epsilon = 0.01 #error que se tiene
paso = epsilon**2 #que tanto se aprox.
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No es posible encontrar un {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es aprox. {respuesta} ')