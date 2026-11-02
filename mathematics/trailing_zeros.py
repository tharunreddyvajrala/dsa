def trailing_zeros(n):
    res=0
    powOf5=5
    while n>=powOf5:
        res+=n//5
        powOf5
        powOf5=powOf5*5
    return res

def main():
    n=int(input("enter the number : "))
    print(trailing_zeros(n))

if __name__ =='__main__':
    main()
