def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    # Encrypted message
    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)
    
    # Decrypted message
    decrypted_message = caesar_cipher(encrypted_message, -shift)
    print("Decrypted message:", decrypted_message)

def caesar_cipher(text, shift):
    def shift_char(char, shift):
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        return char
    
    return ''.join(shift_char(char, shift) for char in text)

if __name__ == "__main__":
    main()
