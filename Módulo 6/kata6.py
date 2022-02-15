#Lista de planetas
planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano','Neptuno','Pluton']

# Solicitamos el nombre de un planeta *Pista:  input()*
inputUsuario = input('Ingrese el nombre de un planeta, la primera letra debe ser mayúscula, favor de no colocar acentos: ')

#Busca el planeta en la lista
planetaUsuario = planetas.index(inputUsuario)

#Muestra los planetas más lejanos al sol
print(f'Los planetas más cercanos a {inputUsuario} son: ')
planetasCercanos=planetas[0:planetaUsuario]
print(planetasCercanos)

# Muestra los planetas más lejanos al sol
print(f'Los planetas más lejanos a {inputUsuario} son: ')
planetasLejanos=planetas[planetaUsuario + 1:]
print(planetasLejanos)

