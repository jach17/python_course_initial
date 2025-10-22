# args

# Argumentos posicionales
def procesar_datos(*param) -> None:
    ''' Recibe argumentos posicionales '''
    print(f"Argumentos: {param}")
    
# Keyword arguments
def procesar_datos_kw(**clv) -> None:
    ''' Recibe argumentos por clave valor '''
    print(f"Argumentos: {clv}")
    
    
procesar_datos(10, 50, 5, 4, 2)
procesar_datos_kw(nombre="Jona", status=True)