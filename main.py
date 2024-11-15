from flask import Flask, request, jsonify
from chain.prompt_handler import procesar_mensaje

app = Flask(__name__)

@app.route('/api/cobranza', methods=['POST'])
def cobrar():
    datos = request.get_json()
    respuesta = procesar_mensaje(datos)
    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(debug=True)
