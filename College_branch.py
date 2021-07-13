import UseMe as u
import C2Dashboard
#college branchs
def branch(self):
    print("\n\t-------------------CHECK TOTAL BRANCH---------------------\n")
    print(" BRANCH ARE ALREADY ADDED\n ")
    u.Print(self.branchs)
    u.return_dashboard(self,C2Dashboard)

#college semester
def sem(self):
    print("\n\t------------------CHECK TOTAL SEMESTER--------------------\n")
    print("TO CHECK SSEMESTER PRESENT IN PARTICULAR BRANCH ")
    print("\n First Select branch\n")
    u.Print(self.branchs)
    print()
    u.select_Branch(self)
    
    print(f"\nSEMESTER PRESENT IN {self.branch} \n")
    u.Print(self.sem)
    u.return_dashboard(self,C2Dashboard)

#college subjects
def subjects(self):
    print("\n\t-------------------CHECK TOTAL SUBJECTS-------------------\n")
    print(" TO CHECK SUBJECTS FIRST SELECT BRANCH \n")
    u.Print(self.branchs)
    print()
    u.select_Branch(self)

    print("\n SELECT SEMESTER \n")
    u.Print(self.sem)
    print()
    u.select_sem(self)

    print(f"SUBJECTS PRESENT IN {self.Sem} \n")
    u.Print(self.subj)

    u.return_dashboard(self,C2Dashboard)