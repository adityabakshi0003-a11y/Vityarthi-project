# Project Title
VIT Grade Point Average (GPA) Calculator

# Overview of the Project
This project is a command-line utility designed to help students at VIT (Vellore Institute of Technology) calculate their current semester's Grade Point Average (GPA) based on an internal grading system that appears to factor in the class average and highest score. The application first takes the user's name and academic year, and if applicable, prompts for a previous semester's GPA for context. It then iterates through the user's list of subjects, taking the individual score, class average, and class highest score to determine the specific grade (S, A, B, C, D, E, or F) for each subject and compute the cumulative GPA for the semester.

# Features
The primary features include interactive user input for student details (name, year), subject information (name, score), and class performance metrics (average score, highest score awarded). The application implements a unique, custom grading logic that compares the user's score against the class average and the highest score to assign a letter grade and corresponding grade point. Finally, it calculates the overall Semester GPA and prints a comprehensive performance summary, including a list of subjects, marks, and the final GPA.

# Technologies/Tools Used
This project is implemented entirely in Python. It uses fundamental Python constructs, including basic input/output functions (input(), print()), data structures (lists), control flow statements (if/elif/else, for loop), and basic arithmetic operations for calculation. The utility is designed to run directly from the command-line interface (CLI) using the standard Python interpreter, requiring no external libraries or complex frameworks.

# Steps to Install & Run the Project
To install and run this project, you must have a Python 3 interpreter installed on your operating system (Windows, macOS, or Linux). Save the provided code into a file named gpa_calculator.py. Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the following command: python gpa_calculator.py. The program will then start and interactively prompt you for the necessary input data.

# Instructions for Testing
To test the application, run the script and ensure you provide valid inputs when prompted. Test cases should cover students in Year 1 (no prior CGPA needed) and students in Year 2 or above (which requires entering a previous CGPA). Crucially, test the grading logic by providing scores that fall into each grade category (S, A, B, C, D, E, F) based on the score difference from the class average and the class high score. Verify that the final displayed GPA is the accurate sum of the weighted grade points for all subjects entered in the semester.
