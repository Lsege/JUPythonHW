
class NewList():
	def __init__(self):
		self.__count = 0
		self.__All_values = {}

	def new_append(self, *args):
		args = list(args)
		for i in args:
			self.__All_values[self.__count] = i
			self.__count += 1

	def get_value(self, i):
		try:
			i = int(i)
			for key in self.__All_values:
				if i == key:
					return(self.__All_values[key])
			else:
				return None

		except ValueError:
			print('The index of the list must be an integer')


	def set_list(self, old_key, New_value):
		try:
			old_key = int(old_key)
			for key, value in self.__All_values.items():
				self.__All_values[old_key] = New_value
		
		except ValueError:
			return('The index of the list must be an integer')

		except RuntimeError:
			return('The index is bigger than the length of the list')

	def __len__(self):
		i = 0
		value = self.get_value(i)
		while value != None:
			i+=1
			value = self.get_value(i)
		return i

	def __str__(self):
		my_list = '['
		for key in self.__All_values:
			my_list = my_list + f'{self.__All_values[key]}, '
		my_list = my_list + ']'
		return my_list
