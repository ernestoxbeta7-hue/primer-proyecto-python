import requests

def procesar_finanzas_empresa():
    print("=== INICIANDO SISTEMA FINANCIERO AUTOMÁTICO ===")
    
    # 1. Traemos el precio real del dólar en Colombia usando una API pública
    print(">> Conectando con el servidor financiero en internet...")
    url = "https://open.er-api.com/v6/latest/USD"
    respuesta = requests.get(url).json()
    
    # Extraemos el valor del dólar en pesos colombianos (COP)
    precio_dolar = respuesta["rates"]["COP"]
    print(f">> ÉXITO: Valor del Dólar detectado hoy: ${precio_dolar} COP\n")
    
    # 2. Base de datos simulada de clientes que deben facturas en USD
    facturas_pendientes = [
        {"cliente": "Carlos Mendoza", "monto_usd": 150},
        {"cliente": "Almacenes Alfa", "monto_usd": 500},
        {"cliente": "Dra. Betancur", "monto_usd": 250}
    ]
    
    # 3. Procesamos los datos y generamos el archivo de reporte para contabilidad
    nombre_reporte = "reporte_financiero.txt"
    with open(nombre_reporte, "w") as archivo:
        archivo.write("=========================================\n")
        archivo.write("   REPORTE DE CARTERA TRADUCIDO A COP\n")
        archivo.write(f"   Tasa de Cambio Utilizada: $ {precio_dolar} COP\n")
        archivo.write("=========================================\n\n")
        
        for factura in facturas_pendientes:
            # Calculamos la conversión matemática exacta
            valor_en_cop = factura["monto_usd"] * precio_dolar
            
            # Escribimos los datos limpios en el archivo
            archivo.write(f"• Cliente: {factura['cliente']}\n")
            archivo.write(f"  Deuda: {factura['monto_usd']} USD  -->  $ {valor_en_cop:,.2f} COP\n")
            archivo.write("-----------------------------------------\n")
            
    print(f">> ¡Reporte '{nombre_reporte}' generado con éxito en el disco!")

# Ejecutamos el automatizador
procesar_finanzas_empresa()

