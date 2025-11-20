import re
from DataFile import Data
from Students import Student
from Subjects import Subject
from copy import deepcopy

class Admin(Student):
    def __init__(self) -> None:
        super().__init__()
        self.std_list = Student().student_list

    def show_students(self):
        if self.std_list:
            for student in self.std_list:
                print(f"\t \033[1;37m {student['Name']}  ::  {student['Student_id']} --> Email: {student['Email']}")
        else:
            print("\t\t \033[1;37m < Nothing to Display >")

    def remove_student(self):
        removed = False
        if self.std_list:
            student_id = input("\t \033[1;37m Remove by ID: ")
            for student in self.std_list:
                if student_id == student["Student_id"]:
                    self.std_list.remove(student)
                    removed = True
                    break
            if removed:
                print(f"\t \033[1;33m Removing Student {student_id} Account")
                Data.write_data(self.std_list)
            else:
                print(f"\t \033[1;31m Student {student_id} does not exist")
        else:
            print("\t\t < No Student Accounts exist >")

    def clear_database(self):
        if self.std_list:
            confirm = input("\t \033[1;31m Are you sure you want to clear the database (Y)ES/(N)O: \033[1;37m").lower()
            while confirm[0] != 'n':
                if confirm == 'y':
                    # Clear the database file
                    Data.clear_file()
                    self.std_list = []
                    print("\t \033[1;33m Students data cleared")
                    break
                else:
                    print("\t  Please enter either - Y for yes or N for no")
                    confirm = input("\t \033[1;31m Are you sure you want to clear the database (Y)ES/(N)O: \033[1;37m").lower()
        else:
            print("\t\t \033[1;37m < No Student Accounts exist in the Database >")

    def group_students(self):
        hd_lst, d_lst, p_lst, c_lst, z_lst, enrol_lst = [], [], [], [], [], []
        stud_list = deepcopy(self.std_list)
        if stud_list:
            for student in stud_list:
                if eval(student["Subjects"]):
                    enrol_lst.append(True)
                    overall_grade = Subject.calculate_grade(self, student["Average_marks"])
                    if overall_grade == 'HD':
                        hd_lst.append(student)
                    elif overall_grade == 'P':
                        p_lst.append(student)
                    elif overall_grade == 'C':
                        c_lst.append(student)
                    elif overall_grade == 'D':  
                        d_lst.append(student)
                    else:
                        z_lst.append(student)
                else:
                    enrol_lst.append(False)
            if any(enrol_lst):
                if hd_lst:
                    print(f"\t \033[1;37m HD --> ["+ ", ".join([f"{stud['Name']}:: {stud['Student_id']} --> GRADE: HD - MARK: {float(stud["Average_marks"]):.2f}" for stud in hd_lst]) + "]")
                if d_lst:
                    print(f"\t \033[1;37m D  --> ["+ ", ".join([f"{stud['Name']}:: {stud['Student_id']} --> GRADE: D  - MARK: {float(stud["Average_marks"]):.2f}" for stud in d_lst]) + "]")
                if c_lst:
                    print(f"\t \033[1;37m C  --> ["+ ", ".join([f"{stud['Name']}:: {stud['Student_id']} --> GRADE: C  - MARK: {float(stud["Average_marks"]):.2f}" for stud in c_lst]) + "]")
                if p_lst:
                    print(f"\t \033[1;37m P  --> ["+ ", ".join([f"{stud['Name']}:: {stud['Student_id']} --> GRADE: P  - MARK: {float(stud["Average_marks"]):.2f}" for stud in p_lst]) + "]")
                if z_lst:
                    print(f"\t \033[1;37m Z  --> ["+ ", ".join([f"{stud['Name']}:: {stud['Student_id']} --> GRADE: Z  - MARK: {float(stud["Average_marks"]):.2f}" for stud in z_lst]) + "]")
            else:
                print("\t\t \033[1;37m < Student(s) has not enrolled in any subjects >")
        else:
            print("\t\t \033[1;37m < Nothing to Display >")
        
    def partition_students(self):
        pass_stud, fail_stud = [], []
        stud_list = deepcopy(self.std_list)
        for student in stud_list:
            enroled_flg = True if eval(student["Subjects"]) else False
            if enroled_flg:
                if float(student["Average_marks"]) >= 50.0:
                    pass_stud.append(student)
                else:
                    fail_stud.append(student)
        print(f"\t \033[1;37m FAIL --> ["+ ", ".join([f"{stud['Name']}:: {stud['Student_id']} --> GRADE: {Subject.calculate_grade(self, stud["Average_marks"])} - MARK: {float(stud["Average_marks"]):.2f}" for stud in fail_stud]) + "]")
        print(f"\t \033[1;37m PASS --> ["+ ", ".join([f"{stud['Name']}:: {stud['Student_id']} --> GRADE: {Subject.calculate_grade(self, stud["Average_marks"])} - MARK: {float(stud["Average_marks"]):.2f}" for stud in pass_stud]) + "]") 

    def admin_helpmenu(self):
        print("\t  Admin Menu Options: \n\t  (c) Clear Student Database \n\t  (g) Group Students \n\t  (p) partition Students \n\t  (r) Remove Student by ID \n\t  (s) Show All Students in the Database \n\t  (x) Back to University Menu")

    def admin_menu(self):
        choice = input("\t \033[1;36m Admin Menu (c/g/p/r/s/x): \033[1;37m")
        while choice != "x":
            match choice:
                case 'c':
                    print("\t \033[1;33m Clearing Student Database")
                    self.clear_database()
                case 'g':
                    print("\t \033[1;33m Grade Grouping")
                    self.group_students()
                case 'p':
                    print("\t \033[1;33m PASS/FAIL Partition")
                    self.partition_students()
                case 'r':
                    self.remove_student()  
                case 's':
                    print("\t \033[1;33m Student List")
                    self.show_students()
                case _:
                    self.admin_helpmenu()
            choice = input("\t \033[1;36m Admin Menu (c/g/p/r/s/x): \033[1;37m")
        print("\t \033[1;37m Back to University Menu")
