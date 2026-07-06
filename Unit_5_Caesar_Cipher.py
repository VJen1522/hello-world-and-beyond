# Caesar Cipher dictionary
caesar_cipher_dict = {
    'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J',
    'F': 'K', 'G': 'L', 'H': 'M', 'I': 'N', 'J': 'O',
    'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S', 'O': 'T',
    'P': 'U', 'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y',
    'U': 'Z', 'V': 'A', 'W': 'B', 'X': 'C', 'Y': 'D',
    'Z': 'E', '0': '5', '1': '6', '2': '7', '3': '8',
    '4': '9', '5': '0', '6': '1', '7': '2', '8': '3',
    '9': '4', '.': '-', '?': '!', '!': '#', ' ': ' '
}

reverse_cipher_dict = {value: key for key, value in caesar_cipher_dict.items()}


def text_to_caesarcipher(text):
    """Convert text to Caesar cipher."""
    caesar_cipher = ""
    for char in text.upper():
        if char in caesar_cipher_dict:
            caesar_cipher += caesar_cipher_dict[char]
        else:
            caesar_cipher += char
    return caesar_cipher


def caesarcipher_to_text(cipher_text):
    """Convert Caesar cipher text back to plain text."""
    plain_text = ""
    for char in cipher_text.upper():
        if char in reverse_cipher_dict:
            plain_text += reverse_cipher_dict[char]
        else:
            plain_text += char
    return plain_text


print("Encode or decode a Caesar cipher sentence!")
while True:
    user_input = input("\nEnter a message to translate (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    mode = input("Type 'e' to encode or 'd' to decode: ").strip().lower()
    if mode == 'e':
        translated_text = text_to_caesarcipher(user_input)
        print("Your secret code is:", translated_text)
    elif mode == 'd':
        translated_text = caesarcipher_to_text(user_input)
        print("Your decoded message is:", translated_text)
    else:
        print("Please choose 'e' or 'd'.")
