from stdiomask import getpass
import UseMe as u
import T2Dashboard
import csv


#TEACHER REGISTRATION
def register(self):
        print("\n\t-------------------REGISTER AS TEACHER-------------------")
        print()
        #GETTIN INFO
        self.name       = u.names_validation()
        
        self.email      = u.email_validation()
        
        self.clg        = u.clg_validation()
       
        self.teacher_id = input("\nENTER TEACHER ID        : ")

        self.mob        = u.mob_validate()
        
        print()

        self.Tpass=u.create_password()
             
        self.info={'SR NO':"1",'NAME':self.name,'TEACHER ID':self.teacher_id,'EMAIL ID':self.email,'COLLEGE':self.clg,'MOBILE NO':self.mob,
        'PASSWORD':self.Tpass}
        TData_export(self)   
        print("\n\t-------------SUCESSFULLY REGISTER AS TEACHER-------------\n")
        print("="*74)
        Tlogin(self)                    

#STORING DATA IN CSV FILE 
def TData_export(self):
        with open("teacher_info.csv",'a',newline="") as f:
            writer=csv.DictWriter(f,fieldnames=['SR NO','NAME','TEACHER ID','EMAIL ID','COLLEGE','MOBILE NO','PASSWORD'])
            writer.writerow(self.info)
            print("row inserted ")
                
#TEACHER LOGIN
def Tlogin(self):
    print("\n\t---------------------LOGIN AS TEACHER---------------------\n")
            
    self.Uname    = input(" ENTER YOUR MOBILE NO OR EMAIL ID : ")
    self.Password = getpass(" ENTER YOUR PASSWORD              : ") 
    self.Tlog=False
    
    #READING TEACHERS DATA FROM FILE
    with open("teacher_info.csv",'r',newline="") as f:
        reader=csv.DictReader(f)
        for data in reader:
            if (data['MOBILE NO']==self.Uname and data['PASSWORD']==self.Password) or (data['EMAIL ID']==self.Uname and data['PASSWORD']==self.Password):
                self.Tlog=True
                #RE -ASIGN DATA IN VARIABLES FOR FURTHER USE
                self.name       = data['NAME']
                self.teacher_id = data['TEACHER ID']
                self.email      = data['EMAIL ID']
                self.Clg        = data['COLLEGE']
                self.mob        = data['MOBILE NO']
                self.Tpass      = data['PASSWORD']
            

    if self.Tlog:
        print("\n\t-------------------SUCESSFULLY LOGIN------------------")
        print("\n")
        print("="*70)
        T2Dashboard.dashboard(self)
    
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
                Tlogin(self)
                False
            elif choice==0:
                exit()
            else:
                print("\n\t OPTION NOTE IN RANGE  ")
                print("\n","="*70)