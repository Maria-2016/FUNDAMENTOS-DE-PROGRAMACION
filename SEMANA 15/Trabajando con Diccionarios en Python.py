#Tarea: Trabajando con Diccionarios en Python
#Objetivo: Utilizar diccionarios en Python para representar información estructurada y realizar operaciones comunes.
#Crear un Diccionario:
#Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".

# 1. Crear un Diccionario
informacion_personal = {
    "nombre": "María Vera",
    "edad": 27,
    "ciudad": "Esmeraldas",
    "profesion": "Ingeniera en TIC"
}

# Imprimir los valores
print("\nInformacion personal:")
print("nombre :", informacion_personal["nombre"])
print("edad :", informacion_personal["edad"])
print("ciudad :", informacion_personal["ciudad"])
print("profesion :", informacion_personal["profesion"])

# 2. Acceder y modificar valores
print("\nModificando la ciudad:")
informacion_personal["ciudad"] = "Santo Domingo"
print("nombre :", informacion_personal["nombre"])
print("edad :", informacion_personal["edad"])
print("ciudad :", informacion_personal["ciudad"])
print("profesion :", informacion_personal["profesion"])

#3. Verificar existencia de claves/ Agregar una nueva clave-valor 'telefono' si no existe
print("\nVerificando si existe la clave 'telefono':")
informacion_personal["telefono"] = "0989358138"
print("Clave 'telefono' añadida:" , informacion_personal)

# 4. Eliminar una clave 'edad' del diccionario
print("\nEliminando la clave 'edad':")
del informacion_personal ["edad"]
print("Clave 'edad' eliminada:", informacion_personal)

#5. Imprimir el Diccionario final
print("\nDiccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave} : {valor}")