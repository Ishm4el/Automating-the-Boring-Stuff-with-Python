def collatz(number):
	if number != 1:
		if number % 2 == 0:
			numb = number // 2
			print('*' * numb)
			return collatz(numb)
		elif number % 2 == 1:
			numb = 3 * number + 1
			print('*' * numb)
			return collatz(numb)
	else:
		return number


collatz(200)