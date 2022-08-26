# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-26 14:16:31
#  * @modify date 2022-08-26 14:16:31
#  * @desc [description]
#  */
# Actual code starts below this line
# --------------------------------------------------------------

def get_student_info():
    
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter the marks: ").split()))
    
    return name, marks

def make_student_report(name : str, roll_no : str, grades : list) -> str:

    # Print the student report in the following format
        # 1. Student Name: <name>
        # 2. Roll No: <roll_no>
        # 3. GPA : <gpa>
    
    
    return 