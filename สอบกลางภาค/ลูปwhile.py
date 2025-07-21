i = 0
while i <= 100:
    print(i)
    i+=1
    
i = 1000
while i >= 0:
    print(i)
    i-=1

min_num = None
while True:
    try:
        num = float(input("ใส่จำนวนจริงบวก  "))
        if num <= 0:
            break
        if min_num is None or num < min_num:
    except:
        break
    if min_num is not None:
        print("จำนวนที่น้อยที่สุด =")
    else:
        print("ไม่มีข้อมูลจำนวนจริงบวก")