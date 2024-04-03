# This is a python program to calculate the Fibonacci sequence. Create the program to do this.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))
