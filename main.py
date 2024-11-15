# main.py
import os
from chain.chatbot import initialize_chatbot

# Token de Mistral
mistral_token = os.environ.get("MISTRAL_API_KEY")

# Inicializa el chatbot
chatbot = initialize_chatbot(mistral_token)

# Prueba el chatbot enviando un mensaje de ejemplo
mensaje = "¿como estas?"
respuesta = chatbot(mensaje)

print("Bot:", respuesta)
