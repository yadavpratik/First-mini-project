import UseMe as u
import S2Dashboard
#check marksheet
def check_maeksheet(self):
        print("\n\t---------CHECK MARKSHEET---------\n")
        print(f"  CUREENT BRANCH   : {self.Sbranch}\n")
        print(f"  CURRENT SEMESTER : {self.Ssem}\n")
        print(f"  MBRANCH          : {self.Mbranch}\n")
        print(f"  MSEM             : {self.MSem}\n")

        if self.Mbranch!=None and self.Sbranch==self.Mbranch:
            if self.MSem!=None and self.Ssem==self.MSem:
                if (self.Name!=self.Student_name and self.Roll!=self.Student_roll) or self.subj_mark==[]:
                    print("\n\t YOUR MARKSHEET NOT UPDATED YET ")
                else:
                    u.Result(self)                
            else:
                print("\n\t YOUR MARKSHEET NOT UPDATED YET ")
        else:
            print("\n\t YOUR MARKSHEET NOT UPDATED YET  ")

        
        u.return_dashboard(self,S2Dashboard)