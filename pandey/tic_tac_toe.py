#### tic tac toe using tkinter
import tkinter
from tkinter import *
import tkinter.messagebox as tkmsg

root=Tk()

root.geometry("200x150")
root.title("Tic Tac Toe Game")

click=True

def checker(buttons):
    global click
    if buttons['text'] == ' ' and click == True:
        buttons['text'] = 'X'
        click = False
    elif buttons['text'] == ' ' and click ==False :
        buttons['text'] = 'O'
        click=True
        
    if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
         b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
         b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' or
         b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
         b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' or
         b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
         b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
         b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
         b7['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
        
        answer=tkinter.messagebox.askquestion('X wins !!!','Do you want to play again')
        tk.destroy()
        if answer=='yes': 
            start()
                     
    elif (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
          b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
          b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
          b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' or
          b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
          b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
          b7['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
        answer=tkinter.messagebox.askquestion('O wins !!!','Do you want to play again')
        tk.destroy()
        if answer=='yes': 
            start()
        
buttons=StringVar()

global b1,b2,b3,b4,b5,b6,b7,b8,b9

b1=Button(root,{'text':' ','bg':"grey",'height':'2','width':'7','bd':'5','command':lambda:checker(b1)})
b1.grid({'row':'0','column':'0'})
b2=Button(root,text=' ',bd=5,command=lambda:checker(b2) , bg="grey",height=2,width=7)
b2.grid(row=0,column=1)
b3=Button(root,text=' ',bd=5,command=lambda:checker(b3) , bg="grey",height=2,width=7)
b3.grid(row=0,column=2)
b4=Button(root,text=' ',bd=5,command=lambda:checker(b4) , bg="grey",height=2,width=7)
b4.grid(row=1,column=0)
b5=Button(root,text=' ',bd=5,command=lambda:checker(b5) , bg="grey",height=2,width=7)
b5.grid(row=1,column=1)
b6=Button(root,text=' ',bd=5,command=lambda:checker(b6) , bg="grey",height=2,width=7)
b6.grid(row=1,column=2)
b7=Button(root,text=' ',bd=5,command=lambda:checker(b7) , bg="grey",height=2,width=7)
b7.grid(row=2,column=0)
b8=Button(root,text=' ',bd=5,command=lambda:checker(b8) , bg="grey",height=2,width=7)
b8.grid(row=2,column=1)
b9=Button(root,text=' ',bd=5,command=lambda:checker(b9), bg="grey",height=2,width=7)
b9.grid(row=2,column=2)

root.mainloop()