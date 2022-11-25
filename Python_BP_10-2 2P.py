Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import Tk, Labl, Button, Entry, IntVar, END, W, E
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from tkinter import Tk, Labl, Button, Entry, IntVar, END, W, E
ImportError: cannot import name 'Labl'
>>> from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
>>> def update_add():
	update("add")

	
>>> def update_subtract():
	update("subtract")

	
>>> def update_reset():
	update("reset")

	
>>> window = Tk()
>>> total = 0
>>> sum = Label(window)
>>> sum.grid(row=0, column=1, columnspan=2)
>>> label = Label(window, text="현재 합계:")
>>> label.grid(row=0, column=0)
>>> 
>>> entry = Entry(window)
>>> entry.grid(row=1, column=0, columnspan=3)
>>> 
>>> add_button = Button(window, text="더하기(+)", command=update_add)
>>> subtract_button = Button(window, text="빼기(-)", command=update_subtract)
>>> reset_button = Button(window, text="초기화", command=update_reset)
>>> 
>>> add_button.grid(row=2, column=0)
>>> subtract_button.grid(row=2, column=1)
>>> reset_button.grid(row=2, column=2)
>>> 
>>> def update(method):
	global total
	if method == "add":
		total += int(entry.get())
	elif method == "subtract":
		total -= int(entry.get())
	else:
		total = 0
	sum['text'] = str(total)
	entry.delete(0, END)

	
>>> window.mainloop()
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\Datasolution\KoreaPlus Statistics\Statistics\26\Python3\lib\tkinter\__init__.py", line 1533, in __call__
    return self.func(*args)
  File "<pyshell#4>", line 2, in update_add
  File "<pyshell#40>", line 4, in update
ValueError: invalid literal for int() with base 10: ''
