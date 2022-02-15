import math
# Almacenar las entradas del usuario
#Pista: variable = input("¿Cuál es tu nombre?")
primer_planeta=input("Ingrese la distancia del primer planeta en km ")
segundo_planeta=input("Ingrese la distancia del segundo planeta en km ")

#Convierte las cadenas de ambos planetas a números enteros
firstPlanet=int(primer_planeta)
secondPlanet=int(segundo_planeta)

# Realizar el cálculo y determinar el valor absoluto
dif_planets = secondPlanet-firstPlanet
print(f'La distancia entre planetas es {abs(dif_planets)}km')

# Convertir de KM a Millas
dif_planets_mi=dif_planets*0.621
dif_planet_mi_ceil=math.ceil(dif_planets_mi)
print(f'La distancia entre planetas es {abs(dif_planet_mi_ceil)}mi')