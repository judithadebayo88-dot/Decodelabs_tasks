def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift the letter, wrapping around the alphabet with %26
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            # Leave spaces, punctuation, numbers unchanged
            result += char
    return result


def decrypt(text, shift):
    # Decrypting is just encrypting with the opposite shift
    return encrypt(text, -shift)


if __name__ == "__main__":
    message = "WELCOME"
    shift = 3

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print(f"Original:  {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
