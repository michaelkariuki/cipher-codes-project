from modules.Substitution_Dict import Substitution_Dict
import string


class Custom_Dict_Cipher():
    def __init__(self):
        self.symbol_list = list(string.ascii_lowercase+string.ascii_uppercase+ string.punctuation)
        self.test_arr = self.make_obj(len(self.symbol_list)+1)
        self.test_dict = self.make_dict(self.symbol_list, self.test_arr)
        self.encrypted_msg_list = []
               
    #functions....
    def make_obj(self, num):
        arr = []
        for _ in range(num):
            obj = Substitution_Dict()
            arr.append(obj.id)

        return arr

    def make_dict(self, list1, list2):
        res_dict = {}
        x = 0

        for x in range(len(list1)):
            value = list2[x]
            res_dict[list1[x]] = value

        value = list2[x+1]
        res_dict['sp'] = value

        return res_dict

    def encrypt_data(self, input):
        input_list = list(input)
        # print(input_list)

        for x in range(len(input_list)):
            if input_list[x] == " ":
                input_list[x] = 'sp'

        # print(input_list)
        encrypted_message_list = []
        encrypted_message = ""

        for x in range(len(input_list)):
            value = self.test_dict.get(input_list[x])
            encrypted_message+= value
            encrypted_message_list.append(value)

        self.encrypted_msg_list = encrypted_message_list
        
        return encrypted_message
    
    def decrypte_msg(self, encrypted):

        if encrypted != ''.join(self.encrypted_msg_list): return "Cipher text missing encryption signature"

        decrypted_msg = ""
        msg_list = self.encrypted_msg_list
        keys = list(self.test_dict.keys())

        for x in range(len(msg_list)):
            val = msg_list[x]
            
            for y in range(len(keys)):
                val2 = self.test_dict[keys[y]]
                if val == val2:      
                    if keys[y] == "sp":
                        decrypted_msg+= " "
                        break
                    else:
                        decrypted_msg+= keys[y]
                        break
            
        return decrypted_msg


# obj = Custom_Dict_Cipher()
# plain_str = input("Write something here : ")
# print("\n\n***CUSTOM ENCRYPTION ALGORITHM****")
# print("\n\n***Test String****")
# print(plain_str)
# ciphertext = obj.encrypt_data(plain_str)
# print("\n\n****Encrypted msg****")
# print(ciphertext)
# print("\n\n****Decrypted msg****")
# print(obj.decrypte_msg(ciphertext))
