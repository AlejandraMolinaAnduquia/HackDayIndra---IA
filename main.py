from flask import Flask, request, jsonify
from chain.prompt_handler import procesar_mensaje
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Endpoint para obtener el JSON de los clientes
@app.route('/api/clientes', methods=['GET'])
def obtener_clientes():
    with open('data/db.json', 'r', encoding='utf-8') as file:
        clientes = json.load(file)
    return jsonify(clientes)

@app.route('/api/cobranza', methods=['POST'])
def cobrar():
    datos = request.get_json()
    respuesta = procesar_mensaje(datos)
    return jsonify({"respuesta": respuesta})
    

if __name__ == "__main__":
    app.run(debug=True)
