import json
import os

# Importar la clase Usuario desde el archivo usuario.py
from usuario import Usuario

# Definir los nombres de los archivos de entrada y salida
archivo_entrada = 'usuarios.txt'
archivo_errores = 'error.log'

# Crear una lista para almacenar las instancias de Usuario
usuarios = []

# Limpiar el archivo error.log si ya existe
if os.path.exists(archivo_errores):
    os.remove(archivo_errores)

# Leer el archivo usuarios.txt
with open(archivo_entrada, 'r') as archivo:
    for numero_linea, linea in enumerate(archivo, start=1):
        try:
            # Cargar la línea como un diccionario JSON
            datos_usuario = json.loads(linea)
            
            # Crear una instancia de Usuario
            usuario = Usuario(
                nombre=datos_usuario['nombre'],
                apellido=datos_usuario['apellido'],
                email=datos_usuario['email'],
                genero=datos_usuario['genero']
            )
            
            # Agregar la instancia a la lista
            usuarios.append(usuario)
        
        except (json.JSONDecodeError, KeyError) as e:
            # Manejar excepciones y escribir en error.log
            with open(archivo_errores, 'a') as archivo_error:
                archivo_error.write(f"Línea {numero_linea}: {str(e)}\n")

# Imprimir la lista de usuarios para verificar
for usuario in usuarios:
    print(f"{usuario.nombre} {usuario.apellidos}, {usuario.email}, {usuario.genero}")

