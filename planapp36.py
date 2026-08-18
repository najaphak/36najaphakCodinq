# Plan Grade
# โปรแกรมคำนวณ GPA และวางแผนการเรียน

print("=" * 50)
print("       PLAN GRADE")
print(" โปรแกรมคำนวณเกรดเฉลี่ยและวางแผนการเรียน")
print("=" * 50)

# --------------------------------
# รับข้อมูลปัจจุบัน
# --------------------------------

current_gpa = float(input("GPA ปัจจุบัน: "))
completed_credit = float(input("หน่วยกิตที่เรียนแล้ว: "))

# --------------------------------
# รับ GPA เป้าหมาย
# --------------------------------

target_gpa = float(input("GPA เป้าหมาย: "))
remaining_credit = float(input("หน่วยกิตที่เหลือ: "))

# --------------------------------
# คำนวณ GPA ที่ต้องได้
# --------------------------------

required_gpa = (
    (target_gpa * (completed_credit + remaining_credit))
    - (current_gpa * completed_credit)
) / remaining_credit

print()
print("-" * 50)
print("ผลการคำนวณ")
print("-" * 50)

print(f"GPA ปัจจุบัน       : {current_gpa:.2f}")
print(f"GPA เป้าหมาย       : {target_gpa:.2f}")
print(f"หน่วยกิตที่เรียนแล้ว: {completed_credit:.0f}")
print(f"หน่วยกิตที่เหลือ    : {remaining_credit:.0f}")
print(f"GPA ที่ต้องได้      : {required_gpa:.2f}")

# --------------------------------
# ตรวจสอบความเป็นไปได้
# --------------------------------

if required_gpa > 4.00:
    print()
    print("❌ ไม่สามารถถึง GPA เป้าหมายได้")
    print("เนื่องจากต้องได้ GPA มากกว่า 4.00")

elif required_gpa < 0:
    print()
    print("✅ GPA ปัจจุบันสูงกว่าเป้าหมายแล้ว")

elif required_gpa >= 3.50:
    print()
    print("⚠️ เป้าหมายค่อนข้างท้าทาย")
    print(f"ต้องรักษา GPA ประมาณ {required_gpa:.2f}")

else:
    print()
    print("✅ สามารถทำถึงเป้าหมายได้")
    print(f"ควรทำ GPA เฉลี่ยอย่างน้อย {required_gpa:.2f}")

# --------------------------------
# ระบบวางแผนรายวิชา
# --------------------------------

print()
print("=" * 50)
print("       วางแผนเกรดรายวิชา")
print("=" * 50)

grades = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "F": 0.0
}

number_of_courses = int(
    input("จำนวนรายวิชาที่ต้องการวางแผน: ")
)

total_credit = 0
total_point = 0

for i in range(number_of_courses):

    print()
    print(f"วิชาที่ {i + 1}")

    credit = float(
        input("หน่วยกิต: ")
    )

    grade = input(
        "เกรดที่คาดว่าจะได้ (A/B+/B/C+/C/D+/D/F): "
    ).upper()

    if grade not in grades:
        print("❌ เกรดไม่ถูกต้อง")
        continue

    total_credit += credit
    total_point += credit * grades[grade]

# --------------------------------
# คำนวณ GPA จากแผน
# --------------------------------

if total_credit > 0:

    planned_gpa = total_point / total_credit

    print()
    print("=" * 50)
    print("ผลการวางแผนการเรียน")
    print("=" * 50)

    print(f"หน่วยกิตรวม : {total_credit:.0f}")
    print(f"GPA ที่คาดว่าจะได้ : {planned_gpa:.2f}")

    if planned_gpa >= target_gpa:
        print("✅ แผนนี้สามารถถึง GPA เป้าหมายได้")

    else:
        print("⚠️ แผนนี้ยังไม่ถึง GPA เป้าหมาย")
        print(
            f"ต้องเพิ่ม GPA อีกประมาณ "
            f"{target_gpa - planned_gpa:.2f}"
        )

else:

    print("ไม่พบข้อมูลสำหรับคำนวณ GPA")

print()
print("=" * 50)
print("ขอบคุณที่ใช้ Plan Grade")
print("=" * 50)