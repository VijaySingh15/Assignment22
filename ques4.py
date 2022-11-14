def sq(n):
    if n==1:
        return 1
    else:
        return n*n + sq(n-1)
    
n=int(input("Enter number :"))
print(sq(n))