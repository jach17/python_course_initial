# '''
#     Inyección de dependencias por constructor
# '''
# # Clase que almacena el pedido
# class RepositorioBD:
#     def guardar(self, pedido: str):
#         print(f"Pedido {pedido} almacenado exitosamente")
        
# # Clase que implementa lógica de negocio del pedido
# class ServicePedidos:
#     def __init__(self, repositorio: RepositorioBD):
#         self.repositorio = repositorio
        
#     def crear_pedido(self, pedido: str):
#         print("Notificación por mensaje")
#         print("Impresion de orden")
#         self.repositorio.guardar(pedido)
#         print("Notificación de almacenado")
    
# # Inyección de dependencias por constructor
# repo = RepositorioBD()
# service = ServicePedidos(repo)

# # Llamada a servicio
# service.crear_pedido("hamburguesita")




#####
#####



# '''
#     Inyección de dependencias por setter
# '''
# # Clase que almacena el pedido
# class RepositorioBD:
#     def guardar(self, pedido: str):
#         print(f"Pedido {pedido} almacenado exitosamente")
        
# # Clase que implementa lógica de negocio del pedido
# class ServicePedidos:
#     def set_repo(self, repositorio: RepositorioBD):
#         ''' Inicializa la instancia de mi repositorio '''
#         self.repositorio = repositorio
    
#     def crear_pedido(self, pedido: str):
#         print("Notificación por mensaje")
#         print("Impresion de orden")
#         self.repositorio.guardar(pedido)
#         print("Notificación de almacenado")
    
# # Inyección de dependencias por constructor
# repo = RepositorioBD()
# service = ServicePedidos()

# # Llamada al setter
# service.set_repo(repo)

# # Llamada a servicio
# service.crear_pedido("hamburguesita")


# '''
#     Interfaces como patrones
# '''

# from abc import ABC, abstractmethod

# class IRepositorioDB(ABC):
#     @abstractmethod
#     def guardar(self, pedido):
#         pass
    
# class RepositorioDB(IRepositorioDB):
#     def guardar(self, pedido):
#         print(f"Pedido {pedido} almacenado exitosamente")
        
# class ApiTercerosAdapter(IRepositorioDB):
#     def guardar(self, pedido):
#         print(f"Guardado pero de forma distinta: {pedido}")
        

# class ServicePedido:
#     def __init__(self, repositorio: IRepositorioDB):
#         self.repo = repositorio
        
#     def crear_pedido(self, pedido: str):
#         print("Notificación por mensaje")
#         print("Impresion de orden")
#         self.repo.guardar(pedido)
#         print("Notificación de almacenado")
        
# repoDB: IRepositorioDB = RepositorioDB()
# repoApi: IRepositorioDB = ApiTercerosAdapter()

# service = ServicePedido(repoApi)

# service.crear_pedido("tacos")
    
# '''
#     Inyeccion manual de dependencias
# '''

# class Container:
#     def __init__(self):
#         self._servicios = {}
        
#     def register(self, nombre, creator):
#         self._servicios[nombre] = creator
        
#     def resolver(self, nombre):
#         return self._servicios[nombre]()
    
# container = Container()
# container.register("repositorio", lambda: ApiTercerosAdapter())
# container.register("service", lambda: ServicePedido(container.resolver("repositorio")))


# service = container.resolver("service")

# service.crear_pedido("Taquitos")