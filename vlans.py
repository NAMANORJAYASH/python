x= int(input("Please enter your first number: "))
y= int(input("Please enter your second number: "))
while x<y:
    print("set vlans v"+str(x)," vlan-id",x)
    x=x+1
while y<=x:
    print("set vlans v"+str(y)," vlan-id",y)
    y=y+1
