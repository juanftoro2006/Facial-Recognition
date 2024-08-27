from flask import Flask, jsonify
import detector  # Asegúrate de importar correctamente tu programa de reconocimiento facial

app = Flask(__name__)

@app.route('/recognize', methods=['GET'])
def recognize():
    # Aquí es donde ejecutas tu programa de reconocimiento facial
    result = detector.run()  # Reemplaza esto con la función que ejecuta el reconocimiento facial
    return jsonify(result)  # Devuelve los resultados en formato JSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

