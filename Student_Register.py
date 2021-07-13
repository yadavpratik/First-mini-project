from stdiomask import getpass
import UseMe as u
import S2Dashboard
import csv

#Student Registration 
def register(self):
        print()
        print("\n\t-------------------REGISTER AS STUDENT-------------------")
        print()
        #get info
        self.Name  = u.names_validation()

        self.Email = u.email_validation()

        self.Clg   = u.clg_validation()
        
        self.Roll  = input("\nENTER ROLL NO           : ")

        self.Mob   = u.mob_validate()
                
        print("\n------SELECT CURRENT BRANCH-----\n")
        u.Print(self.branchs)
        print()
        u.select_Branch(self)
        self.Sbranch=self.branch 
    
        print("\n--------SELECT SEMESTER----------\n")
        u.Print(self.sem)
        print()
        u.select_sem(self)
        self.Ssem=self.Sem

        u.Print(self.subj)
        print()
        
        self.Spass=u.create_password()
        
        self.info={'SR NO': " ",'NAME':self.Name,'ROLL NO':self.Roll,'EMAIL ID':self.Email,'COLLEGE':self.Clg,
                'MOBILE NO':self.Mob,'BRANCH':self.Sbranch,'SEMESTER':self.Sem,'PASSWORD':self.Spass}
        
       
        SData_export(self) 
        print("\n\t---------------SUCESSFULLY REGISTER AS STUEDENT------------\n")
        print("="*74)

        Slogin(self)

#storing student data in csv file
def SData_export(self):
        with open("student_info.csv",'a',newline="") as f:
            writer=csv.DictWriter(f,fieldnames=['SR NO','NAME','ROLL NO', 'EMAIL ID', 'COLLEGE', 'MOBILE NO','BRANCH','SEMESTER','PASSWORD'])
            writer.writerow(self.info)
            print("row inserted ")

#student login           
def Slogin(self):
    print("\n\t----------------------LOGIN AS STUDENT----------------------\n")
            
    self.Uname    = input(" ENTER YOUR MOBILE NO OR EMAIL ID : ")
    self.Password = getpass(" ENTER YOUR PASSWORD              : ") 
    self.Slog=False
    #import student data from csv file
    with open("student_info.csv",'r',newline="") as f:
        reader=csv.DictReader(f)
        for data in reader:

            if (data['MOBILE NO']==self.Uname and data['PASSWORD']==self.Password) or (data['EMAIL ID']==self.Uname and data['PASSWORD']==self.Password):
                self.Slog=True
                #re-asign data in variables for further use
                self.Name       = data['NAME']
                self.Roll       = data['ROLL NO']
                self.Email      = data['EMAIL ID']
                self.Clg        = data['COLLEGE']
                self.Mob        = data['MOBILE NO']
                self.Sbranch    = data['BRANCH']
                self.Sem        = data['SEMESTER']
                self.Spass      = data['PASSWORD']


    if self.Slog:
        print("\n\t-------------------SUCESSFULLY LOGIN------------------")
        print("\n")
        print("="*74)
        S2Dashboard.dashboard(self)
    else:
        print("\n","="*70)
        print("\n\tYOUR DETAILS NOT FOUND ")
        print("\n   PLEASE REGISTER OR LOGIN WITH CORECT CREDENTIAL")
        print("\n\t1.REGISTER ","\t2. LOGIN AGAIN ","\t0. Exit")
        while True:
            choice=u.handle_error()
            print("="*70)
            if choice==1:
                register(self)
                False
            elif choice==2:
                Slogin(self)
                False
            elif choice==0:
                exit()
            else:
                print("\n\t OPTION NOTE IN RANGE  ")
                print("\n","="*70)
                
