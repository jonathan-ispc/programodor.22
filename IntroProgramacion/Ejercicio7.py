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