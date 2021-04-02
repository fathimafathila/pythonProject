from tkinter import *
import tkinter.messagebox
import tkinter as tk

root=Tk()
var1=StringVar()
var2=StringVar()
file_data=open("register_file.txt",'a')
file_data.close()
root.title('Student Record')
def register_student():
    if var1.get() !="" or var2.get() != "":
        val1=var1.get() + ":" + var2.get() + "\n"
        file_data=open("register_file.txt",'a')
        file_data.write(val1)
        file_data.close()
    var1.set("")
    var2.set("")

def fetch_display_from_file():

    file_data = open("register_file.txt", 'r')
    data=file_data.readlines()
    file_data.close()
    value1 = []
    value2 = []
    display_data = "%30s%30s\n" % ("First Name", "Last Name")
    if len(data) != 0:
        for c in data:
            c1=c.strip()
            value2=c1.split(":")
            display_data += "%30s%30s\n" % (value2[0],value2[1])
            value2=[]
        root2 = tk.Tk()
        root2.title('Student Information')
        display = Text(root2, padx=5, pady=5, spacing1=1, spacing3=1)
        scroll_v = Scrollbar(root2, orient="vertical")
        scroll_v.pack(side=RIGHT, fill=Y)
        display["yscrollcommand"] = scroll_v
        display.insert(END,display_data)
        display.pack()
        scroll_v.config(command=display.yview)
        display.pack(side=LEFT, fill=BOTH)
        root2.mainloop()
    else:
        tkinter.messagebox.showinfo('No Data in File',message='There is no student registered in the program')

label1=Label(root,text="First Name",font=('ariel', 12, 'bold')).grid(row=0,column=0,padx=25)
label2=Label(root,text="Last Name",font=('ariel', 12, 'bold')).grid(row=1,column=0,padx=25)
text1=Entry(root,textvariable=var1).grid(row=0,column=1 ,padx=25)
text2=Entry(root,textvariable=var2).grid(row=1,column=1 ,padx=25)
button1=Button(root,text="Get Student Information", bg="aqua", fg="red",command=register_student).grid(row=2,column=0)
button2=Button(root,text="Display Student Information", bg="aqua", fg="red",command=fetch_display_from_file).grid(row=2,column=1)




root.mainloop()
