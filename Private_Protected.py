#Protected Class
class Employee:
    def __init__(self,name,job_title,num_citations):
        self._name = name #protected can be accessed but not advised. 
        self.job_title = job_title #public
        self.__num_citations = num_citations # private gives attribute error



e1 = Employee("Sam Kavkewitz","CEO",183)
     
print(e1.__num_citations) # attribute error given


