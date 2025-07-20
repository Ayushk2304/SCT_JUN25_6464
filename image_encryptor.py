from PIL import Image

def encrypt_image(input_path, output_path, key=50):
    image = Image.open(input_path)
    pixels = image.load()

    for i in range(image.size[0]):  # width
        for j in range(image.size[1]):  # height
            r, g, b = pixels[i, j]
            # Add key (modulo 256 to keep RGB in range)
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path, key=50):
    image = Image.open(input_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            # Subtract key (modulo 256)
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

def main():
    print("=== Image Encryption Tool ===")
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
    input_file = input("Enter image path (e.g. input.jpg): ")
    output_file = input("Enter output file name (e.g. encrypted.jpg): ")
    key = int(input("Enter encryption key (e.g. 50): "))

    if choice == 'e':
        encrypt_image(input_file, output_file, key)
    elif choice == 'd':
        decrypt_image(input_file, output_file, key)
    else:
        print("Invalid choice. Use 'e' or 'd'.")

if __name__ == "__main__":
    main()
