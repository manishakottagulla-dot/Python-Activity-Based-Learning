age = 65
consultation = 500
diagnostics = 1200
treatment = 3000
valid_card = False
amount_paid = 2500

charges = [consultation, diagnostics, treatment, amount_paid]

if age < 0 or any(charge < 0 for charge in charges):
    raise ValueError("Age and charges must be non-negative")

service_total = consultation + diagnostics + treatment

if age >= 60 or valid_card:
    discount = service_total * 0.10
else:
    discount = 0

subtotal = service_total - discount
tax = subtotal * 0.05
final_bill = subtotal + tax

if amount_paid >= final_bill:
    status = "Paid"
elif amount_paid > 0:
    status = "Partial payment"
else:
    status = "Unpaid"

print("HOSPITAL BILL")
print(f"Service total: Rs.{service_total:.2f}")
print(f"Concession: Rs.{discount:.2f}")
print(f"Subtotal: Rs.{subtotal:.2f}")
print(f"Tax: Rs.{tax:.2f}")
print(f"Final bill: Rs.{final_bill:.2f}")
print(f"Amount paid: Rs.{amount_paid:.2f}")
print("Payment classification:", status)
