def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Do you want to (E)Encrypt or (D)Decrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter E or D.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'E':
        encrypted = encrypt(message, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = decrypt(message, shift)
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
