def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Encryption/Decryption ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g. 3): "))

    if choice == 'e':
        result = encrypt(message, shift)
        print("Encrypted message:", result)
    elif choice == 'd':
        result = decrypt(message, shift)
        print("Decrypted message:", result)
    else:
        print("Invalid choice. Please type 'e' or 'd'.")

if __name__ == "__main__":
    main()
