# Añadir grupos a mi usuario

La necesidad de crear este script es poder hacer la copia de seguridad deja-dup de los datos mapeados con los contenedores dockers que usamos. 

Muchas veces no conocemos el grupo que crea el docker , puede ser www-data , manolito o pepito. Pues bien, si no perteneces a ese grupo, cuando vayas a hacer la copia de seguridad te va a dar error, así que por eso este script.

Es un script muy sencillito el cual de forma recursiva ver los grupos de carpetas y te pregunta si quieres añadirlos a tu usuario.
