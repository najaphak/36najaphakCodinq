print("โปรแกรมคำนวณคะแนนรวม\n")

point_math = int(input("คะแนนวิชาคณิตศาสตร์ "))
point_science = int(input("คะแนนวิชาวิทยาศาสตร์ "))
point_english = int(input("คะแนนวิชาภาษาอังกฤษ "))

total_point = ( point_math + point_science + point_english )
average_point = total_point / 3

print("ระดับคะแนนของคุณ = ", total_point)
print("คะแนนเฉลี่ยสามวิชา = ", average_point)
    
if average_point < 60 :
    print("ผลการเรียน = ควรปรับปรุง")
elif total_point < 79 :
    print("ผลการเรียน = ผ่าน")
else:
    print("ระดับคะแนน = ยอดเยี่ยม")

print("progrommer : najaphak phanthahom")