# chatbot.py
import requests

def initialize_chatbot(token):
    # URL de la API de Mistral
    url = "https://api.mistral.ai/v1/chat/completions"  # Asegúrate de usar la URL correcta según la documentación de Mistral

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    def conversar(mensaje):
        # Configura los datos para la solicitud
        data = {
            "model": "mistral-large-latest",  # Reemplaza con el ID del modelo de Mistral que deseas usar
            "messages": [{"role": "user", "content": mensaje}]
        }

        # Realizar la solicitud POST a la API de Mistral
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code} - {response.text}"

    # Retorna la función para interactuar con el modelo
    return conversar
