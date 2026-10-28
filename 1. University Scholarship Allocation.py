applicants = [
    {"name": "Asha", "aggregate": 88, "subjects": [82, 90, 85],
     "attendance": 92, "income": 180000},
    {"name": "Bala", "aggregate": 88, "subjects": [75, 80, 60],
     "attendance": 95, "income": 200000},
    {"name": "Charan", "aggregate": 72, "subjects": [80, 75, 70],
     "attendance": 90, "income": 150000},
    {"name": "Divya", "aggregate": 81, "subjects": [78, 84, 80],
     "attendance": 85, "income": 220000},
]

eligible = []

for student in applicants:
    valid = (
        0 <= student["aggregate"] <= 100
        and all(0 <= mark <= 100 for mark in student["subjects"])
        and 0 <= student["attendance"] <= 100
        and student["income"] >= 0
    )

    if not valid:
        print("Invalid data:", student["name"])
        continue

    qualifies = (
        student["aggregate"] >= 75
        and all(mark >= 60 for mark in student["subjects"])
        and student["attendance"] >= 75
        and student["income"] <= 250000
    )

    if qualifies:
        eligible.append(student)

eligible.sort(
    key=lambda s: (-s["aggregate"], -s["attendance"], s["income"])
)

print("UNIVERSITY SCHOLARSHIP MERIT LIST")

if not eligible:
    print("No applicants qualify.")
else:
    for rank, student in enumerate(eligible, start=1):
        print(
            f"{rank}. {student['name']} | "
            f"Aggregate: {student['aggregate']}% | "
            f"Attendance: {student['attendance']}% | "
            f"Income: Rs.{student['income']}"
        )
