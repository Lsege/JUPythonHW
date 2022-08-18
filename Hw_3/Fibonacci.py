def Fibonacci(term):
	if term == 0: return 0
	elif term == 1: return 1

	Xn = 0
	for i in range(term+1):
		if i == 0:
			N_2 = 0
		elif i == 1:
			N_1 = 1
		else:
			Xn = N_1 + N_2
			N_2 = N_1
			N_1 = Xn

	return Xn

for i in range(3):
	print(i)


#print(Fibonacci(2))



