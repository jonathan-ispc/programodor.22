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