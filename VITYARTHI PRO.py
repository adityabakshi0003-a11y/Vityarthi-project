print("Welcome to VIT GPA Calcula44tor")
name=str(input("Enter your name: "))
print("Hello",name)
year=int(input("which year are you in: "))
if(year>1):
    cgpa=float(input("Enter your previous semester GPA: "))
if (year==0):
    print("Invalid year")
    exit()
no_of_subject=int(input("How many subjects do you have in this semester: "))
subjects=[]
marks=[]
totalgpa=0
gpa=0
S=10/no_of_subject
A=9/no_of_subject
B=8/no_of_subject
C=7/no_of_subject
D=6/no_of_subject
E=5/no_of_subject
F=0
for i in range(no_of_subject):
    name1=str(input("Enter the subject's name: "))
    subjects.append(name1)
    submarks=float(input("Enter the score(out of 50/100): "))
    marks.append(submarks)
    avg=float(input("Enter the average score of the subject: "))
    value=submarks-avg
    highestmarksawarded=float(input("Enter the highest score of the class: "))
    value2=highestmarksawarded-submarks
    subjectgrade=0
    if(value2<=5):
        print("S Grade in the subject, congrats")
        subjectgrade=S
    elif(value>=3):
        print("A Grade awarded")
        subjectgrade=A
    elif(value<=3 and value>=-3):
        print("B Grade awarded")
        subjectgrade=B
    elif(value>=-5):
        print("C Grade awarded")
        subjectgrade=C
    elif(value>=-10):
        print("D Grade awarded")
        subjectgrade=D
    elif(value>=-15):
        print("E Grade awarded")
        subjectgrade=E
    elif(submarks<=20 or submarks<=40):
        print("F Grade awarded")
        subjectgrade=F
    totalgpa=totalgpa+subjectgrade

print(totalgpa)