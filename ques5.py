def cube(n):
    if n==1:
        return 1
    else:
        return n**3 + cube(n-1)
    
n=int(input("Enter number :"))
print(cube(n))