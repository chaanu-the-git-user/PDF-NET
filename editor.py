from customtkinter import *
from tkinter import *
from tkinter import messagebox as msgb
from win32api import GetSystemMetrics as GSM


def confirm_close():
   ans = msgb.askyesno(title="close", message="are you sure you want to close?", icon="warning")
   if ans:
    mainwindow.destroy()
mainwindow = CTk()
editor = Text(height=GSM(0), width=GSM(1))
editor.pack()
mainwindow.protocol('WM_DELETE_WINDOW', confirm_close)
mainwindow.title('PDF-NET')
mainwindow.mainloop()