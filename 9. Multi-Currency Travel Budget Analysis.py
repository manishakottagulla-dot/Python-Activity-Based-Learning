# 9. Multi-Currency Travel Budget Analysis

expenses = [
    {"category": "Accommodation", "amount": 300, "currency": "USD"},
    {"category": "Food", "amount": 120, "currency": "EUR"},
    {"category": "Transport", "amount": 10000, "currency": "INR"},
]

rates_to_inr = {
    "USD": 83.0,
    "EUR": 90.0,
    "INR": 1.0
}

budget = 50000
fee_rate = 0.02
converted_expenses = []

for e in expenses:
    if e["amount"] < 0 or e["currency"] not in rates_to_inr:
        raise ValueError("Invalid expense or missing exchange rate")

    converted = e["amount"] * rates_to_inr[e["currency"]]
    fee = converted * fee_rate
    final = converted + fee

    converted_expenses.append((e["category"], final))
    print(f"{e['category']}: INR {final:.2f} including fee")

total = sum(value for _, value in converted_expenses)
largest = max(converted_expenses, key=lambda item: item[1])

print(f"Total travel spending: INR {total:.2f}")

if total <= budget:
    print(f"Budget remaining: INR {budget - total:.2f}")
else:
    print(f"Budget exceeded by: INR {total - budget:.2f}")

print(f"Largest expense category: {largest[0]} (INR {largest[1]:.2f})")
