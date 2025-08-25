import tkinter as tk

root = tk.Tk()
root.title("นับเวลาถอยหลัง")
root.geometry("500x500")

count = 10

label = tk.Label(root, text="", font=("Helvetica", 30))
label.pack(pady=20)

info_label = tk.Label(root, text="", font=("Helvetica", 12))
info_label.pack()

def countdown():
    global count
    if count > 0:
        label.config(text=str(count))
        count -= 1
        root.after(1000, countdown)  
    else:
        label.config(text="เสร็จแล้ว!")
        info = (
            "\nชื่อ - นามสกุล: จิรายุ ชัยปรีชา"
            "\nชื่อเล่น: ปูเล"
            "\nห้องเรียน: ม.5/8"
            "\nแผนการเรียน: เทคโนโลยี"
            "\nอยากเรียนคณะ: เทคโนโลยีสารสนเทศ สาขาวิศวกรรมศาสตร์"
        )
        info_label.config(text=info)

countdown()

root.mainloop()