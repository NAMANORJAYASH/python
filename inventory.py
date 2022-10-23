inventory={"apple":10,"banana":20,"orange":15,"raisin":5,"apricots":8}
x=0
while not x==4:
    if x== 1 :
        for i,j in inventory.items():
            print(i,j)
    if x== 2 :
        name = input("which fruit do you want?: ")
        quantity = int(input("how many do you want ? :"))
        l1=inventory.keys()
        count=0
        for i in l1:
            if name == i:
                if quantity <= inventory[name]:
                   print("your purchase is successful")
                   inventory[name]=  inventory[name] - quantity
                else: print("the demanded value is more than available")
            else: count=count +1
        if count == len(l1):
            print ("please enter valid value")
    if x== 3:
        name = input("which fruit do you want to store?: ")
        quantity = int(input("how many do you want to store ? : ")) 
        l1=inventory.keys()
        count=0
        for i in l1:
            if name == i:
                   print("your purchase is successful")
                   inventory[name]=  inventory[name] + quantity
                   print("your storage was successful")
            else:count=count+1
        if count == len(l1):
            inventory[name] = quantity
            
    if x==4:
        break
        try : x= int(input(""" --------------------------------------------
1. Display Inventory
2. Buy the fruits
3. Stock the fruits
4. Exit
Please enter a choice 1,2,3 or 4 :  """))
        except : print("please enter valid values ")
    x= int(input(""" --------------------------------------------
1. Display Inventory
2. Buy the fruits
3. Stock the fruits
4. Exit
Please enter a choice 1,2,3 or 4 :  """))
