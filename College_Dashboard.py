import UseMe as u
import C3branch
def dashboard(self):
        print("\n\t-----------------------DASHBOARD--------------------------\n")
        print("  1.PROFILE           ")
        print("  2.CHECK TOTAL BRANCH ")
        print("  3.CHECK TOTAL SEMESTER ")
        print("  4.CHECK TOTAL SUBJECTS PER SEMESTR ")
        print("  5.LOGOUT            ")
        print()

        while True:
            choice=u.handle_error()
            print("="*74)
        
            if choice==1:
                #college profile
                print()
                display(self)
                
            elif choice==2:
                #check total branch in college
                C3branch.branch(self)               
                
            elif choice==3:
                #college semester in particular branch
                C3branch.sem(self)                
            
            elif choice==4:
                # subjects in particular semester of particular branch
                C3branch.subjects(self)              

            elif choice==5:
                False
                print("\n\t LOGOUT FROM SESSION ")
                print("="*74)
                self.Login()
            else:
                print("\n\t***OPTION IS NOT IN RANGE ****")
                print("="*74)
                dashboard(self)

#diplay informtion of college
def display(self):
    
    print("\n\t---------------------USER PROFILE-------------------------\n")
    print()
    print("   COLLEGE NAME     :",self.Cname)
    print('   COLLEGE ADDRESS  :',self.Cadd)
    print("   EMAILID          :",self.Cemail)
    print("   MOBILE NO        :",self.Cmob)
    print("   PASSWORDS        :",self.Cpass)

    choice=input("\n PRESS ENTER TO RETURN ON DASHBOARD ")
    print("="*74)
    if choice!="" or choice=="":
        dashboard(self)
        