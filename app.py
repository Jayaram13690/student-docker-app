class Student:

    # Constructor
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    # Calculate total marks
    def calculate_total(self):
        return sum(self.marks)

    # Calculate percentage
    def calculate_percentage(self):
        total = self.calculate_total()
        return total / len(self.marks)

    # Determine result
    def get_result(self):
        percentage = self.calculate_percentage()

        if percentage >= 75:
            return "Distinction"
        elif percentage >= 50:
            return "Pass"
        else:
            return "Fail"

    # Display student details
    def display_details(self):
        print("\n----- Student Details -----")
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Marks      : {self.marks}")
        print(f"Total      : {self.calculate_total()}")
        print(f"Percentage : {self.calculate_percentage():.2f}%")
        print(f"Result     : {self.get_result()}")


# Taking input from user
student_id = int(input("Enter Student ID: "))
name = input("Enter Student Name: ")

marks = []
num_subjects = int(input("Enter number of subjects: "))

for i in range(num_subjects):
    mark = int(input(f"Enter marks for Subject {i+1}: "))
    marks.append(mark)

# Creating object
student = Student(student_id, name, marks)

# Displaying details
student.display_details()