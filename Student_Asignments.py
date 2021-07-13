import UseMe as u
import S2Dashboard
#CHECK ASSIGNMENT UPLOAD FROM TEACHERS
def check_asignment(self):
    print("\n\t--------CHECK ASSIGNMENTS---------")
    print()

    print(f"  CUREENT BRANCH   : {self.Sbranch}\n")
    print(f"  CURRENT SEMESTER : {self.Ssem}\n")
    print(f"  ABRANCH          : {self.Abranch}\n")
    print(f"  ASem             : {self.ASem}\n")
    
    if self.Abranch!=None:
        if self.Sbranch==self.Abranch:
            if self.Ssem==self.ASem:
                print()
                Asignments(self)
            else:
                print("\n\t  ASSIGNMENTS NOT UPLOADED YET ")
        else:
            print("\n\t ASSIGNMENTS NOT UPLOADED YET ")
    else:
        print("\n\t ASSIGNMENTS NOT UPLOADED YET ")

    u.return_dashboard(self,S2Dashboard)


def Asignments(self):
    self.work='No asignment'
    self.subjects={}
    for i in self.subj:
        self.subjects[i]=self.work

    
    if self.Asignment=={}:
        print("\t NO ASSIGNMENT UPDATED ")
    else:
        for k,l in self.subjects.items():
            for i,j in self.Asignment.items():
                if k==i:
                    self.subjects[k]=j

        print("ASSIGNMENT UPDATED")
        for i,j in self.subjects.items():
            if j!=self.work:
                print(i,":")
                u.Print(j)