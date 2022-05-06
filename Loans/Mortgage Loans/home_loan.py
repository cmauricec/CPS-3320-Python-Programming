# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:38:03 2022

@author: Mauri
"""

def footer(rate, loan_amount, year, down_payment):
    nan = (rate / 100)/12
    nan1 = nan + 1
    number_payment = year *12
    neg = number_payment * -1
    nan2 = nan1**neg
    nan3 = 1-nan2
    nan4 = nan / nan3
    monthly_payment = loan_amount * nan4
 
    print("Loan Amount ", +loan_amount)
    print("Interest Rate ", rate)
    print("Down Payment ", down_payment)
    print('Monthly Payment', format(monthly_payment,'.2f'))
    
    
    



def body(value, down_payment, year):
    loan_amount = value - down_payment
    credit=float(input("Credit Score: "))
    rate = 0
    if(credit >= 760):
        rate = 3.02
    elif(credit >= 700 and credit <=759):
        rate = 3.3
    elif(credit >= 680 and credit <=699):
        rate = 4.0
    elif(credit >= 660 and credit <=679):
        rate = 4.2
    elif(credit >= 640 and credit <=659):
        rate = 4.6
    else:
        rate = 3.8
    footer(rate, loan_amount, year, down_payment)

    
    
    



def check(value, down_payment, year):
    holder = value * 0.20
    if (down_payment >= holder):
        body(value, down_payment, year)
    else:
        print("Error the Down paymnet is not 20% of the loan")
        value = float(input("What is the value of the home: "))
        down_payment = float(input("Down payment: "))
        year = float(input("Financing year: "))
        check(value, down_payment, year)
        
        

    
    

def main():
    income = float(input("What is your Monthly income(Befor Taxes): "))
    expensses = float(input("Mnthly Expenses: "))
    dti = expensses/income
    if(dti < 0.43 ):
            value = float(input("What is the value of the home: "))
            down_payment = float(input("Down payment: "))
            year = float(input("Financing year: "))
            check(value, down_payment, year)
    else: 
        print("Error ")
            
main()
            