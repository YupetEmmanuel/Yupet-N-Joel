import json
import time
import os
from process import Process

# super market registor program
  
with open("id.json","r") as file:
    data = json.load(file)

id_Input = input("Enter your user password : ")

if id_Input == data["password"]:
    #count down
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)

    print("......................................................")
    time.sleep(0.5)
    print("             welcome to our store                     ")
    print("......................................................")
    time.sleep(1)



    # program process code
    print("                                   ")
    print("What do you want to buy?")
    print("1. tomatoes \n2. onions \n3. cabbage \n4. latice \n5. bread" )

  
  
    # Game for user


    def Game():
        print("would like to play a game, just for the fun of it?")
        Answer_4 = input("Yes/No \n :").upper()
        if Answer_4 == "YES" :
            print("knock ! Knock!! ")
            Answer_5 = input("Put in your answer \n :").lower()
            print("                    ")
            # create a text file and record the answer from the game
            path = "'Game_records.txt'"
            try:
                if os.path.exists(path):
                    with open('Game_records.txt' , 'a') as newfile:
                        newfile.write(Answer_5)

                else:
                    with open('Game_records.txt' , 'w') as newfile:
                        newfile.write(Answer_5)
                    
            except FileNotFoundError:
                print("file not found")

            if Answer_5 == ("who's there?") or ("who is there?"): 
                print("                       ")
                print("Its the boogey man!!")
                print("\U0001F023 \U0001F023 \U0001F023  \U0001F023 \U0001F023 \U0001F023 \U0001F023 \U0001F023")
                print(".....................................................................................")

            elif Answer_5 != ("who's there?") or  ("who is there?"):
                print("That's not right try again")
            else:
                print("That's not possible") 
        elif Answer_4 == "NO" :
            print("Its always nice to have you at our store")
        else:
            print("its okay")


    with open("id.json","r") as file:
        data = json.load(file)
        
  

        
    # __name__

    if __name__ == "__main__":
        try:
            Process()
            Game()
        except FileNotFoundError:
            print("File not found")

    print("thank you for shopping with us")
    print("                                 ")

elif id_Input != data["password"]:
    print("incorrect password")

else:
    print("Invalid answer")










    
    
    













 




