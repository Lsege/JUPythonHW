listita = New_List()
listita.New_append(155)
listita.New_append('rojo')
listita.New_append(True)
listita.New_append(['Rojo', 'Amarillo', 'Verde'])

listita.get_list()
listita.set_list(0, 'NUEVO VALOR')
listita.get_list()
listita.set_list(5, 'AAAAAAAA')
listita.get_list()
#print(listita.get_length())
listita.set_list(5,'POSICION 5')
listita.get_list()
print(listita.get_value(0))


listita = New_List()
print(listita)
listita.New_append(155)
listita.New_append('rojo')
listita.New_append(True)
listita.New_append(['Rojo', 'Amarillo', 'Verde'])

print(listita.get_value(2))

listita.New_append(650)
print(listita)

listita.set_list(0, 'Lucas Sanabria')
print(listita)

listita.set_list(7, 'Liverpoool')
print(listita)

print(listita.get_length())

for i in range(listita.get_length()):
	print(listita.get_value(i))