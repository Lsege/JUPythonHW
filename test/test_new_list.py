import unittest
from new_list import NewList

class test_new_list(unittest.TestCase):

	def test_is_empty_true(self):
		my_list = NewList()
		self.assertIsNone(my_list.get_value(0))

	def test_is_empty_false(self):
		my_list = NewList()
		my_list.new_append('First Value')
		self.assertIsNotNone(my_list.get_value(0))

	def test_append(self):
		my_list = NewList()
		my_list.new_append('First Value')
		self.assertEqual('First Value', my_list.get_value(0))

	def test_len(self):
		my_list = NewList()
		my_list.new_append('First Value')
		my_list.new_append(0)
		my_list.new_append(True)
		self.assertEqual(3, len(my_list))

	def test_set_list(self):
		my_list = NewList()
		my_list.new_append('First Value')
		my_list.set_list(0, 'New First Value')
		self.assertEqual('New First Value', my_list.get_value(0))

	def test_set_higher_value(self):
		my_list = NewList()
		my_list.set_list(15, 'random value')
		self.assertIsNone(my_list.get_value(15))

	def test_set_list_str(self):
		my_list = NewList()
		my_list.set_list('red', 'random value')
		self.assertIsNone(my_list.get_value('red'))

	def test_get_value(self):
		my_list = NewList()
		my_list.set_list('red', 'random	value')
		with self.assertRaises(ValueError):
			my_list.get_value('red')
