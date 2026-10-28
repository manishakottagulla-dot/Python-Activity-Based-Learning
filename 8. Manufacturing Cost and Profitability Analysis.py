# 8. Manufacturing Cost and Profitability Analysis

material_qty = 500
unit_material_cost = 12
wastage_percent = 5
labour_cost = 2500
machine_cost = 1800
units_produced = 450
selling_price = 25
target_margin = 20

if (
    material_qty < 0 or unit_material_cost < 0 or labour_cost < 0
    or machine_cost < 0 or units_produced <= 0 or selling_price < 0
    or not 0 <= wastage_percent <= 100
):
    raise ValueError("Invalid production data")

material_cost = material_qty * unit_material_cost
wastage_cost = material_cost * wastage_percent / 100
total_cost = material_cost + wastage_cost + labour_cost + machine_cost
unit_cost = total_cost / units_produced
revenue = units_produced * selling_price
profit = revenue - total_cost
margin = profit / total_cost * 100 if total_cost else 0

print("MANUFACTURING REPORT")
print(f"Material cost: Rs.{material_cost:.2f}")
print(f"Wastage cost: Rs.{wastage_cost:.2f}")
print(f"Labour cost: Rs.{labour_cost:.2f}")
print(f"Machine cost: Rs.{machine_cost:.2f}")
print(f"Total production cost: Rs.{total_cost:.2f}")
print(f"Cost per unit: Rs.{unit_cost:.2f}")
print(f"Revenue: Rs.{revenue:.2f}")
print(f"Profit: Rs.{profit:.2f}; Margin: {margin:.2f}%")
print("Target achieved" if margin >= target_margin else "Target not achieved")
