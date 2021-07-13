
import machenical.subjects as me
import CS.subjects as cs
import IT.subjects as it
import Civil_Engg.subjects as ce
import datetime as dt
import csv
from stdiomask import getpass
import re
from validate_email import validate_email

class variable:
    def __init__(self):
       #Studrnt class variables
        self.Name   = None
        self.Email = None
        self.Clg    = None
        self.Class  = None
        self.Roll   = None
        self.Mob    = None
        self.Asignment={}
        self.Abranch = None
        self.ASem    = None
        self.Ebranch = None
        self.ESem    = None
        self.Mbranch = None
        self.MSem    = None

        # teacher class variables
        self.name=None
        self.email=None
        self.clg=None
        self.teacher_id=None
        self.mob=None
        self.Tpass=None

        self.branch = None
        self.Sem    = None
        self.subj   = None
        self.obj    = None
        self.fd     = None
        self.DATE   = None
        self.subj_mark=[]

        self.login=['STUDENT','TEACHER','COLEGE']
        self.branchs=["MACHENICAL ENGINEERING","INFORAMTION TECHNOLOGY",
                "COMPUTER SCIENCE","CIVIL ENGINEERING"]  

        self.sem=['FIRST SEMESTER','SECOND SEMESTER']  
        self.objects=[me,it,cs,ce]


                
def Print(subj):
    x=1
    for i in subj:
        print(f"\t{x} . {i}")
        x+=1

def select(item,choice):
    for i in range(1,len(item)+1):
        if choice==i:
            return item[i-1]

    
def select_sem(self):
    #select sem and assign subjects
    choice=handle_error()
    self.Sem=select(self.sem,choice)

    if self.Sem==self.sem[0]:
        self.subj=self.obj.First_sem()

    elif self.Sem==self.sem[1]:
        self.subj=self.obj.Second_sem()
    else:
        select_sem(self)


def select_Branch(self):
    #selecs branch
    choice=handle_error()
    if choice!=0 and choice<=len(self.branchs):
        self.branch=select(self.branchs,choice)
        self.obj=select(self.objects,choice)
    else:
        print("****ENTER CORRECT CHOICE ****")
        select_Branch(self)


#get date and time 
def Date(self):
    d,m,y=map(int, input("\n ENTER DATE IN FORMAT(dd mm yy) : ").split())
    fd=dt.date(y,m,d)
    fd=dt.date.strftime(fd,'%d-%m-%Y')
    self.DATE=fd
    print()

    return fd

def Time():
    hr,mm=map(int,input(" ENTER START TIME OF EXAM IN (hh mm) : ").split())
    st=dt.time(hr,mm)
    st=dt.time.strftime(st,'%I:%M %p')
    hr,mm=map(int,input(" ENTER START TIME OF EXAM IN(hh mm)  : ").split())
    et=dt.time(hr,mm)
    et=dt.time.strftime(et,'%I:%M %p')
    return st,et

def Result(self):
    print()
    print("="*60)
    print(" "*41,"DATE : ",self.DATE,"\n")
    print(" "*10,"COLLEGE :",self.clg,"\n")
    print("="*60)

    print("|"," "*8,"STUDENT NAME   :",self.Student_name," "*(29-len(self.Student_name)),"|")
    print("|"," "*8,"ROLL NO        :",self.Student_roll," "*(29-len(self.Student_roll)),"|")
    print("|"," "*8,"BRANCH         :",self.branch," "*(29-len(self.branch)),"|")
    print("|"," "*8,"SEMESTER       :",self.Sem," "*(29-len(self.Sem)),"|")
    

    print("="*60)
    print()
    
    print(" ","SUBJECTS NAME   :  TOTAL MARKS   :   OBTAINED MAEKS   :")
    print(" ","-"*55)
    
    for i in range(0,len(self.subj)):
        le=len(self.subj[i])
        print(" ",self.subj[i]," "*(14-le),":\t100 "," "*5,":\t",self.subj_mark[i],"\t\t:")

    print("="*60)
    print()
    print(" RESULT STATUS   :",self.result)
    print(" TOTAL MARK      :",self.total)
    print(" OBTAINED MAEKS  :",self.obtained)
    print(" PERCENTAGE      :",self.percent)
    print("="*60)


def handle_error():
    while True:
        try:
            choice=int(input("\nENTER YOUR CHOICE : "))
        except:
            print("\n\t**CHOICE IS ONLY IN DIGIT**")
        else:
            False
            return choice


def return_dashboard(self,D):
    choice=input("\n PRESS ENTER TO RETURN ON DASHBOARD ")
    print("\n","="*74)
    
    if choice!="" or choice=="":
        D.dashboard(self)
        


def Export():
    import csv
    with open("teacher_info.csv",'a',newline="") as T:
        writer=csv.DictWriter(T,fieldnames=['SR NO','NAME','TEACHER ID','EMAIL ID','COLLEGE','MOBILE NO','PASSWORD'])
        writer.writeheader()
        print("teacher_data storage conected ")
    
    with open("student_info.csv",'a',newline="") as S:
        writer=csv.DictWriter(S,fieldnames=['SR NO','NAME','ROLL NO', 'EMAIL ID', 'COLLEGE', 'MOBILE NO','BRANCH','SEMESTER','PASSWORD'])
        writer.writeheader()
        print("student data storage connected ")
         
    with open("college_info.csv",'a+',newline="") as f:
        writer=csv.DictWriter(f,fieldnames=['SR NO','COLLEGE NAME','COLLEGE ADDRESS','EMAIL ID','MOBILE NO','PASSWORD'])
        writer.writeheader()
        print("college data1 storage connected")




def create_password():
    print("\n\t--------Create Password--------\n")
    miss=0
    Pass  = getpass(" ENTER PASWWORD   :")
    cpass = getpass("\n CONFIRM PASWWORD :")
    if Pass==cpass:
        print("\n\t---Pasword  Created Sucessfully---")
    else:
        print("\n","-"*40)
        print("\t-----PASWWORD DID NOT MATCH----")
        print("\t\tTRY AGAIN :")
        Pass=create_password()

    return Pass

def paswword_validate(Pass):
    if not len(Pass)>=8:
        print('\nPassword lenth must be eight character or more')
        miss=1

    if re.search('\s',Pass):
        print("\nPassword not cotain any space ")
        miss=1
        
    if not re.search('[a-z]',Pass):
        print("\npassword must contains atleast one lowercase letters")
        miss=1
    if not re.search('[A-Z]',Pass):
        print("\npassword must contains atleast one uppercase letters")
        miss=1
    if not re.search('[0-9]',Pass):
        print("\npassword must contains atleast one digits")
        miss=1
    if not re.search('[@]',Pass):
        print("\nPassword must contains only '@' special symbols")
        miss=1

    if miss==0:
        return True
    


def names_validation():
    miss =0
    name=input("\nENTER NAME              : ")

    if re.findall('\W',name):
        if not re.findall('\s[A-Za-z]',name):
            miss=1
    if re.findall("[0-9]",name):
        miss=1

    if name!='' and miss==0 :
        print('valid name ')

    else:
        print('invalid name')
        print("\nEnter again :")
        name=names_validation()
    return name


def clg_validation():
    miss =0
        
    clg=input("\nENTER COLLEGE NAME      : ")
    if re.findall('\W',clg):
        if not re.findall('\s[A-Za-z]',clg):
            miss=1

    if re.findall("[0-9]",clg):
        miss=1

    if clg!='' and miss==0:
        print('valid name')
    else:
        print('invalid name')
        print("Enter again :")
        clg=clg_validation()

    return clg

def mob_validate():
    miss=0
    
    mob=input("\nENTER MOBILE NUMBER     : ")
    if not re.findall('\D',mob):
        if len(mob)==10:
            print("valid number ")
        else:
            print("\nmobile number must contain 10 digit")    
            mob=mob_validate()
    else:
        print("\nEnter mobile number in digits only")
        mob=mob_validate()

    return mob
    

def email_validation():
         
    mail=input("\nENTER EMAIL ID          : ")

    if validate_email(mail):
        print("Valid Email")
    else:
        print("Invalid Email")
        print("\nEnter again :")
        mail=email_validation()

    return mail

