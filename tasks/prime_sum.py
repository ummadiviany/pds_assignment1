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
    Output : returns True if num is prime else returns False
    
    Additional Notes: It is not necessary to write a function to find the prime numbers.
                        You can also directly do it in the get_prime_sum function.
    """
    # Write your code here
    
    c = 0
    if num > 0:
        for i in range(1, num + 1):
            if num % i == 0:
                c += 1

        if c == 2:
            return True
        else:
            return False
    
        

def get_prime_sum(n : int) -> int:
    """
    This function returns the sum of all the prime numbers less than n
    Input : n
    Output : Returns the sum of all the prime numbers less than n
    """
    # Write your code here
    
    s = 0
    if n > 1:
        for i in range(1, n + 1):
            if is_prime(i) == True:
                s += i
        return s
    else:
        return print("invalid input")
    
    

        
    
    
    
