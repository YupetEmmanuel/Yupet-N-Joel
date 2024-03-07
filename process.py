
import csv

# class with dictionary of items available and their prices
class Buys:
    dict1={"tomatoes":"price = 1100ugx per piece","onions":"price = 2000ugx per piece ",
           "cabbage":"price = 3000ugx per piece","latice":"latice = 3000ugx per piece","bread":"price = 5000ugx per loaf"}
    
    dict2={"tomatoes":1100 ,"onions":2000 ,
           "cabbage":3000 ,"latice": 3000 ,"bread": 5000 }
  
         
    
 # class implimentation
T = Buys.dict2.get("tomatoes")
O = Buys.dict2.get("onions")
C = Buys.dict2.get("cabbage")
L = Buys.dict2.get("latice")
B = Buys.dict2.get("bread")
def Process():
    Answer_1 = input("Enter your answer :")
    
    if Answer_1 == "1":
        print(Buys.dict1.get("tomatoes"))
        Answer_2 = int(input("How many do you want : "))    
        print("Your total is = ",Answer_2*T, "ugx")
        with open('files/shopping_csv.csv','a+') as file:
            New_data = csv.writer(file,delimiter=' ')
            data = [int(Answer_1),Answer_2]
            New_data.writerow(data)
            

        

    
    elif Answer_1 =="2":
        print(Buys.dict1.get("onions"))
        Answer_2 = int(input("How many do you want : "))
        print("Your total is = ",Answer_2*O, "ugx")
        with open('files/shopping_csv.csv','a+') as file:
            New_data = csv.writer(file,delimiter=' ')
            data = [int(Answer_1),Answer_2]
            New_data.writerow(data)
            
   
    elif Answer_1 =="3":
        print(Buys.dict1.get("cabbage"))
        Answer_2 = int(input("How many do you want : "))
        print("Your total is = ",Answer_2*C, "ugx")
        with open('files/shopping_csv.csv','a+') as file:
            New_data = csv.writer(file,delimiter=' ')
            data = [int(Answer_1),Answer_2]
            New_data.writerow(data)
            


    elif Answer_1 == "4":
        print(Buys.dict1.get("latice"))
        Answer_2 = int(input("How many do you want : ")) 
        print("Your total is = ",Answer_2*L, "ugx")
        with open('files/shopping_csv.csv','a+') as file:
            New_data = csv.writer(file,delimiter=' ')
            data = [int(Answer_1),Answer_2]
            New_data.writerow(data)
            

    elif Answer_1 == "5":
        print(Buys.dict1.get("bread"))
        Answer_2 = int(input("How many do you want : "))
        print("Your total is = ",Answer_2*B, "ugx")
        with open('files/shopping_csv.csv','a+') as file:
            New_data = csv.writer(file,delimiter=' ')
            data = [int(Answer_1),Answer_2]
            New_data.writerow(data)
            

    else:
        print("Sorry we don't have that in stock") 

    

