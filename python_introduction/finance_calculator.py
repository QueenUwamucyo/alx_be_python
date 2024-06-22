monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your total monthly expense: "))
monthly_savings = monthly_income - monthly_expense
annual_savings_without_inerest = monthly_savings * 12
annual_interest = annual_savings_without_inerest * 0.05
projected_annual_savings = annual_savings_without_inerest + annual_interest
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
