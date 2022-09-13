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
    
    a = n   #Created 'a' variable for my convenience.
    l = []
    for i in range(a):
        d = '-'*(a * 2-(2*(1+i)))+chr(96+a)
        for j in range(i):
            d += '-' + chr(96 + a - j - 1)
        l.append((d+d[-2::-1]))
    
    
    print('\n'.join(l+l[-2::-1]))
    
