alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_modified_alphabet(key2):
#Generate modified alphabet with a word as a key
    key2 = ''.join(sorted(set(key2.upper()),
    key=key2.upper().index))
    modified_alphabet = key2 + \
        ''.join(filter(lambda char: char not in key2, alphabet))
    print(f'Your Modified alphabet is: {modified_alphabet}')
    return modified_alphabet


def caesar_cipher(input_text, key1, key2, operation):
# Checking if the key is Valid
    modified_alphabet = generate_modified_alphabet(key2)
    if key1 < 1 or key1 > 25:
        return 'Please, enter a valid key between 1 and 25.'
# Turn all the charachters in Upper case and remove all the spaces
    modified_text = ''.join(input_text.split()).upper()
    result = ''

# Making interactive menu with choice for Encryption or Decryption
    for char in modified_text:
        if char in modified_alphabet:
            index = modified_alphabet.index(char)
            if operation == '1':
                new_index = (index + key1) % len(modified_alphabet)
            elif operation == '2':
                new_index = (index - key1 + len(modified_alphabet)
                             ) % len(modified_alphabet)
            else:  # For wrong choice of operation
                return 'Your operation can not be Processed.\nPlease, enter "1" for Encryption or "2" for Decryption.'
            result += modified_alphabet[new_index]
        else: #For non-english charachters
            return 'Only English alphabet characters (A-Z) are allowed.'

    return result


operation = input('Choose the operation from the list above:\n"1" for Encrypt\n"2" for Decrypt\nInput:').strip().upper()
key1_input = input('Type the key for your encryption/decryption\nIt must be between 1 and 25: ').strip()
key2 = input('Type the second key, it must to:\n1.Use only English letters from A to Z.\n2.To be a string more than 7 charachters.\nYour second key:  ').strip()

try:
    key1 = int(key1_input)
    if key1 < 1 or key1 > 25:
        print('Wrong key. Key must be between 1 and 25.')
    elif len(key2) < 7:
        print('Invalid key. Second key must be at least 7 characters long.')
    else:
        message = input('Enter message: ')
        result = caesar_cipher(message, key1, key2, operation)
        print(f'Result: {result}')
except ValueError:
    print('Invalid key. Key must be an integer between 1 and 25.')