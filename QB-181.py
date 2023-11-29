"""Gross Pay, Annual Income and Income Tax Calculator"""

grossPay = 0    
professionalTax = 200  # constant for each grade lvl, each month
classCity = hra = basicPay = 0
grade = 0
oAllowance = 0

# Inputs : City, Grade

grade = input("Please Enter A Grade Level (A,B,C,D,E,F) : ")
classCity = int(input("Enter The City Class (1,2,3): "))

# , Other allowances are given in table which varies 
# according to different grade levels, Provident Fund= 0.11 times of Basic Pay for each grade levels,

if(grade == 'A'):
    basicPay = 60000
    oAllowance = 8000
elif(grade == 'B'):
    basicPay = 50000
    oAllowance = 7000
elif(grade == 'C'):
    basicPay = 40000
    oAllowance = 6000
elif(grade == 'D'):
    basicPay = 30000
    oAllowance = 5000
elif(grade == 'E'):
    basicPay = 20000
    oAllowance = 4000
elif(grade == 'F'):
    basicPay = 10000
    oAllowance = 3000

providentFund = basicPay * 11/100
transport = 900


# House Rent Allowance (hra) varies as per the city- 
# For Class 1 Cities it is 0.3 times of Basic Pay of each grade levels, 
# for Class 2 Cities it is 0.2 times of Basic Pay of each grade levels,
# for Class 3 Cities it is 0.1 times of Basic Pay of each grade levels

if(classCity == 1):
    hra = basicPay * 30/100
elif(classCity == 2):
    hra = basicPay * 20/100
elif(classCity == 3):
    hra = basicPay * 10/100
else:
    print("Please Enter A Valid class City") 

# Dearness Allowance (dra)= 0.5 times of Basic Pay of each grade levels

dAllowance = basicPay * 50/100


# Gross Pay= Basic Pay+ House Rent Allowance (hra) + Dearness Allowance (dra) +other allowances 
# +Transport Allowance (TA)– Professional tax –Employees’ Provident fund (EPF)

grossPay = basicPay + hra + dAllowance + oAllowance + transport - professionalTax - providentFund
AnnualIncome = grossPay * 12
incomeTax = 0

if(AnnualIncome <= 250000):
    incomeTax = 0
elif(AnnualIncome > 250000 and AnnualIncome <= 500000):
    incomeTax = (AnnualIncome  - 250000)* 5/100
elif(AnnualIncome > 500000 and AnnualIncome <= 750000):
    incomeTax = (AnnualIncome - 500000) * 10/100 + 12500 
elif(AnnualIncome > 750000 and AnnualIncome <= 1000000):
    incomeTax = ((AnnualIncome - 750000) * 15/100) + 37500
elif(AnnualIncome > 1000000 and AnnualIncome <= 1250000):
    incomeTax = ((AnnualIncome - 1000000) * 20/100) + 75000
elif(AnnualIncome > 1250000 and AnnualIncome <= 1500000):
    incomeTax = ((AnnualIncome - 1250000) * 25/100) + 125000
elif(AnnualIncome > 1500000):
    incomeTax = ((AnnualIncome - 1500000) * 30/100) + 187500

print(grossPay,AnnualIncome,incomeTax)