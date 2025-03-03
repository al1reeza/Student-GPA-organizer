# This will be our course class which will represent a class
class Course:
    # Constructor for our course/class
    def __init__(self, title, num_credits, grade):
        self.title = title
        self.num_credits = num_credits
        self.grade = grade
        Course.setGPA(self)

    # A method that sets the Gpa for a course
    def setGPA(self):
        if self.grade == "A+":
            self.gpa = 4.0
        elif self.grade == "A":
            self.gpa = 4.0
        elif self.grade == "A-":
            self.gpa = 3.7
        elif self.grade == "B+":
            self.gpa = 3.3
        elif self.grade == "B":
            self.gpa = 3.0
        elif self.grade == "B-":
            self.gpa = 2.7
        elif self.grade == "C+":
            self.gpa =2.3
        elif self.grade == "C":
            self.gpa = 2.0
        elif self.grade == "C-":
            self.gpa = 1.7
        elif self.grade == "D+":
            self.gpa = 1.3
        elif self.grade == "D":
            self.gpa = 1.0
        elif self.grade == "D-":
            self.gpa = 0.7
        elif self.grade == "F":
            self.gpa = 0.0

# This Class will represent a student
class Student:
    # This will be our custom Constructor
    def __init__(self, first_name, last_name, id, semester, year, major):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.semester = semester
        self.year = year
        self.major = major
        self.classes = []
        self.gpa = None

    # This method adds a course to the list of classes
    def addCourse(self, course):
        self.classes.append(course)

    # A toString method for student
    def __str__(self):
         return f"{self.first_name} {self.last_name} earned a GPA of {self.gpa:.2f}"

# This will be a helper method that takes in as input the title, theali semester,
# the year, the grade and the number of credits for the course.
def createCourse():
    title = input("Enter title of the course: ")
    num_credits = input("Enter the number of credits for the course: ")
    while not num_credits.isdigit():
        num_credits = input("Wrong format! Please enter your number of credits: ")
    num_credits = int(num_credits)
    grade = input("Enter the grade as a percentage without the '%': ")
    # Check for percentage symbol before converting to int
    while not grade.isdigit():
        print("Grade has to be a number. Check to make sure you do not have the"
            " '%' character")
        grade = input("Please re-enter grade with the correct format: ")
    grade = int(grade)
    if grade <= 100 and grade >= 97:
        grade = "A+"
    elif grade < 97 and grade >= 93:
        grade = "A"
    elif grade < 93 and grade >= 90:
        grade = "A-"
    elif grade < 90 and grade >= 87:
        grade = "B+"
    elif grade < 87 and grade >= 83:
        grade = "B"
    elif grade < 83 and grade >= 80:
        grade = "B-"
    elif grade < 80 and grade >= 77:
        grade = "C-"
    elif grade < 77 and grade >= 73:
        grade = "C"
    elif grade < 73 and grade >= 70:
        grade = "C-"
    elif grade < 70 and grade >= 67:
        grade = "D+"
    elif grade < 67 and grade >= 63:
        grade = "D"
    elif grade < 63 and grade >= 60:
        grade = "D-"
    elif grade < 60:
        grade = "F"
    return Course(title, num_credits, grade)

# This method will create a student
def createStudent():
    first_name = input("Please enter the first name: ")
    last_name = input("Please enter the last name: ")
    id = input("Please enter the student ID: ")
    while not id.isdigit():
        id = input("Wrong format! Please enter the student ID: ")
    id = int(id)
    # This while loop makes sure that the semester title is accurate and not just
    # made up
    while True:
        semester = input("Enter the semester: (Fall/Winter/Spring): ")
        # List of acceptable semesters that will be used in the if statement
        valid_semesters =["fall", "winter", "spring"]
        # Makes sure code is case-insensetive
        if semester.lower().strip() in valid_semesters:
            break
        else:
            print("Wrong semester tite. Please try again and choose one of the "
                  "following: (Fall/Winter/Spring): ")
    year = input("Enter the year: ")
    while not year.isdigit():
        year = input("Wrong format! Please enter the year: ")
    year = int(year)
    major = input("Please enter the major: ")
    return Student(first_name, last_name, id, semester, year, major)


# This will be a helper function that will calculate the Gpa of a student
def calculateGpa(student):
    total_score = 0
    total_credits = 0
    for course in student.classes:
        total_score += course.gpa * course.num_credits
        total_credits += course.num_credits
    if total_credits == 0:
        raise ValueError("Student can not have 0 classes")
    gpa = total_score / total_credits
    return gpa

# This will be the main app
def main():
    print("Hello!\nThis Program will help you organize your stduents.\nPlease " +
          "input the required information and I will do the rest!")
    sentinel_for_student = True  # This will be our sentinel for course
    list_of_students = []
    while sentinel_for_student:
        student = createStudent()
        sentinel_for_course = True  # This will be our sentinel for course
        while sentinel_for_course:
            course = createCourse()
            student.addCourse(course)
            move_on_1 = input("Are there any courses left? (Yes/No): ").strip().lower()
            while move_on_1.lower() != "yes" and move_on_1.lower() != "no": # Makes sure this is case-insensetive
                move_on_1 = input("Wrong format please answer either 'Yes' or 'No': ").strip().lower()
            if move_on_1.lower().strip() == "no":
                sentinel_for_course = False
        list_of_students.append(student)  # Appends the student to the list of students
        student.gpa = calculateGpa(student) # Calculates the Students GPA
        move_on_2 = input("Are there students left? (Yes/No): ").strip().lower()
        while move_on_2 != "yes" and move_on_2 != "no":
            move_on_2 = input("Wrong format please answer either 'Yes' or 'No': ").strip().lower()
        if move_on_2.lower() == "no":
            sentinel_for_student = False
    print("Thank you for using our interface! Here are your results:")
    for stdnt in list_of_students:
        print(stdnt)

# Runs the main method
if __name__ == "__main__":
    main()
