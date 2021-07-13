from abc import ABC, abstractmethod

class crime(ABC):
    def theftArmed(self,sentence): 
         print("The time served for armed robbery: ",sentence)
    @abstractmethod # passing water arugment for water parameter
    def timeServe(self,sentence):
        pass
class penaltyFelony(crime):
    def timeServe(self,sentence):
        print("Number of months to serve: {} ".format(sentence))

obj = penaltyFelony()
obj.theftArmed(42)
obj.timeServe(42)

