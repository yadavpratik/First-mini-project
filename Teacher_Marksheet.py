import UseMe as u
import T2Dashboard
#GENRATE STUDENT MARKSHEET
def genrate_marksheet(self):
        print("\n\t---------------------GENRATE MARKSHEET-------------------")
        print("\n----PROVIDE STUDENT DETAILS----")
        marksheetInput(self)
        print("\n---PROVIDE MARKS OF SUBJECTS----\n")
        calci(self)
        u.Result(self)

        u.return_dashboard(self,T2Dashboard)

#FIRST TO SELECT BRANCH AND SEMESTER
#TO KNOW THAT FOR WHICH BRANCH STUDENT MARKSHEET WILL BE GENRATED 
def marksheetInput(self):
    print()
    print("\n-------SELLECT BRANCH------\n")
    u.Print(self.branchs)
    print()
    u.select_Branch(self)
    self.Mbranch=self.branch
    print("\n BRANCH SELECTED   :",self.Mbranch)

    print("\n-------SELLECT SEMESTER------\n")
    u.Print(self.sem)
    u.select_sem(self)
    self.MSem=self.Sem
    print("\n SEMESTER SELECTED :",self.MSem)

    print("\n-----------SUBJECTS---------\n")
    u.Print(self.subj)

    self.Student_name   = input("\n ENTER NAME OF STUDENT : ")
    self.Student_roll   = input("\n ENTER ROLL NO         : ")
    u.Date(self)


def calci(self):
    self.subj_mark=[]
    print()
    for i in range(0,len(self.subj)):
        l=len(self.subj[i])
        
        self.mark=float(input(f" MARK OF {self.subj[i]}: " ))
        self.subj_mark.append(self.mark)

    for i in self.subj_mark:
        if i>=40:
            self.result='Pass'
        else:
            self.result='Fail'
            break

    self.total=len(self.subj)*100
    self.obtained=sum(self.subj_mark)
    self.percent=self.obtained/len(self.subj)
