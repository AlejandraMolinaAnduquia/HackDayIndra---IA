# Lectura de JSON
import json

def get_client_info(client_id):
    """Obtiene la información del cliente por ID."""
    with open("data/.json", "r") as file:
        data = json.load(file)
    for client in data:
        if client["ID_Cliente"] == client_id:
            return client
    return None

