hour = int(input("โปรดใส่จำนวนชั่วโมง   "))
minute = int(input("โปรดใส่จำนวนนาที   "))
if hour < 0 or minute < 0:
    print("โปรดใส่จำนวนที่ไม่ติดลบ")
else :
    total_hours = hour
    if minute < 1:
        total_hours + 1
    if total_hours <= 1:
        fee = 0
fee = (total_hours * 30)
print(fee)