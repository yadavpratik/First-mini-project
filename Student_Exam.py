import S2Dashboard
import UseMe as u

#check exam details
def exam(self):
    print("\n\t--------EXAM DEATLS----------\n")
    print(f"  CUREENT BRANCH   : {self.Sbranch}\n")
    print(f"  CURRENT SEMESTER : {self.Ssem}\n")
    print(f"  EBRANCH          : {self.Ebranch}\n")
    print(f"  ESem             : {self.ESem}\n")


    if self.Ebranch!=None and self.Sbranch==self.Ebranch:
        if self.ESem!=None and self.Ssem==self.ESem:
            if self.fd!=None:
                print()
                print(" SUBJECT  :",self.s)
                print(" DATE     :",self.fd)
                print(" TIME     :",self.st," to", self.et)     
            else:
                print("\n\tTHERE IS NO EXAM DTAILS ARE UPDATED BY YOUR TEACHER ") 
        else:
            print("\n\tEXAM DETAILS ARE NOT UPDATED ")
    else:
        print("\n\tEXAM DETAILS ARE NOT UPDATED ")


    u.return_dashboard(self,S2Dashboard)

