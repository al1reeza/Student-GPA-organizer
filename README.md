# Student-GPA-organizer
This project is a Python-based application designed to calculate the GPA of students based on their course grades and credits. It allows users to create students, add courses, and compute their GPA dynamically. The program is built using object-oriented programming principles, making it modular, scalable, and easy to understand.

Features: 
  1- Student Creation: Users can create a student profile by entering their first name, last name, graduation year, and major.
  2- Course Creation: Users can add courses to a student's profile by providing details such as the course title, semester, year, number of credits, and grade.
  3- GPA Calculation: The program calculates the GPA for each student based on the grades and credits of their courses.
  4- Grade Conversion: Converts percentage grades into letter grades (e.g., A+, A, B+, etc.) and assigns corresponding GPA values.
  5- User-Friendly Interface: The program uses a command-line interface to interact with users, ensuring ease of use.
  6- Error Handling: Includes input validation to ensure data integrity (e.g., valid semester names, numeric grades, etc.).
  
Classes:
  1- Course: 
      - Represents a course with attributes like title, semester, year, numCredits, and grade.
      - Includes a method setGPA() to convert letter grades into GPA values.
  2- Student Class:
      - Represents a student with attributes like firstName, lastName, gradYear, major, and a list of classes.
      - Includes methods to add courses and calculate the student's GPA.
      
Helper Functions:
  1- createCourse():
        - Prompts the user to input course details and returns a Course object.
        - Validates inputs such as semester and grade.
  2- createStudent():
        - Prompts the user to input student details and returns a Student object.
        - Validates inputs such as graduation year.
  3- calculateGpa():
        - Calculates the GPA for a student based on their courses' grades and credits.

Thank you for your time! Feel free to take a look at the code under STUDENT_MANAGER.py!
