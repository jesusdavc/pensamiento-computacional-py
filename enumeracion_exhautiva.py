objetivo = int(input('Escoje un numero: '))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1
    print(respuesta)
if respuesta**2 == objetivo:
    print(f'La raiz cuadrada exacta de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene raiz cuadrada exacta')