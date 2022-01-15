input_number=float(input('Please Enter A Number: '))
x=0
y=1
if  (input_number%1==0 and input_number>0):
    while (input_number//y>0):
        x=x+1
        y=y*10
    print (x)
else: print('The input is not valid')
