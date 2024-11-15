from transformers import pipeline
emotion_recognizer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


def detectar_emocion(mensaje):
    resultado = emotion_recognizer(mensaje)
    return resultado[0]["label"]
