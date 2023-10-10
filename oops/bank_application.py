#using abstraction 
from abc import ABC,abstractmethod

class BankingApp(ABC):

    @abstractmethod
    def FundTransfer(self):
        pass

    @abstractmethod
    def BalanceEnquiry(self):
        pass

    @abstractmethod
    def TransactionHistory(self):
        pass

class G_pay(BankingApp):

    def FundTransfer(self):
        print("Fund transfering")

    def BalanceEnquiry(self):
        print("Balance Enquiry")

    def TransactionHistory(self):
        print("Transaction details")


obj=G_pay()
obj.FundTransfer()
obj.BalanceEnquiry()
obj.TransactionHistory()