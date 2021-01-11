# asserts <bollean expresion>, <error message>

listas_de_palabras = ['Juan', 0 , 'Alberto', 'Natalia']

def primera_letra(listas_de_palabras):
    
    primeras_letras = []

    for palabra in listas_de_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es string'
            assert len(palabra) > 0, 'No se permiten Strings vacíos'

            primeras_letras.append(palabra[0])
        except AssertionError as e:
                print(e)
    return primeras_letras


print(primera_letra(listas_de_palabras))