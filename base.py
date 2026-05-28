import sqlite3
import requests
import json  # <-- Importamos la librería nativa de JSON
from flask import Flask, Response  # <-- Usaremos Response en lugar de jsonify

app = Flask(__name__)

@app.route("/api/trm", methods=["GET"])
def obtener_datos_api():
    # 1. Traemos la TRM viva de internet
    url = "https://open.er-api.com/v6/latest/USD"
    respuesta = requests.get(url).json()
    precio_dolar = respuesta["rates"]["COP"]
    
    # 2. Conexión SQL
    conexion = sqlite3.connect("orion_empresa.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, deuda_usd FROM clientes")
    registros_db = cursor.fetchall()
    conexion.close()
    
    # 3. Procesamos los datos
    lista_clientes_procesada = []
    for fila in registros_db:
        lista_clientes_procesada.append({
            "cliente": fila[0],
            "deuda_usd": fila[1],
            "deuda_cop": fila[1] * precio_dolar
        })
        
    datos_salida = {
        "origen": "Base Orion - Medellín",
        "estado_servidor": "Operacional con Base de Datos SQL",
        "trm_usd_cop": precio_dolar,
        "clientes_pendientes": lista_clientes_procesada
    }
    
    # 4. EL TRUCO SOBERANO: Convertimos a texto asegurando UTF-8
    # 'ensure_ascii=False' obliga a Python a mantener las tildes reales
    json_limpio = json.dumps(datos_salida, ensure_ascii=False, indent=4)
    
    # Retornamos un objeto de respuesta HTTP explícito con el tipo de contenido correcto
    return Response(json_limpio, mimetype="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

