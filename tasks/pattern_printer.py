# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-26 15:12:40
#  * @modify date 2022-08-26 15:12:40
#  * @desc [description]
#  */
# Actual code starts below this line
# --------------------------------------------------------------


def print_pattern(n : int) -> None:
    """
    This function prints the following pattern
    Input : n
    Output : Your function should print the pattern as described below. 
             Do not return anything.
    """
    # Write your code here
    n = int(input("Enter the value of n\n"))
    for i in range(n+1, 1, -1):

        for k in range(1, i - 1):
            print("-", end="-")
        for k in range(65 + n - 1, 65 + i - 3, -1):
            print(chr(k), end="-")
        for k in range(65 + i - 1, 65 + n):
            if k == 65 + n - 1:
                print(chr(k), end="")
            else:
                print(chr(k), end="-")
        for k in range(i, 2, -1):
            if k == n+1:
                print("-", end="")
            else:
                print("-", end="-")
        print("")

    for i in range(1, n):

        for j in range(i):
            print("-", end="-")

        for k in range(65 + (n-1), 65 + (i - 1), -1):
            print(chr(k), end="-")

        for j in range(65 + i + 1, 65 + (n-1) + 1):
            print(chr(j), end="-")

        for k in range(i):
            if k == 0:
                print("-", end="")
            else:
                print("-", end="-")
        print("")
    return 0
    
