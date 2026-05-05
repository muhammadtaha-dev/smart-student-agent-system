# Smart Student Profile Agent System
# Built using Python (Beginner Agentic AI Project)
# Features:
# - Add Student
# - View Students
# - Search Student
# - Grade & Status (Agent Decision Making)


student_info:list=[]   #created an empty list in order to store student info

student_names:set=set()   #created a set in order to store names,so that name can not be duplicated

def AddStudent(name,age,subject1,subject2,subject3):   #function for adding a student
    
    avg=Average(subject1,subject2,subject3)
    grade=Grade(avg)
    status=Status(avg)

    if name in student_names:
        print(f"Student of name {name} already exists!")
        return

    student_names.add(name)    
    student:dict={
        "Name":name,
        "Age":age,
        "Subject1":subject1,
        "Subject2":subject2,
        "Subject3":subject3,

        "Average":avg,
        "Grade":grade,
        "Status":status,
    }
    student_info.append(student)
    print("Student added successfully!")

def Average(sub1,sub2,sub3):   #function for calculating average
    average:float=(sub1+sub2+sub3)/3
    return average

def Grade(avg):   #function for calculating grade
    if(avg>=80 and avg<=100):
        return "A"
    elif(avg>=60 and avg<80):
        return "B"
    elif(avg>=40 and avg<60):
        return "C"
    else:
        return "F"
    
def Status(avg):   #function for determining status

    if(avg>85):
        return "Top Student!"
    elif(avg<40):
        return "Needs Improvement!"
    else:
        return "Good Student!"
    
def ViewStudents():   #function to view all students
    if not student_info:
        print("No students found!")
        return
    for students in student_info:
        print(f"Name: {students['Name']}")
        print(f"Age: {students['Age']}")
        print(f"Average: {students['Average']}")
        print(f"Grade: {students['Grade']}")
        print(f"Status: {students['Status']}")
        print("------------------------------")

def SearchStudent(name):   #function to search for a student in list
    found:bool=False

    for student in student_info:
        if student["Name"].lower()==name:
            print(f"\nStudent {name} found!\n")
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Average: {student['Average']}")
            print(f"Grade: {student['Grade']}")
            print(f"Status: {student['Status']}")
            print("------------------------------")
            found=True
            break
    if not found:
        print(f"{name} not found!")



print("******************** Welcome to Smart Student Profile System ********************")
print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Exit")

while True:

    option:int=int(input("Enter choice (1-4): "))

    match option:
        case 1:
            name:str=input("Write student name: ")
            age:int=int(input("Write student age: "))
            sub1:int=int(input("Write the marks of subject 1: "))
            sub2:int=int(input("Write the marks of subject 2: "))
            sub3:int=int(input("Write the marks of subject 3: "))
            
            AddStudent(name,age,sub1,sub2,sub3)
        case 2:
            ViewStudents()
        case 3:
            name=input("Enter student name: ").lower()
            SearchStudent(name)
        case 4:
            print("Thanks for using Smart Student Profile System!")
            break
        case _:
            print("Invalid option")