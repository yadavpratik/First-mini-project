import UseMe as u
import T2Dashboard
#giving assignments
def give_asignments(self):
        print("\n\t------------UPLOAD ASSIGNMENTS FOR STUDENTS---------------- ")
        
        print("\n-------SELLECT BRANCH------\n")
        u.Print(self.branchs)
        print()

        u.select_Branch(self)
        self.Abranch=self.branch
        print("\nSELECTED BRANCH : ",self.Abranch)
        
        print("\n-------SELLECT SEMESTER------\n")
        u.Print(self.sem)
        print()

        u.select_sem(self)
        self.ASem=self.Sem
        print("\nSELECTED SEMESTER : ",self.ASem)
        print("\n-------SELLECT SUBJECTS------\n")
        
        again(self)
         
        while True:
            print("\n YOU WANT TO UPLOAD MORE ASIGNMENT ENTER [Yes / No] ")
            choice=input(" ENTER YOUR CHOICE :")
            if choice=='yes' or choice=='Yes' or choice=='YES':
                print("\n-------SELLECT SUBJECTS------\n")
                again(self)
            else:
                False
                u.return_dashboard(self,T2Dashboard)

def again(self):
        u.Print(self.subj)
        print()
        choice=int(input(" ENTER YOUR CHOICE :"))
        x=1
        self.Asignment={}
        self.Asign_name=[]

        for i in self.subj:
            if choice==x:
                print(f"\n SELECTED SUBJECT  :  {i}")
                print("\n\t-------ENTER BASIC DATAILS------\n")
    
                no=int(input(f" HOW MANY ASSIGNMENT TO BE GIVEN FOR SUBJECT {i} : "))
                
                for j in range(0,no):
                    name=input(f"\n ENTER ASSIGNMENT{j+1} NAME :")
                    
                    self.Asign_name.append(name)
                    self.Asignment[i]=self.Asign_name
                
                print("\n----ENTER 'post' TO UPLOAD ASSIGNMENT-----")
                a=True
                choice=input("\nENTER CHOICE : ")
                while a:
                    if choice =='post' or choice=='Post' or choice=='POST':
                        
                        print("\n\t-------------ASSIGNMENT POSTED SUCCESSFULLY--------------")
                        a=False
                    else:
                        print("\n*** YOU GIVEN WRONG INPUT  ***")
                        choice=input("ENTER AGAIN :")
            x+=1


