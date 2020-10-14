#pip install googletrans
from googletrans import Translator
from tkinter import *

root=Tk()
root.title("Translator")

inputwords=Entry(root,borderwidth=6)
inputwords.grid(row=0,column=0,columnspan=3,padx=10,pady=10) #input for the translation
outputwords=Entry(root,borderwidth=6)
outputwords.grid(row=1,column=0,columnspan=3,padx=10,pady=10) #output for the translation

language_one=StringVar()
language_one.set("English")

language_two=StringVar()
language_two.set("Spanish")

firstlist = OptionMenu(root,language_one,"English","French","Spanish","Italian","German","Russian","Romanian","Norwegian","Polish","Hungarian","Croatian","Bosnian","Japanese","Chinse","Korean","Hindi","Estonian","Swedish","Finnish","Tagalog","Czech","Bulgarian","Dutch","Icelandic","Stupid","Microwave")
firstlist.grid(row=0,column=3) #first list of languages (for the input)

secondlist = OptionMenu(root,language_two,"English","French","Spanish","Italian","German","Russian","Romanian","Norwegian","Polish","Hungarian","Croatian","Bosnian","Japanese","Chinse","Korean","Hindi","Estonian","Swedish","Finnish","Tagalog","Czech","Bulgarian","Dutch","Icelandic","Stupid","Microwave")
secondlist.grid(row=1,column=3) #second list of languages (for the output)

def convert(): #converts input into another language, then outputs it
	global outputwords
	trans = Translator()
	one=language_one.get()
	two=language_two.get()
	outputwords.delete(0,END)
	if two=="Microwave":
		outputwords.insert(0,"m"*len(inputwords.get()))
	if two=="Stupid":
		charnum=0
		for char in inputwords.get():
			print(charnum%2)
			if charnum%2==0:
				outputwords.insert(len(outputwords.get()),char.upper())
			else:
				outputwords.insert(len(outputwords.get()),char.lower())
			charnum+=1
			print(charnum)
	if not two=="Microwave" and not two=="Stupid":
		t=trans.translate(inputwords.get(), src=language_one.get(), dest=language_two.get())
		outputwords.insert(0,t.text)

def clear():
	global inputwords
	global outputwords
	inputwords.delete(0,END)
	outputwords.delete(0,END)

def leave():
	root.destroy()

clear=Button(root,text="Clear",command=clear)
clear.grid(row=2,column=2)
button=Button(root,text="Convert!",command=convert)
button.grid(row=2,column=1)
leave=Button(root,text="Exit Window",command=leave)
leave.grid(row=2,column=3)

root.mainloop()