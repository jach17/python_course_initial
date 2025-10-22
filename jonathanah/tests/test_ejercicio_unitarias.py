from src.ejercicio_unitarias import Cliente

def test_validar_email_succes():
    # Arrange
    email_valido = "email@test.com"
    
    # Llamada
    cliente_test = Cliente("Jona", email_valido)
    
    # Assert
    assert cliente_test.validar_email() is True
    