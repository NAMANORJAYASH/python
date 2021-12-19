e=-1
o=0
n=1
while n!=0:
    n=int(input("Enter the number: "))
    if n%2==0:
        e=e+1
    else: o=o+1
print("The Even count is: ", e)
print("The Odd count is: ",o)
