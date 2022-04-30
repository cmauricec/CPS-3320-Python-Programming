# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:23:34 2022

@author: Mauri
"""
import tkinter as tk  
from tkinter import ttk, Toplevel
import csv

#

def calculation():

    
    values2 ={
        'borrow': borw.get(),
        'years': years.get(),
     
        
        }
    
    

    borrow = values2["borrow"]
    

   # print(borrow)
    
    #final calculations
    rate = 6.08 / 100

    interest = (rate / 12) * borrow

   # print(round(interest, 2))
    
    final_values = {
        'SSN': ssn.get(),
        'home_value' : value.get(),
        'mortgage' : mort.get(),
        'borrow': borw.get(),
        'equity': holder['equity'],
        'payment': round(interest, 2),
        'years': years.get()
        }
    #writes values to a csv for storage 
    profile = [final_values["SSN"],final_values["home_value"],final_values["mortgage"],final_values["equity"],final_values["borrow"], final_values["payment"], final_values["years"] ]
    with open('Home_equity2.csv', 'w') as infile:
        writer = csv.writer(infile, lineterminator = '\n')
        writer.writerow(profile)
    


#This function gets the values of the variables inputed from the main window
def insert():
    
    #The values are then stored in dictionary for better management and to be used later 
    global holder
    holder = {}
    values = {
        'SSN': ssn.get(),
        'home_value' : value.get(),
        'mortgage' : mort.get(),
        'income' : incm.get(),
        'expense' : exps.get()
     
    }
    
    
    #Check to see if the applicant makes enougth before moving forward
    checkpoint = incm.get()
    if(checkpoint < 1000):
        #display warning window 
        tk.messagebox.showinfo("Not Approved", "Your income does not meet the requirments")
    
    else:
    
        expensses = values["expense"]
        income = values["income"]
        mortgage = values["mortgage"]
        home_value = values["home_value"]


        #Checks the debt to income ratio of the applicant (dti)
        dti = (int(expensses)/int(income)) * 100
        if(dti < 43):
            #creates a secondary window on top of the existing window to finallize the application 
            branche = Toplevel(root)
            branche.title("Countinue")
            branche.geometry('325x250')
        
            max_borrow = int(home_value) * 0.80
            equity = max_borrow - int(mortgage)

            holder = {
                'equity': equity
           
            }
        
            #borw = tk.StringVar()
            #years = tk.StringVar()
        
            #labels
            side = tk.Label(branche, text="Your Equity is: ")
            side.grid(row = 0, column =0)
            
            #Displays the equity of the applicant to the window
            display = tk.Label(branche, text = equity)
            display.grid(row = 0, column=1)
        
            e = tk.Label(branche ,text = "Borrowing Amount")
            e.grid(row = 1,column = 0)
            g = tk.Label(branche ,text = "Financing Years")
            g.grid(row = 2,column = 0)
            
            #Ebtry boxes
            entry_6 = tk.Entry(branche, textvariable= borw)
            entry_6.grid(row=1, column=1)

            entry_7 = tk.Entry(branche, textvariable= years)
            entry_7.grid(row=2, column=1)
        
        
            btn3 = ttk.Button(branche, text="Submit", command = calculation)
            btn3.grid(row=3,column=0, sticky = "nsew")

            btn4 = ttk.Button(branche ,text="Cancel", command= branche.destroy)
            btn4.grid(row=3,column=1, sticky = "nsew")
        elif(dti >= 43): 
            #displays warning message
            tk.messagebox.showinfo("Not Approved", "Sorry we are unable to approve your application at this time")

        
        
        
        





#the main GUI window
root = tk.Tk()
root.title("Home Equity Form")
root.geometry('325x250')

#Labels to identify entry values 
security = tk.Label(root ,text = "SSN 4-Digits").grid(row = 0,column = 0)
a = tk.Label(root ,text = "Home Value").grid(row = 1,column = 0)
b = tk.Label(root ,text = "Mortgage Balance").grid(row = 2,column = 0)
c = tk.Label(root ,text = "Monthly Income").grid(row = 3,column = 0)
d = tk.Label(root ,text = "Monthly Expenses").grid(row = 4,column = 0)



#Initiallize variables use to get values from entry boxes
ssn = tk.IntVar()
value = tk.IntVar()
mort = tk.IntVar()
incm = tk.IntVar()
exps = tk.IntVar()
borw = tk.IntVar()
years = tk.IntVar()



#Entry boxes for all required values 
entry_1 = tk.Entry(root, textvariable= ssn)
entry_1.grid(row = 0,column = 1)

entry_2 = tk.Entry(root, textvariable= value)
entry_2.grid(row = 1,column = 1)

entry_3 = tk.Entry(root, textvariable= mort)
entry_3.grid(row = 2,column = 1)

entry_4 = tk.Entry(root, textvariable= incm)
entry_4.grid(row = 3,column = 1)

entry_5 = tk.Entry(root, textvariable= exps)
entry_5.grid(row = 4,column = 1)






#When giving a command to a button, don't use (). 
#   i.e. command = insert
#   if the function needs paramaters, call it in a lambda
#       i.e. command = lambda: insert(x,y,z)

#Submit buttons which creates a new window onclick 

btn = ttk.Button(root, text="Submit", command = insert)
btn.grid(row=5,column=0, sticky = "nsew")
#Cancel button that destroy/close the window
btn2 = ttk.Button(root ,text="Cancel", command=root.destroy)
btn2.grid(row=5,column=1, sticky = "nsew")

#prnt = ttk.Button(root, text="Print to Console", )
#prnt.grid(row=5,column=2, sticky = "nsew")




root.mainloop()