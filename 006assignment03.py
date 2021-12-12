h1=int(input("Give me the start time hour:"))
m1=int(input("Give me the start time minute:"))
d=int(input("Give me the duration in minutes:"))
f=h1*60+m1+d
h2=f//60
m2=f-h2*60
print("The finish time is=",h2,":",m2)
