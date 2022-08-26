from unittest import TestCase
from tasks.student_report import make_student_report
from .get_func_output import return_func_output

class TestStudentReport(TestCase):
    def test_case_1(self):
        self.assertEqual(return_func_output(make_student_report, "Vinay", "1", [10, 10, 10]), "Student Name: Vinay\nRoll No: 1\nStatus: Pass\nGPA: 10.0\n")
        
    def test_case_2(self):
        self.assertEqual(return_func_output(make_student_report, "Pavan", "1", [10, 10, 5]), "Student Name: Pavan\nRoll No: 1\nStatus: Fail\nGPA: None\n")
        
    def test_case_3(self):
        self.assertEqual(return_func_output(make_student_report, "Pooja", "1", [10, 9, 8]), "Student Name: Pooja\nRoll No: 1\nStatus: Pass\nGPA: 9.0\n")
