# 1) Crear una lista en Python denominada “Dueno” que contenga los siguientes valores:  28957346,  Juan,  Perez, 4789689,  Belgrano 101
# Dichos datos se corresponden  con los datos del dueño de un perro (DNI, nombre, apellido, teléfono y dirección). 
# Muestre en pantalla el teléfono del dueño si el DNI es mayor a 26000000.


# Creo lista Dueno con sus valores.
dueno=[28957346, "Juan", "Perez", 4789689, "Belgrano 101"]

# Muestro en pantalla el teléfono del dueño si el DNI es mayo a 26000000.

if dueno[0] > 26000000:
    print ("El teléfono del dueño es", dueno[3])


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


# 4)  Crear un lista en Python denominado “Perro2” que contenga los siguientes valores:  14,  Fido,  12/12/2012 , Macho, 23546987
#  Recorrer la lista “Perro2” con un bucle y mostrar sus elementos por pantalla , comenzando desde el último hasta el primero.


# Creo lista Perro2 con sus valores.

perro2 = [14,  'Fido',  '12/12/2012' , 'Macho', 23546987]

# Recorro dicha lista con un bucle y muestro sus elementos en pantalla comenzando desde el último hasta el primero.

for i in reversed(perro2):
  print(i)

# 5) Crear una tupla en Python con el nombre de “Historial” la cual contenga los siguientes valores: 2350, 5960, 23000, 1000, 8900
# Que representa montos de atención en pesos por diferentes servicios/consultas de la mascota “Puppy”. 

# Calcular el monto total gastado a lo largo del tiempo por atención de “Puppy”.
# Si el gasto efectuado es menor a 30000, mostrar en pantalla dicho resultado, caso contrario mostrar el mensaje “Gastos por encima de lo presupuestado”.


# Creo una tupla Historial con sus elementos.

historial=(2350, 5960, 23000, 1000, 8900)

# Monto total gastado por atención Puppy.

gastosPuppy= sum(historial)


# Si el resultado en menor a 300000, muestro el resultado obtenido, caso contrario muestro el mensaje “Gastos por encima de lo presupuestado”.

if gastosPuppy < 30000:
    print(f"El gasto de Puppy es {gastosPuppy}")
else:
    print("Gastos por encima de lo presupuestado.")



# 6) Crear una tupla en Python con el nombre de “Historial2” la cual contenga los siguientes valores: 23500, 5960, 2300, 10200, 8900
# Que representa montos de atención en pesos por diferentes servicios/consultas de la mascota “Frida”. 
# Calcular el monto total gastado a lo largo del tiempo por atención de “Frida”.
# Crear una función que cuente cuantos gastos fueron superiores a 5000 mostrando  el número calculado en pantalla.


# Creo una tupla denominada Historial2 con sus valores.

historial2=(23500, 5960, 2300, 10200, 8900)

# Calculo el monto total gastado por atención de Frida.

gastosFrida= sum(historial2)

# Muestro el monto total por atención de Frida.

print(f"Monto total gastado a lo largo del tiempo por atención de Frida es {gastosFrida}.")
print()

# Función que cuenta cuantos gastos fueron superiores a 5000 mostrando  el número calculado en pantalla.

def recuentoDeGastos():
    contador = 0
    for elem in historial2:
        if elem > 5000:
            contador = contador + 1
    return contador

# Muestro en pantalla la cantidad de gastos superiores a 5000.

print(f"La cantidad de gastos superiores a 5000 para Frida fueron {recuentoDeGastos()}.")



# 7) Crear una tupla en Python con el nombre de “Historial3” la cual contenga los siguientes valores: 9530, 4120, 4580, 1500, 890,7516,426
# Que representa montos de atención en pesos por diferentes servicios/consultas de la mascota “Lennon”. 
# Calcular el promedio de gasto en pesos por atención de “Lennon” mostrándolo en pantalla. 
# Si el promedio es mayor a 4500 indicar con un mensaje “Se ha excedido del gasto promedio para su mascota”.



# Creo una tupla Historial3 con sus valores.

historial3 = (9530, 4120, 4580, 1500, 890,7516,426)

# Calculo el promedio de gasto por atención de Lennon.
promedio= sum(historial3) / len(historial3)

# Muestro en pantalla dicho promedio.

print(f"El promedio de gastos por atención de Lennon es {round((promedio),2)}")

# Si el promedio es mayor a 4500 indicar con un mensaje “Se ha excedido del gasto promedio para su mascota”.
 
if promedio > 4500 :
    print("Se ha excedido del gasto promedio para su mascota")

# 8) Crear una tupla en Python con el nombre de “Historial4” la cual contenga los siguientes valores: 7510, 7960, 76180, 800, 4100
# Que representa montos de atención en pesos por diferentes servicios/consultas de la mascota “Olivia”.
# Cree una función para determinar el valor mínimo de atención gastada en “Olivia”  mostrándolo en pantalla.


# Creo tupla denominada Historial4 con sus elementos.

historial4 = (7510, 7960, 76180, 800, 4100)


# Creo función para determinar el valor mínimo de atención gastado en Olivia mostrándolo en pantalla.

def valorMinimo(unaTupla):
    minimo = min(unaTupla)
    print(f"El valor mínimo de atención gastado en Olivia es {minimo}.")

valorMinimo(historial4)


# 9) Crear una tupla en Python con el nombre de “Historial5” la cual contenga los siguientes valores: 8520, 9510, 7530, 3570, 1590
# Que representa montos de atención en pesos por diferentes servicios/consultas de la mascota “Toto”. 
# Crear una función para determinar el valor máximo de atención gastada en “Toto”.


# Creo una tupla Historial5 con sus valores.

historial5 = (8520, 9510, 7530, 3570, 1590)


# Creo función para determinar el valor maximo de atención gastado en Toto mostrándolo en pantalla.

def valorMaximo(unaTupla):
    maximo = max(unaTupla)
    print(f"El valor máximo de atención gastado en Toto es {maximo}.")

valorMaximo(historial5)


# 10) Crear una lista denominada “Clientes” con los nombres de los diferentes  dueños de perros: Juan,  Mario,  Ariel,  Josefina,  Marianella.
# Ordenarla alfabéticamente y mostrarla por pantalla.


# Creo una lista Clientes con los nombres de los diferentes dueños de perros. 

clientes = ["Juan", "Mario",  "Ariel", "Josefina", "Marianell"]

# Ordeno la lista alfabéticamente.
clientes.sort() 

# Muestro la lista ordenada.

print(clientes)


