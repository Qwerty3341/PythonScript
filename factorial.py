number: int = int(input('Number: '))

if number == 0 or number == 1:
	print(f'{number}! = {1}')
elif number < 0:
	print("Can't calculate the factorial of a negative number")
else:
	previous_numbers: [int] = []

	for n in range(number):
		previous_numbers.append(n+1)

	factorial_number: int = 1

	for num in previous_numbers:
		factorial_number *= num
	
	print(f'\t{number}! = {factorial_number:,}')
	print(f'\tScientific notation {factorial_number:e}')