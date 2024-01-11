from modules.SubstitutionCipher import SubstitutionCipher
from modules.DictionaryCipher import Custom_Dict_Cipher

def main():
    # SUBSTITUTION CIPHER DEMO
    cipher = SubstitutionCipher()
    print("\n***SUBSTITUTION CIPHER DEMO****")
    plain = input("Write something here : ")
    encrypt = cipher.substitute(plain)
    decrypt = cipher.decryptSubstitution(encrypt)
    print("\n****Encrypted msg****")
    print(encrypt)
    print("\n****Decrypted msg****")
    print(decrypt)

    # CUSTOM SUBSTITUTION CIPHER USING RANDOMLY GENERATED DICT-BASED SIGNATURE
    obj = Custom_Dict_Cipher()
    print("\n\n***CUSTOM SUBSTITUTION CIPHER DEMO****")
    plain_str = input("Write something here : ")
    print("\n***Test String****")
    print(plain_str)
    ciphertext = obj.encrypt_data(plain_str)
    print("\n****Encrypted msg****")
    print(ciphertext)
    print("\n****Decrypted msg****")
    print(obj.decrypte_msg(ciphertext))

if __name__ == '__main__':
    main()




        






