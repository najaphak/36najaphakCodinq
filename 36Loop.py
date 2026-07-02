import random

secret_number = random.randint(1, 100)
count = 0

print("สุ่มตัวเลขให้ทาย")

while True:
    guess = int(input("ลองทายตัวเลข "))
    count += 1

    if guess > secret_number:
        print("มากไป! ลองใหม่อีกครั้ง")
    elif guess < secret_number:
        print("น้อยไป! ลองใหม่อีกครั้ง")

    else:
        print("ถูกต้อง เลขคือ ", secret_number)
        print("ทายไปทั้งหมด ", count, " ครั้ง")
        break