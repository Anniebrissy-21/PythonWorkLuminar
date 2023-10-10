# hiding implementation details  #14.04
from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass      #implementation details is not give hidden 

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def acclerate(self):
        pass

class Swift(Car):

    def start(self):
        print("swift start")

    def stop(self):
        print("swift stop")

    def acclerate(self):
        print("swift acclerate")


obj=Swift()
obj.start()
obj.stop()
obj.acclerate()

