Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import Tk, Label, Button
>>> def greet():
	print("파이썬에 오신 것을 환영합니다. ")

	
>>> window = Tk()
>>> label = Label(window, text="간단한 GUI 프로그램!")
>>> label.pack()
>>> 
>>> greet_button = Button(window, text="환영합니다.", command=greet)
>>> greet_button.pack()
>>> close_button = Button(window, text="종료", command=window.quit)
>>> close_button.pack()
>>> window.mainloop()
