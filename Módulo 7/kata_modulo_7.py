#Ejercicio 1: Creación de un bucle "while"
#Ejercicio 1: Uso de ciclos while en Python

# Creamos la variable que almacena el texto
new_planet = ''
# Creamos la lista que almacena cada uno de los textos que el usuario ingresa
planets = []

# Ciclo while
while new_planet.lower() != 'done':
    # Verificamos si hay un valor en user_input
    if new_planet:
        # Almacenamos ese valor en la lista
        planets.append(new_planet)
    # Capturamos un nuevo valor
    new_planet = input('Enter a new planet or done when done: ')



#Ejercicio 2: Creación de un ciclo "for"
#Ejercicio: - Ciclo para una lista

#En el ejercicio anterior, creaste código para solicitar a los usuarios que introduzcan una lista de nombres de planetas. 
#En este ejercicio, completarás la aplicación escribiendo código que muestre los nombres de esos planetas.

#Mostrar la lista de los planetas

#La variable planets almacena los nombres de planeta que ha introducido un usuario. Ahora usarás un ciclo para mostrar esas entradas.
#Crea un ciclo for para iterar sobre la lista planets. Puedes usar como nombre de la variable planet para cada planeta.
#Dentro del ciclo for, recuerda utilizar print para mostrar cada planet.

planetas = [planets] #La variable planets almacena los nombres de planeta que ha introducido un usuario
for planet in planetas:
    print(f'Los planetas ingresados son: {planet}')
