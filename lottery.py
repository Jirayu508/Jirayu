import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

    #���ͧ�ҡ BeautifulSoup �� pip ��� error ����������Թ����� Interpreter �ջѭ��㹡����Ŵ ���������¹�� Selenium ᷹

        #***  ��͹ Run Code ��س���� command ���� cmd ���� Terminal � VSC ���� -> ""pip install selenium""  ***
        #�͡����Ԫ���Ҥ�Ѻ :)

def get_lottery_results():
    url = "https://www.lottery.co.th/small"
    results = {}
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get(url)
        time.sleep(3)  # ����� JS ��Ŵ����

        numbers = [el.text for el in driver.find_elements(By.TAG_NAME, "strong")]

        driver.quit()

        if len(numbers) >= 4:
            results["�ҧ��ŷ�� 1"] = numbers[1]
            results["�Ţ���� 2 ���"] = numbers[3]
            results["�Ţ˹�� 3 ���"] = str(numbers[5] + " " + numbers[6])
            results["�Ţ���� 3 ���"] = str(numbers[8] + " " + numbers[9])
        else:
            results["Error"] = "��辺�����Ťú��ǹ"

        return results

    except Exception as e:
        messagebox.showerror("Error", f"�������ö�֧��������\n{e}")
        return {}


def show_results():
    text_box.delete("1.0", tk.END)
    results = get_lottery_results()
    if results:
        for k, v in results.items():
            text_box.insert(tk.END, f"{k} : {v}\n\n")
    else:
        text_box.insert(tk.END, "����բ�����")


root = tk.Tk()
root.title("����ҡ�Թ���Ѱ���")
root.geometry("560x560")

frame = ttk.Frame(root, padding=20)
frame.pack(fill="x", expand=True)

label = ttk.Label(frame, text="����ҡ�Թ���Ѱ���", font=("Kanit", 32, "bold"))
label.pack(pady=10)

text_frame = ttk.Frame(frame)
text_frame.pack(fill="x", expand=True, pady=10)

scrollbar = ttk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

text_box = tk.Text(text_frame, width=30, height=10, font=("Consolas", 18), yscrollcommand=scrollbar.set)
text_box.pack(side="top", anchor="center", fill="both", expand=True)
scrollbar.config(command=text_box.yview)

button = ttk.Button(frame, text="�֧������ش", command=show_results)
button.pack(ipady=20, pady=10,side="top", anchor="center", fill="both")

root.mainloop()
