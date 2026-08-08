'''
Factorial(2) = 2*1
Factorial(3) = 3*2*1
Factorial(4) = 4*3*2*1
Factorial(5) = 5 *4*3*2*1
Factorial(n) = n * n-1 * ....... * 3 * 2 * 1
Factorial(n) = n * Factorail(n-1)

'''
def factorial(n):
    if(n == 1 or n == 0):
        return 1 
    return n * factorial( n - 1)
n = int(input("Enter a number :"))
print(f"The factorial of this number {factorial(n)}")