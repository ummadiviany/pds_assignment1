# pds_assignment1
Assignment1 for CS60013 : Programming &amp; Data Structures. Due on **September 1, 2022 at 11:59 PM**

---

## Tasks
This assignment is divided into 4 tasks. All the tasks are detailed below. All the below tasks use concepts discussed in theory and tutorial classes. You are expected to connect the dots to solve these tasks. In some tasks you are r 
### Task 1 : Cubeth Root
    1. In this task, you have to complete the function `cube_root` in `1_cubeth_root.py` file.
    2. Conditions:
       1. Do not use any inbuilt functions like `pow`, `math.pow`, `math.cbrt`, etc.
       2. Only `**` operator is allowed.
    3. Input constraints:
       1. `n` is a positive integer.
       2. `n` is a perfect cube.
    4. Example:
       1. `cube_root(27)` should return `3`.
       2. `cube_root(125)` should return `5`.
       3. `cube_root(729)` should return `9`.



### Task 2 : Pattern Printing
    1. Complete the function `print_pattern` in `2_pattern_printer.py` file. 
    2. Input constraints:
       1. `n` is a positive integer and less than 27.
    3. Examples:
       1. Example 1:
            - Input : n = 3
            - Output :
                ----c----
                --c-b-c--
                c-b-a-b-c
                --c-b-c--
                ----c----
        
        2. Example 2:
           - Input : n = 10
           - Output :
                ------------------j------------------
                ----------------j-i-j----------------
                --------------j-i-h-i-j--------------
                ------------j-i-h-g-h-i-j------------
                ----------j-i-h-g-f-g-h-i-j----------
                --------j-i-h-g-f-e-f-g-h-i-j--------
                ------j-i-h-g-f-e-d-e-f-g-h-i-j------
                ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
                --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
                j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
                --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
                ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
                ------j-i-h-g-f-e-d-e-f-g-h-i-j------
                --------j-i-h-g-f-e-f-g-h-i-j--------
                ----------j-i-h-g-f-g-h-i-j----------
                ------------j-i-h-g-h-i-j------------
                --------------j-i-h-i-j--------------
                ----------------j-i-j----------------
                ------------------j------------------

### Task 3 - Prime Sum
    1. Complete the functions `prime_sum` and `is_prime` in `3_prime_sum.py` file.
    2. Prime Number : A number is prime if it is divisible by 1 and itself only. These are some examples of prime numbers {2, 3, 5, 7, 9, 11 ...}. All prime numbers are odd except 2.
    3. Function `is_prime` :
       1. This function takes a number `n` as input and returns `True` if `n` is prime and `False` otherwise.
       2. Input constraints:
          1. `n` is a positive integer.
    4. Function `prime_sum` :
       1. This function takes a number `n` as input and returns the sum of all prime numbers less than `n`.
       2. Input constraints:
          1. `n` is a positive integer.
       3. Examples:
          1. `prime_sum(10)` should return `17`.
                - Sum of all prime numbers less than 10 is 2 + 3 + 5 + 7 = 17.
          2. `prime_sum(20)` should return `77`.
                - Sum of all prime numbers less than 20 is 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77.

### Task 4 - Student Report Card
    1. In this task, a single line student report is to be generated based on the student marks.
    2. The student report should be generated in the following format:
        * Name : <student_name>
        * Roll Number : <student_roll_number>
        * GPA : <student_grade_point_average>
    3. You can assume that the student name and roll number are strings and the GPA is a floating point number.
    4. GPA is calculated as the sum of the grades divided by the number of subjects.
    5. Conditions:
       1. Passing grade for each subject is  greater than 5.
       2. Student GPA is calculated only if the student has passed in all the subjects.
       3. If the student has failed in any subject, the GPA is not calculated and the student is considered to have failed. In that case, GPA is displayed as `None` and `status` is displayed as `Fail`.
    6. What I have to do:
       1. Complete the function `make_student_report` in `student_report.py` file.
       2. This function will take name, roll number and grades as input and print the student report as mentioned above.

    7. Examples :
        1. Example 1:
            - Input:
                - Name : Vinay
                - Roll Number : 21MM60001
                - Grades : [10, 10, 10, 10, 10]
            - Output:
                - Name: Vinay
                - Roll Number: 21MM60001
                - Status: Pass
                - GPA: 10.00
            - Condition satisfied:
                - All the grades are greater than 5.
                - Student status is Pass.
                - GPA is calculated as the sum of the grades divided by the number of subjects. 
        2. Example 2:
            - Input:
                - Name : Pavan
                - Roll Number : 21MM60002
                - Grades : [10, 9, 10, 8, 5]
            - Output:
                - Name : Pavan
                - Roll Number : 21MM60002
                - Status: Fail
                - GPA: None
            - Reason: The student has failed in the subject with grade 5.
        3. Example 3:
           - Input:
                - Name : Pooja
                - Roll Number : 21MM60003
                - Grades: [10, 9, 9, 8, 6]
            - Output:
                - Name : Pooja
                - Roll Number : 21MM60003
                - Status: Pass
                - GPA : 8.40
            - Condition satisfied:
                - All the grades are greater than 5.
                - Student status is Pass.
                - GPA is calculated as the sum of the grades divided by the number of subjects.


---
## Instructions to work on the assignment

1. Clone this repository to your local machine using the following command:
    ```bash 
    git clone your_repository_url
    ```
2. Change the directory to the cloned repository using the following command:
    ```bash
    cd your_repository_name
    ```
3. Open the cloned repository in VS Code using the following command:
    ```bash
    code .
    ```
4. Once you have completed each task, try to run the test cases using the following command:
    ```bash
    python -m unittest
    ```

---
## Submission
1. 

---
## Grading

---
## Resources



