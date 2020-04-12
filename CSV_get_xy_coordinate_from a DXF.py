# -*- coding: utf-8 -*-
"""
1.get x,y coord. of all the center of circles from a dxf file 
2.Record all coordinate data in csv file

"""
#%%
import ezdxf
import tkinter as tk
from tkinter import filedialog

#%%
## Use GUI to select files
root = tk.Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("DXF files","*.DXF"),("all files","*.*")))
#print (root.filename)
root.withdraw()

#%%
# Read files with ezdxf
doc = ezdxf.readfile(root.filename)

#%%
def save_circle(e):
    data1.append([e.dxf.center,e.dxf.radius])
 
#%%    
# iterate over all entities in modelspace
msp = doc.modelspace()
data1=[]
for e in msp:
    if e.dxftype() == 'CIRCLE':
        save_circle(e)

        
#%%
# Automatic file naming
# Set the string "_coord." as a suffix
newname=root.filename.split('/')  
newname = newname[-1].split('.')[0]+'_coord.'


#%%
# Write data to csv file
import csv
with open(newname+'.csv', 'w', newline='') as csvfile:
# 以,分隔欄位，建立 CSV 檔寫入器
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['x','y'])
    for n in range(len(data1)):
        writer.writerow([data1[n][0][0],data1[n][0][1]])