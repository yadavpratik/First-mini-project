import UseMe as u
import S3Asignments 
import S4Exam
import S5Marksheet
#STUDENT DASHBOARD
def dashboard(self):
        print()
        print("\t-----------------------DASHBOARD--------------------------\n")
        print("  1.PROFILE            ")
        print("  2.CHECK ASSIGNMENTS  ")
        print("  3.CHECK EXAM DETAILS ")
        print("  4.CHECK MARKSHEET    ")
        print("  5.LOGOUT             ")
        print()
        while True:
            choice=u.handle_error()
            print("\n")
            print("="*74)
            if choice==1:
                #print student profile
                print()
                display(self)
                
            elif choice==2:
                #check assignment of subjects
                S3Asignments.check_asignment(self)

            elif choice==3:
                #check Exam details
                S4Exam.exam(self)
                
            elif choice==4:
                #check marksheet
                S5Marksheet.check_maeksheet(self)

            elif choice==5:
                #Exit program
                False
                print("\n\t LOGOUT FROM SESSION ")
                print("="*74)
                self.Login()

            else:
                print("\n\t***OPTION IS NOT IN RANGE ****")
                print("="*74)
                dashboard(self)

#DISPLAY STUDENT INFORMATION 
def display(self):
    print("\n\t--------USER PROFILE---------")
    print()
    print("   NAME           :",self.Name)
    print("   ROLL NO        :",self.Roll)
    print("   EMAIL ID       :",self.Email)
    print("   COLLEGE NAME   :",self.Clg)
    print("   MOBILE NO      :",self.Mob)
    print("   BRANCH         :",self.Sbranch)
    print("   SEMESTER       :",self.Sem)
    print("   PASSWORD       :",self.Spass)

    choice=input("\n PRESS ENTER TO RETURN ON DASHBOARD ")
    if choice!="" or choice=="":
        dashboard(self)
