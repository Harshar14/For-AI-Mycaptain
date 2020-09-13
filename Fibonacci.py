def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    # Starting Fibonacci number is 0
    elif n==1:
        return 0
    # The second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Main Program
 
print(Fibonacci(9))
 
#This code is contributed by Harsha R
