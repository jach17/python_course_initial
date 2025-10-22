# Comentario en una linea

"""
    Para comentarions multilinea usamos
    triple comilla
    
"""

'''
    Comentario 
    multilinea
'''


variable_numero = 3
variable_bool = False

print(type(variable_numero))

variable_numero = "Hola"


print(type(variable_numero))

a, b, c = 1, 2, 3

print(a + b)

a = b = c = 2

print(a*a)

#Compresiones
# Lista de numeros
numeros = [1, 2, 3, 4, 5]

pares = [numero for numero in numeros if numero % 2 == 0]

print(type(pares))
print(pares)