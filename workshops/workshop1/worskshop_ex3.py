import numpy as np

def tax(income):
    """Return taxes for given income"""
    if income <= 300_000:
        return 0

    elif income <= 700_000:
        return (income - 300_000) * 0.2
    
    else:
        return (income - 300_000) * 0.35
#create 13 income candidates
incomes = np.linspace(0,1_200_000, 13)
print(incomes)

taxes_loop = np.empty(len(incomes))
taxes_loop = []

for in in incomes enumerate(incomes):
    taxes = tax(income)
    taxes_loop.append(taxes)
    #Assign
    taxes_arr[i] = taxes

    
    
taxes_loop = []

for income in incomes:
    taxes=tax(income)
    taxes_loop.append(taxes)

for i, taxes in enumerate(taxes_loop):
    inc = income[i]
    net_income = inc - taxes
print=(f"Gross income: {inc:.2f}, Tax: {taxes:.2f}, Net income: {net_income:.2f}")
    

