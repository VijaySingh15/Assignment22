def converttooctal(n):
    if n>1:
        converttooctal(n//8)
    print(n % 8,end=" ")

dec=int(input("Enter number :"))
print(converttooctal(dec))