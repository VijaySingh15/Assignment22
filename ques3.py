def even(n):
    if n==1:
        return 2
    else:
        return 2*n + even(n-1)
    
n=int(input("Enter nummber :"))
print(even(n))