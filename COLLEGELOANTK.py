#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:44:06 2022

@author: kaitlinc
"""

from tkinter import *

from turtle import color



root = Tk()
root.title("College Loan Application")
root.geometry('800x500')

lbl = Label(root, text = "Enter Name: ")
lbl.grid()
name = Entry(root, width=40)
name.grid(column =1, row =0)

lbl = Label(root, text = "How many years have you had credit: ")
lbl.grid()
history = Entry(root, width=40)
history.grid(column =1, row =1)

lbl = Label(root, text = "Enter your credit score: ")
lbl.grid()
credit = Entry(root, width=40)
credit.grid(column =1, row =2)

lbl = Label(root, text = "Enter your request amount: ")
lbl.grid()
amount = Entry(root, width=40)
amount.grid(column =1, row =3)

lbl = Label(root, text = "Enter University name: ")
lbl.grid()
schoot = Entry(root, width=40)
schoot.grid(column =1, row =4)

lbl = Label(root, text = "Enter Attending Student Name")
lbl.grid()
STUname=Entry(root, width =40)
STUname.grid(column =1, row =5)


def clicked():
    try:

      myname=name.get()

      myhistory=int(history.get())

      mycredit=int(credit.get())

      myamount=int(amount.get())

      myschool=schoot.get()

      mySTUname=STUname.get()

      if myhistory>=1:
          lbl = Label(root, text = "you will declined for the loan amount of "+ str(myamount) +". Need to have more than 12 months of credit History")
          lbl.config(font=('Helvetica bold',20), fg= "red")
          lbl.grid()

      elif mycredit<699 and myamount >=1500:
          lbl = Label(root, text = "you will not be accepted for the loan amount of "+ str(myamount) +".Your credit isnt high enough")
          lbl.config(font=('Helvetica bold',20), fg= "red")
          lbl.grid()

      elif mycredit>=700 and myamount <=12000:
          lbl = Label(root, text = "you will be accepted for the loan amount of "+ str(myamount) +".Your interest rate is 11%")
          lbl.config(font=('Helvetica bold',20), fg= "red")
          lbl.grid()

      elif mycredit<=720 and myamount==20000:
          lbl = Label(root, text = "you will not be accepted for the loan amount of "+ str(myamount) +". Your credit isnt high enough")
          lbl.config(font=('Helvetica bold',20), fg= "red")
          lbl.grid()

      elif mycredit<760 and myamount<= 20000:
          lbl = Label(root, text = "you will accepted for the loan amount of "+ str(myamount) +". Your interest rate is 7%")
          lbl.config(font=('Helvetica bold',20), fg= "red")
          lbl.grid()

      else:
          lbl = Label(root, text = "invalid input")
          lbl.config(font=('Helvetica bold',40), fg= "red")
          lbl.grid()

    except:
          lbl = Label(root, text = "invalid input")
          lbl.config(font=('Helvetica bold',40), fg= "red")
          lbl.grid()



btn = Button(root, text = "Submit" ,
fg = "black", command=clicked)
btn.grid(column=2, row=0)

root.mainloop()