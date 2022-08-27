# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-08-26 15:27:53
#  * @modify date 2022-08-26 15:27:53
#  * @desc [description]
#  */
# # Actual code starts below this line
# # --------------------------------------------------------------

def is_prime(num : int) -> bool:
    """
    This function checks if a number is prime or not
    Input : num
    Output : True if num is prime else False
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
    Output : sum of all the prime numbers less than n
    """
    # Write your code here

        
    sum = 0
    for i in range(n):
        if is_prime(i):
            sum += i
    
    return sum