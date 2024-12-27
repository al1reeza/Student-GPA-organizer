# This will be our course class which will represent a class
class Course:
    # Constructor for our course/class
    def __init__(self, title, semester, year, numCredits, grade):
        self.title = title
        self.semester = semester
        self.year = year
        self.numCredits = numCredits
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
    def __init__(self, first_name, last_name, grad_year, major):
        self.firstName = first_name
        self.lastName = last_name
        self.gradYear = grad_year
        self.major = major
        self.classes = []
        self.gpa = None

    # This method adds a course to the list of classes
    def addCourse(self, course):
        self.classes.append(course)

    # A toString method for student
    def __str__(self):
        return (f"{self.firstName} {self.lastName} earned a GPA of {self.gpa:.2f}"
              f" in {self.classes[0].semester} of {self.classes[0].year}")

# This will be a helper method that takes in as input the title, the semester,
# the year, the grade and the number of credits for the course.
def createCourse():
    title = input("Enter title of the course: ")
    # This while loop makes sure that the semester title is accurate and not just
    # made up
    while True:
        semester = input("Enter the semester: (Fall/Winter/Spring): ")
        if semester == "Fall" or semester == "Winter" or semester == "Spring":
            break
        else:
            print("Wrong semester tite. Please try again and choose one of the "
                  "following: (Fall/Winter/Spring): ")
    year = int(input("Enter the year: "))
    numCredits = int(input("Enter the number of credits for the course: "))
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
    return Course(title, semester, year, numCredits, grade)

# This method will create a student
def createStudent():
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    gradYear = input("Please enter your graduation year: ")
    while not gradYear.isdigit():
        gradYear = input("Wrong format! Please enter your graduation year: ")
    gradYear = int(gradYear)
    major = input("Please enter your major: ")
    return Student(firstName, lastName, gradYear, major)


# This will be a helper function that will calculate the Gpa of a student
def calculateGpa(student):
    totalScore = 0
    totalCredits = 0
    for course in student.classes:
        totalScore += course.gpa * course.numCredits
        totalCredits += course.numCredits
    if totalCredits == 0:
        raise ValueError("Student can not have 0 classes")
    Gpa = totalScore / totalCredits
    return Gpa

# This will be the main app
def main():
    sentinelForStudent = True  # This will be our sentinel for course
    listOfStudnets = []
    while sentinelForStudent:
        student = createStudent()
        sentinelForCourse = True  # This will be our sentinel for course
        while sentinelForCourse:
            course = createCourse()
            student.addCourse(course)
            moveOn1 = input("Are there courses left? (Yes/No): ")
            while moveOn1 != "Yes" and moveOn1 != "No":
                moveOn1 = input("Wrong format please answer either 'Yes' or 'No': ")
            if moveOn1 == "No":
                sentinelForCourse = False
        listOfStudnets.append(student)  # Appends the student to the list of students
        student.gpa = calculateGpa(student) # Calculates the Students GPA
        moveOn2 = input("Are there students left? (Yes/No): ")
        while moveOn2 != "Yes" and moveOn2 != "No":
            moveOn2 = input("Wrong format please answer either 'Yes' or 'No': ")
        if moveOn2 == "No":
            sentinelForStudent = False
    for stdnt in listOfStudnets:
        print(stdnt)

# Runs the main method
if __name__ == "__main__":
    main()