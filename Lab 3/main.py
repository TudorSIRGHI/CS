ALPHA = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZaăâbcdefghiîjklmnopqrsștțuvwxyz"

def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_length = len(key)
    index = 0

    for char in plaintext:
        if char in ALPHA:
            key_char = key[index % key_length]
            shift = ord(key_char) - ord('A')
            if char.islower():
                encrypted_char = ALPHA[(ALPHA.index(char) + shift) % len(ALPHA)]
            else:
                encrypted_char = ALPHA[(ALPHA.index(char) + shift) % len(ALPHA)]
            ciphertext += encrypted_char
            index += 1
        else:
            ciphertext += char

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    index = 0

    for char in ciphertext:
        if char in ALPHA:
            key_char = key[index % key_length]
            shift = ord(key_char) - ord('A')
            decrypted_char = ALPHA[(ALPHA.index(char) - shift) % len(ALPHA)]
            plaintext += decrypted_char
            index += 1
        else:
            plaintext += char

    return plaintext


def main_menu():
    while True:
        print("Choose an option:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            key = input("Enter the encryption key (at least 7 letters long): ")
            if len(key) < 7:
                print("The key should be at least 7 letters long.")
            else:
                plaintext = input("Enter the text to be encrypted: ")
                encrypted_text = vigenere_encrypt(plaintext, key)
                print("Encrypted Text:", encrypted_text)
        elif choice == '2':
            key = input("Enter the decryption key: ")
            ciphertext = input("Enter the text to be decrypted: ")
            decrypted_text = vigenere_decrypt(ciphertext, key)
            print("Decrypted Text:", decrypted_text)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
