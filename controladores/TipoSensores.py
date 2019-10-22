from flask import jsonify, request
from db.db import cnx

class TipoSensor():
    global cur
    cur = cnx.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM tipo_sensores")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]

        for row in rows:
            registro = zip(columns, row)

            json = dict(registro)
            lista.append(json)
        
        return jsonify(lista)
        cnx.close
    
    def create(body):
        data = (body['codigo'],body['nombre'],body['descripcion'],body['tipoIndicador'],body['prioridad'])

        sql = 'INSERT INTO tipo_sensores(codigo, nombre, descripcion, tipoIndicador, prioridad) VALUES(%s, %s, %s, %s, %s)'
        cur.execute(sql,data)
        cnx.commit()
        return {'estado':'insertado'}, 200