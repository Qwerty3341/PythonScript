numbers: list[float] = list(map(float, input('Put numbers: ').split()))

max_number = numbers[0]
for num in numbers[1:]:
	if num > max_number:
		max_number = num
print(f'Maximum number = {max_number}')