Y= int(input("Please Enter the Year"))
if Y>1582:
    if Y%4>0:
        print("common year")
    elif Y%100>0:
        print("leap year")
    elif Y%400>0:
        print("common year")
    else: print("leap year")
else: print("not within the georgian calender")
