# 4)  Crear un lista en Python denominado “Perro2” que contenga los siguientes valores:  14,  Fido,  12/12/2012 , Macho, 23546987
#  Recorrer la lista “Perro2” con un bucle y mostrar sus elementos por pantalla , comenzando desde el último hasta el primero.


# Creo lista Perro2 con sus valores.

perro2 = [14,  'Fido',  '12/12/2012' , 'Macho', 23546987]

# Recorro dicha lista con un bucle y muestro sus elementos en pantalla comenzando desde el último hasta el primero.

for i in reversed(perro2):
  print(i)