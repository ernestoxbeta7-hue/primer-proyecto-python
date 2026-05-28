# Una base de datos real simulada: Una lista que contiene diccionarios
usuarios_empresa = [
    {"nombre": "Ernesto", "correo": "ernesto@orion.com", "rol": "Admin", "activo": True},
    {"nombre": "Emilia", "correo": "emilia@orion.com", "rol": "Desarrollador", "activo": True},
    {"nombre": "Carlos", "correo": "carlos@gmail.com", "rol": "Cliente", "activo": False}
]

print("=== SISTEMA DE GESTIÓN DE USUARIOS ===")

# Función para buscar y filtrar datos en la base
def filtrar_usuarios_activos(lista_usuarios):
    print("\n>> Filtrando usuarios activos en el sistema...")
    for usuario in lista_usuarios:
        # Evaluamos una condición dentro del diccionario
        if usuario["activo"] == True:
            print(f"✔ [ACTIVO] {usuario['nombre']} ({usuario['correo']}) - Rol: {usuario['rol']}")
        else:
            print(f"❌ [INACTIVO] {usuario['nombre']} - Cuenta suspendida.")

# Ejecutamos nuestra lógica de negocio
filtrar_usuarios_activos(usuarios_empresa)

