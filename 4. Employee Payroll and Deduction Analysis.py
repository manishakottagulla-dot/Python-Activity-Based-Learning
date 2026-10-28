# 4. Employee Payroll and Deduction Analysis

basic = 30000
overtime_hours = 8
incentive = 2000

if basic < 0 or overtime_hours < 0 or incentive < 0:
    raise ValueError("Salary inputs must be non-negative")

hra = basic * 0.20
other_allowance = basic * 0.10
overtime_pay = overtime_hours * (basic / 160) * 1.5
gross = basic + hra + other_allowance + overtime_pay + incentive


def progressive_tax(amount):
    tax = 0
    tax += min(amount, 20000) * 0
    tax += min(max(amount - 20000, 0), 20000) * 0.05
    tax += max(amount - 40000, 0) * 0.10
    return tax


tax = progressive_tax(gross)
pf = basic * 0.08
net = gross - tax - pf

print("EMPLOYEE SALARY STATEMENT")
print(f"Basic pay:          Rs.{basic:,.2f}")
print(f"HRA:                Rs.{hra:,.2f}")
print(f"Other allowance:    Rs.{other_allowance:,.2f}")
print(f"Overtime pay:       Rs.{overtime_pay:,.2f}")
print(f"Incentive:          Rs.{incentive:,.2f}")
print(f"Gross salary:       Rs.{gross:,.2f}")
print(f"Progressive tax:    Rs.{tax:,.2f}")
print(f"PF deduction:       Rs.{pf:,.2f}")
print(f"Net salary:         Rs.{net:,.2f}")
