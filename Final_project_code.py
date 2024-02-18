# super market registor program

  # class with dictionary of items available and their prices
class Buys:
    dict1={"tomatoes":"price = 1100ugx per piece","onions":"price = 2000ugx per piece ",
           "cabbage":"price = 3000ugx per piece","latice":"latice = 3000ugx per piece","bread":"price = 5000ugx per loaf"}
    
    dict2={"tomatoes":1100 ,"onions":2000 ,
           "cabbage":3000 ,"latice": 3000 ,"bread": 5000 }
    def __init__(self):
        pass
    

  # class implimentation
T = Buys.dict2.get("tomatoes")
O = Buys.dict2.get("onions")
C = Buys.dict2.get("cabbage")
L = Buys.dict2.get("latice")
B = Buys.dict2.get("bread")
    
    
    
    
  # program code
print("What do you want to buy?")
print("1. tomatoes \n2. onions \n3. cabbage \n4. latice \n5. bread" )

Answer_1 = input("Enter your answer :")

def pre():
    if Answer_1 == "1":
        print(Buys.dict1.get("tomatoes"))
        Answer_2 = int(input("How many do you want : "))
    
        print("Your total is = ",Answer_2*T, "ugx")
        

    
    elif Answer_1 =="2":
        print(Buys.dict1.get("onions"))
        Answer_2 = int(input("How many do you want : "))
        print("Your total is = ",Answer_2*O, "ugx")
   
    elif Answer_1 =="3":
        print(Buys.dict1.get("cabbage"))
        Answer_2 = int(input("How many do you want : "))
        print("Your total is = ",Answer_2*C, "ugx")


    elif Answer_1 == "4":
        print(Buys.dict1.get("latice"))
        Answer_2 = int(input("How many do you want : ")) 
        print("Your total is = ",Answer_2*L, "ugx")

    elif Answer_1 == "5":
        print(Buys.dict1.get("bread"))
        Answer_2 = int(input("How many do you want : "))
        print("Your total is = ",Answer_2*B, "ugx")

    else:
        print("Sorry we don't have that in stock")    
    return;


pre()








    
    
    













 




