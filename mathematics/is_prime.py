def is_prime(n):
    for i in range (2,(n//2)+1):
        if n%i==0:
            return "Not Prime"
    return "Prime"

def main():
    n=int(input("Enter a number: "))
    print(n,"is",is_prime(n))

if __name__=="__main__":
    main()