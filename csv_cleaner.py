import pandas as pd

data1 = pd.read_csv('files/shopping_csv.csv')
data1.dropna(inplace=True)  
data1.to_csv('clean_csv.csv',index = False) 


        
