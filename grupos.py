#!/usr/bin/env python3
import os
import pwd
import sys
import subprocess

def obtener_usuarios(directorio):
    usuarios = set()
    for ruta_actual, directorios, archivos in os.walk(directorio):
        for nombre_archivo in archivos + directorios:
            ruta_completa = os.path.join(ruta_actual, nombre_archivo)
            permisos = os.stat(ruta_completa).st_mode
            if (permisos & 0o400) or (permisos & 0o100):
                usuario = os.stat(ruta_completa).st_uid
                nombre_usuario = pwd.getpwuid(usuario).pw_name
                usuarios.add((usuario, nombre_usuario))
    return usuarios

def mostrar_ayuda():
    print("Uso: ./mostrar_usuarios.py [directorio]")
    print("\nEste script muestra los usuarios con permisos de lectura o ejecución en el directorio especificado.")
    print("\nArgumentos:")
    print("  [directorio]  Ruta del directorio a analizar (opcional si se proporciona como argumento).")

def obtener_grupos_usuario():
    return set(subprocess.getoutput("groups").split())

def agregar_grupo_usuario(grupo):
    usuario_actual = pwd.getpwuid(os.getuid()).pw_name
    grupos_usuario_actual = obtener_grupos_usuario()

    if grupo in grupos_usuario_actual:
        print(f"Ya eres miembro del grupo {grupo}.")
        return

    try:
        subprocess.check_output(["sudo", "usermod", "-aG", grupo, usuario_actual], stderr=subprocess.STDOUT)
        print(f"Se te ha añadido al grupo {grupo}.")
    except subprocess.CalledProcessError as e:
        print(f"No se pudo añadir al grupo {grupo}. Mensaje de error: {e.output.decode('utf-8')}")

if len(sys.argv) == 2:
    directorio = sys.argv[1]
else:
    directorio = input("Introduce la ruta del directorio: ")

# Verificar si el directorio existe
if not os.path.exists(directorio):
    print(f"El directorio '{directorio}' no existe.")
    mostrar_ayuda()
    sys.exit(1)

usuarios_con_permisos = obtener_usuarios(directorio)

if not usuarios_con_permisos:
    print(f"No se encontraron usuarios con permisos de lectura o ejecución en '{directorio}'.")
    sys.exit(0)

print("Usuarios con permisos de lectura o ejecución en", directorio)
for usuario, nombre_usuario in usuarios_con_permisos:
    print(f"{usuario}: {nombre_usuario}")

# Preguntar si se quieren añadir los grupos al usuario actual
grupos_encontrados = {nombre_grupo for _, nombre_grupo in usuarios_con_permisos}
grupos_a_agregar = grupos_encontrados - obtener_grupos_usuario()

if not grupos_a_agregar:
    print("Ya eres miembro de todos los grupos encontrados.")
else:
    print("Grupos encontrados:", ', '.join(grupos_a_agregar))
    for grupo in grupos_a_agregar:
        respuesta = input(f"¿Quieres añadirte al grupo {grupo}? (y/n): ").lower()
        if respuesta == 'y':
            agregar_grupo_usuario(grupo)
        else:
            print(f"No se te añadirá al grupo {grupo}.")
