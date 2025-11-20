import csv
import os

file_path = "Students.csv"
headers = ["Student_id", "Name", "Email", "Password", "Subjects", "Average_marks"]

class Data:
    @staticmethod
    def check_file():
        """ Checks if the file exists in the given path
            If not, it creates the students database file in csv format with headers"""
        try:
            if not os.path.exists(file_path):
                with open(file_path, mode='w', newline='') as file:
                    writerfile = csv.DictWriter(file, fieldnames=headers)
                    writerfile.writeheader()
            return True
        except FileExistsError:
            print("\033[1;31m Issue in creating student data file")
            return False
    @staticmethod
    def read_data():
        """ It reads the data records from the .csv file as a list of dictionaries
            where each row corresponding to a student record is a dictionary"""
        students_lst = []
        with open(file_path, mode='r') as file:
            student_data = csv.DictReader(file)
            for data in student_data:
                students_lst.append(data)
        return students_lst
    @staticmethod
    def write_data(data):
        """ The data argument passed in written in the .csv file
            The data argument is in the format of list of dictionaries"""
        with open(file_path, mode='w', newline='') as file:
            writerfile = csv.DictWriter(file, fieldnames=headers)
            writerfile.writeheader()
            writerfile.writerows(data)
    @staticmethod
    def clear_file():
        """ It clears all the data records in the csv file except for the headers row"""
        with open(file_path, mode='w+') as file:
            writerfile = csv.DictWriter(file, fieldnames=headers)
            writerfile.writeheader()
            file.truncate()