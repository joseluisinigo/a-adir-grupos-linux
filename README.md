# Script: `grupos.py`

## Descripción

Este script simple está diseñado para facilitar la tarea de añadir grupos de archivos y directorios a un usuario en un sistema Linux. Su utilidad principal es para aquellos que necesitan realizar copias de seguridad de datos mapeados por contenedores Docker, donde los grupos de archivos pueden variar.

## Motivación

La necesidad de crear este script surge al realizar copias de seguridad con `deja-dup` de datos que están mapeados con contenedores Docker. En ocasiones, no conocemos el grupo que crea el contenedor Docker, y si no pertenecemos a ese grupo, la copia de seguridad puede fallar. Este script resuelve ese problema al proporcionar una manera sencilla de identificar y añadir grupos de forma recursiva.

## Uso

### Requisitos

- Python 3
- Permisos de `sudo` para añadir grupos al usuario

### Ejemplo de uso

1. Clona el repositorio o copia el contenido del script en un archivo local llamado `grupos.py`.
2. Abre una terminal y navega al directorio donde se encuentra el script.
3. Ejecuta el script proporcionando la ruta del directorio a analizar:

    ```bash
    ./grupos.py /ruta/al/directorio
    ```

4. El script mostrará los usuarios con permisos de lectura o ejecución en el directorio especificado y preguntará si deseas añadir esos grupos a tu usuario actual.

5. Responde las preguntas de confirmación para añadir los grupos deseados a tu usuario.

## Notas

- Asegúrate de tener permisos de `sudo` para ejecutar el script y añadir grupos al usuario.
- El script solicitará confirmación para añadir cada grupo encontrado, evitando añadir grupos a los que ya perteneces.

## Contribuciones

Si encuentras algún problema o tienes sugerencias para mejorar el script, no dudes en abrir un problema o enviar una solicitud de extracción.
