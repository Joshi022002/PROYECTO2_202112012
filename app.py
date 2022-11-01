from flask import *
import os
import json 
app=Flask(__name__)

#with open(os.getcwd()+"\teams.json") as f:
 #   equipos=json.load(f)

#with open(os.getcwd()+"groups.json") as f:
 #   grupos=json.load(f)

@app.route('/ping')
def ping():
    return jsonify({"mensaje": "hola"})

@app.route('/teams')
def obtenerequipos():
    return jsonify(teams)
    if __name__ == '__main__':
        app.run(debug=True, port=5000)
