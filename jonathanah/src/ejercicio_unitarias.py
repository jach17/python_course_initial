class Cliente:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
    
    def validar_email(self) -> bool:
        '''Valida la estructura de mi correo'''
        return "@" in self.correo and "." in self.correo
    
    
client = Cliente("Jony", "cor@re.o")

print(client.validar_email())