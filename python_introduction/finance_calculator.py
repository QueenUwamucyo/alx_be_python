monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your total monthly expense: "))
monthly_savings = monthly_income - monthly_expense
projected_annual_savings =  monthly_savings * 12 +  monthly_savings * 12 * 0.05
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")