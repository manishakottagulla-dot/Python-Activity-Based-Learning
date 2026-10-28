# 6. Railway Fare and Reservation Calculator

def distance_fare(km):
    first = min(km, 100) * 0.75
    second = min(max(km - 100, 0), 400) * 0.60
    rest = max(km - 500, 0) * 0.45
    return first + second + rest


distance = 350
travel_class = "AC"
ages = [25, 62, 4]
cancelled = False

multipliers = {
    "Sleeper": 1.0,
    "AC": 2.0
}

if (
    distance <= 0
    or travel_class not in multipliers
    or any(age < 0 for age in ages)
):
    raise ValueError("Invalid journey or passenger data")

print("RAILWAY FARE AND RESERVATION DETAILS")
print(f"Distance: {distance} km")
print(f"Travel class: {travel_class}")
print(f"Cancellation requested: {'Yes' if cancelled else 'No'}")

base_fare = distance_fare(distance)
grand_total = 0

for index, age in enumerate(ages, start=1):
    fare = base_fare * multipliers[travel_class]

    if age < 5:
        fare = 0
    elif age >= 60:
        fare *= 0.80

    reservation_fee = 40 if fare > 0 else 0
    total = fare + reservation_fee

    if cancelled and total > 0:
        refund = max(0, fare * 0.75)
        print(
            f"Passenger {index}: "
            f"cancellation refund Rs.{refund:.2f}"
        )
    else:
        grand_total += total
        print(
            f"Passenger {index}, age {age}: "
            f"fare Rs.{total:.2f}"
        )

if not cancelled:
    print(f"Total booking amount: Rs.{grand_total:.2f}")
