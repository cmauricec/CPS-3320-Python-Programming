# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:52:19 2022

@author: Mauri
"""

import tkinter as tk  
from tkinter import ttk
import csv


def calculate():
    
    try:
        int(years.get())
        int(rev_v.get())
        int(option.get())
        int(down_p.get())
        int(value.get())
        int(score.get())
    except ValueError:
        tk.messagebox.showinfo("Wrong Values", "Please check your number inputs")
 

    
    values = {
        'company_name': company.get(),
        'operational_years': years.get(),
        'revenue': rev_v.get(),
        'borrowing': value.get(),
        'equipment_type': equipment.get(),
        'financing_years': option.get(),
        'down_payment': down_p.get(),
        'credit_score': score.get() 
        }
   
  
   
   
  
       
    var = values['operational_years']
    var2 = values['revenue']
    var3 = values['financing_years']
    var4 = values['down_payment']

    var6 = values['company_name']
    var7 = values['borrowing']
    var8 = values['equipment_type']
   

        

      
       
   
   
   
   
   

    if( int(var) <5 or int(var2) < 50000):
        tk.messagebox.showinfo("Not Approved", "You can not apply at this time")
        
    else:        
        rate = 9/100
        numberOfPayments = int(var3)*12
        
        borrow = int(var7)-int(var4)
        
        monthlyPayment = borrow * rate * (1+ rate) * numberOfPayments \
            / ((1 + rate) * numberOfPayments -1) 
            
        
            
        #print(format(monthlyPayment, '.2f'))
        #company name, equipment, equipment price, down payment, Financing Years, Monthly Payments
        
        #header = ['Compnay Nmae', 'Equipment', 'Equipment price', 'Down payment', 'Financing Years', 'Monthly Payments']
        tab = [ str(var6), str(var8), str(var7), str(var4), str(var3), round(monthlyPayment)]
        line = []
        #CSV files has headers and shoudl write to the next line 
        #It follows the format bellow 
        #header = ['Compnay Nmae', 'Equipment', 'Equipment price', 'Down payment', 'Financing Years', 'Monthly Payments']
        with open('testwe.csv', 'a', newline = '\n') as infile:
            writer = csv.writer(infile)
            writer.writerow(line)
            writer.writerow(tab)
            infile.close()
   
 

   
    
            

root = tk.Tk()
root.title("Equipment Loan form")
root.geometry('325x250')





#Labels to identify entry values 
company_name = ttk.Label(root ,text = "Company Name")
company_name.grid(row = 0,column = 0)
op_years = ttk.Label(root, text = "Operational Years")
op_years.grid(row=1, column=0)
rev = ttk.Label(root, text ="Revenue")
rev.grid(row=2, column=0)
a = ttk.Label(root ,text = "Borrowing Amount")
a.grid(row = 3,column = 0)
b = ttk.Label(root ,text = "Equipment Type")
b.grid(row = 4,column = 0)
d = ttk.Label(root ,text = "Financing Years")
d.grid(row = 5,column = 0)
e = ttk.Label(root ,text = "Down Payment")
e.grid(row = 6,column = 0)
credit = ttk.Label(root, text = "Credit Score")
credit.grid(row =7, column=0)


company = tk.StringVar()
years = tk.IntVar()
value = tk.IntVar()
rev_v = tk.IntVar()
equipment = tk.StringVar()
price = tk.IntVar()
option = tk.IntVar()
down_p = tk.IntVar()
score = tk.IntVar()



#Entry boxes, inputs, slider and dropdown 
name = tk.Entry(root, textvariable = company)
name.grid(row = 0, column = 1)

operational_years = tk.Entry(root, textvariable = years)
operational_years.grid(row = 1, column = 1)

revenue = tk.Entry(root, textvariable=rev_v)
revenue.grid(row=2, column=1)

borrowing = tk.Scale(root, from_=0, to=1000000, variable = value, orient = 'horizontal')
borrowing.grid(row = 3, column=1)

typ = tk.Entry(root, textvariable = equipment)
typ.grid(row = 4, column = 1)



years = tk.Entry(root, textvariable=option)
years.grid(row = 5,column = 1)

down_payment = tk.Entry(root, textvariable=down_p)
down_payment.grid(row = 6,column = 1)

credit_sc = tk.Entry(root, textvariable= score)
credit_sc.grid(row=7, column=1)



#Submit button
btn = ttk.Button(root, text="Submit", command = calculate)
btn.grid(row=8,column=0, sticky = "nsew")

#Cancel button that destroy/close the window
btn2 = ttk.Button(root ,text="Cancel", command=root.destroy)
btn2.grid(row=8,column=1, sticky = "nsew")





root.mainloop()