def find_gcd(a,b):
    if a<b:
        min=a
    else:
        min=b
        for i in range (min,0,-1):
            if a%i==0 and b%i==0:
                return i

def main():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("The GCD of",a,"and",b,"is",find_gcd(a,b))

if __name__=="__main__":
    main()