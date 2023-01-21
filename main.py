import tkinter
from tkinter import *
import requests

# Настройка окна приложения
window = Tk()
window.title("MADNESS sender")
window.geometry('200x225')
window['bg'] = 'black'
window.resizable(True, True)


# Функция отправки сообщения
def send_telegram():
    TOKEN = token.get()
    ID = chatID.get()
    message = entry.get()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={message}"
    print(requests.get(url).json())


# Поле ввода токена
txt1 = Label(text="Введите токен бота", background='green', font='Times 10').pack(padx=6, pady=6)
token = tkinter.Entry(width=35)
token.pack(anchor=NW, padx=6, pady=6)

# Поле ввода id получателя
txt2 = Label(text="Введите ID пользователя", background='green', font='Times 10').pack(padx=6, pady=6)
chatID = tkinter.Entry(width=35)
chatID.pack(anchor=NW, padx=6, pady=6)

# Поле ввода сообщения
txt3 = Label(text="Введите сообщение", background='green', font='Times 10').pack(padx=6, pady=6)
entry = tkinter.Entry(width=35)
entry.pack(anchor=NW, padx=6, pady=6)

# Кнопка отправки сообщения
btn = tkinter.Button(text="Отправить", command=send_telegram, background='red', font='Times 10').pack(padx=6, pady=6)

window.mainloop()
window = tkinter.Tk()
