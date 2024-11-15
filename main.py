from audio.audio import GrabadoraDeVoz

def main():
    # Instanciamos la clase GrabadoraDeVoz
    grabadora = GrabadoraDeVoz()  # Puedes pasar otros parámetros si lo necesitas, como el umbral de silencio o la duración

    # Grabar audio
    archivo_wav = grabadora.grabar_audio()

    # Reconocer el texto del audio
    texto = grabadora.reconocer_voz()

    if texto:
        # Imprimir el texto reconocido
        print("Texto reconocido:", texto)

    # Convertir y guardar el archivo en formato MP3
    archivo_mp3 = grabadora.convertir_a_mp3()

if __name__ == "__main__":
    main()
