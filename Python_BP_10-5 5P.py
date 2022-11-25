Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> fields = '이름', '직업', '국적'
>>> 
>>> def fetch(entries):
	for entry in entries:
		field = entry[0]
		text = entry[1].get()
		print('%s: "%s"' %(field, text))

		
>>> def makeform(root, fields):
	entries = []
	for field in fields:
		row = Frame(root)
		lab = Label(row, width=15, text=field)
		ent = Entry(row)
		row.pack(side=TOP, fill=X)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		entries.append((field, ent))
	return entries

>>> root = Tk()
>>> ents = makeform(root, fields)
>>> root.bind('<Return>', (lambda event, e=ents: fetch(e)))
'54772744<lambda>'
>>> b1 = button(root, text='보여주기', command=(lambda e=ents: fetch(e)))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    b1 = button(root, text='보여주기', command=(lambda e=ents: fetch(e)))
NameError: name 'button' is not defined
>>> b1 = Button(root, text='보여주기', command=(lambda e=ents: fetch(e)))
>>> b1.pack(side=LEFT, padx=5, pady=5)
>>> b2 = Button(root, text='종료하기', command=root.quit)
>>> b2.pack(side=LEFT, padx=5, pady=5)
>>> root.mainloop()
이름: "이승주"
직업: ""
국적: ""
이름: "이승주"
직업: "학생"
국적: ""
이름: "이승주"
직업: "학생"
국적: "한국"
