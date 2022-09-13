# pds_assignment1
Solutions for this assignment are provided in **/tasks** directory itself and also pasted in this README.md file.
 - [Task 1 Solution](#task-1-solution) 
 - [Task 2 Solution](#task-2-solution)
 - [Task 3 Solution](#task-3-solution)
 - [Task 4 Solution](#task-4-solution) 


Assignment1 for CS60013 : Programming & Data Structures. Due on **September 10, 2022 at 23:59**. 

---

## Tasks 
This assignment is divided into 4 tasks. All the tasks are detailed below. All the below tasks use concepts discussed in theory and tutorial classes. You are expected to connect the dots to solve these tasks. In some tasks you are learning new concepts. You are expected to learn them and use them to solve the tasks. All the tasks are in the **/tasks** directory.
### Task 1 : Cubeth Root
    1. In this task, you have to complete the function `cube_root` in `cubeth_root.py` file.
    2. Your function should return the cube root of the given number.
    3. Conditions:
       1. Do not use any inbuilt functions like `pow`, `math.pow`, `math.cbrt`, etc.
       2. Only `**` operator is allowed.
    4. Input constraints:
       1. `n` is a positive integer.
       2. `n` is a perfect cube.
    5. Example:
       1. `cube_root(27)` should return `3`.
       2. `cube_root(125)` should return `5`.
       3. `cube_root(729)` should return `9`.

### Task 1 Solution:

```python
def find_cube_root(num : int) -> int:
    """
    This function finds the cube root of a number
    Input : num
    Output : Your function should return the cube root of the given number
    """
    # Write your code here
    
    return int(num ** (1./3))

```
    
### Task 2 : Pattern Printing
    1. Complete the function `print_pattern` in `pattern_printer.py` file. 
    2. Your function should print the pattern as described below. Do not return anything.
    3. Input constraints:
       1. `n` is a positive integer and less than 27.
    4. Examples:
       1. Example 1:
            - Input : n = 3
            - Output :
                ----c----
                --c-b-c--
                c-b-a-b-c
                --c-b-c--
                ----c----
        
        1. Example 2:
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

### Task 2 Solution:
```python
def print_pattern(n : int) -> None:
    """
    This function prints the following pattern
    Input : n
    Output : Your function should print the pattern as described below. 
             Do not return anything.
    """
    # Write your code here
    
    a = n   #Created 'a' variable for my convenience.
    l = []
    for i in range(a):
        d = '-'*(a * 2-(2*(1+i)))+chr(96+a)
        for j in range(i):
            d += '-' + chr(96 + a - j - 1)
        l.append((d+d[-2::-1]))
        
    print('\n'.join(l+l[-2::-1]))
```

### Task 3 - Prime Sum
    1. Complete the functions `get_prime_sum` and `is_prime` in `prime_sum.py` file.
    2. Prime Number : A number is prime if it is divisible by 1 and itself only. These are some examples of prime numbers {2, 3, 5, 7, 9, 11 ...}. All prime numbers are odd except 2.
    3. Function `is_prime` :
       1. This function takes a number `n` as input and returns `True` if `n` is prime and `False` otherwise.
       2. Input constraints:
          1. `n` is a positive integer.
    4. Function `get_prime_sum` :
       1. This function takes a number `n` as input and returns the sum of all prime numbers less than `n`.
       2. Return the sum of all prime numbers less than `n` and do not print anything.
       3. Only `get_prime_sum` function is called in the test code.
       4. If you wish you can scrap the `is_prime` function and implement it in the `get_prime_sum` function itself.
       5. Input constraints:
          1. `n` is a positive integer.
       6. Examples:
          1. `prime_sum(10)` should return `17`.
                - Sum of all prime numbers less than 10 is 2 + 3 + 5 + 7 = 17.
          2. `prime_sum(20)` should return `77`.
                - Sum of all prime numbers less than 20 is 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77.

### Task 3 Solution:
```python
def is_prime(num : int) -> bool:
    """
    This function checks if a number is prime or not
    Input : num
    Output : returns True if num is prime else returns False
    
    Additional Notes: It is not necessary to write a function to find the prime numbers.
                        You can also directly do it in the get_prime_sum function.
    """
    # Write your code here
    
    flag = False
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
    else:
        return False
    # check if flag is True
    if flag:
        return False
    else:
        return True
    
        
def get_prime_sum(n : int) -> int:
    """
    This function returns the sum of all the prime numbers less than n
    Input : n
    Output : Returns the sum of all the prime numbers less than n
    """
    # Write your code here
    sum = 0
    for i in range(n):
        if is_prime(i):
            sum += i
    
    return sum

```

### Task 4 - Student Report Card
    1. In this task, a single line student report is to be generated based on the student marks.
    2. The student report should be generated in the following format:
        * Name : <student_name>
        * Roll Number : <student_roll_number>
        * Status : <student_result_status>
        * GPA : <student_grade_point_average>
    3. You can assume that the student name roll number and status are strings, and the GPA is a floating point number.
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

### Task 4 Solution:
```python
def make_student_report(name : str, roll_no : str, grades : list) -> str:
    
    """
    Input : name, roll_no, grades
    Output : Prints the student report in the following format
                # Student Name: <name>
                # Roll No: <roll_no>
                # Status: <status>
                # GPA: <gpa>
                
    Do not return anything.
    """
    
    # Write your code here
    

    print(f"Student Name: {name}")
    print(f"Roll No: {roll_no}")
    
    status = "Pass" if all([True if g>5 else False for g in grades]) else "Fail"
    gpa = None
    if status == "Pass":
        gpa = sum(grades)/len(grades)
    
    print(f"Status: {status}")
    print(f"GPA: {gpa}")
```

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
4. Once you have completed each task, try to run the test cases. For example if you have completed task 1 **cubeth_root**, run the following command:
    ```bash
    python -m unittest tests/test_cubeth_root.py
    ```
    and similarly for other tasks. Check the **/tests** folder for associated test files.

---
## Submission Instructions
### How to Submit
1. Once you have ran all the test and are satisfied with the results, commit your changes using the following commands in sequence:
    
    To add all the files to the staging area:
    ```bash
    git add .
    ```

    To finalize the commit:
    ```bash
    git commit -m "your_commit_message"
    ```
    To push the changes to your repository:
    ```bash
    git push
    ```
     or use the VS Code GUI to commit your changes and push them to the remote repository.

### Deadline
This assignment is due on **September 1, 2022 at 23:59:59**.

---
## Grading
This assignment is auto-graded. Please make sure that you have completed all the tasks and have passed all the test cases. The final score will be calculated based on the number of test cases passed. 

---
## Resources
1. [Python Documentation](https://docs.python.org/3/)
2. [Unofficial Python Tutorial](https://www.programiz.com/python-programming)


---
Assignment created by [**Vinay**](https://ummadiviany.github.io/) and approved by [**Prof Subhamoy Mandal**](https://sites.google.com/site/smandalbiomed/home).

## All the best!