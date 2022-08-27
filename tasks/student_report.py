# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-26 14:16:31
#  * @modify date 2022-08-26 14:16:31
#  * @desc [description]
#  */
# Actual code starts below this line
# --------------------------------------------------------------


def make_student_report(name : str, roll_no : str, grades : list) -> str:

    # Print the student report in the following format
        # Student Name: <name>
        # Roll No: <roll_no>
        # Status : <status>
        # GPA: <gpa>
    

    print(f"Student Name: {name}")
    print(f"Roll No: {roll_no}")
    
    status = "Pass" if all([True if g>5 else False for g in grades]) else "Fail"
    gpa = None
    if status == "Pass":
        gpa = sum(grades)/len(grades)
    
    print(f"Status: {status}")
    print(f"GPA: {gpa}")


