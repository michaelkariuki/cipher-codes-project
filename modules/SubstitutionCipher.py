# Let's create a basic substitution cipher. A substitution cipher is a method of encryption where each letter in the plaintext is replaced with another letter. Here's a simple example using a Caesar cipher, where each letter is shifted a certain number of places down the alphabet.

# Key Generation:

# Choose a shift value (key) for the cipher. For simplicity, you can start with a fixed value, say 3.
# Encryption Function:

# Create a function that takes a plaintext and the shift value as input and returns the encrypted text.
# Iterate through each character in the plaintext.
# For each character, shift it by the specified value (use the ord and chr functions in Python).
# Decryption Function:

# Create a function that takes the encrypted text and the shift value as input and returns the decrypted text.
# Similar to the encryption function, but shift the characters in the opposite direction.
# Testing:

# Write a simple script that takes user input for plaintext, encrypts it, then decrypts it and prints the results.
# Ensure that the decrypted text matches the original plaintext.

from typing import Union
import random

class SubstitutionCipher():
    def __init__(self, shiftVal: Union[int, None] = None):
        self.shiftVal = shiftVal if shiftVal else self.generateShiftVal()

    def generateShiftVal(self):
        return random.randint(1, 25)# size of the alphabet
    
    def substitute(self, plaintext: str):
        res = ""

        for char in plaintext:
            if char.isalpha(): # Check if the character is a letter
                shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + self.shiftVal) % 26 + ord('a' if char.islower() else 'A'))
                res += shifted_char
            else:
                res += char # Keep non-alphabetic characters unchanged

        return res
    
    def decryptSubstitution(self, ciphertext: str):
        res = ""
        for char in ciphertext:
            if char.isalpha():# Check if the character is a letter
                reversed_char = chr((ord(char) - ord('a' if char.islower() else 'A') - self.shiftVal) % 26 + ord('a' if char.islower() else 'A'))
                res += reversed_char
            else:
                res += char

        return res




