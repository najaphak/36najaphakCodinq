start_n = int(input("เริ่มต้น "))
end_n = int(input("สิ้นสุด "))


for mae in range (start_n, end_n + 1):
    print("แม่", mae)
    
    for multiplier in range(1, 13):
        ans = mae * multiplier
        print(mae, "x",multiplier, "=",ans)