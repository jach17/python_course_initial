import requests

def get_user_data(user_id: int) -> dict:
    """Simula una llamada HTTP a un servicio externo."""
    response = requests.get(f"https://rickandmortyapi.com/api/character/{user_id}")
    if response.status_code == 200:
        return response.json()
    return {"error": "User not found"}


result = get_user_data(1)

print(result)

def apply_discount(order_total: float, discount_percent: float) -> float:
    """Calcula el total con descuento aplicado."""
    if not (0 <= discount_percent <= 100):
        raise ValueError("Invalid discount")
    return round(order_total * (1 - discount_percent / 100), 2)