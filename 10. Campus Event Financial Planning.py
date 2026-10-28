# 10. Campus Event Financial Planning

import math

venue = 12000
equipment = 5000
transport = 3000
catering_per_person = 180
certificate_per_person = 20
sponsorship = 10000
registration_fee = 300
expected_participants = 80

values = [
    venue, equipment, transport, catering_per_person,
    certificate_per_person, sponsorship, registration_fee,
    expected_participants
]

if any(v < 0 for v in values):
    raise ValueError("All costs and counts must be non-negative")

fixed_cost = venue + equipment + transport
variable_per_person = catering_per_person + certificate_per_person
total_cost = fixed_cost + expected_participants * variable_per_person
registration_income = expected_participants * registration_fee
available_funds = registration_income + sponsorship
shortfall = max(total_cost - available_funds, 0)
surplus = max(available_funds - total_cost, 0)

net_per_registration = registration_fee - variable_per_person

if fixed_cost <= sponsorship:
    break_even = 0
elif net_per_registration <= 0:
    break_even = None
else:
    break_even = math.ceil(
        (fixed_cost - sponsorship) / net_per_registration
    )

print("CAMPUS EVENT BUDGET")
print(f"Fixed costs: Rs.{fixed_cost:.2f}")
print(f"Variable cost per participant: Rs.{variable_per_person:.2f}")
print(f"Total cost for {expected_participants} participants: Rs.{total_cost:.2f}")
print(f"Registration income: Rs.{registration_income:.2f}")
print(f"Sponsorship: Rs.{sponsorship:.2f}")
print(f"Funding shortfall: Rs.{shortfall:.2f}")
print(f"Surplus: Rs.{surplus:.2f}")
print(
    "Break-even registrations:",
    break_even if break_even is not None else "Not possible at this fee"
)
