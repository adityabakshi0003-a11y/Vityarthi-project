##Problem Statement
Manually calculating the Semester Grade Point Average (SGPA) and tracking the Cumulative Grade Point Average (CGPA) for university students, especially those using a relative grading system (like the one implied in the code where scores are compared to class average/highest score), is often time-consuming, complex, and prone to human error. Students need a reliable, quick, and easily accessible tool to accurately determine their academic standing based on these specific, custom grading parameters. The existing generic online calculators may not cater to the specific formula or input requirements of this institution, leading to discrepancies.

##Scope of the Project
The scope of this project is limited to developing a command-line interface (CLI) application that correctly implements the custom VIT-like grading logic to calculate the Semester GPA for a single current term. It will handle the input of student details (name, year), subject data (name, score), and comparative class metrics (average and highest score). The application will calculate individual subject grades (S, A, B, C, D, E, F) and then aggregate these to present the final semester GPA. While it accepts a previous CGPA for context, the project does not include database persistence, CGPA aggregation, or a graphical user interface (GUI).

##Target Users
The primary target users are undergraduate students enrolled in institutions that utilize a complex or relative grading system similar to the one implemented in the code (e.g., VIT students). Secondary users include academic counselors or faculty members who might use the tool for quick, on-the-spot academic performance estimations. Users must be comfortable interacting with a command-line environment to input the required data.

##High-Level Features
1.Custom Grading Logic: Implement the unique grading algorithm that determines subject grade points based on a comparison between the student's score, the class average, and the highest score achieved in the class.
2.Semester GPA Calculation: Accurately calculate the current term's GPA by summing the weighted grade points of all subjects.
3.Interactive Input Interface: Guide the user through a series of prompts to collect necessary data, including student name, academic year, number of subjects, and subject-specific scores and class metrics.
4.Performance Summary Output: Display a clear, organized report detailing the names of subjects entered, the individual marks, and the final calculated GPA for the semester.
