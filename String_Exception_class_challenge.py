s="try to write a usecase of python with your understanding"

import logging
logging.basicConfig(filename="Stringtask.log", level=logging.DEBUG, format="%(levelname)s %(asctime)s %(message)s")


class String1:
    """This custom String_Task class Where we try do some python operation"""
    logging.info("We created a class here")
    def extraxt3(self,s):
        """This is function for string we give back 3 jumps"""
        self.s=s
        try:
            if len(s)==0:
                raise ValueError("Given String have No length")
                logging.info("the given string have zero length")
            else:
                s1=s[::3]
                logging.info("The String is with jum %s :",s1)
                return s1
        except Exception as e:
            logging.info(e)


    def reverse_string(self,s):
        """This function will return all string in reverse"""
        logging.info("we into the reverse string function")
        self.s=s
        try:
            s1=s[::-1]
            logging.info("String Reverse Sucessful %s",s1)
            return s1
        except Exception as e:
            logging.exception(e)
#split string
    def split_String(self,s):
        """This function will split the string in each index one value"""
        logging.info("we in the function split string")
        try:
            s1=s.upper()
            s2=s1.split()
            logging.info("Succesfully converted in upper case and splited string %s",s2)
            return s2
        except Exception as e:
            logging.exception(e)

    def lower_string(self,s):
        """This the function for coverting string into lowercase"""
        logging.info("we are insode the lower_string")
        self.s=s
        try:
            s1=s.lower()
            logging.info("We suscessfully convert all string in lower case %s",s1)
            return s1
        except Exception as e:
            logging.exception(e)

    def Capital(self,s):
        self.s=s
        """This function will capitialize the whole string"""
        logging.info("We are inside the Capital function")
        try:
            S1=s.capitalize()
            logging.info("we sucessfully done the task %s",S1)
            return S1
        except Exception as e:
            logging.exception(e)


    def filter_volwel(self,s):
        """This function will Help to filter the vowels in string"""
        logging.info("we are inside the filter volwel function")
        self.s=s
        try:
            l=[]
            for i in self.s:
                if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
                    l.append(i)
            logging.info("we succusefully extracted the vowels from python")
            return l
        except Exception as e:
            logging.exception(e)

    def len_str(self,s):
        """This function will give you the length of the string"""
        logging.info("we are inside len_Str")
        try:
            s1=len(s)
            logging.info("we suceesfully completed the len_str task")
            return s1
        except Exception as e:
            logging.exception(e)
    def concat_Str(self,*s):
        """This function will help us to concatinate the string"""
        logging.info("we are inside the concat_str")
        self.s=s
        try:
            for i in self.s:
                j=','.join(i)
            logging.info("conacatination suscessfull")
            return j
        except Exception as e:
            logging.exception(e)








