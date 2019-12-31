# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:57:21 2019

@author: ashwa
"""

from  googletrans import Translator
import pandas as pd
from tkinter import *
import numpy as np


#Language codes
languages=pd.read_csv("language-codes_csv.csv")


def language_translator():
    global e1,e2
    try:
        translator=Translator()
        #Text to Translate
        user_input=str(e1.get())
        
        #Destination translated language code
        dest_language=str(e2.get())
        
        if(len(user_input)<10000):
            #passing the original text to detection function,to check the orginal language
            detected = translator.detect(user_input)
            #passing the text to translator function, to translate the given text
            translated = translator.translate(user_input,dest=dest_language)
            Label(root,width=60,height=5, text = ("Source Language Code = {}".format(detected.lang)), bd = '5').place(relx = 0.5, rely = 0.51, anchor = CENTER)
            Label(root,width=60,height=5, text = (translated.text), bd = '5', bg="black", fg="white").place(relx = 0.5, rely = 0.31, anchor = CENTER)
            
        else:
            translations = translator.translate([user_input[:int(len(user_input)/2)],user_input[int(len(user_input)/2):]], dest=dest_language)
            for translated in translations:
                print(translated.text)
                Label(root,width=60,height=5, text = (translated.text), bd = '5', bg="black", fg="white").place(relx = 0.4, rely = 0.31, anchor = CENTER)
                
    except:
        Label(root,width=60,height=5, text = "Connection Error OR Wrong Input!", bd = '5', bg="black", fg="white").place(relx = 0.4, rely = 0.31, anchor = CENTER)
    




def codes():
    new=Tk()
    new.geometry("1300x1000")
    new.title("Languages and Codes")
    new.config(bg="#D9FA91")
    n,m,p,a,b,c,d=0,0,0,0,0,0,0
    for i in languages[1:27].values:
        Label(new,text=(i[1],"->"),bg="#D9FA91").grid(row=n)#,bg="blue",fg="white",width=15
        Button(new,text=(i[0]),bg="black",fg="white",height=1,width=1).grid(row=n,column=1)
        n+=1
    for i in languages[27:53].values:
        Label(new,text=(i[1],"->"),bg="#D9FA91").grid(row=m,column=2)
        Button(new,text=(i[0]),bg="black",fg="white",height=1,width=1).grid(row=m,column=3)
        m+=1
    for i in languages[53:80].values:
        Label(new,text=(i[1],"->"),bg="#D9FA91").grid(row=p,column=4)
        Button(new,text=(i[0]),bg="black",fg="white",height=1,width=1).grid(row=p,column=5)
        p+=1
    for i in languages[80:107].values:
        Label(new,text=(i[1],"->"),bg="#D9FA91").grid(row=a,column=6)
        Button(new,text=(i[0]),bg="black",fg="white",height=1,width=1).grid(row=a,column=7)
        a+=1
    for i in languages[107:134].values:
        Label(new,text=(i[1],"->"),bg="#D9FA91").grid(row=b,column=8)
        Button(new,text=(i[0]),bg="black",fg="white",height=1,width=1).grid(row=b,column=9)
        b+=1
    for i in languages[134:160].values:
        Label(new,text=(i[1],"->"),bg="#D9FA91").grid(row=c,column=10)
        Button(new,text=(i[0]),bg="black",fg="white",height=1,width=1).grid(row=c,column=11)
        c+=1
    for i in languages[160:].values:
        Label(new,text=(i[1],"->"),bg="#D9FA91").grid(row=d,column=12)
        Button(new,text=(i[0]),bg="black",fg="white",height=1,width=1).grid(row=d,column=13)
        d+=1
    new.mainloop()
    
    
    
    
    
def report():
    with open("Report_Translator.txt","r") as file:
        text1=file.readlines()
        print(text1)
    rpt=Tk()
    rpt.geometry("1200x700")
    rpt.title("Report")
    rpt.config(bg="#D9FA91")
    scrollbar = Scrollbar(rpt)
    scrollbar. pack( side = RIGHT, fill=Y )
    mylist=Listbox(rpt, yscrollcommand = scrollbar.set)
    for line in text1:  
        mylist.insert(END,line)  
    mylist.pack( fill = BOTH ,expand=True)
    scrollbar.config( command = mylist.yview )
    rpt.mainloop()
        


def User_Manual():
    pass    
    





def save():
    global e1,e2
    try:
        translator=Translator()
        text=str(e1.get())
        dest=str(e2.get())
        detected = translator.detect(text)
        source=detected.lang
        translated = translator.translate(text,dest=dest)
        translated=translated.text
        list1=[text,source,dest,translated]
        df=np.array(list1).reshape(1,4)
        df=pd.DataFrame(df,columns=['Text','Source','Destination','Translated'])
        df.to_csv("Translated Text")
        Label(root,width=60,height=5, text = "Successfully Saved", bd = '5', bg="black", fg="white").place(relx = 0.5, rely = 0.31, anchor = CENTER)
    except:
        Label(root,width=60,height=5, text = "Saving Failedm", bd = '5', bg="black", fg="white").place(relx = 0.5, rely = 0.31, anchor = CENTER)






def reset():
    try:
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        Label(root,width=60,height=5, text = "", bd = '5').place(relx = 0.5, rely = 0.51, anchor = CENTER)
        Label(root,width=60,height=5, text = "", bd = '5', bg="black", fg="white").place(relx = 0.5, rely = 0.31, anchor = CENTER)
    except:
        Label(root,width=60,height=5, text = "Error Reseting the Input or Result", bd = '5', bg="black", fg="white").place(relx = 0.5, rely = 0.31, anchor = CENTER)



#TK window
        
root=Tk()
root.geometry("800x500")
root.title("Language Translator")
root.configure(bg='#ebedeb')
menu = Menu(root)                
root.config(menu=menu)               

#Adding first label and entry
Label(root, text='Enter the Text to translate : ',bd='5',bg="#ebedeb").place(relx = 0.1, rely = 0.05, anchor = CENTER) 
e1 = Entry(root) 
e1.place(relx = 0.3, rely = 0.05, anchor = CENTER) 

#Adding second label and entry
Label(root, text='Destination Language Code : ',bd='5',bg="#ebedeb").place(relx = 0.1, rely = 0.09, anchor = CENTER) 
e2 = Entry(root)
e2.place(relx = 0.3, rely = 0.09, anchor = CENTER) 

#Adding button to translate the text
b1=Button(root, text = 'Translate', bd = '5',command=language_translator, fg="red",height=2,width=15)
b1.place(relx = 0.5, rely = 0.069, anchor = CENTER)

#Adding the button to check codes
b2=Button(root, text = 'Click To see Language Codes', bd = '5',command=codes, fg="red",height=2,width=25)
b2.place(relx = 0.8, rely = 0.069, anchor = CENTER)

#Adding the file menu
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='Reset',command=reset) 
filemenu.add_command(label='Save Results',command=save) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.destroy) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='Report',command=report)
helpmenu.add_command(label='User Manual',command=User_Manual)

 
root.mainloop()

