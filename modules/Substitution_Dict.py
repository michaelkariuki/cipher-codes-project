#place imports here
import random
import string

class Substitution_Dict:
    """
        This class creates a unique id for its objects
        by using the inbuilt the random and string modules
        of  python
    """
    def __init__(self):
        super().__init__()
        self.id = "0"
        self.id = self.set_id(self.id)

    def set_id(self, id1):
            #initializing the list variables
            letter_list = [] 
            #using the string module to get all the alphanumeric chars into a list
            letter_list = list(string.ascii_lowercase+string.ascii_uppercase+ string.punctuation) 
            #using the random() method to get a random float value
            rand_id = str(random.random())
            id_list = list(rand_id)
            id_list = self.combine_ls(id_list, letter_list)

            return id_list


    #This method combines the contents of 2 lists (str) 
    #grabs the contents of the first list and combines it with a randomly picked item
    #from the second list
    def combine_ls(self, list1, list2):
        final_str = ""
        for _ in range(len(list1)):
            final_str += random.choice(list1) + random.choice(list2)

        return final_str

