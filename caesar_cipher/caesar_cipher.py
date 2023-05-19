import string


def encrypt(phrase, shift):
    encrypted_phrase = ""
    for char in phrase:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_phrase += encrypted_char
        else:
            encrypted_phrase += char
    return encrypted_phrase


def decrypt(encrypted_phrase, shift):
    decrypted_phrase = ""
    for char in encrypted_phrase:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_phrase += decrypted_char
        else:
            decrypted_phrase += char
    return decrypted_phrase


def crack(encrypted_phrase):
    word_list = [
        'it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times'
    ]
    decrypted_phrase = ""
    max_match_count = 0

    for shift in range(26):
        decrypted = decrypt(encrypted_phrase, shift)
        match_count = sum(word.lower() in decrypted.lower().split() for word in word_list)
        if match_count >= max_match_count:
            max_match_count = match_count
            decrypted_phrase = decrypted

    if encrypt(decrypted_phrase, max_match_count) == encrypted_phrase:
        return decrypted_phrase

    return ""
