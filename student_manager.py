import json 
import os
File_Name = "students.json"
# load data from file
def Load_Data():
    if  not os.path.exists(File_Name):
        return []
        with open(File_Name,"r") as file:
            data= json.load(file)
    with open(File_Name,"r") as file:
        data=json.load(file)
    if isinstance(data,list):
        return data
    else:
        return []
# save data to file
def save_data(data):
    with open(File_Name,"w") as file:
        json.dump(data,file,indent=4)
# add student
def add_student():
    students=Load_Data()
    name=input("enter student name:")
    age=int(input("enter student age:"))
    roll=input("enter student roll number:")
    student={ "name":name ,"age":age,"roll":roll }
    students.append(student)
    save_data(students)
    print("student added successfully!")
# view students
def view_student():
    students= Load_Data()
    if students:
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Roll: {student['roll']}")
        else:
            print ("no students found!")
# search student
def search_student():
    students=Load_Data()
    roll=input("enter student roll number to  search:")
    for student in students:
        if student["roll"]==roll:
            print(f"Name: {student['name']}, Age: {student['age']}, Roll: {student['roll']}")
            break
        else:
            print("student not found!")
# update student
def update_student():
    roll=input("enter student roll number to update:")
    students=Load_Data()
    for student in students:
        if student["roll"]==roll:
            name=input("enter new student name:")
            age=int(input("enter new student age:"))
            student["name"]=name
            student["age"]=age
            save_data(students)
            print("student updated successfully!")
            break
        else: 
            print("student not found!")
#delete student
def delete_student():
    roll=input("enter student roll number to delete:")
    students=Load_Data()
    for student in students:
        if student["roll"]==roll:
            students.remove(student)
            save_data(students)
            print("student deleted successfully!")
            break
        else:
            print("student not found")
# main menu
def main_menu():
    while True:
        print("\nstudent manager")
        print("1. add student")
        print("2. view students")
        print("3. search student")
        print("4. update student")
        print("5. delete student")
        print("6.exit")
        choice=input("enter your choice:")
        if choice=="1":
            add_student()
        elif choice=="2":
            view_student()
        elif choice=="3":
            search_student()
        elif choice=="4":
            update_student()
        elif choice=="5":
            delete_student()
        elif choice=="6":
            print("exiting student manager. goodbye!")
            break
        else:
            print("invalid choice. please try again.")
# run the main menu
main_menu()
def search_student():
    students=Load_Data()
    roll=input("enter student roll number to search:")
    for student in students:
        if student["roll"]==roll:
            print(f"Name: {student['name']}, Age: {student['age']}, Roll: {student['roll']}")
            break
        else:
            print("student not found!")
    