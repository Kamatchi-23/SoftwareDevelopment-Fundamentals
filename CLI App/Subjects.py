import random

class Subject:
    """
    A class to manage subjects, including assigning unique IDs, calculating marks,
    and determining grades.

    Attributes:
        subs (list of dict): A list of dictionaries representing current subjects, 
                             each with keys 'id', 'marks', and 'grade'.
        sub (dict): A dictionary template to store details of a new subject, with keys 'id', 'marks', and 'grade'.

    Methods:
        assign_sub(): Assigns a new subject with a unique ID, random marks, and corresponding grade.
        calculate_avg_mark(): Calculates and returns the average mark of all current subjects.
        calculate_grade(mark): Determines the grade based on the provided mark according to the grading scale.
    """

    # Initializes the Subject class with a list of current subjects.
    def __init__(self, current_sub) -> None: 
        self.subs = current_sub           
        self.sub = dict.fromkeys(["id", "marks", "grade"])

    # Assigns a new subject with a unique ID, random marks, and a corresponding grade.    
    def assign_sub(self):
        ids = [sub["id"] for sub in self.subs if self.subs]
        new_id = str(random.randint(1, 999)).zfill(3)
        while new_id in ids:
            new_id = str(random.randint(1, 999)).zfill(3)
        self.sub["id"] = new_id
        self.sub["marks"] = random.randint(25, 100)
        self.sub["grade"] = self.calculate_grade(self.sub["marks"])
        return self.sub

    # Calculates and returns the average mark of all current subjects.    
    def calculate_avg_mark(self):
        average_mark = 0.0
        if self.subs:
            total_marks = sum([subject['marks'] for subject in self.subs])
            average_mark = total_marks / len(self.subs)
        return average_mark
    
    # Determines the grade based on the provided mark according to the grading scale.
    def calculate_grade(self, mark):
        mark = float(mark)
        if mark < 50:
            return 'Z'
        elif mark < 65:
            return 'P'
        elif mark < 75:
            return 'C'
        elif mark < 85:
            return 'D'
        else:
            return 'HD'
