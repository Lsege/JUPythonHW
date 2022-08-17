def word_count(file):
	counts = dict()
	for line in file:
		words = line.split()
		for Uword in words:
			word = Uword.lower()
			if word in counts:
				counts[word] +=1
			else:
				counts[word] = 1
	return counts

def max_word(Dict):
	times = 0
	for key, value in Dict.items():
		if value > times:
			The_word = key
			times = value
	return f'The highest repeated word is "{The_word}" that repeats {times} times'

if __name__ == "__main__":
	file = open('words.txt', 'r')
	aux = word_count(file)
	print(aux)
	print(max_word(aux))
