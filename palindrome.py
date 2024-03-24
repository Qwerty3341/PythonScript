text: str = input('Put a string: ').lower().replace(' ', '')
reverse_text = text[::-1]
if text == reverse_text:
    print('Is it a palindrome?:',True)
else:
    print('Is it a palindrome?:',False)