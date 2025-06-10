class bank:
    def __init__(self, accname, balance):
        self.bnk_acc_name = accname
        self.__bnk_acc_balance = balance

    def getter(self):
        return("Bank Balance is", self.__bnk_acc_balance)
    
    def setter(self, balance):
        self.__bnk_acc_balance = balance

bankdetails = bank("Muthu" , 100000000)
print(bankdetails.bnk_acc_name, bankdetails.getter())
bankdetails.setter(9999999999999999)
print(bankdetails.getter())
