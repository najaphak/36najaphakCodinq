import tkinter as tk
from tkinter import ttk, messagebox
from decimal import Decimal, ROUND_HALF_UP


# =========================================================
# PLAN GRADE
# โปรแกรมคำนวณเกรดเฉลี่ยสะสม (GPA)
# และวางแผนการเรียน
# =========================================================


# =========================================================
# คะแนนของแต่ละเกรด
# =========================================================

GRADE_POINTS = {
    "A": 4.00,
    "B+": 3.50,
    "B": 3.00,
    "C+": 2.50,
    "C": 2.00,
    "D+": 1.50,
    "D": 1.00,
    "F": 0.00
}


# =========================================================
# สีของโปรแกรม
# =========================================================

PURPLE = "#5B4BDB"
DARK_PURPLE = "#4033A3"
LIGHT_PURPLE = "#F2F0FF"

BLUE = "#4D8DFF"
WHITE = "#FFFFFF"

TEXT = "#29264B"
GRAY = "#777777"

GREEN = "#16A05D"
ORANGE = "#E79A00"
RED = "#D9363E"


# =========================================================
# ฟังก์ชันปัดทศนิยมแบบทั่วไป
# เช่น 3.995 -> 4.00
# =========================================================

def round_gpa(value):
    return float(
        Decimal(str(value)).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )
    )


# =========================================================
# ฟังก์ชันตรวจสอบ GPA
# =========================================================

def valid_gpa(value):
    return 0 <= value <= 4


# =========================================================
# ฟังก์ชันคำนวณ GPA จากรายวิชา
# =========================================================

def calculate_gpa_from_courses():

    total_credit = 0
    total_point = 0

    try:

        for row in course_rows:

            credit_text = row["credit"].get().strip()
            grade = row["grade"].get()

            # ถ้าไม่ได้กรอกหน่วยกิต ให้ข้าม
            if credit_text == "":
                continue

            credit = float(credit_text)

            # หน่วยกิตต้องมากกว่า 0
            if credit <= 0:
                continue

            # ต้องเลือกเกรด
            if grade not in GRADE_POINTS:
                continue

            total_credit += credit
            total_point += credit * GRADE_POINTS[grade]

        if total_credit == 0:

            messagebox.showwarning(
                "แจ้งเตือน",
                "กรุณากรอกข้อมูลรายวิชาอย่างน้อย 1 วิชา"
            )

            return

        # GPA จริง
        gpa = total_point / total_credit

        # GPA ที่แสดง 2 ตำแหน่ง
        displayed_gpa = round_gpa(gpa)

        # -----------------------------------------
        # แสดงผลหน้ารายวิชา
        # -----------------------------------------

        current_gpa_label.config(
            text=f"GPA = {displayed_gpa:.2f}"
        )

        current_credit_label.config(
            text=f"หน่วยกิต = {total_credit:.0f}"
        )

        # -----------------------------------------
        # อัปเดต Dashboard
        # -----------------------------------------

        dashboard_gpa_label.config(
            text=f"{displayed_gpa:.2f}"
        )

        dashboard_credit_label.config(
            text=f"{total_credit:.0f}"
        )

        # -----------------------------------------
        # อัปเดตช่อง GPA ปัจจุบันในหน้า Target
        # -----------------------------------------

        target_current_gpa.delete(0, tk.END)
        target_current_gpa.insert(
            0,
            f"{displayed_gpa:.2f}"
        )

        target_completed_credit.delete(0, tk.END)
        target_completed_credit.insert(
            0,
            f"{total_credit:.0f}"
        )

    except ValueError:

        messagebox.showerror(
            "ข้อมูลไม่ถูกต้อง",
            "กรุณากรอกหน่วยกิตเป็นตัวเลข"
        )


# =========================================================
# ฟังก์ชันคำนวณ GPA ที่ต้องได้เพื่อให้ถึงเป้าหมาย
# =========================================================

def calculate_target_gpa():

    try:

        current_gpa = float(
            target_current_gpa.get().strip()
        )

        completed_credit = float(
            target_completed_credit.get().strip()
        )

        remaining_credit = float(
            target_remaining_credit.get().strip()
        )

        target_gpa = float(
            target_gpa_entry.get().strip()
        )

        # =================================================
        # ตรวจสอบข้อมูล
        # =================================================

        if not valid_gpa(current_gpa):

            raise ValueError

        if not valid_gpa(target_gpa):

            raise ValueError

        if completed_credit < 0:

            raise ValueError

        if remaining_credit <= 0:

            messagebox.showwarning(
                "แจ้งเตือน",
                "หน่วยกิตที่เหลือต้องมากกว่า 0"
            )

            return

        # =================================================
        # คำนวณ GPA ที่ต้องได้
        # =================================================

        required_gpa = (
            target_gpa *
            (completed_credit + remaining_credit)
            -
            current_gpa *
            completed_credit
        ) / remaining_credit

        # =================================================
        # คำนวณ GPA สูงสุด
        # สมมติว่าได้ A = 4.00 ทุกวิชา
        # =================================================

        maximum_gpa = (
            current_gpa * completed_credit
            +
            4.00 * remaining_credit
        ) / (
            completed_credit + remaining_credit
        )

        maximum_gpa_display = round_gpa(
            maximum_gpa
        )

        required_gpa_display = round_gpa(
            required_gpa
        )

        # =================================================
        # แสดง GPA ที่ต้องได้
        # =================================================

        if required_gpa <= 4:

            required_gpa_label.config(
                text=f"{required_gpa_display:.2f}",
                fg=PURPLE
            )

        else:

            required_gpa_label.config(
                text=f"{required_gpa_display:.2f}",
                fg=RED
            )

        # =================================================
        # แสดง GPA สูงสุด
        # =================================================

        maximum_gpa_label.config(
            text=(
                f"ถ้าได้ A ทุกวิชา "
                f"GPA สูงสุด = {maximum_gpa_display:.2f}"
            )
        )

        # =================================================
        # Dashboard
        # =================================================

        dashboard_target_label.config(
            text=f"{target_gpa:.2f}"
        )

        dashboard_required_label.config(
            text=f"{required_gpa_display:.2f}"
        )

        # =================================================
        # วิเคราะห์ผล
        # =================================================

        # -------------------------------------------------
        # กรณีต้องการ GPA <= 4.00
        # สามารถทำได้ในทางคณิตศาสตร์
        # -------------------------------------------------

        if required_gpa <= 4.00:

            if required_gpa <= 3.00:

                target_status_label.config(
                    text="✓ เป้าหมายสามารถทำได้",
                    fg=GREEN
                )

            else:

                target_status_label.config(
                    text="⚠ เป้าหมายค่อนข้างท้าทาย",
                    fg=ORANGE
                )

        # -------------------------------------------------
        # กรณี required > 4
        # แต่ GPA สูงสุดเมื่อปัด 2 ตำแหน่งยังถึงเป้าหมาย
        #
        # เช่น
        # 3.99 + A ทุกวิชา = 3.995
        # แสดง 2 ตำแหน่ง = 4.00
        # -------------------------------------------------

        elif maximum_gpa_display >= target_gpa:

            target_status_label.config(
                text=(
                    "✓ เมื่อปัด GPA เป็น 2 ตำแหน่ง "
                    "มีโอกาสแสดงถึงเป้าหมายได้"
                ),
                fg=GREEN
            )

        # -------------------------------------------------
        # กรณีทำไม่ได้จริง
        # -------------------------------------------------

        else:

            target_status_label.config(
                text=(
                    "✕ ไม่สามารถถึงเป้าหมายได้\n"
                    f"แม้ได้ A ทุกวิชา "
                    f"GPA สูงสุด = {maximum_gpa_display:.2f}"
                ),
                fg=RED
            )

    except ValueError:

        messagebox.showerror(
            "ข้อมูลไม่ถูกต้อง",
            "กรุณาตรวจสอบข้อมูลที่กรอก\n\n"
            "• GPA ต้องอยู่ระหว่าง 0.00 - 4.00\n"
            "• หน่วยกิตต้องเป็นตัวเลข\n"
            "• หน่วยกิตที่เหลือต้องมากกว่า 0"
        )


# =========================================================
# ฟังก์ชันคำนวณ GPA จากแผนการเรียน
# =========================================================

def calculate_plan():

    total_credit = 0
    total_point = 0

    try:

        for row in plan_rows:

            credit_text = row["credit"].get().strip()
            grade = row["grade"].get()

            if credit_text == "":
                continue

            credit = float(credit_text)

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

        # GPA จริง
        planned_gpa = (
            total_point / total_credit
        )

        # GPA หลังปัด
        planned_gpa_display = round_gpa(
            planned_gpa
        )

        planned_gpa_label.config(
            text=f"GPA จากแผน = {planned_gpa_display:.2f}"
        )

        # =================================================
        # ตรวจสอบ GPA เป้าหมาย
        # =================================================

        try:

            target = float(
                plan_target_entry.get().strip()
            )

            if not valid_gpa(target):

                raise ValueError

            # ---------------------------------------------
            # เปรียบเทียบ GPA ที่ปัดแล้ว
            # ---------------------------------------------

            if planned_gpa_display >= target:

                plan_status_label.config(
                    text=(
                        "✓ แผนนี้สามารถถึง GPA เป้าหมาย"
                    ),
                    fg=GREEN
                )

            else:

                difference = (
                    target -
                    planned_gpa_display
                )

                plan_status_label.config(
                    text=(
                        f"⚠ ยังต่ำกว่าเป้าหมาย "
                        f"{difference:.2f}"
                    ),
                    fg=ORANGE
                )

        except ValueError:

            plan_status_label.config(
                text="กรุณากรอก GPA เป้าหมายระหว่าง 0.00 - 4.00",
                fg=RED
            )

    except ValueError:

        messagebox.showerror(
            "ข้อมูลไม่ถูกต้อง",
            "กรุณากรอกหน่วยกิตเป็นตัวเลข"
        )


# =========================================================
# ฟังก์ชันเปลี่ยนหน้า
# =========================================================

def show_page(page):

    dashboard_frame.pack_forget()
    target_frame.pack_forget()
    course_frame.pack_forget()
    plan_frame.pack_forget()

    page.pack(
        fill="both",
        expand=True
    )


# =========================================================
# หน้าต่างหลัก
# =========================================================

root = tk.Tk()

root.title(
    "Plan Grade - โปรแกรมวางแผนการเรียน"
)

root.geometry(
    "1200x750"
)

root.minsize(
    1000,
    650
)

root.configure(
    bg=LIGHT_PURPLE
)


# =========================================================
# Sidebar
# =========================================================

sidebar = tk.Frame(
    root,
    bg=DARK_PURPLE,
    width=230
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


# =========================================================
# Logo
# =========================================================

tk.Label(
    sidebar,
    text="🎓",
    font=("Arial", 35),
    bg=DARK_PURPLE,
    fg=WHITE
).pack(
    pady=(30, 0)
)

tk.Label(
    sidebar,
    text="Plan Grade",
    font=("Arial", 22, "bold"),
    bg=DARK_PURPLE,
    fg=WHITE
).pack()

tk.Label(
    sidebar,
    text="Study Planner",
    font=("Arial", 10),
    bg=DARK_PURPLE,
    fg="#D9D5FF"
).pack(
    pady=(0, 30)
)


# =========================================================
# ปุ่ม Sidebar
# =========================================================

def sidebar_button(text, command):

    button = tk.Button(
        sidebar,
        text=text,
        command=command,
        font=("Arial", 12, "bold"),
        bg=DARK_PURPLE,
        fg=WHITE,
        activebackground=PURPLE,
        activeforeground=WHITE,
        relief="flat",
        bd=0,
        anchor="w",
        padx=25,
        pady=14,
        cursor="hand2"
    )

    button.pack(
        fill="x",
        padx=10,
        pady=3
    )


sidebar_button(
    "🏠  หน้าหลัก",
    lambda: show_page(dashboard_frame)
)

sidebar_button(
    "🎯  คำนวณ GPA เป้าหมาย",
    lambda: show_page(target_frame)
)

sidebar_button(
    "📚  รายวิชาและเกรด",
    lambda: show_page(course_frame)
)

sidebar_button(
    "📊  วางแผนการเรียน",
    lambda: show_page(plan_frame)
)


# =========================================================
# พื้นที่หลัก
# =========================================================

main_area = tk.Frame(
    root,
    bg=LIGHT_PURPLE
)

main_area.pack(
    side="right",
    fill="both",
    expand=True
)


# =========================================================
# Header
# =========================================================

header = tk.Frame(
    main_area,
    bg=WHITE,
    height=80
)

header.pack(
    fill="x"
)

header.pack_propagate(False)


tk.Label(
    header,
    text="Plan Grade",
    font=("Arial", 24, "bold"),
    bg=WHITE,
    fg=TEXT
).pack(
    side="left",
    padx=30,
    pady=20
)

tk.Label(
    header,
    text="โปรแกรมคำนวณ GPA และวางแผนการเรียน",
    font=("Arial", 11),
    bg=WHITE,
    fg=GRAY
).pack(
    side="left"
)


# =========================================================
# Container
# =========================================================

content = tk.Frame(
    main_area,
    bg=LIGHT_PURPLE
)

content.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=20
)


# =========================================================
# PAGE 1 : Dashboard
# =========================================================

dashboard_frame = tk.Frame(
    content,
    bg=LIGHT_PURPLE
)


tk.Label(
    dashboard_frame,
    text="📊 Dashboard",
    font=("Arial", 26, "bold"),
    bg=LIGHT_PURPLE,
    fg=TEXT
).pack(
    anchor="w",
    pady=(0, 20)
)


# =========================================================
# Dashboard Cards
# =========================================================

dashboard_cards = tk.Frame(
    dashboard_frame,
    bg=LIGHT_PURPLE
)

dashboard_cards.pack(
    fill="x"
)


# =========================================================
# ฟังก์ชันสร้าง Card
# =========================================================

def create_card(parent, title, value, color):

    card = tk.Frame(
        parent,
        bg=WHITE,
        padx=20,
        pady=18
    )

    label = tk.Label(
        card,
        text=title,
        font=("Arial", 11),
        bg=WHITE,
        fg=GRAY
    )

    label.pack(
        anchor="w"
    )

    value_label = tk.Label(
        card,
        text=value,
        font=("Arial", 28, "bold"),
        bg=WHITE,
        fg=color
    )

    value_label.pack(
        anchor="w",
        pady=(8, 0)
    )

    return card, value_label


card1, dashboard_gpa_label = create_card(
    dashboard_cards,
    "GPA ปัจจุบัน",
    "0.00",
    PURPLE
)

card1.grid(
    row=0,
    column=0,
    padx=8,
    sticky="nsew"
)


card2, dashboard_target_label = create_card(
    dashboard_cards,
    "GPA เป้าหมาย",
    "0.00",
    BLUE
)

card2.grid(
    row=0,
    column=1,
    padx=8,
    sticky="nsew"
)


card3, dashboard_credit_label = create_card(
    dashboard_cards,
    "หน่วยกิตที่เรียนแล้ว",
    "0",
    GREEN
)

card3.grid(
    row=0,
    column=2,
    padx=8,
    sticky="nsew"
)


card4, dashboard_required_label = create_card(
    dashboard_cards,
    "GPA ที่ต้องได้",
    "0.00",
    ORANGE
)

card4.grid(
    row=0,
    column=3,
    padx=8,
    sticky="nsew"
)


for i in range(4):

    dashboard_cards.columnconfigure(
        i,
        weight=1
    )


# =========================================================
# คำอธิบาย Dashboard
# =========================================================

info_box = tk.Frame(
    dashboard_frame,
    bg=WHITE,
    padx=30,
    pady=25
)

info_box.pack(
    fill="x",
    pady=25
)


tk.Label(
    info_box,
    text="💡 Plan Grade ช่วยอะไรได้บ้าง?",
    font=("Arial", 18, "bold"),
    bg=WHITE,
    fg=TEXT
).pack(
    anchor="w"
)


tk.Label(
    info_box,
    text=(
        "• คำนวณ GPA จากรายวิชาและหน่วยกิต\n"
        "• คำนวณ GPA ที่ต้องได้เพื่อให้ถึงเป้าหมาย\n"
        "• คำนวณ GPA สูงสุดหากได้ A ทุกวิชา\n"
        "• วางแผนเกรดของรายวิชาที่เหลือ\n"
        "• วิเคราะห์ว่าเป้าหมายสามารถทำได้หรือไม่"
    ),
    font=("Arial", 12),
    bg=WHITE,
    fg=GRAY,
    justify="left"
).pack(
    anchor="w",
    pady=15
)


# =========================================================
# PAGE 2 : Target GPA
# =========================================================

target_frame = tk.Frame(
    content,
    bg=LIGHT_PURPLE
)


tk.Label(
    target_frame,
    text="🎯 คำนวณ GPA เป้าหมาย",
    font=("Arial", 26, "bold"),
    bg=LIGHT_PURPLE,
    fg=TEXT
).pack(
    anchor="w",
    pady=(0, 20)
)


# =========================================================
# Target Input Box
# =========================================================

target_box = tk.Frame(
    target_frame,
    bg=WHITE,
    padx=30,
    pady=25
)

target_box.pack(
    fill="x"
)


# =========================================================
# ฟังก์ชันสร้าง Input
# =========================================================

def create_input(parent, text, default, row):

    tk.Label(
        parent,
        text=text,
        font=("Arial", 12),
        bg=WHITE,
        fg=TEXT
    ).grid(
        row=row,
        column=0,
        sticky="w",
        pady=8
    )

    entry = tk.Entry(
        parent,
        font=("Arial", 12),
        width=25,
        relief="solid",
        bd=1
    )

    entry.insert(
        0,
        default
    )

    entry.grid(
        row=row,
        column=1,
        padx=30,
        pady=8
    )

    return entry


target_current_gpa = create_input(
    target_box,
    "GPA ปัจจุบัน",
    "3.00",
    0
)


target_completed_credit = create_input(
    target_box,
    "หน่วยกิตที่เรียนแล้ว",
    "60",
    1
)


target_remaining_credit = create_input(
    target_box,
    "หน่วยกิตที่เหลือ",
    "60",
    2
)


target_gpa_entry = create_input(
    target_box,
    "GPA เป้าหมาย",
    "3.50",
    3
)


# =========================================================
# ปุ่มคำนวณ
# =========================================================

tk.Button(
    target_box,
    text="🧮 คำนวณ",
    command=calculate_target_gpa,
    font=("Arial", 13, "bold"),
    bg=PURPLE,
    fg=WHITE,
    activebackground=DARK_PURPLE,
    activeforeground=WHITE,
    relief="flat",
    padx=30,
    pady=10,
    cursor="hand2"
).grid(
    row=4,
    column=0,
    columnspan=2,
    pady=20
)


# =========================================================
# Target Result Box
# =========================================================

result_target_box = tk.Frame(
    target_frame,
    bg=WHITE,
    padx=30,
    pady=25
)

result_target_box.pack(
    fill="x",
    pady=20
)


tk.Label(
    result_target_box,
    text="GPA ที่ต้องได้ในรายวิชาที่เหลือ",
    font=("Arial", 15),
    bg=WHITE,
    fg=GRAY
).pack()


required_gpa_label = tk.Label(
    result_target_box,
    text="0.00",
    font=("Arial", 42, "bold"),
    bg=WHITE,
    fg=PURPLE
)

required_gpa_label.pack(
    pady=8
)


# =========================================================
# GPA สูงสุด
# =========================================================

maximum_gpa_label = tk.Label(
    result_target_box,
    text="ถ้าได้ A ทุกวิชา GPA สูงสุด = 0.00",
    font=("Arial", 13),
    bg=WHITE,
    fg=BLUE
)

maximum_gpa_label.pack(
    pady=(0, 8)
)


# =========================================================
# สถานะ
# =========================================================

target_status_label = tk.Label(
    result_target_box,
    text="กรอกข้อมูลแล้วกดคำนวณ",
    font=("Arial", 14, "bold"),
    bg=WHITE,
    fg=GRAY,
    justify="center"
)

target_status_label.pack()


# =========================================================
# หมายเหตุเรื่องการปัดเศษ
# =========================================================

tk.Label(
    result_target_box,
    text=(
        "หมายเหตุ: โปรแกรมคำนวณ GPA จริงและแสดงผล 2 ตำแหน่ง "
        "เช่น 3.995 จะปัดเป็น 4.00"
    ),
    font=("Arial", 10),
    bg=WHITE,
    fg=GRAY
).pack(
    pady=(15, 0)
)


# =========================================================
# PAGE 3 : รายวิชาและเกรด
# =========================================================

course_frame = tk.Frame(
    content,
    bg=LIGHT_PURPLE
)


tk.Label(
    course_frame,
    text="📚 รายวิชาและเกรด",
    font=("Arial", 26, "bold"),
    bg=LIGHT_PURPLE,
    fg=TEXT
).pack(
    anchor="w",
    pady=(0, 20)
)


course_box = tk.Frame(
    course_frame,
    bg=WHITE,
    padx=20,
    pady=20
)

course_box.pack(
    fill="both",
    expand=True
)


# =========================================================
# หัวตาราง
# =========================================================

headers = [
    "รหัสวิชา",
    "ชื่อรายวิชา",
    "หน่วยกิต",
    "เกรด"
]


for column, header_text in enumerate(headers):

    tk.Label(
        course_box,
        text=header_text,
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=TEXT
    ).grid(
        row=0,
        column=column,
        padx=10,
        pady=10
    )


# =========================================================
# สร้างแถวรายวิชา
# =========================================================

course_rows = []


for i in range(8):

    code = tk.Entry(
        course_box,
        width=15
    )

    name = tk.Entry(
        course_box,
        width=25
    )

    credit = tk.Entry(
        course_box,
        width=10
    )

    grade = ttk.Combobox(
        course_box,
        values=list(GRADE_POINTS.keys()),
        width=8,
        state="readonly"
    )

    grade.set("B+")

    code.grid(
        row=i + 1,
        column=0,
        padx=8,
        pady=5
    )

    name.grid(
        row=i + 1,
        column=1,
        padx=8,
        pady=5
    )

    credit.grid(
        row=i + 1,
        column=2,
        padx=8,
        pady=5
    )

    grade.grid(
        row=i + 1,
        column=3,
        padx=8,
        pady=5
    )

    course_rows.append({
        "code": code,
        "name": name,
        "credit": credit,
        "grade": grade
    })


# =========================================================
# ปุ่มคำนวณ GPA
# =========================================================

tk.Button(
    course_box,
    text="🧮 คำนวณ GPA",
    command=calculate_gpa_from_courses,
    font=("Arial", 12, "bold"),
    bg=PURPLE,
    fg=WHITE,
    relief="flat",
    padx=25,
    pady=8,
    cursor="hand2"
).grid(
    row=10,
    column=0,
    columnspan=4,
    pady=15
)


# =========================================================
# แสดง GPA ปัจจุบัน
# =========================================================

current_gpa_label = tk.Label(
    course_box,
    text="GPA = 0.00",
    font=("Arial", 20, "bold"),
    bg=WHITE,
    fg=PURPLE
)

current_gpa_label.grid(
    row=11,
    column=0,
    columnspan=2,
    pady=10
)


current_credit_label = tk.Label(
    course_box,
    text="หน่วยกิต = 0",
    font=("Arial", 20, "bold"),
    bg=WHITE,
    fg=BLUE
)

current_credit_label.grid(
    row=11,
    column=2,
    columnspan=2,
    pady=10
)


# =========================================================
# PAGE 4 : วางแผนการเรียน
# =========================================================

plan_frame = tk.Frame(
    content,
    bg=LIGHT_PURPLE
)


tk.Label(
    plan_frame,
    text="📊 วางแผนการเรียน",
    font=("Arial", 26, "bold"),
    bg=LIGHT_PURPLE,
    fg=TEXT
).pack(
    anchor="w",
    pady=(0, 20)
)


# =========================================================
# GPA เป้าหมาย
# =========================================================

plan_top = tk.Frame(
    plan_frame,
    bg=WHITE,
    padx=25,
    pady=20
)

plan_top.pack(
    fill="x"
)


tk.Label(
    plan_top,
    text="GPA เป้าหมาย",
    font=("Arial", 12),
    bg=WHITE,
    fg=TEXT
).pack(
    side="left"
)


plan_target_entry = tk.Entry(
    plan_top,
    width=15,
    font=("Arial", 12)
)

plan_target_entry.insert(
    0,
    "3.50"
)

plan_target_entry.pack(
    side="left",
    padx=20
)


# =========================================================
# Plan Box
# =========================================================

plan_box = tk.Frame(
    plan_frame,
    bg=WHITE,
    padx=20,
    pady=15
)

plan_box.pack(
    fill="both",
    expand=True,
    pady=20
)


# =========================================================
# หัวตาราง Plan
# =========================================================

tk.Label(
    plan_box,
    text="รายวิชา",
    font=("Arial", 11, "bold"),
    bg=WHITE
).grid(
    row=0,
    column=0,
    padx=20
)


tk.Label(
    plan_box,
    text="หน่วยกิต",
    font=("Arial", 11, "bold"),
    bg=WHITE
).grid(
    row=0,
    column=1,
    padx=20
)


tk.Label(
    plan_box,
    text="เกรดที่คาดว่าจะได้",
    font=("Arial", 11, "bold"),
    bg=WHITE
).grid(
    row=0,
    column=2,
    padx=20
)


# =========================================================
# สร้างรายวิชาในแผน
# =========================================================

plan_rows = []


for i in range(6):

    tk.Label(
        plan_box,
        text=f"วิชาที่ {i + 1}",
        bg=WHITE,
        font=("Arial", 11)
    ).grid(
        row=i + 1,
        column=0,
        pady=6
    )


    credit = tk.Entry(
        plan_box,
        width=12
    )

    credit.insert(
        0,
        "3"
    )

    credit.grid(
        row=i + 1,
        column=1
    )


    grade = ttk.Combobox(
        plan_box,
        values=list(GRADE_POINTS.keys()),
        width=12,
        state="readonly"
    )

    grade.set("B+")

    grade.grid(
        row=i + 1,
        column=2
    )


    plan_rows.append({
        "credit": credit,
        "grade": grade
    })


# =========================================================
# ปุ่มคำนวณแผน
# =========================================================

tk.Button(
    plan_box,
    text="📊 คำนวณ GPA จากแผน",
    command=calculate_plan,
    font=("Arial", 12, "bold"),
    bg=PURPLE,
    fg=WHITE,
    relief="flat",
    padx=25,
    pady=9,
    cursor="hand2"
).grid(
    row=8,
    column=0,
    columnspan=3,
    pady=15
)


# =========================================================
# ผล GPA จากแผน
# =========================================================

planned_gpa_label = tk.Label(
    plan_box,
    text="GPA จากแผน = 0.00",
    font=("Arial", 22, "bold"),
    bg=WHITE,
    fg=PURPLE
)

planned_gpa_label.grid(
    row=9,
    column=0,
    columnspan=3,
    pady=8
)


# =========================================================
# สถานะแผน
# =========================================================

plan_status_label = tk.Label(
    plan_box,
    text="",
    font=("Arial", 13, "bold"),
    bg=WHITE
)

plan_status_label.grid(
    row=10,
    column=0,
    columnspan=3
)


# =========================================================
# แสดง Dashboard เป็นหน้าแรก
# =========================================================

show_page(
    dashboard_frame
)


# =========================================================
# เริ่มโปรแกรม
# =========================================================

root.mainloop()
