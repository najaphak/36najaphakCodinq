score1 = int(input("คะแนนวิชาที่ 1: "))
score2 = int(input("คะแนนวิชาที่ 2: "))
score3 = int(input("คะแนนวิชาที่ 3: "))
             
total_score = (score1 + score2 + score3)

if total_score < 60:
    print("ระดับคะแนน  ควรปรับปรุง")
elif total_score < 79 :
    print("ระดับระแนน = ผ่าน")
else:
    print("ระดับคะแนน = ดีเยี่ยม")

    print("ระดับคะแนนของคุณ = ", total_score)
    print("คะแนนเฉลี่ย 3 วิชา = ", total_score / 3)
