# 5. Multi-Plan Telecommunications Cost Optimization

import math

usage_gb = 18
budget = 500

plans = [
    {"name": "Basic", "price": 199, "data": 10,
     "extra_rate": 20, "validity": 28},
    {"name": "Smart", "price": 349, "data": 20,
     "extra_rate": 15, "validity": 30},
    {"name": "Max", "price": 449, "data": 30,
     "extra_rate": 10, "validity": 56},
]

if usage_gb < 0 or budget < 0:
    raise ValueError("Usage and budget must be non-negative")

eligible = []

print("MOBILE PLAN COST COMPARISON")

for plan in plans:
    excess = max(0, usage_gb - plan["data"])
    extra_charge = math.ceil(excess) * plan["extra_rate"]
    total = plan["price"] + extra_charge

    print(
        f"{plan['name']}: base Rs.{plan['price']}, "
        f"excess Rs.{extra_charge}, total Rs.{total}, "
        f"validity {plan['validity']} days"
    )

    if plan["validity"] >= 30 and total <= budget:
        eligible.append(
            (total, plan["name"], plan["validity"])
        )

if eligible:
    eligible.sort()
    total, name, validity = eligible[0]
    print(
        f"Best eligible plan: {name} | Total Rs.{total} "
        f"| Validity {validity} days"
    )
else:
    print("No plan satisfies validity and budget constraints.")
