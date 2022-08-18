import MostRepeatedWord

def Romeo_and_Juliet(Dict):
	Couple = dict()
	for key, value in Dict.items():
		if key == 'romeo':
			Couple[key] = value
		elif key == 'juliet':
			Couple[key] = value
	return Couple

def any_word(Dict):
	YourWord = input('What word do you want to know how many times it appear: ')
	WordOutput = dict()
	for key, value in Dict.items():
		if key == YourWord:
			WordOutput[key] = value
			return WordOutput

	if len(WordOutput) ==0:
		return'Your word wasnt found'

if __name__ == "__main__":
	file = open('romeo.txt', 'r')
	aux = MostRepeatedWord.word_count(file)
	print(any_word(aux))
