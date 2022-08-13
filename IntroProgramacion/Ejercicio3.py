# 3)  Crear un lista en Python denominado “Perro” que contenga los siguientes valores:  13,  Puppy,  12/12/2012 , Macho, 123
# Que se corresponde con los datos de un perro de nuestra base de datos (Id_Perro, nombre, fecha de nacimiento, sexo y dni del dueño). 
# Modificar la fecha de nacimiento por 13/12/2012 y reemplazar “dni del dueño” por 28957346.



#------- Opción 1

# Creo lista Perro con sus valores.
 
Perro=[13,"Puppy","12/12/2012","Macho",123]

# Modifico la fecha de nacimiento (2) y reemplazo el dni del dueño (4).
Perro[2] = "13/12/2012"
Perro[4] = 28957346

# Muestro el contenido de la lista para corroborar los cambios.

print(Perro)

print()


#------- Opción 2

# Creo lista Perro con sus valores.

Perro=[13,"Puppy","12/12/2012","Macho",123]

# Recorro la lista con un bucle buscando la fecha de nacimiento "12/12/2012" y el dni 123, y una vez que los encuentro, los reemplazo por "13/12/2012" y 28957346 respectivamente.

for x in range(len(Perro)):
    if Perro[x]== "12/12/2012":
        Perro[x]= "13/12/2012"
    if Perro[x]== 123:
        Perro[x]= 28957346

# Muestro el contenido de la lista para corroborar los cambios.

print(Perro)