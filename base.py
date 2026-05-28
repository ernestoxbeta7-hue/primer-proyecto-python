import requests
from flask import Flask, jsonify

# Inicializamos la aplicación Flask
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# Definimos la ruta de navegación (La URL de nuestra API)
@app.route("/api/trm", methods=["GET"])
def obtener_trm_corporativa():
    # 1. Consumimos los datos de internet como la sesión anterior
    url = "https://open.er-api.com/v6/latest/USD"
    respuesta = requests.get(url).json()
    precio_dolar = respuesta["rates"]["COP"]
    
    # 2. Creamos la estructura de datos empresarial
    datos_salida = {
        "origen": "Base Orion - Medellín",
        "estado_servidor": "Operacional",
        "trm_usd_cop": precio_dolar,
        "clientes_pendientes": [
            {"cliente": "Carlos Mendoza", "deuda_usd": 150, "deuda_cop": 150 * precio_dolar},
            {"cliente": "Almacenes Alfa", "deuda_usd": 500, "deuda_cop": 500 * precio_dolar},
            {"cliente": "Dra. Betancur", "deuda_usd": 250, "deuda_cop": 250 * precio_dolar}
        ]
    }
    
    # 3. jsonify convierte nuestro diccionario de Python en formato JSON estándar internacional
    return jsonify(datos_salida)

# Encendemos el servidor en el puerto 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

