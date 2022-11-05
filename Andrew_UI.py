import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def func_end():#function of the button
   win.quit()
   
def func_start():#function of the button
    win.quit()
def clears():
    for widget in win.winfo_children():
        widget.destroy()
def help():
   
    mn = Menu(win) 
    win.config(menu=mn) 
    file_menu = Menu(mn) 
    mn.add_checkbutton ( label ='Help', command = help_text ) 
    edit_menu = Menu(mn)
    #end menu stuff
    
    # A Label widget to show in toplevel
    #Label(begintext ="This is a new window").pack()
    #starts buttons
    #btn_altitude=Button(win,text="altitude", width=10,height=1)
    #btn_altitude.place(x=150,y=150)
    #btn_demo=Button(win,text="demo", width=10,height=1)
    #btn_demo.place(x=150,y=180)
    #btn_moveA=Button(win,text="movement a", width=10,height=1)
    #btn_moveA.place(x=220,y=150)
    #btn_moveB=Button(win,text="movement b", width=10,height=1)
    #btn_moveB.place(x=220,y=180)
    #btn_moveC=Button(win,text="movement c", width=10,height=1)
    #btn_moveC.place(x=220,y=210)
    #btn_moveD=Button(win,text="movement d", width=10,height=1)
    #btn_moveD.place(x=220,y=240)
    #btn_confirm=Button(win,text="Confirm", width=10,height=1)
    #btn_confirm.place(x=150,y=270)
    #btn_exit=Button(win,text="STOP", width=10,height=1)
    #btn_exit.place(x=220,y=270)
    def display_selection():
    # Get the selected value.
            selection = combo_aMove.get()
            messagebox.showinfo(message=f"The selected value is: {selection}",title="Selection")
    #first movement
    combo_aMove = ttk.Combobox(state="readonly",values=["Python", "C", "C++", "Java"])
    combo_aMove.place(x=50, y=50)
    button_aMove = ttk.Button(text="Confirm selection",command=display_selection)
    button_aMove.place(x=50, y=75)
    text_aMove=Label(win, text='Please select one of the movements for point a')
    text_aMove.place(x =50, y = 30 )
    #second movement
    def display_selection1():
    # Get the selected value.
            selection = combo_bMove.get()
            messagebox.showinfo(message=f"The selected value is: {selection}",title="Selection")
    combo_bMove = ttk.Combobox(state="readonly",values=["Python", "C", "C++", "Java"])
    combo_bMove.place(x=50, y=130)
    button_bMove = ttk.Button(text="Confirm selection",command=display_selection1)
    button_bMove.place(x=50, y=155)
    text_bMove=Label(win, text='Please select one of the movements for point a')
    text_bMove.place(x =50, y =110)
    #third movement
    def display_selection2():
    # Get the selected value.
            selection = combo_cMove.get()
            messagebox.showinfo(message=f"The selected value is: {selection}",title="Selection")
    combo_cMove = ttk.Combobox(state="readonly",values=["Python", "C", "C++", "Java"])
    combo_cMove.place(x=50, y=210)
    button_cMove = ttk.Button(text="Confirm selection",command=display_selection2)
    button_cMove.place(x=50, y=235)
    text_cMove = Label(win, text='Please select one of the movements for point a')
    text_cMove.place(x =50, y = 190 )
    #fourth movement
    def display_selection3():
    # Get the selected value.
            selection = combo_dMove.get()
            messagebox.showinfo(message=f"The selected value is: {selection}",title="Selection")
    combo_dMove = ttk.Combobox(state="readonly",values=["Python", "C", "C++", "Java"])
    combo_dMove.place(x=50, y=290)
    button_dMove = ttk.Button(text="Confirm selection",command=display_selection3)
    button_dMove.place(x=50, y=315)
    text_dMove=Label(win, text='Please select one of the movements for point a')
    text_dMove.place(x =50, y = 270)
    #point a to point b distance
    text_a_b_dist=Label(win, text='Please choose a distance in feet from point a to b')
    text_a_b_dist.place(x =50, y = 350)
    sc_a_bMove= Scale(win, from_=0, to=5,orient = HORIZONTAL) 
    #sc1.pack(anchor = CENTER) 
    #sc1.grid(row=1, column = 0)
    sc_a_bMove.place(x = 50, y = 365)
    #point b to point c distance
    text_b_c_dist=Label(win, text='Please choose a distance in feet from point b to c')
    text_b_c_dist.place(x =50, y = 405)
    sc_b_cMove= Scale(win, from_=0, to=5,orient = HORIZONTAL) 
    #sc1.pack(anchor = CENTER) 
    #sc1.grid(row=1, column = 0)
    sc_b_cMove.place(x = 50, y = 420)
    #point c to point d distance
    text_c_d_dist=Label(win, text='Please choose a distance in feet from point c to d')
    text_c_d_dist.place(x =50, y = 460)
    sc_c_dMove= Scale(win, from_=0, to=5,orient = HORIZONTAL) 
    #sc1.pack(anchor = CENTER) 
    #sc1.grid(row=1, column = 0)
    sc_c_dMove.place(x = 50, y = 475)
    #point d to a distance
    text_d_a_dist=Label(win, text='Please choose a distance in feet from point a to b')
    text_d_a_dist.place(x =50, y = 515)
    sc_d_aMove= Scale(win, from_=0, to=5,orient = HORIZONTAL) 
    #sc1.pack(anchor = CENTER) 
    #sc1.grid(row=1, column = 0)
    sc_d_aMove.place(x = 50, y = 535)
    #altitude
    text_altitude=Label(win, text='Please choose an altitude')
    text_altitude.place(x =500, y = 30)
    sc_altitude= Scale(win, from_=0, to=5,orient = HORIZONTAL) 
    #sc1.pack(anchor = CENTER) 
    #sc1.grid(row=1, column = 0)
    sc_altitude.place(x = 500, y = 45)
    #demo button
    demo_selection = ''
    def display_selection4():
    # Get the selected value.
            selection = combo_demo.get()
            demo_selection = str(combo_demo.get())
            messagebox.showinfo(message=f"The selected value is: {selection}",title="Selection")
    combo_demo = ttk.Combobox(state="readonly",values=["Movement A", "Movement B", "Movement C", "Movement D"])
    combo_demo.place(x=500, y=110)
    button_demo = ttk.Button(text="DEMO",command=display_selection4)
    button_demo.place(x=500, y=135)
    text_demo=Label(win, text='Please select one of the movements for point a')
    text_demo.place(x =500, y = 90)
    print("dumb cunt " + demo_selection)
    #point a to point b distance




    #text_demo=Label(win, text='')
    #text_demo.place(x =500, y = 85)
    #sc_demo= Scale(win, from_=0, to=5,orient = HORIZONTAL) 
    #sc1.pack(anchor = CENTER) 
    #sc1.grid(row=1, column = 0)
    #sc_demo.place(x = 500, y = 110)
    #button_demo = ttk.Button(text="DEMO")
    #button_demo.place(x=500, y=110)# 110 for beneath other one
    
    
win=Tk() #creating the main window and storing the window object in 'win'
#win.attributes('-fullscreen',True)

win.title('Welcome') #setting title of the window
#win.geometry('500x200') #setting the size of the window
win.state('zoomed')
txt= Text(win) 
txt.tag_configure("tag_name", justify='center')

txt.pack() 
txt.configure(font=("Times New Roman", 20, "italic"))
txt.insert(INSERT,"Hello!")
txt.insert(END, 'PythonGeeks\nOne stop for building your Python skills\n')
txt.configure(state = 'disabled')

btn_start=Button(win,text="end", width = 50,height=5,command=func_end)
btn_start.place(x=400,y=700)
btn_start=Button(win,text="start", width=50,height=5,command=lambda:[clears(),help()])
btn_start.place(x=800,y=700) #middle middle

def help_text():
    rules = Toplevel(win)
    rules.title("Hope this helps")
    rules.geometry("500x500")
    rules.state('zoomed')
    txt= Text(rules) 
    txt.tag_configure("tag_name", justify='center')
    txt.pack() 
    txt.configure(font=("Times New Roman", 20, "italic"))
    txt.insert(INSERT,"Hello!")
    txt.insert(END, 'PythonGeeks\nOne stop for building your Python skills\n')
    txt.configure(state = 'disabled')
    #buttons


win.mainloop()
