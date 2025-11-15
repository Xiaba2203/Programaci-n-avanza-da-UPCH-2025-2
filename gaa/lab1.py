def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def f1(n):
    print(n)
    if (n>0):
        f1(n-1)
def f2(n):
    if(n==1):
        return 1
    else:
        return n+f2(n-1)
    
if __name__ == "__main__":
    a=int(input("Enter a number: "))
    print(f"The factorial of {a} is {factorial(a)}")
    print("Printing numbers from n to 0:")
    f1(a)
    print(f2(a))