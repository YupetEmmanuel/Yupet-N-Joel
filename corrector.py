    # This is a program that coreects sentences or questions that were written without the right punctuation
import csv
class corrector:
    def __init__(self):

        self.__sent1="You are free to use this program"

    def entrance_sentence(self):
        print(self.__sent1)
      

    def run_program():
        Input = input("Do have any thing you would like to comment ? \n:")
        Is_True = Input.find("yes")
        Negative_first_index = str(Is_True)

        if Negative_first_index[0] != "-":           
            if Input == 'Yes' or 'yes':
                Input1 = input("Enter your words : ")
                Input2 = input("Is it a question or a sentence ? \n: ").lower()
                with open('files/comments.csv','a+') as file:
                    data_to_record = [Input2,Input1]
                    data = csv.writer(file)
                    data.writerows(data_to_record)

                Is_True = Input2.find("sentence")
                Negative_first_index = str(Is_True)

                if Negative_first_index[0] == "-":
                    string3 = Input1.split(",")

                    if string3[-1] != "?":
                        string3.append("?")
                        result = string3[0],string3[-1]


                elif Negative_first_index[0] != "-":
                    string3 = Input1.split(",")

                    if string3[-1] != " ":
                        string3.append(".")
                        result2 = string3[0],string3[-1]

        elif Negative_first_index == '-':

            print("Thanks for shopping with us") 
            



                






    



