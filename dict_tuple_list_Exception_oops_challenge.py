l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

import logging
logging.basicConfig(filename="Itrable.log",level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")

class list_test:
    """In this class we are going to have some operations on list tuple and dictionary"""
    logging.info("We are inside the class")

    def reverse_list(self,l):
        """This function will try to give you opposite of list"""
        logging.info("we are inside the function")
        self.l=l
        try:
            l1=l.reverse()
            logging.info("we sucessfully able to reverse the list %s",l1)
            return l
        except Exception as e:
            logging.exception(e)

    def list_extract(self,l):
        """We will extract the list inside the list"""
        self.l=l
        logging.info("we are inside the list_extract function")

        try:
            list1 = []
            for i in self.l:
                if type(i)==list:
                    list1.append(i)
            return list1
        except Exception as e:
            logging.exception(e)





    def int_str_Extract(self,l):
        self.l=l
        """We are going to extract integer value and string"""
        logging.info("We are inside list_Str_extract function")

        try:
            list1=[]
            for i in l:
                if type(i)==int:
                    list1.append(i)
                    logging.exception("we sucessfully append the int")
            return list1

        except Exception as e:
            logging.exception(e)







#tuple extraction
    def tuple_extract(self,l):
        """We are try to extract tuple from the list"""
        logging.info("we are inside the tuple_extract class")
        list1=[]
        try:
            for i in  l:
                if type(i)==tuple:
                    list1.append(i)
                    logging.info("we suscessfully extracted tuple from the this")
            return list1
        except Exception as e:
            logging.exception(e)


    def dict_values(self,l):
        """We will try to fetch the values of the diction"""
        logging.info("We are inside the dict_values")
        list1=[]
        try:
            for i in l:
                if type(i)==dict:
                    for j in i.values():
                        list1.append(j)
            return list1

        except Exception as e:
            logging.exception(e)










