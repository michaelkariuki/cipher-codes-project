import unittest
from modules.SubstitutionCipher import SubstitutionCipher
from modules.DictionaryCipher import Custom_Dict_Cipher
from modules.Substitution_Dict import Substitution_Dict


class TestCiphers(unittest.TestCase):

    def test_substitution_cipher(self):
        cipher = SubstitutionCipher(shiftVal=3)
        plaintext = "Hello, World!"
        ciphertext = cipher.substitute(plaintext)
        self.assertEqual(cipher.decryptSubstitution(ciphertext), plaintext)

        cipher = SubstitutionCipher(shiftVal=10)
        ciphertext = cipher.substitute(plaintext)
        self.assertEqual(cipher.decryptSubstitution(ciphertext), plaintext)

        cipher = SubstitutionCipher(shiftVal=10)
        plaintext = ""
        ciphertext = cipher.substitute(plaintext)
        self.assertEqual(cipher.decryptSubstitution(ciphertext), plaintext)

    def test_substitution_dict_id_generation(self):
        substitution_dict = Substitution_Dict()
        self.assertIsNotNone(substitution_dict.id)
        self.assertIsInstance(substitution_dict.id, str)

    def test_custom_dict_cipher_encryption_decryption(self):
        custom_cipher = Custom_Dict_Cipher()

        # Test encryption and decryption
        plaintext = "Hello, World!"
        encrypted_text = custom_cipher.encrypt_data(plaintext)
        decrypted_text = custom_cipher.decrypte_msg(encrypted_text)

        self.assertEqual(decrypted_text, plaintext)

    def test_custom_dict_cipher_invalid_decryption(self):
        custom_cipher = Custom_Dict_Cipher()

        # Attempt to decrypt without setting encrypted_msg_list
        result = custom_cipher.decrypte_msg("random_cipher_text")
        self.assertEqual(result, "Cipher text missing encryption signature")