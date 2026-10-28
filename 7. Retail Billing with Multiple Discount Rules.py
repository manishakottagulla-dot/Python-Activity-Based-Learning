# 7. Retail Billing with Multiple Discount Rules

products = [
    {"name": "Headphones", "category": "electronics", "price": 1800, "qty": 2},
    {"name": "Shirt", "category": "clothing", "price": 900, "qty": 2},
    {"name": "Rice", "category": "groceries", "price": 700, "qty": 1},
]

tax_rates = {
    "electronics": 0.18,
    "clothing": 0.05,
    "groceries": 0.00
}

for p in products:
    if p["price"] < 0 or p["qty"] <= 0 or p["category"] not in tax_rates:
        raise ValueError("Invalid product details")

subtotal = sum(p["price"] * p["qty"] for p in products)
discount = min(subtotal * 0.10, 1000) if subtotal >= 5000 else 0
total_tax = 0

print("ITEMIZED INVOICE")

for p in products:
    line = p["price"] * p["qty"]
    share = line / subtotal if subtotal else 0
    taxable = line - discount * share
    tax = taxable * tax_rates[p["category"]]
    total_tax += tax

    print(
        f"{p['name']}: {p['qty']} x Rs.{p['price']} "
        f"= Rs.{line:.2f}; tax Rs.{tax:.2f}"
    )

final_total = subtotal - discount + total_tax

print(f"Subtotal: Rs.{subtotal:.2f}")
print(f"Discount: Rs.{discount:.2f}")
print(f"Tax: Rs.{total_tax:.2f}")
print(f"Final amount: Rs.{final_total:.2f}")
