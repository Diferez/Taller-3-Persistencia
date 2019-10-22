from flask import Flask, jsonify, request
from flask_cors import CORS
from controladores.TipoSensores import TipoSensor

app = Flask(__name__)
CORS(app)

@app.route('/tipoSensores', methods=['GET'])
def getAll():
    return (TipoSensor.list())

@app.route('/tipoSensores', methods=['POST'])
def postOne():
    body = request.json
    return(TipoSensor.create(body))


app.run(port=5000, debug=True)