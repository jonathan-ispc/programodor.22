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