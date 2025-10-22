class Producto:
    ''' Clase producto. Propiedades de un producto. '''
    
    def __init__(self, nombre: str, precio: float):
        '''Constructor de clase'''
        self.nombre = nombre
        self.precio = precio
        
producto_uno = Producto("Pan integral", 3.2)

print(f"Producto 1: {producto_uno.nombre} costo de {producto_uno.precio}")

# Property y setter

class ProductoSetter:
    ''' Clase producto. Propiedades de un producto. '''
    
    def __init__(self, nombre: str, precio: float):
        '''Constructor de clase'''
        self.nombre = nombre
        self.precio = precio
    
    @property    
    def precio(self) -> float:
        ''' Getter. Nos permite acceder a la propiedad de .precio pero sin pasarle los parentecis'''
        return self._precio
    
    @precio.setter
    def precio(self, value: float):
        '''Nos permite modificar el valor de la propiedad precio, y aplicar validaciones'''
        if value <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self._precio = value
        
    def __str__(self) -> str:
        '''Metodo especial que nos permite el llamado para convertir a cadena de texto'''
        return f"--- El producto {self.nombre} tiene un costo de {self.precio}"
        


producto_dos = ProductoSetter("Pan con linzasa", 32.0)

print(producto_dos)

print(f"Producto 2: {producto_dos.nombre} costo de {producto_dos.precio}")

producto_dos.precio = 89

print(f"Producto 2: {producto_dos.nombre} costo de {producto_dos.precio}")
