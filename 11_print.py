I=float(input("Please Enter the Income: "))
if I<85528:
    tax=round(0.18*I - 556.02)
    if tax <0:
        tax=0
else:
    tax=round(14839.02+ (I-85528)*0.32)
print(float(tax))
