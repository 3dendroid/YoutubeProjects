import random
import string

# import math

alphabet = list(
    string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.whitespace + " ")  # all strings



def generate_key(alphabet):
    """Creating Cipher key"""

    shuffled_alphabet = alphabet.copy()
    random.shuffle(shuffled_alphabet)  # makes random combinations of alphabet
    return shuffled_alphabet


# print(generate_key(alphabet))
# print(math.factorial(len(alphabet)))  # all combinations of shuffle

def encrypt(text, key, alphabet):
    """Encryption function"""

    encrypted = [key[alphabet.index(c)] for c in text]
    return ''.join(encrypted)


def decrypt(text, key, alphabet):
    """Decryption function"""

    decrypted = [alphabet[key.index(c)] for c in text]
    return ''.join(decrypted)


generated_key = generate_key(alphabet)
# print(generate_key)

message = "Hello, my name is Denis. I like to eat alot."

encrypted_message = encrypt(message, generated_key, alphabet)
print(encrypted_message)

decrypted_message = decrypt(encrypted_message, generated_key, alphabet)
print(decrypted_message)
