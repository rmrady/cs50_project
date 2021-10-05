from tkinter import*
from tkinter import messagebox
import math
#saat azafe karee~~~~~~~~~~~~~~~~~~~~~~
def func1(d):
    global azf
    lbl=Label(d,
              text="...................",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="green")
    lbl.grid(row=0,column=2)

    saat= int(azafekary.get())
    azf=math.trunc(saat*1.4*1620620)
    azff="{:,}".format(azf)
    print(azff)
    lbl['text']=azff

#holiday~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def func2(e):
    global ho
    lbl1=Label(e,
              text="...................",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="green" )
    lbl1.grid(row=1,column=2)

    h= int(holiday.get())
    
    ho=math.trunc(h*0.4*1690620)
    hoo="{:,}".format(ho)
    print(hoo)
    lbl1['text']=hoo
#shab_kary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def func3(o):
    global shab_kary,sh
    lbl2=Label(o,
              text="...................",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="green" )
    lbl2.grid(row=2,column=2)
    s= int(shab_kary.get())
    
    sh=math.trunc(s*0.35*1690620)
    shh="{:,}".format(sh)
    print(shh)
    lbl2['text']=shh
#hagh bema~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def func5(m):
    global bema,pai ,bon
    lbl3=Label(m,
              text="...................",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="green" )
    lbl3.grid(row=3,column=2)

    pai= int(paih_hoghogh.get())
    bon=600000
    bema=math.trunc((pai+bon)*(0.30))
    bemaa="{:,}".format(bema)
    print(bemaa)
    lbl3['text']=bemaa
#result~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def func6(w):
    global olad,ho_kl , result,ko ,ghst
    lbl4=Label(w,
              text=".................................",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="white" )
    lbl4.grid(row=4,column=2)

    ko= int(kosorat.get())
    ghst=int(ghaste_mahane.get())
    tada= int(olad.get())
    olad1=math.trunc (tada * 2655490)
    
    maskan=450000
    sanavad=140000
    ho_kl=math.trunc(pai+maskan+bon+sanavad+sh+ho+azf+olad1)
    result= math.trunc(ho_kl - bema - ko - ghst)
    result1="{:,}".format(result)
    print(result1)
    lbl4['text']=result1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
def ask_quest():
    messagebox.askquestion("ask question ","Do you want exit??" )

def tx():
    global text 
    with open("te.txt")as f:
        data=f.read()
    text.insert(INSERT,data)
        

def help1():
    global text
    winh = Toplevel()
    winh.title("* help *")
    winh.geometry("570x520+500+100")
    text=Text(winh,fg="blue", font=("tohoma",15,"bold") )
    text.grid(row=2,column=1 )
    b=Button(winh,text="help",command=tx)
    b.grid(row=1,column=0)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def func11(str1):
    li= str1.split(",")
    return li

def prsnl(w):
    global kod
    fi= Label(w,
         width=20,
          fg="green",
          font=("tohoma",10,"bold"))
    fi.grid(row=2,column=0)

    ls= Label(w,
         width=20,
          fg="green",
          font=("tohoma",10,"bold"))
    ls.grid(row=3,column=0)

    sh= Label(w,
         width=20,
          fg="green",
          font=("tohoma",10,"bold"))
    sh.grid(row=4,column=0)

    tm= Label(w,
         width=23,
          fg="green",
          font=("tohoma",10,"bold"))
    tm.grid(row=5,column=0)

    lis=[]
    f=open("ss.txt",mode = 'r')
    for i in f:
        lis.append(func11(i))
   
    pp=(kod.get())
    for j in lis:
        if j [0]== pp:
           fi["text"]=j[1]
           ls["text"]=j[2]
           sh["text"]=j[3]
           tm["text"]=j[4]

    f.close()
#~~~~~~~~~~~~~
def save1():
    global kod ,first_name,last_name,how,tamas
    
    for i in range(10):
        f1=(kod.get())
        l=(first_name .get())
        n=(last_name .get())
        h=(how.get())
        t=(tamas.get())

    
    sum1=f1 +','+l +','+ n +','+ h +',' +t
        
    f=open("ss.txt", mode="a+",encoding="utf-8")
    f.write(sum1)
    f.write("\n")
##    messagebox.showinfo("save","save shod")
    f.close()
    
    



#safe44444444444444444444444444444444444444444444444444444444444444444
def win_4():
    win4 = Toplevel()
    win4.title("* emolument: 4*")
    win4.geometry("550x450+500+100")
    win4.configure(bg="gray")
    win4.iconbitmap("7.ico")
    frame1=Frame(win4,bg="white",)
    frame1.pack(fill="both",expand= True)
    frame2=Frame(win4,bg="black",)
    frame2.pack(fill="both",expand= True)
    khorog=Menu(win4)
    khorog.add_command(label="exit",command=ask_quest)
    khorog.add_command(label="exposition",command= help1)
    win4.config(menu=khorog)
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    lbl=Label(frame1,
              text="* محاسبات کل *",
              width=20,
              height=3,
              font=("tohoma",15,"bold"),
              bg="white",
              fg="green")
    lbl.pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    bt_azfe_kary= Button(frame2,
              text="اضافه کاري ",
              width=10,
              height=1,
              font=("tohoma",11,"bold"),
              bg="green",
              fg="white",
              #relife="ralsed",
              anchor="e",
              command=lambda:func1(frame2))

    bt_azfe_kary.grid(row=0,column=4)

    bt_holiday = Button(frame2,
              text="تعطيل کاري",
              width=10,
              height=1,
              anchor="e",
              font=("tohoma",11,"bold"),
              bg="green",
              fg="white",
              command=lambda:func2(frame2))

    bt_holiday.grid(row=1,column=4)


    bt_shab_kary = Button(frame2,
              text="شب کاري",
              width=10,
              height=1,
              font=("tohoma",11,"bold"),
              anchor="e",

              bg="green",
              fg="white",
              command=lambda:func3(frame2))

    bt_shab_kary.grid(row=2,column=4)


    bt_bema= Button(frame2,
              text="بيمه",
              width=10,
              height=1,
              anchor="e",
     
              font=("tohoma",11,"bold"),
              bg="green",
              fg="white",
              command=lambda:func5(frame2))

    bt_bema.grid(row=3,column=4)


    bt_kle_hoghogh= Button(frame2,
              text="کل حقوق دريافتي ",
              width=21,
              height=1,
              anchor="e",
        
              font=("tohoma",13,"bold"),
              bg="green",
              fg="white",
              command=lambda:func6(frame2))

    bt_kle_hoghogh.grid(row=4,column=4)

    lbl=Label(frame2,
              text="...................",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="green")
    lbl.grid(row=0,column=2)

    lbl1=Label(frame2,
              text="...................",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="green")
    lbl1.grid(row=1,column=2)

    lbl2=Label(frame2,
              text="...................",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="green")
    lbl2.grid(row=2,column=2)


    lbl3=Label(frame2,
              text="...................",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="green")
    lbl3.grid(row=3,column=2)

    
    lbl4=Label(frame2,
              text="...................",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="green")
    lbl4.grid(row=4,column=2)
 
    
#safe 3 333333333333333333333333333333333333333333333333333333333333333333333

def win_3():
    global paih_hoghogh,ghaste_mahane,kosorat,azafat
    
    win3 = Toplevel()
    win3.title("* emolument: 3*")
    win3.geometry("550x450+500+100")
    win3.configure(bg="gray")
    win3.iconbitmap("7.ico")
    frame1=Frame(win3,bg="white",)
    frame1.pack(fill="both",expand= True)
    frame2=Frame(win3,bg="black",)
    frame2.pack(fill="both",expand= True)


    lbl=Label(frame1,
              text="* اطلاعات حقوق *",
              width=20,
              height=3,
              font=("tohoma",15,"bold"),
              bg="white",
              fg="green")
    lbl.pack()



    
    lbl=Label(frame2,
          text=":پايه حقوق",
          width=20,
          height=3,
          font=("tohoma",12,"bold"),
          anchor="e",
          bg="black",
          fg="white")
    lbl.grid(row=3,column=4)

    lbl1=Label(frame2,
              text=":قسط ماهانه ",
              width=20,
              height=3,
              anchor="e",

              font=("tohoma",12,"bold"),
              bg="black",
              fg="white" )
    lbl1.grid(row=4,column=4)

    lbl2=Label(frame2,
              text=":کسورات",
              width=20,
              height=3,
              anchor="e",
              font=("tohoma",12,"bold"),
              bg="black",
              fg="white" )
    lbl2.grid(row=5,column=4)

    lb3=Label(frame2,
              text=" : اضافات ",
              width=20,
              height=3,
              anchor="e",

              font=("tohoma",12,"bold"),
              bg="black",
              fg="white" )
    lb3.grid(row=6,column=4)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    paih_hoghogh= Entry(frame2,
             width=20,
             fg="green",
             font=("tohoma",12,"bold"))
    paih_hoghogh.grid(row=3,column=3)

    ghaste_mahane= Entry(frame2,
             width=20,
             fg="green",
             font=("tohoma",12,"bold"))
    ghaste_mahane.grid(row=4,column=3)


    kosorat= Entry(frame2,
             width=20,
             fg="green",
             font=("tohoma",12,"bold"))
    kosorat.grid(row=5,column=3)

    azafat= Entry(frame2,
             width=20,
             fg="green",
             font=("tohoma",12,"bold"))
    azafat.grid(row=6,column=3)
    
    bt4=Button(frame2,
         text="<<<<",
         bg="green", 
         font=("tohoma",12,"bold"),
         command=win_4)
    bt4.grid(row=15,column=4,padx=5,pady=10)

    bt5=Button(frame2,
         text=">>>> ",
         bg="green",
         font=("tohoma",12,"bold"),
         command=win_2)
    bt5.grid(row=15,column=2,padx=5,pady=10)





#safe 222222222222222222222222222222222222222222222222222222222222222222
def win_2():
    global roz_kary
    global shab_kary
    global azafekary
    global holiday ,olad
    win2 = Toplevel()
    win2.title("* emolument: 2*")
    win2.geometry("550x450+500+100")
    win2.configure(bg="gray")
    win2.iconbitmap("7.ico")
    frame1=Frame(win2,bg="white",)
    frame1.pack(fill="both",expand= True)
    frame2=Frame(win2,bg="black",)
    frame2.pack(fill="both",expand= True)
#aaaaaaaaaaaaaaaaa


    lbl=Label(frame1,
              text="* اطلاعات ساعات کاري *",
              width=20,
              height=3,
              font=("tohoma",15,"bold"),
              bg="white",
              fg="green")
    lbl.pack()




    

    lbl2=Label(frame2,
          text=":تعداد فرزند",
          width=20,
          height=3,
          font=("tohoma",12,"bold"),
          bg="black",
          fg="white" )
    lbl2.grid(row=3,column=4)

    lbl1=Label(frame2,
              text=":شب کاري",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="white" )
    lbl1.grid(row=4,column=4)

    lbl2=Label(frame2,
              text=":اضافه کاري",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="white" )
    lbl2.grid(row=5,column=4)

    lb3=Label(frame2,
              text=" :تعطيل کاري ",
              width=20,
              height=3,
              font=("tohoma",12,"bold"),
              bg="black",
              fg="white" )
    lb3.grid(row=6,column=4)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    olad= Entry(frame2,
         width=20,
          fg="green",   
         font=("tohoma",12,"bold"))
    olad.grid(row=3,column=3)

    shab_kary= Entry(frame2,
             width=20,
              fg="green",
             font=("tohoma",12,"bold"))
    shab_kary.grid(row=4,column=3)


    azafekary= Entry(frame2,
             width=20,
             fg="green",
             font=("tohoma",12,"bold"))
    azafekary.grid(row=5,column=3)

    holiday= Entry(frame2,
             width=20,
             fg="green",
             font=("tohoma",12,"bold"))
    holiday.grid(row=6,column=3)

    bt3=Button(frame2,
         text="<<<<",
         bg="green",
         font=("tohoma",12,"bold"),
         command=win_3)
    bt3.grid(row=15,column=4,padx=5,pady=10)

    
    bt5=Button(frame2,
         text=">>>> ",
         bg="green",
         font=("tohoma",12,"bold"),
         command=sh1)
    bt5.grid(row=15,column=2,padx=5,pady=10)
    


  
#safe11111111111111111111111111111111111111111111111111111111111111111111111111
def sh1():
    global kod
    global how 
    global first_name 
    global last_name
    global tamas

    win = Toplevel()
    win.title("* emolument*")
    win.geometry("550x450+500+100")
    win.configure(bg="gray")
    win.iconbitmap("7.ico")
    frame1=Frame(win,bg="white",)
    frame1.pack(fill="both",expand= True)
    frame2=Frame(win,bg="black",)
    frame2.pack(fill="both",expand= True)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    lbla=Label(frame1,
          text="year",
         
          font=("tohoma",13,"bold"),
          bg="white",
          fg="green")
    lbla.grid(row=0,column=0,padx=1,pady=10)

    lblb=Label(frame1,
          text="month",

          font=("tohoma",13,"bold"),
          bg="white",
          fg="green" )
    lblb.grid(row=0,column=1)

    lblc=Label(frame1,
          text="day",

          font=("tohoma",13,"bold"),
          bg="white",
          fg="green" )
    lblc.grid(row=0,column=2,padx=1,pady=10)

    
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    lbl_kod=Label(frame2,
          text=":کد پرسنلي",
          width=20,
          height=3,
          font=("tohoma",12,"bold"),
          bg="black",
          fg="white")
    lbl_kod.grid(row=2,column=2)
    kod= Entry(frame2,
          fg="green",
          width=8,   
          justify=RIGHT,
          font=("tohoma",12,"bold"))
    kod.grid(row=3,column=2)
    bt_kod=Button(frame2,
         text="جستجو",
         fg="green",         
         width=8,         
         font=("tohoma",10,"bold"),
         command=lambda : prsnl(frame2))
    bt_kod.grid(row=4,column=2)
    bt_save=Button(frame2,
         text="ذخيره",
         fg="green",         
         width=8,         
         font=("tohoma",10,"bold"),
         command=save1)
    bt_save.grid(row=5,column=2)








    lbl=Label(frame2,
          text=" :نام",
          width=20,
          height=3,
          font=("tohoma",12,"bold"),
          bg="black",
          fg="white")
    lbl.grid(row=2,column=1)

    lbl1=Label(frame2,
          text=":نام خانوادگي",
          width=20,
          height=3,
          font=("tohoma",12,"bold"),
          bg="black",
          fg="white" )
    lbl1.grid(row=3,column=1)


    lb3=Label(frame2,
          text=":شغل",
          width=20,
          height=3,
          font=("tohoma",12,"bold"),
          bg="black",
          fg="white" )
    lb3.grid(row=4,column=1)

  

    lbl4=Label(frame2,
          text=":شماره تماس",
          width=20,
          height=3,
          font=("tohoma",12,"bold"),
          bg="black",
          fg="white" )
    lbl4.grid(row=5,column=1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    first_name= Entry(frame2,
         width=20,
          fg="green",
          justify=RIGHT,
          font=("tohoma",12,"bold"))
    first_name.grid(row=2,column=0)

    last_name= Entry(frame2,
         width=20,
          fg="green",
          justify=RIGHT,           
         font=("tohoma",12,"bold"))
    last_name.grid(row=3,column=0)
    
    how= Entry(frame2,
         width=20,
          fg="green",
          justify=RIGHT,     
         font=("tohoma",12,"bold"))
    how.grid(row=4,column=0)


    
    tamas = Entry(frame2,
         width=20,
          fg="green",   
         font=("tohoma",12,"bold"))
    tamas.grid(row=5,column=0)



#تاريخ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    year=Spinbox(frame1,from_=1400,to=2000,
       
         font=("tohoma",11,"bold"))
 
    year.grid(row=1,column=0)



    month=Spinbox(frame1,from_=1,to=12,
       
         font=("tohoma",11,"bold"))
 
    month.grid(row=1,column=1)

    day=Spinbox(frame1,from_=1,to=31,

         font=("tohoma",11,"bold"))

    day.grid(row=1,column=2)

    bt2=Button(frame2,
         text="<<<<",
         width=8,
         bg="green",
         font=("tohoma",10,"bold"),
         command=win_2)
    bt2.grid(row=12,column=1)
#safeh 0000000000000000000000000000000000000000000000000000000000000000000000000000000
win = Tk()
win.title("* emolument*")
win.geometry("550x450+500+100")
win.configure(bg="black")
win.iconbitmap("7.ico")

image_file4=PhotoImage(file="4.png")
lm=Label(win,
      image=image_file4,
         bg="black"
          )
lm.grid(row=10,column=0)



bt2=Button(win,
         text="<<start",
         bg="green", 
         font=("tohoma",12,"bold"),
         command=sh1)
bt2.grid(row=12,column=0)
lb3=Label(win,
          text="*you welcom *",
          width=20,
          height=3,
          font=("tohoma",30,"bold"),
          bg="black",
          fg="white" )
lb3.grid(row=0,column=0)


win.mainloop()







