from collections import Counter
import re


def get_frequency(text: str, n: int | None = None) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common(n)


def read_file(file_name: str) -> str:
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            content: str = f.read()
        return content

    except FileNotFoundError:
        print(f"File '{file_name}' not found")
        return ""


def check_text(text: str) -> None:
    n: str = input(
        '┌Select the number of the most frequent words (Press ENTER to see all the words)\n└─> '
    ).strip()

    if n.isdigit():
        word_frequencies: list[tuple[str, int]] = get_frequency(text, int(n))
    else:
        word_frequencies: list[tuple[str, int]] = get_frequency(text)

    for word, count in word_frequencies:
        print(f'{word}: {count}')



def main() -> None:

    # text_input: str = input("\n┌How do you prefer to put the text?\nן\t1 -> read a file\n|\t2 -> paste text\n└─>")
    text_input: str = input("\n┌How do you prefer to put the text?\n│   1 -> read a file\n│   2 -> paste text\n└──> ")

    match text_input:
        case '1':
            file: str = input(
                '\n┌Put the name of the file (must be in the same directory)\n└─> '
            ).strip()

            file = file if file.endswith('.txt') else file + '.txt'

            text: str = read_file(file)
            
            if text: # Check if the text variable is empty or not
                check_text(text)
            else:
                print('Empty file')

        case '2':
            text: str = input('Enter your text: ').strip()
            check_text(text)

        case _:
            pass


if __name__ == '__main__':
    main()
