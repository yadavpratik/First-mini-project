
import UseMe as u
import S1register
import T1register
import C1register
class user:
    def __init__(self):
        u.variable.__init__(self)
        u.Export()
        self.welcome()
        

    def register(self):
        print()
        print("\t-------------------USER REGISTERATION-------------------\n")
        print("--------CHOOSE USER--------")
        print("1. COLLEGE   ")
        print("2. TEACHER   ")
        print("3. STUDENT   ")
        print()
        print("--------ALLREADY REGISTER--------\n")
        print("4. LOGIN PAGE",end=" ")
        print("\t 0. EXIT      ")
        
        print()
       
        while True:
            choice=u.handle_error()
            
            print("="*74)
            if choice==1:
                #COLLEGE REGISTRATION
                C1register.register(self)
                False

            elif choice==2:
                #TEACHER REGISTRATION
                T1register.register(self)
                False

            elif choice==3:
                #STUDENT REGISTRATION
                S1register.register(self)
                False

            elif choice==4:
                #MAIN LOGIN PAGE
                self.Login()
                False
                
            elif choice==0:
                exit()
            else:
                print("\n\t*** PLEASE PROVIDE VALIDE INPUT ****")
            

    def Login(self):
        print()
        print("\t-----------------------USER LOGIN-------------------------")
        print("1. COLLEGE   ")
        print("2. TECHER    ")
        print("3. STUDENT   ")
        print()
        print("--------NOT REGISTER--------\n")
        print("4. REGISTRATION PAGE ",end=" ")
        print("\t 0. EXIT   ")

        print()
        
        while True: 
            choice=u.handle_error()
            print("="*74)
            if choice==1:
                #college login
                C1register.Clogin(self)
                False
            elif choice==2:
                #teacher login
                T1register.Tlogin(self)
                False    
            elif choice==3:
                #student login
                S1register.Slogin(self)
                False

            elif choice==4:
                #main regitration page
                self.register()
                False     
            elif choice==0:
                exit()

            else:
                print("\n\t*** PLEASE PROVIDE VALIDE INPUT ***")
               


    def welcome(self):
        print("\n\n\n")
        print("","="*70)
        print("|"," "*67,"|\n|\t\t\tCOLLEGE PROTAL"," "*30,"|")
        print("|"," "*41, "-created by PRATIK YADAV"," |")
        print("","="*70)


        print("\nlets Start Project ")
        choice=input("\nPRESS ENTER TO START PROJECT ")
        if choice=='' or choice!='':
            print("\n\n\n")
            self.register()
r=user()
r.welcome()
