# Cipher Codes

This repository contains Python implementations of simple substitution ciphers. The ciphers are designed for educational purposes and may not provide robust security.

## Substitution Cipher

The `SubstitutionCipher` class implements a basic substitution cipher where each letter in the plaintext is shifted by a fixed amount in the alphabet.

### Usage:

1. Import the class:

    ```python
    from modules.SubstitutionCipher import SubstitutionCipher
    ```

2. Create an instance with an optional shift value:

    ```python
    cipher = SubstitutionCipher(shiftVal=3)
    ```

3. Encrypt and decrypt messages:

    ```python
    plaintext = "Hello, World!"
    ciphertext = cipher.substitute(plaintext)
    decrypted_text = cipher.decryptSubstitution(ciphertext)
    ```

## Dictionary Cipher

The `Custom_Dict_Cipher` class uses a custom dictionary-based approach for encryption and decryption.

### Usage:

1. Import the class:

    ```python
    from modules.DictionaryCipher import Custom_Dict_Cipher
    ```

2. Create an instance:

    ```python
    custom_cipher = Custom_Dict_Cipher()
    ```

3. Encrypt and decrypt messages:

    ```python
    plaintext = "Hello, World!"
    encrypted_text = custom_cipher.encrypt_data(plaintext)
    decrypted_text = custom_cipher.decrypte_msg(encrypted_text)
    ```

## Substitution Dictionary

The `Substitution_Dict` class generates unique IDs using a combination of random numbers and characters.

### Usage:

1. Import the class:

    ```python
    from modules.Substitution_Dict import Substitution_Dict
    ```

2. Create an instance:

    ```python
    substitution_dict = Substitution_Dict()
    ```

3. Access the generated ID:

    ```python
    unique_id = substitution_dict.id
    ```

## Running Tests

Tests for the cipher classes are provided in the `tests` folder. To run the tests, execute the following command:

```bash
python -m unittest tests.py
