def find_lcm(a,b):
    res=max(a,b)
    while True:
        if res%a==0 and res%b==0:
            break
        res=res+1
    return res

def main():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("The LCM of",a,"and",b,"is",find_lcm(a,b))

if __name__=="__main__":
    main()