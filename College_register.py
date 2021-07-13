from stdiomask import getpass

import UseMe as u
import csv
import C2Dashboard
#college regitration
def register(self):
    
        print("\n\t-------------------REGISTER YOUR COLLEGE PORTAL -------------------")
        print()
        #GETTIN INFO
        self.Cname       = u.clg_validation()
        self.Cadd        = input("\nENTER COLLEGE ADDRESS   : ")
        self.Cmob        = u.mob_validate()
        self.Cemail      = u.email_validation()

        print()

        self.Cpass=u.create_password()
             
        self.info={'SR NO':"1",'COLLEGE NAME':self.Cname,'COLLEGE ADDRESS':self.Cadd,'EMAIL ID':self.Cemail,'MOBILE NO':self.Cmob,
        'PASSWORD':self.Cpass}
        CData_export(self)
        print("\n\t-------------SUCESSFULLY REGISTER ON COLLEGE PORTAL-------------\n")
        print("="*74)
        Clogin(self)


#storing clg data in csv
def CData_export(self):
        with open("college_info.csv",'a',newline="") as f:
            writer=csv.DictWriter(f,fieldnames=['SR NO','COLLEGE NAME','COLLEGE ADDRESS','EMAIL ID','MOBILE NO','PASSWORD'])
            writer.writerow(self.info)
            print("row inserted ")
        
#college login
def Clogin(self):
    print("\n\t--------------------LOGIN AS COLLEGE--------------------\n")
            
    self.Uname    = input(" ENTER YOUR MOBILE NO OR EMAIL ID : ")
    self.Password = getpass("\n ENTER YOUR PASSWORD              : ") 
    self.Clog=False
    #READING TEACHERS DATA FROM FILE
    with open("college_info.csv",'r',newline="") as f:
        reader=csv.DictReader(f)
        for data in reader:
            if (data['MOBILE NO']==self.Uname and data['PASSWORD']==self.Password) or (data['EMAIL ID']==self.Uname and data['PASSWORD']==self.Password):
                self.Clog=True
                #RE -ASIGN DATA IN VARIABLES FOR FURTHER USE
                self.Cname      = data['COLLEGE NAME']
                self.Cadd       = data['COLLEGE ADDRESS']               
                self.Cemail     = data['EMAIL ID']
                self.Cmob       = data['MOBILE NO']
                self.Cpass      = data['PASSWORD']
                

    if self.Clog:
        print("\n\t-------------------SUCESSFULLY LOGIN------------------")
        print("\n")
        print("="*74)
        C2Dashboard.dashboard(self)
    
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
                Clogin(self)
                False
            elif choice==0:
                exit()
            else:
                print("\n\t OPTION NOTE IN RANGE  ")
                print("\n","="*70)
                
                    

