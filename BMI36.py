print("คำนวณค่าbmiและแปลผลสุขภาพ")

bmi_weight = float(input("น้ำหนักของคุณ: " ))
bmi_height = float(input("ส่วนสูงของคุณ: " ))

total_bmi = bmi_weight / ( bmi_height /100)** 2 

print("คำนวณผลbmi = ", total_bmi)
print("ผลสุขภาพ = ", total_bmi)

if total_bmi < 18.5 :
    print("ผลของคุณ : น้ำหนักน้อย ")
elif total_bmi <= 22.9 :
    print("ผลของคุณ : ปกติ ")
else :
    print("ผลของคุณ : อ้วน ")
