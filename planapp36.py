import tkinter as tk
from tkinter import ttk, messagebox

# ==============================
# ระบบแปลงเกรดเป็นคะแนน
# ==============================

GRADE_POINTS = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "F": 0.0
}


# ==============================
# ฟังก์ชันคำนวณ GPA
# ==============================

def calculate_gpa():
    try:
        current_gpa = float(current_gpa_entry.get())
        completed_credit = float(completed_credit_entry.get())
        remaining_credit = float(remaining_credit_entry.get())
        target_gpa = float(target_gpa_entry.get())

        if not 0 <= current_gpa <= 4:
            raise ValueError

        if not 0 <= target_gpa <= 4:
            raise ValueError

        if completed_credit < 0 or remaining_credit <= 0:
            raise ValueError

        required_gpa = (
            target_gpa * (completed_credit + remaining_credit)
            - current_gpa * completed_credit
        ) / remaining_credit

        result_gpa_label.config(
            text=f"{required_gpa:.2f}"
        )

        if required_gpa <= 4:

            if required_gpa <= 3:

                result_label.config(
                    text="✓ เป้าหมายสามารถทำได้",
                    foreground="#159447"
                )

            else:

                result_label.config(
                    text="! เป้าหมายค่อนข้างท้าทาย",
                    foreground="#d68b00"
                )

        else:

            result_label.config(
                text="✕ ไม่สามารถถึงเป้าหมายได้",
                foreground="#d93025"
            )

    except ValueError:

        messagebox.showerror(
            "ข้อมูลไม่ถูกต้อง",
            "กรุณากรอกข้อมูลเป็นตัวเลขให้ถูกต้อง"
        )


# ==============================
# คำนวณ GPA จากรายวิชา
# ==============================

def calculate_courses():

    try:

        total_credit = 0
        total_point = 0

        for credit_entry, grade_box in courses:

            credit = float(credit_entry.get())
            grade = grade_box.get()

            if credit <= 0:
                continue

            if grade not in GRADE_POINTS:
                continue

            total_credit += credit

            total_point += (
                credit * GRADE_POINTS[grade]
            )

        if total_credit == 0:

            messagebox.showwarning(
                "แจ้งเตือน",
                "กรุณากรอกข้อมูลรายวิชา"
            )

            return

        gpa = total_point / total_credit

        course_result.config(
            text=f"GPA จากแผนการเรียน = {gpa:.2f}"
        )

    except ValueError:

        messagebox.showerror(
            "ข้อมูลไม่ถูกต้อง",
            "กรุณาตรวจสอบหน่วยกิต"
        )


# ==============================
# หน้าต่างหลัก
# ==============================

root = tk.Tk()

root.title(
    "Plan Grade - โปรแกรมวางแผนการเรียน"
)

root.geometry("1000x700")

root.configure(
    bg="#f5f3ff"
)


# ==============================
# Header
# ==============================

header = tk.Frame(
    root,
    bg="#5a4bdc",
    height=120
)

header.pack(
    fill="x"
)

title = tk.Label(
    header,
    text="🎓 Plan Grade",
    font=("Arial", 30, "bold"),
    bg="#5a4bdc",
    fg="white"
)

title.pack(
    pady=(20, 5)
)

subtitle = tk.Label(
    header,
    text="โปรแกรมคำนวณเกรดเฉลี่ยสะสมและวางแผนการเรียน",
    font=("Arial", 14),
    bg="#5a4bdc",
    fg="white"
)

subtitle.pack()


# ==============================
# Notebook
# ==============================

notebook = ttk.Notebook(root)

notebook.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=25
)


# ==========================================================
# TAB 1 : คำนวณเป้าหมาย GPA
# ==========================================================

gpa_page = tk.Frame(
    notebook,
    bg="#f5f3ff"
)

notebook.add(
    gpa_page,
    text="  🎯 คำนวณเป้าหมาย GPA  "
)


# ------------------------------
# กล่องข้อมูล
# ------------------------------

input_box = tk.Frame(
    gpa_page,
    bg="white",
    padx=30,
    pady=25
)

input_box.pack(
    fill="x",
    padx=20,
    pady=20
)


tk.Label(
    input_box,
    text="ข้อมูลการเรียนปัจจุบัน",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="#40378f"
).grid(
    row=0,
    column=0,
    columnspan=2,
    pady=(0, 20)
)


# GPA ปัจจุบัน

tk.Label(
    input_box,
    text="GPA ปัจจุบัน",
    font=("Arial", 12),
    bg="white"
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=8
)

current_gpa_entry = tk.Entry(
    input_box,
    font=("Arial", 12),
    width=25
)

current_gpa_entry.insert(
    0,
    "3.00"
)

current_gpa_entry.grid(
    row=1,
    column=1,
    pady=8
)


# หน่วยกิตที่เรียนแล้ว

tk.Label(
    input_box,
    text="หน่วยกิตที่เรียนแล้ว",
    font=("Arial", 12),
    bg="white"
).grid(
    row=2,
    column=0,
    sticky="w",
    pady=8
)

completed_credit_entry = tk.Entry(
    input_box,
    font=("Arial", 12),
    width=25
)

completed_credit_entry.insert(
    0,
    "60"
)

completed_credit_entry.grid(
    row=2,
    column=1,
    pady=8
)


# หน่วยกิตที่เหลือ

tk.Label(
    input_box,
    text="หน่วยกิตที่เหลือ",
    font=("Arial", 12),
    bg="white"
).grid(
    row=3,
    column=0,
    sticky="w",
    pady=8
)

remaining_credit_entry = tk.Entry(
    input_box,
    font=("Arial", 12),
    width=25
)

remaining_credit_entry.insert(
    0,
    "60"
)

remaining_credit_entry.grid(
    row=3,
    column=1,
    pady=8
)


# GPA เป้าหมาย

tk.Label(
    input_box,
    text="GPA เป้าหมาย",
    font=("Arial", 12),
    bg="white"
).grid(
    row=4,
    column=0,
    sticky="w",
    pady=8
)

target_gpa_entry = tk.Entry(
    input_box,
    font=("Arial", 12),
    width=25
)

target_gpa_entry.insert(
    0,
    "3.50"
)

target_gpa_entry.grid(
    row=4,
    column=1,
    pady=8
)


# ปุ่มคำนวณ

calculate_button = tk.Button(
    input_box,
    text="🧮 คำนวณ GPA ที่ต้องได้",
    font=("Arial", 13, "bold"),
    bg="#5a4bdc",
    fg="white",
    activebackground="#4538b8",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    command=calculate_gpa
)

calculate_button.grid(
    row=5,
    column=0,
    columnspan=2,
    pady=20
)


# ==============================
# ผลลัพธ์
# ==============================

result_box = tk.Frame(
    gpa_page,
    bg="white",
    padx=30,
    pady=25
)

result_box.pack(
    fill="x",
    padx=20
)


tk.Label(
    result_box,
    text="GPA ที่ต้องได้ในวิชาที่เหลือ",
    font=("Arial", 16),
    bg="white"
).pack()


result_gpa_label = tk.Label(
    result_box,
    text="0.00",
    font=("Arial", 40, "bold"),
    bg="white",
    fg="#5a4bdc"
)

result_gpa_label.pack(
    pady=10
)


result_label = tk.Label(
    result_box,
    text="กรอกข้อมูลแล้วกดคำนวณ",
    font=("Arial", 14, "bold"),
    bg="white"
)

result_label.pack()


# ==========================================================
# TAB 2 : วางแผนรายวิชา
# ==========================================================

course_page = tk.Frame(
    notebook,
    bg="#f5f3ff"
)

notebook.add(
    course_page,
    text="  📚 วางแผนรายวิชา  "
)


tk.Label(
    course_page,
    text="วางแผนเกรดรายวิชา",
    font=("Arial", 22, "bold"),
    bg="#f5f3ff",
    fg="#40378f"
).pack(
    pady=20
)


# หัวตาราง

table = tk.Frame(
    course_page,
    bg="white",
    padx=20,
    pady=20
)

table.pack(
    padx=30,
    fill="x"
)


tk.Label(
    table,
    text="วิชา",
    font=("Arial", 12, "bold"),
    bg="white"
).grid(row=0, column=0, padx=20)


tk.Label(
    table,
    text="หน่วยกิต",
    font=("Arial", 12, "bold"),
    bg="white"
).grid(row=0, column=1, padx=20)


tk.Label(
    table,
    text="เกรด",
    font=("Arial", 12, "bold"),
    bg="white"
).grid(row=0, column=2, padx=20)


courses = []


# สร้าง 6 รายวิชา

for i in range(6):

    tk.Label(
        table,
        text=f"วิชาที่ {i + 1}",
        bg="white",
        font=("Arial", 11)
    ).grid(
        row=i + 1,
        column=0,
        pady=7
    )

    credit_entry = tk.Entry(
        table,
        width=12
    )

    credit_entry.insert(
        0,
        "3"
    )

    credit_entry.grid(
        row=i + 1,
        column=1
    )

    grade_box = ttk.Combobox(
        table,
        values=list(GRADE_POINTS.keys()),
        width=10,
        state="readonly"
    )

    grade_box.set("B+")

    grade_box.grid(
        row=i + 1,
        column=2
    )

    courses.append(
        (
            credit_entry,
            grade_box
        )
    )


# ปุ่มคำนวณรายวิชา

tk.Button(
    course_page,
    text="📊 คำนวณ GPA",
    font=("Arial", 13, "bold"),
    bg="#5a4bdc",
    fg="white",
    relief="flat",
    padx=25,
    pady=10,
    command=calculate_courses
).pack(
    pady=25
)


course_result = tk.Label(
    course_page,
    text="GPA จากแผนการเรียน = -",
    font=("Arial", 20, "bold"),
    bg="#f5f3ff",
    fg="#5a4bdc"
)

course_result.pack()


# ==============================
# Footer
# ==============================

tk.Label(
    root,
    text="Plan Grade | โปรแกรมช่วยวางแผนการเรียน",
    font=("Arial", 10),
    bg="#f5f3ff",
    fg="#777777"
).pack(
    pady=8
)


# ==============================
# เริ่มโปรแกรม
# ==============================

root.mainloop()