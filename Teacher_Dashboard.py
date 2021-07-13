from os import truncate
import UseMe as u   
import T3Assignment
import T4Exam
import T5Marksheet

#teacher Dashboard
def dashboard(self):
        print("\n\t-----------------------DASHBOARD--------------------------\n")
        print("  1.PROFILE           ")
        print("  2.GIVE ASSIGNMENTS  ")
        print("  3.GIVE EXAM DETAILS ")
        print("  4.UPLOD MARKSHEET   ")
        print("  5.LOGOUT            ")
        print()

        while True:
            choice=u.handle_error()
            print("\n")
            print("="*74)
            if choice==1:
                #teacher profile
                print()
                display(self)
                
            elif choice==2:
                #give Assignment
                T3Assignment.give_asignments(self)
                
            elif choice==3:
                #upload Exam details 
                T4Exam.Exam(self)
                
            elif choice==4:
                #genrate Markshhet
                T5Marksheet.genrate_marksheet(self)
            
            elif choice==5:
                False
                print("\n\t LOGOUT FROM SESSION ")
                print("="*74)
                self.Login()
            else:
                print("\n\t***OPTION IS NOT IN RANGE ****")
                print("="*74)
                dashboard(self)

#diplay informtion of teacher
def display(self):
    print("\n\t--------USER PROFILE---------")
    print()
    print("   NAME           :",self.name)
    print("   TEACHER ID     :",self.teacher_id)
    print("   EMAIL ID       :",self.email)
    print("   COLLEGE NAME   :",self.Clg)
    print("   MOBILE NO      :",self.mob)
    print("   PASSWORD       :",self.Tpass)

    choice=input("\n PRESS ENTER TO RETURN ON DASHBOARD ")
    if choice!="" or choice=="":
        dashboard(self)
