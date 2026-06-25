from PIL import Image
from tkinter import Tk, filedialog
import os


root = Tk()
root.withdraw()


def select_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.bmp")
        ]
    )
    return file_path


def encrypt_image():
    image_path = select_image()

    if not image_path:
        print("No image selected.")
        return

    try:
        secret_key = int(input("Enter Secret Key (1-255): "))

        if secret_key < 1 or secret_key > 255:
            print("Invalid Secret Key!")
            return

        img = Image.open(image_path)
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                pixels[x, y] = (
                    (r + secret_key) % 256,
                    (g + secret_key) % 256,
                    (b + secret_key) % 256
                )

        folder = os.path.dirname(image_path)
        encrypted_path = os.path.join(folder, "encrypted_image.png")

        img.save(encrypted_path)

        print("\nImage Encrypted Successfully!")
        print("Saved at:", encrypted_path)

    except Exception as e:
        print("Error:", e)


def decrypt_image():
    image_path = select_image()

    if not image_path:
        print("No image selected.")
        return

    try:
        secret_key = int(input("Enter Secret Key: "))

        img = Image.open(image_path)
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                pixels[x, y] = (
                    (r - secret_key) % 256,
                    (g - secret_key) % 256,
                    (b - secret_key) % 256
                )

        folder = os.path.dirname(image_path)
        decrypted_path = os.path.join(folder, "decrypted_image.png")

        img.save(decrypted_path)

        print("\nImage Decrypted Successfully!")
        print("Saved at:", decrypted_path)

    except Exception as e:
        print("Error:", e)


def main():

    while True:

        print("\n========== IMAGE ENCRYPTION TOOL ==========")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            encrypt_image()

        elif choice == "2":
            decrypt_image()

        elif choice == "3":
            print("\nThank you for using the program.")
            break

        else:
            print("\nInvalid Choice! Try Again.")


if __name__ == "__main__":
    main()