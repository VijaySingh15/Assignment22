def odd(n):
    if n==1:
        return 1
    else:
        return n+(n-1)+odd(n-1)

n=int(input("Enter number :"))
print(odd(n))