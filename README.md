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




# Script: `grupos.py`

## Description

This simple script is designed to facilitate the task of adding groups of files and directories to a user on a Linux system. Its main utility is for those who need to back up data mapped by Docker containers, where file groups can vary.

## Motivation

The need to create this script arises when performing backups with `deja-dup` of data that is mapped with Docker containers. Sometimes, we don't know the group that the Docker container creates, and if we don't belong to that group, the backup may fail. This script solves that problem by providing an easy way to identify and add groups recursively.

## Usage

### Requirements

- Python 3
- `sudo` permissions to add groups to the user

### Example Usage

1. Clone the repository or copy the contents of the script to a local file named `grupos.py`.
2. Open a terminal and navigate to the directory where the script is located.
3. Execute the script by providing the directory path to analyze:

    ```bash
    ./grupos.py /path/to/directory
    ```

4. The script will display users with read or execute permissions in the specified directory and will ask if you want to add those groups to your current user.

5. Answer the confirmation prompts to add the desired groups to your user.

## Notes

- Make sure to have `sudo` permissions to execute the script and add groups to the user.
- The script will ask for confirmation to add each found group, avoiding adding groups you already belong to.

## Contributions

If you find any issues or have suggestions to improve the script, feel free to open an issue or submit a pull request.
