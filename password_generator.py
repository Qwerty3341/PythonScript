import random
import os

usage: str = input('Password of...')
size: int = int(input('Put the size of the password: '))
password: str = ''

def generate_character()-> str:
	random_number = random.randint(33,126)
	character = chr(random_number)
	yield character

#Generate the password
for longitud in range(size):
	for c in generate_character():
		password+=c

#Saving the passwords
FILE_NAME: str = '.Password_Manager.txt'

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'a') as file:
        file.write('\n--------------------------------------------------\n')
        file.write(f'Password for {usage}:\n')
        file.write(password+'\n')
else:
    with open(FILE_NAME, 'w') as file:
        file.write('Password Manager\n')
        file.write('--------------------------------------------------\n')
        file.write(f'Password for {usage}:\n')
        file.write(password+'\n')

print('Password: ', password)
print(f'Save in {FILE_NAME}')