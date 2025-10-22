from abc import ABC, abstractmethod
from dependency_injector import containers, providers

# Interfaz: define comportamiento
class IRepositorioDB(ABC):
    @abstractmethod
    def guardar(self, pedido):
        pass
    
# Implementación de interfaz
class RepositorioDB(IRepositorioDB):
    def guardar(self, pedido):
        print(f"Pedido {pedido} almacenado exitosamente")
        
class ApiTercerosAdapter(IRepositorioDB):
    def guardar(self, pedido):
        print(f"Guardado pero de forma distinta: {pedido}")
        
# Lógica de negocio
class ServicePedido:
    def __init__(self, repositorio: IRepositorioDB):
        self.repo = repositorio
        
    def crear_pedido(self, pedido: str):
        print("Notificación por mensaje")
        print("Impresion de orden")
        self.repo.guardar(pedido)
        print("Notificación de almacenado")
        
        
# Dependency injector with pip package
class Contenedor(containers.DeclarativeContainer):
    repositorio = providers.Singleton(RepositorioDB)
    service = providers.Factory(ServicePedido, repositorio=repositorio)
        
container = Contenedor()
service_instance = container.service()
service_instance_two = container.service()

service_instance.crear_pedido("Pan de muerto")
service_instance_two.crear_pedido("Pan de muerto")

print(service_instance_two is service_instance)