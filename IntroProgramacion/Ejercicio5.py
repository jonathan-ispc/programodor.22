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