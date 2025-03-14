from translate import Translator
"""
# To use translate you must run 'pip install translate' to install it
# The module only translates from English (unless you modify the configuration of it)
# translate documentation: https://pypi.org/project/translate/
"""

def translate_text_from_file(translator: Translator) -> str:
    file_name: str = input("Put the file name: ")
    file_path = file_name if file_name.endswith('.txt') else file_name + '.txt'

    try:
        with open(file_path, mode='r') as my_file:
            text = my_file.read()
            translation = translator.translate(text)
            print('\nOriginal:')
            print(text)
            print("\nTranslation:")
            print(translation)
    except Exception as e:
        print(f'ERROR: {e}')


def translate_text_directly(translator: Translator) -> str:
    """
    Function to translate by a copied text from the user
    """
    text: str = input('Text:\n')
    translation = translator.translate(text)
    print("\nTranslation:")
    print(translation)


def validate_input(input_message: str, valid_options: tuple) -> str:
    """
    Function to check if the user put a correct option
	"""
    user_input: str = input(input_message).strip()
    while user_input not in valid_options:
        print('CHOOSE A CORRECT OPTION')
        user_input: str = input(input_message).strip()
    return user_input


def main() -> None:
    text_input: str = validate_input(
        "\n┌How do you prefer to translate the text?\n│   1 -> read a file (The file should be in the same directory as the script)\n│   2 -> paste text\n└──> ",
        ('1', '2')
    )

    supported_languages = (
        "es", "fr", "de", "zh", "zh-TW", "it", "ru", "pt", "ja", "ko", "ar", "nl", 
        "sv", "pl", "da", "fi", "no", "tr", "cs", "el", "he", "id", "hi", "ro", "hu", "th", 
        "uk", "bg", "ms", "vi", "ht"
    )

    menu_text = "\n".join([
        "┌Choose the language:",
        "│  es  → Spanish     |  fr  → French      |  de  → German",
        "│  zh  → Chinese     |  it  → Italian,    |  zh-TW → Traditional Chinese",
        "│  ru  → Russian     |  pt  → Portuguese  |  ja  → Japanese",
        "│  ko  → Korean      |  ar  → Arabic      |  nl  → Dutch",
        "│  sv  → Swedish     |  pl  → Polish      |  da  → Danish",
        "│  fi  → Finnish     |  no  → Norwegian   |  tr  → Turkish",
        "│  cs  → Czech       |  el  → Greek       |  he  → Hebrew",
        "│  id  → Indonesian  |  hi  → Hindi       |  ro  → Romanian",
        "│  hu  → Hungarian   |  th  → Thai        |  uk  → Ukrainian",
        "│  bg  → Bulgarian   |  ms  → Malay       |  vi  → Vietnamese",
        "│  ht  → Haitian Creole",
        "└──> "
    ])

    language: str = validate_input(menu_text,supported_languages)

    translator: Translator = Translator(to_lang=language)

    match text_input:
        case '1':
            translate_text_from_file(translator)
        case '2':
            translate_text_directly(translator)
        case _:
            pass


if __name__ == '__main__':
    main()
