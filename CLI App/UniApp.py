from DataFile import Data
from Students import Student
from Admins import Admin

class University:
    def university_helpmenu(self):
        print(" University Menu Options: \n (a) Admin System \n (s) Student System  \n (x) Exit")

    def university_menu(self):
        choice = input("\033[1;36m University System (A)dmin, (S)tudents or X: \033[1;37m").lower()
        while choice != "x":
            match choice:
                case 'a':
                    Admin().admin_menu()
                case 's':
                    Student().student_menu()
                case _:
                    self.university_helpmenu()
            choice = input("\033[1;36m University System (A)dmin, (S)tudents or X: \033[1;37m").lower()
        print("\033[1;33m Thank You \033[1;37m")
        exit(0)
if __name__ == "__main__":
    uni = University()
    uni.university_menu()