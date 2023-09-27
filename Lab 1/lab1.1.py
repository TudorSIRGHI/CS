alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_cipher(input_text, key, operation):
#Checking if the key is Valid
    if key < 1 or key > 25:
        return 'Please, enter a valid key between 1 and 25.'
#Turn all the charachters in Upper case and remove all the spaces
    modified_text = ''.join(input_text.split()).upper()
    result = ''

#Making interactive menu with choice for Encryption or Decryption
    for char in modified_text:
        if char in alphabet:
            index = alphabet.index(char)
            if operation == '1':
                new_index = (index + key) % 26
            elif operation == '2':
                new_index = (index - key + 26) % 26
            else: #For wrong choice of operation
                return 'Your operation can not be Processed.\nPlease, enter "1" for Encryption or "2" for Decryption.'
            result += alphabet[new_index]
        else: #For non-english charachters
            return 'Your message it is not valid.\nUse only English alphabet from A to Z.'
    return result

#Reading the input for choices from the user
operation = input('Choose the operation from the list above:\n"1" for Encrypt\n"2" for Decrypt\nInput:').strip()
key_input = input('Type the key for your encryption/decryption\nIt must be between 1 and 25: ').strip()

try:
    key = int(key_input)
    if key < 1 or key > 25:
        print('Wrong key. Key must be between 1 and 25.')
    elif key == 0:
        print('You do not need encryption/decryption for key 0.')
    else:
        message = input('Please, enter your message:')
        result = caesar_cipher(message, key, operation)
        print(f'Result: {result}')
except ValueError:
    print('Wrong key. Key must be a natural number.')