import UseMe as u
import T2Dashboard
#ADD EXAM DETAILS 
def Exam(self):

    print("\n\t------------------UPLOAD EXAM DETAILS--------------------- ")
    #GET BRANCH FIRST
    #TO KNOW FOR WITCH BRANCH EXAM DETALS ARE UPDATED
    print("\n-------SELLECT BRANCH------\n")
    u.Print(self.branchs)
    print()

    u.select_Branch(self)
    self.Ebranch=self.branch
    print("\nSELECTED BRANCH : ",self.Ebranch)
    print()

    #GET SEMESTER
    #TO KNOW FOR WITCH SEMESTER OF THAT BRANCH EXAM DETALS ARE UPDATED
    print("\n-------SELLECT SEMESTER------\n")
    u.Print(self.sem)
    print()

    u.select_sem(self)
    self.ESem=self.Sem
    #GET SUBJECT
    #SELECT ONE SUBJECT FOR WITCH DATE AND TIME OF EXAM SHOULD BE UPDATED
    print("\nSELECTED SEMESTER : ",self.ESem)
    print()

    self.s,self.fd,self.st,self.et=add_Again(self)

    print("\n---POST DATE AND TIME ---")
    print("\n1. SUBMIT     ")
    print("\n2. RE-SHEDULE ")
    print()
    choice=int(input("ENTER YOUR CHOICE : "))
    a=True
    while a:
        if choice==1:
            print("\n YOU SUCESSFULY SHEDULED DATE AND TIME FOR EXAM ")
            print(f"\nSUBJECT    : {self.s}")
            print(f"EXAM DATE  : {self.fd} ")
            print(f"EXAM TIME  : {self.st} to {self.et}")
            a=False
        elif choice==2:
            print("RE-SHEDULED :")
            add_Again(self)
        else:
            print()
            choice=int(input(" SELECT CORRECT OPTION :"))

    u.return_dashboard(self,T2Dashboard)


#add date and time for another subject
def add_Again(self):
    print("\n-------SELLECT SUBJECTS------\n")
    u.Print(self.subj)
    print()
    choice=u.handle_error()
    x=1
    for i in self.subj:
        if choice==x:
            print(f"\n SHEDULE DATE AND TIME OF THE EXAM FOR SUBJEC :  {i}")
            s=i
            print()
            print("---SHEDULE DATE---")
            fd=u.Date(self)

            print("---SHUDELE TIME---\n")

            st,et=u.Time()
            
        x+=1
    return s,fd,st,et