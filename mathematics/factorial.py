def factorial(n):
    res=1
    for i in range (1,n+1):
        res*=i
    return res

def main():
    n=int(input("Enter a number: "))
    print("Factorial of", n, "is:", factorial(n))

if __name__=="__main__":
    main()