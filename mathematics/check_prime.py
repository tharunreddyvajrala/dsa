import math

def check_prime(n):
    if(n==1):
        return False
    if(n==2 or n==3):
        return True
    if(n%2==0 or n%3==0):
        return False
    for i in range(5, int(math.sqrt(n))+1, 6):
        if(n%i==0 or n%(i+2)==0):
            return False
    return True

def main():
    n=int(input("Enter a number: "))
    if check_prime(n):
        print(n,"isPrime")
    else:
        print(n,"is Not Prime")
if __name__=="__main__":
    main()
