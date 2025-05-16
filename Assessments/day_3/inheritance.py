#parent class
class hospital:
    def __init__(self,pid, pname):
        self.pid = pid
        self.pname = pname
    def display(self):
        print(f"Patient id: {self.pid}\npatient name: {self.pname}")


#sub class
class visit(hospital):
    def __init__(self, pid, pname, issue, dname):
        super().__init__(pid, pname)
        self.issue = issue
        self.dname = dname

    def display(self):
        print(f"Patient id:{self.pid} \npatient name:{self.pname} \npurpose of visit:{self.issue} \nvisiting Doctor:{self.dname}")

class pharmacy(hospital):
    def __init__(self, pid, pname,quantity,spend):
        super().__init__(pid, pname)
        self.quantity = quantity
        self.spend = spend

    def display(self):
        print(f"Patient id:{self.pid} \npatient name:{self.pname} \nMedicine collect:{self.quantity} \ntotal spend:${self.spend}")
#main function

def main():
    p1=visit(101,'praveen','fever','Dr. raghu')
    p2=visit(102,'arun','fever','Dr. tharun')
    p3=pharmacy(103,'koushik',20,5000)
    p1.display()
    print('-'*5)
    p2.display()
    print('-'*5)
    p3.display()
    print('-'*5)

if __name__ == "__main__":
    main()