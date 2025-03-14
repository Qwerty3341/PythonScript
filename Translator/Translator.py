from translate import Translator

language = input("""
ht = Haitian	pt = Portuguese
es = Spanish	zh = Chinese 
	
Choose the language: """)

translator = Translator(to_lang=language)

print("The file should be in the same directory as the script")

file_name : str = input("Put the file name: ")

file_path = ".\\" + file_name + ".txt"

try:
	with open(file_path, mode= 'r') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		print('\nOriginal')
		print(text)
		print("\nTranslation:")
		print(translation)
except Exception as e:
	print(f'ERROR: {e}')