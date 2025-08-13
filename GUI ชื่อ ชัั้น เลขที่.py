import tkinter as tk

def update_label():
    my_label.config(text="นาย จิรายุ ชัยปรีชา\nม.5/8\nเลขที่26",fg="red")
root= tk.Tk()
root.title("myGUI")

my_label = tk.Label(root,text="กดปุ่ม",fg="green")
my_label.pack()
my_button = tk.Button(root, text="click here", command=update_label)
my_button.pack()
root.mainloop()