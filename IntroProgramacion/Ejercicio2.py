# 2)  Crear una lista en Python denominada “Dueno2”.
# Los elementos de la lista son: 23546987,  “Maria”,  “Perez”, 4789689,  “Pueyrredon  811”.
# Representan los datos del dueño de un perro (DNI, nombre, apellido, teléfono y dirección) 
# Recorrerla con un bucle  mostrando sus elementos por pantalla con excepción del DNI y el apellido. 


# Creo Lista Dueno2

dueno2=[23546987,'Maria', 'Perez', 4789689, 'Pueyrredon  811']


# Recorro dicha lista con un bucle mostrando sus elementos en pantalla, omitiendo el DNI (1) y el apellido (3).

for x in range(len(dueno2)):
    if x==1:
        print(dueno2[x])
    if x==3:
        print(dueno2[x])
    if x==4:
        print(dueno2[x])