from chain.gemini_client import iniciar_conversacion, enviar_mensaje
from chain.emotion_recognition import detectar_emocion

def procesar_mensaje(datos):
    # emocion = detectar_emocion(datos["mensaje_cliente"])
    # prompt = f"Asistente de cobranza: Cliente {datos['nombre_cliente']} debe {datos['deuda']}. Emoción: {emocion}. Responde:"
    
    prompt = f"Actúa como un asistente de cobranza profesional: Cliente {datos['nombre_cliente']} debe {datos['deuda']}. Responde de manera breve y directa. Responde:"
    chat = iniciar_conversacion(prompt)
    return enviar_mensaje(chat, datos["mensaje_cliente"])
