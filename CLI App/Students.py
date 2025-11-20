import re
from DataFile import Data
from Subjects import Subject
import random

class Student():
    def __init__(self) -> None:
        self.name = ""
        self.email = ""
        self.password = ""
        self.email_regex = r"(^[a-zA-Z]+\.+[a-zA-Z]+@+university+\.+com+$)"
        self.password_regex = r"(^[A-Z]+[a-z]{5,}+[0-9]{3,}+$)"
        self.current_subjects = []
        self.data_initialise()

    def data_initialise(self):
        """Read the dat from the students data file (.csv file) if it exists"""
        file_check = Data.check_file()
        if file_check:
            self.student_list = Data.read_data()

    def verify_credentials(self, email, password):
        """ To check if the entered email and password align with the pattern conditions using regular expressions
            If either email or password does not align with the requirements returns False """
        verify_cred_result = True
        email_match = re.match(self.email_regex, email)
        password_match = re.match(self.password_regex, password)
        if not email_match or not password_match:
            verify_cred_result = False
        return verify_cred_result

    def verify_email(self, email):
        """ To check if the entered email has been already registered/saved in the database records
            If found, returns True and name of the student
            else returns False and empty string value for name """
        stu_found = False
        for student in self.student_list:
            if email.lower() == student["Email"].lower():
                self.name = student["Name"]
                stu_found = True
        return stu_found, self.name

    def generate_stud_id(self):
        """ Upon successful registration, random 6 digits student id is generated
            If it is less than 6-digits, the rest of the digits is filled with zeroes
            It is also ensured that randomly generated id does not exist in current database records
            as student id must be unique for each student"""
        ids = [student["Student_id"] for student in self.student_list]
        stud_id = str(random.randint(1,999999)).zfill(6)
        while stud_id in ids:
            stud_id = str(random.randint(1,999999)).zfill(6)
        return stud_id

    def register(self):
        """
        Student details registration includes the below steps:
        1. Obtaining the user credentials - email and password
        2. Verifying if the credentials match the given pattern requirements
        3. Ask for credentials until the pattern specifications match
        4. Check if the given email has been already registered
        5. Only if the email is not registered, the student id is generated and provided details are stored in student.data file
        6. Student menu is displayed for the user to navigate to other options (l/r/x)
        """
        #Getting the credentials from user as input
        self.email = input("\t \033[1;37m Email: ")
        self.password = input("\t \033[1;37m Password: ")
        #Verify if the credentials satisfy the given pattern conditions
        register_verify = self.verify_credentials(self.email, self.password)
        while not register_verify:
            print("\t \033[1;31m Incorrect email or password format")
            self.email = input("\t \033[1;37m Email: ")
            self.password = input("\t \033[1;37m Password: ")
            register_verify = self.verify_credentials(self.email, self.password)
        print("\t \033[1;33m email and password formats acceptable")
        #Check if student email has already been registered
        email_verify, self.name = self.verify_email(self.email)
        if email_verify:
            print(f"\t \033[1;31m Student {self.name} already exists")
        #If not registered, generate the unique student id and store the student details to the data file
        else:
            self.name = input("\t \033[1;37m Name: ").title()
            self.id = self.generate_stud_id()
            self.new_student = {"Student_id":self.id, "Name": self.name, "Email": self.email, "Password":self.password, "Subjects":str([]), "Average_marks": 0.0}
            self.student_list.append(self.new_student)
            Data.write_data(self.student_list)
            print(f"\t \033[1;33m Enrolling Student {self.name}")

    def login(self):
        """ Successful Login involves below steps:
            1. Enter valid email and password that was already registered
            2. The entered password must match with registered password 
            3. Upon successful login, the student sub-menu gets displayed"""
        self.email = input("\t \033[1;37m Email: ")
        self.password = input("\t \033[1;37m Password: ")
        login_verify = self.verify_credentials(self.email, self.password)
        stored_password = [student["Password"] for student in self.student_list if self.email.lower() == student["Email"].lower()]
        
        while not login_verify:
            print("\t \033[1;31m Incorrect email or password format")
            self.email = input("\t \033[1;37m Email: ")
            self.password = input("\t \033[1;37m Password: ")
            login_verify = self.verify_credentials(self.email, self.password)
        print("\t \033[1;33m email and password formats acceptable")
        email_verify, self.name = self.verify_email(self.email)
        if not email_verify:
            print("\t \033[1;31m Student does not exist")
            pass
        else:
            stored_password = [student["Password"] for student in self.student_list if self.email.lower() == student["Email"].lower()]
            str_password = stored_password[0]
            while str_password != self.password:
                print("\t \033[1;31m Password mismatch. Please enter correct password")
                self.password = input("\t \033[1;37m Password: ")
            #upon successful login the enrolled subjects are read and converted to appropriate type from string
            self.current_subjects = [student["Subjects"] for student in self.student_list if self.email.lower() == student["Email"].lower()]
            if self.current_subjects[0]:
                self.current_subjects = eval(self.current_subjects[0])
            self.student_course_menu()
        
    def change_password(self):
        """ It allows the registered student to change password upon successful login
            It ensures, new password follows the pattern conditions using regular expressions
            Also, the confirm password must match with the valid new password entered before updating the database."""
        self.new_password = input("\t\t \033[1;37m New Password: ")
        password_match = re.match(self.password_regex, self.new_password)
        while not password_match:
            print("\t\t \033[1;31m Incorrect password format.")
            self.new_password = input("\t\t \033[1;37m New Password: ")
            password_match = re.match(self.password_regex, self.new_password)
        self.confirm_password = input("\t\t \033[1;37m Confirm Password: ")
        while self.new_password != self.confirm_password:
            print("\t\t \033[1;31m Password does not match. Try Again!")
            self.confirm_password = input("\t\t \033[1;37m Confirm Password: ")
        for student in self.student_list:
            if self.email.lower() == student["Email"].lower():
                student["Password"] = self.new_password
        Data.write_data(self.student_list)
        
    def remove_subject(self):
        """ It allows registered student to remove a subject by ID upon successful login
            It ensures the student has enroled in at least 1 subject before asking for the ID
            Also, it checks if the entered subject ID is valid otherwise prompts not found in currently enrolled list
            If valid subject id was entered, it is removed from the database records and displays the updated count of enrolled subjects"""
        sub_found = False
        if len(self.current_subjects) >= 1:
            sub_id = input("\t\t  Remove Subject by ID: ")
            for subject in self.current_subjects:
                if sub_id == subject["id"]:
                    sub_found = True
                    idx = self.current_subjects.index(subject)
                    self.current_subjects.pop(idx)
                    for student in self.student_list:
                        if self.email.lower() == student["Email"].lower():
                            student["Subjects"] = str(self.current_subjects)
                    Data.write_data(self.student_list)
                    print(f"\t\t \033[1;33m Dropping Subject-{sub_id}\n\t\t  You are now enrolled in {len(self.current_subjects)} out of 4 subjects")
            if not sub_found:
                print(f"\t\t \033[1;31m Subject-{sub_id} not found in currently enrolled list of subjects")
        else:
            print("\t\t \033[1;31m There are no subjects currently enrolled")

    def enrol_subjects(self):
        if len(self.current_subjects) == 4:
            print("\t\t \033[1;31m Students are allowed to enrol in 4 subjects only.\033[0m")
        else:
            # Add new Subject
            new_subject = Subject(self.current_subjects).assign_sub()
            # Add the subject to the student's enrolled subjects
            self.current_subjects.append(new_subject)
            for student in self.student_list:
                if self.email.lower() == student["Email"].lower():
                    student["Subjects"] = str(self.current_subjects)
                    student["Average_marks"] = Subject(self.current_subjects).calculate_avg_mark()
            # Save the updated student data
            Data.write_data(self.student_list)
            # Print the enrolled subject details
            print(f"\t\t \033[1;33m Enrolling in Subject-{new_subject["id"]}", f"\n\t\t \033[1;33m You are now enrolled in {len(self.current_subjects)} out of 4 subjects")

    def view_enrolment(self):
        if self.current_subjects:
            print(f"\t\t \033[1;33m Showing {len(self.current_subjects)} subjects")
            for subj in self.current_subjects:
                print(f"\t\t \033[1;37m [ Subject:: {subj["id"]} -- mark = {subj["marks"]} -- grade =  {subj["grade"]} ]")
        else:
            print("\t\t \033[1;33m Showing 0 subjects")

    def student_helpmenu(self):
        print("\t \033[1;37m Student Menu Options: \n\t  (l) Login and access the student course menu \n\t  (r) Register for new students to gain system access \n\t  (x) Go back to University Menu")
    
    def student_sub_helpmenu(self):
        print("\t\t \033[1;37m Student Course Menu Options: \n\t\t  (c) Change login password \n\t\t  (e) Enrol in new subjects \n\t\t  (r) Remove a subject \n\t\t  (s) View currently enrolled subjects and respective results \n\t\t  (x) Sign Out and Go back to Student Menu")

    def student_course_menu(self):
        choice = input("\t\t \033[1;36m Student Course Menu (c/e/r/s/x): \033[1;37m").lower()
        while choice != "x":
            match choice:
                case 'c':
                    print("\t\t \033[1;33m Updating Password")
                    self.change_password()
                case 'e':
                    self.enrol_subjects()
                case 'r':
                    self.remove_subject()
                case 's':
                    self.view_enrolment()
                case _:
                    self.student_sub_helpmenu()
            choice = input("\t\t \033[1;36m Student Course Menu (c/e/r/s/x): \033[1;37m").lower()
        print("\t\t \033[1;37m Signed Out!! Back to Student Menu")
    
    def student_menu(self):
        choice = input("\t \033[1;36m Student System (l/r/x): \033[1;37m").lower()
        while choice != "x":
            match choice:
                case 'l':
                    print("\t \033[1;32m Student Sign In")
                    self.login()
                case 'r':
                    print("\t \033[1;32m Student Sign Up")
                    self.register()
                case _:
                    self.student_helpmenu()
            choice = input("\t \033[1;36m Student System (l/r/x): \033[1;37m").lower()
        print("\t \033[1;37m Back to University Menu")