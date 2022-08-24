class New_List():
	def __init__(self):
		self.__count = 0
		self.__All_values = {}


	def New_append(self, New_value):
		self.__All_values[self.__count] = New_value
		self.__count += 1

	def get_length(self):
		return self.__count

	def get_value(self, i):
		for key in self.__All_values:
			if i == key:
				return(self.__All_values[key])
		else:
			return 'Value not found, please insert a correct key.'


	def __str__(self):
		List_as_Str = '['
		for value in self.__All_values.values():
			List_as_Str = List_as_Str + f'{value}' + ' ,'
		List_as_Str = List_as_Str + ']'
		return List_as_Str

	def set_list(self, old_key, New_value):
		if old_key > self.__count:
			self.New_append(New_value)
		else:
			for key, value in self.__All_values.items():
				self.__All_values[old_key] = New_value


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

