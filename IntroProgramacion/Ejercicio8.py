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