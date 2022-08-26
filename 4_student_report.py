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

def make_student_report(name : str, roll_no : str, marks : list) -> str:
    # Task Write code to calculate the average of the marks
    # Return the report as a string
    
    
    return 