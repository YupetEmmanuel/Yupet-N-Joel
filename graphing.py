import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

with open('files/clean_csv.csv','r') as file:
    data = csv.reader(file)
    for row in data:
        di={index:row for index,row in enumerate(data)}
        print(di)
        print(di[0][1])



x = di[0][0], di[1][0] ,di[2][0]
y = di[0][1],di[1][1],di[2][1]


plt.plot(x,y)
plt.xlabel('item selection')
plt.ylabel('price per item')
plt.title('Graph of transaction from the store')
plt.show()
