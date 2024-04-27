import os

#manipular un archivo
log_file1 = open(os.path.abspath("dia11/logs/error.log"))
#FileNotFoundError: [Errno 2] No such file or directory: 
#'/Volumes/DD/TalentoDigital/2023/0044-2/MODULO_POO/dia11/logs/error.log'

#lectura de un archivo existente
log_file2 = open(os.path.abspath("dia11/index.html"),'r')
#ller el contenido del archivo
print(log_file2.read())
log_file2.close()
print("**********************")
log_file3 = open(os.path.abspath("dia11/index.html"),'r')
print(log_file3.readlines())
print("**********************")
with open(os.path.abspath("dia11/index.html"),'r') as archivo:
    print(archivo)
    for linea in archivo:
        print(linea.strip())


#SOLO ESCRITURA
#la ruta donde se creara el archivo debe existir 
log_file4 = open(os.path.abspath("dia11/assets/css/style.css"),'w')
log_file4.write("*{\n\tmargin: 0px\n}")
log_file4.write("\nbody{\n\tpadding: 0px\n}")
log_file4.close()

log_file5 = open(os.path.abspath("dia11/assets/js/script.js"),'w')
lista= ["function prueba()\n","{\n\tconsole.log('hola mundo')\n}"]

log_file5.write("/* esto es una prueba*/\n")
log_file5.writelines(lista)
log_file5.close()

import time

log_file6 = open(os.path.abspath(f"dia11/{round(time.time())}.log"),'w')