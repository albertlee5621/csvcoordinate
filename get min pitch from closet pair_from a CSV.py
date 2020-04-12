# -*- coding: utf-8 -*-
"""
1. read a CSV file
2. find closest pair
3. print min. pitch and x,y coordinate of these two cirlces
"""

#%%
import tkinter as tk
from tkinter import filedialog

#%%
## use GUI to select file
root = tk.Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
#print (root.filename)
root.withdraw()

#%%
# read a  CSV File
import pandas as pd # 引用套件並縮寫為 pd  
df = pd.read_csv(root.filename)

# dummy array A
import numpy as np
A = np.zeros(shape=(len(df['x']),2))

for i in range(len(df['x'])-1):
    A[i,0]=df['x'][i]
    A[i,1]=df['y'][i]
    
print(A)


#%%
def find_closest_brute_force(array):
    
    result = {}
    result["p1"] = array[0]
    result["p2"] = array[1]
    result["distance"] = np.sqrt((array[0][0]-array[1][0])**2
                                +(array[0][1]-array[1][1])**2)
    
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            distance = np.sqrt((array[i][0]-array[j][0])**2
                              +(array[i][1]-array[j][1])**2)
            if distance < result["distance"]:
                result["p1"] = array[i]
                result["p2"] = array[j]
                result["distance"] = distance
    return result

print(find_closest_brute_force(A))
