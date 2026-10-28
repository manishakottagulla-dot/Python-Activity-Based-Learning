def energy_charge(units):
    if units <= 100:
        return units * 1.50
    elif units <= 200:
        return 100 * 1.50 + (units - 100) * 2.50
    else:
        return 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00


monthly_units = [80, 120, 260]
bills = []

print("PROGRESSIVE ELECTRICITY BILLING")

for month, units in enumerate(monthly_units, start=1):
    if units < 0:
        raise ValueError("Units cannot be negative")

    energy = energy_charge(units)
    surcharge = energy * 0.05
    rebate = 20 if units <= 100 else 0
    total = energy + 50 + surcharge - rebate

    bills.append(total)

    print(f"\nMonth {month}")
    print(f"Units: {units}")
    print(f"Energy charge: Rs.{energy:.2f}")
    print(f"Fixed charge: Rs.50.00")
    print(f"Surcharge: Rs.{surcharge:.2f}")
    print(f"Rebate: Rs.{rebate:.2f}")
    print(f"Total bill: Rs.{total:.2f}")

print("\nMONTHLY BILL COMPARISON")

for i in range(1, len(bills)):
    previous = bills[i - 1]
    current = bills[i]

    increase = (
        (current - previous) / previous * 100
        if previous != 0 else 0
    )

    status = "UNUSUAL INCREASE" if increase > 30 else "Normal"
    print(f"Month {i + 1}: {increase:.1f}% - {status}")
