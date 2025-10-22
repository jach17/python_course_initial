
#Funcion
def saludar(nombre: str) -> None:
    ''' Funcion que devuelve un saludo '''
    return f"Hola {nombre}"


print(saludar("Jona"))

# Funcion con argumendo por default
def saludo_generico(nombre = "Usuario"):
    return f"Hola {nombre}"


print(saludo_generico("Jonn"))


# Funcion con argumendo kwargs


#lambda

def suma(num1: int, num2: int) -> int:
    '''Suma de dos numeros'''
    return num1 + num2


suma_lambda = lambda n1, n2 : n1 + n2


print(suma(2, 3))
print(suma_lambda(2, 3))

# Map y filter

# Map

'''
    Un map nos modifica cada elemento de mi lista
    Un filter nos selecciona cada elemento de mi lista
'''
lista_numeros = [1, 2, 3, 4, 5]

print("Antes de map y de filter")
print(lista_numeros)

cuadrados = list(map(lambda x: x**2, lista_numeros))


print(cuadrados)

# filter

pares = list(filter(lambda x: x%2 == 0, lista_numeros))

print(pares)

print("Despues de map y de filter")
print(lista_numeros)