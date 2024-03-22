import random

size: int = int(input('Put the size of the password: '))
password: str = ''

def generate_character()-> str:
	random_number = random.randint(33,126)
	character = chr(random_number)
	yield character


for longitud in range(size):
	for c in generate_character():
		password+=c


print('Password: ')
print(password)