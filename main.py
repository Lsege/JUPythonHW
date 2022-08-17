import MostRepeatedWord, romeoAndJuliet

def menu():
	option = int(input("""*Welcome to Lucas Sanabria's Program*
1. Return the word that repeats the most
2. Return how many times the words 'romeo' and 'juliet' appears
3. Select a word and look how many times it appears.
Please, select your option: """))
	return option

def actions(option, file):
	aux = MostRepeatedWord.word_count(file)
	
	if option == 1:
		print(MostRepeatedWord.max_word(aux))
	elif option == 2:
		print(romeoAndJuliet.Romeo_and_Juliet(aux))
	elif option == 3:
		print(romeoAndJuliet.any_word(aux))




if __name__ == '__main__':
	file = open('romeo.txt', 'r')
	option = menu() 
	actions(option, file)