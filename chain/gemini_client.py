import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyD7_zaQY_iMf7XvY4ZAzWzcJsB3mpEhzGw")

def iniciar_conversacion(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(history=[{"role": "user", "parts": prompt}])
    return chat

def enviar_mensaje(chat, mensaje):
    # Añade el mensaje del usuario al historial y envía
    chat.history.append({"role": "user", "parts": mensaje})
    response = chat.send_message(mensaje)
    
    # Añade la respuesta del modelo al historial y retorna la respuesta
    chat.history.append({"role": "model", "parts": response.text})
    return response.text
