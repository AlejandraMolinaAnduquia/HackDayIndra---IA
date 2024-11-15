from flask import Flask, request, jsonify
from chain.prompt_handler import procesar_mensaje
from audio.audio import GrabadoraDeVoz

app = Flask(__name__)

@app.route('/api/cobranza', methods=['POST'])
def cobrar():
    datos = request.get_json()
    respuesta = procesar_mensaje(datos)
    return jsonify({"respuesta": respuesta})
    

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
    app.run(debug=True)
    main()
