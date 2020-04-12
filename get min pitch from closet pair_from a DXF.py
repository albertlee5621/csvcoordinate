# -*- coding: utf-8 -*-
"""
1. select a dxf file
2. get x,y coordinate of all circles
3. get the distance between closest pair.
"""
#%%
import ezdxf
import tkinter as tk
from tkinter import filedialog

#%%
## select a file by GUI
root = tk.Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("DXF files","*.DXF"),("all files","*.*")))
#print (root.filename)
root.withdraw()

#%%
# read dxf file by ezdxf
doc = ezdxf.readfile(root.filename)

# save circle's information
def save_circle(e):
    all_circle_info.append([e.dxf.center,e.dxf.radius])
  
# iterate over all entities in modelspace
msp = doc.modelspace()
all_circle_info=[]
for e in msp:
    if e.dxftype() == 'CIRCLE':
        save_circle(e)

#%%
# Get the x, y coordinates of the center of the circle from all_circle_info
import numpy as np

coord_circle = np.zeros(shape=(len(all_circle_info),2))

for n in range(len(all_circle_info)):
    coord_circle[n]= [all_circle_info[n][0][0],all_circle_info[n][0][1]]
    
    
#%%
# find closest pairs by brute_force
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

print(find_closest_brute_force(coord_circle))
