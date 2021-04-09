from tkinter import *
from tkinter import messagebox
import pickle

   
def unhide():
   a=password.get()
   txtpwd=Entry(root,textvariable=password,show="",font=("Helevetica",30,"bold"),width=17,bd=5,fg="red4")
   txtpwd.place(x=500,y=272)
   txtpwd.delete(0,END)
   txtpwd.insert(0,a)
      
   
def hide():
    a=password.get()
    txtpwd=Entry(root,textvariable=password,show="*",font=("Helevetica",30,"bold"),width=17,bd=5,fg="red4")
    txtpwd.place(x=500,y=272)
    txtpwd.delete(0,END)
    txtpwd.insert(0,a)
def exitf():
   root.destroy()
def lgn():
   if txtuser.get()=="" or txtpwd.get()=="":
      messagebox.showerror("ERROR","Fill the required boxes")
   else:
      if (str(txtuser.get())=="Nathan" and str(txtpwd.get())=="11213") or (str(txtuser.get())=="Kevin" and str(txtpwd.get())=="12213") or (str(txtuser.get())=="Harris" and str(txtpwd.get())=="12209") or (str(txtuser.get())=="Jeswin" and str(txtpwd.get())=="12212")or (str(txtuser.get())=="Guru" and str(txtpwd.get())=="12206")or (str(txtuser.get())=="Jai Praveen" and str(txtpwd.get())=="12210")or (str(txtuser.get())=="Harish" and str(txtpwd.get())=="12207"):
         def exit1():
            root1.destroy()
         def add():
            def repeat():
               txtname.delete(0,END)
               txtage.delete(0,END)
               txtgen.delete(0,END)
               txtpn.delete(0,END)
               txtarea.delete(1.0,END)
            def exit2():
               root2.destroy()
            def append():
               if txtname.get()=="" or txtage.get()=="" or txtgen.get()=="" or txtpn.get()=="" or txtarea.get(1.0,END)=="\n":
               
                  messagebox.showerror("ERROR","Fill the required boxes")

               else:
                  Handle=open('HC.log','ab')
                  Rec={}
                  Rec['Name']=str(txtname.get())
                  Rec['Age']=int(txtage.get())
                  Rec['Gender']=str(txtgen.get())
                  Rec['Patient number']=int(txtpn.get())
                  Rec['Report']=str(txtarea.get(1.0,END))
                  pickle.dump(Rec,Handle)
                  Handle.close()
                  messagebox.showinfo("INFORMATION","Record has been updated successfully.")
            root1.destroy()
            root2=Tk()
            root2.resizable(0,0)
            photo2=PhotoImage(file ="iconmed1.png")
            root2.iconphoto(False, photo2)
            appheight2=667
            appwidth2=1000

            screenwidth2=root2.winfo_screenwidth()
            screenheight2=root2.winfo_screenheight()

            x2=(screenwidth2/2)-(appwidth2/2)
            y2=(screenheight2/2)-(appheight2/2)

            root2.geometry(f'{appwidth2}x{appheight2}+{int(x2)}+{int(y2)}')
            root2.title("HC HOSPITAL")
            bg2=PhotoImage(file="bg.png")
            my_canvas2=Canvas(root2,width=1000,height=667)
            my_canvas2.pack(fill="both",expand=True)

            my_canvas2.create_image(0,0,image=bg2,anchor='nw')

            my_canvas2.create_text(507,50,text="HC HOSPITAL",font=("Helevetica",50,"bold"),fill="black")
            my_canvas2.create_text(500,50,text="HC HOSPITAL",font=("Helevetica",50,"bold"),fill="white")

            my_canvas2.create_text(157,150,text=" Name:",font=("Helevetica",35,"bold"),fill="red4")
            my_canvas2.create_text(150,150,text=" Name:",font=("Helevetica",35,"bold"),fill="white")

            txtname=Entry(root2,font=("Helevetica",30,"bold"),width=17,bd=5,fg="red4")
            txtname.place(x=257,y=120)

            my_canvas2.create_text(557,250,text="Gender:",font=("Helevetica",35,"bold"),fill="red4")
            my_canvas2.create_text(550,250,text="Gender:",font=("Helevetica",35,"bold"),fill="white")

            
            txtgen=Entry(root2,font=("Helevetica",30,"bold"),width=7,bd=5,fg="red4")
            txtgen.place(x=657,y=220)



            my_canvas2.create_text(157,250,text="Age :",font=("Helevetica",35,"bold"),fill="red4")
            my_canvas2.create_text(150,250,text="Age :",font=("Helevetica",35,"bold"),fill="white")

            
            txtage=Entry(root2,font=("Helevetica",30,"bold"),width=4,bd=5,fg="red4")
            txtage.place(x=257,y=220)

            my_canvas2.create_text(157,350,text="\t  Patient number:",font=("Helevetica",35,"bold"),fill="red4")
            my_canvas2.create_text(150,350,text="\t  Patient number:",font=("Helevetica",35,"bold"),fill="white")

            txtpn=Entry(root2,font=("Helevetica",30,"bold"),width=7,bd=5,fg="red4")
            txtpn.place(x=457,y=320)

            my_canvas2.create_text(157,450,text="  Report:",font=("Helevetica",35,"bold"),fill="red4")
            my_canvas2.create_text(150,450,text="  Report:",font=("Helevetica",35,"bold"),fill="white")

            txtarea=Text(root2,font=('arial',30,'bold'),height=3,width=25,bd=8,relief=GROOVE,wrap='word',fg="red4")#wrap is used for the complete word which goes to new line
            txtarea.place(x=257,y=420)

            man=PhotoImage(file="man.png")
            manbtn=Button(root2,image=man,bd=5,command=append).place(x=470,y=580)

            cls1=PhotoImage(file="exit2.png")
            clsbtn1=Button(root2,bd=5,image=cls1,command=exit2).place(x=570,y=580)

            rpt=PhotoImage(file="repeat.png")
            rptbtn=Button(root2,image=rpt,bd=5,command=repeat).place(x=370,y=580)





            

            root2.mainloop()
         def search():
            def repeat1():
               txtsname.delete(0,END)
               txtspn.delete(0,END)
               txtarea1.delete(1.0,END)
            def exit3():
               root3.destroy()
            def find():
               if txtsname.get()=="" or txtspn.get()=="" :
                  messagebox.showerror("ERROR","Fill the required boxes")
               else:
                  with open('HC.log','rb')as S:
                     flag=False
                     try:
                        while True:
                           med=pickle.load(S)
                           if med['Name']==str(txtsname.get()) and med['Patient number']==int(txtspn.get()):
                              name=med['Name']
                              age=med['Age']
                              gen=med['Gender']
                              pn=med['Patient number']
                              rep=med['Report']
                              txtarea1.insert(END,f'Name of the patient:{str(name)}')
                              txtarea1.insert(END,f'\nAge of the patient:{int(age)}')
                              txtarea1.insert(END,f'\nGender:{str(gen)}')
                              txtarea1.insert(END,f'\nPatient number:{int(pn)}')
                              txtarea1.insert(END,f'\nReport:{str(rep)}')
                              flag=True
                     except EOFError:
                        if flag==False:
                           messagebox.showerror('ERROR','No medical record is found')
                           S.close()
            root1.destroy()
            root3=Tk()
            root3.resizable(0,0)
            photo3=PhotoImage(file ="iconmed1.png")
            root3.iconphoto(False, photo3)
            appheight3=667
            appwidth3=1000

            screenwidth3=root3.winfo_screenwidth()
            screenheight3=root3.winfo_screenheight()

            x3=(screenwidth3/2)-(appwidth3/2)
            y3=(screenheight3/2)-(appheight3/2)

            root3.geometry(f'{appwidth3}x{appheight3}+{int(x3)}+{int(y3)}')
            root3.title("HC HOSPITAL")
            bg3=PhotoImage(file="bg.png")
            my_canvas3=Canvas(root3,width=1000,height=667)
            my_canvas3.pack(fill="both",expand=True)

            my_canvas3.create_image(0,0,image=bg3,anchor='nw')

            my_canvas3.create_text(507,50,text="HC HOSPITAL",font=("Helevetica",50,"bold"),fill="black")
            my_canvas3.create_text(500,50,text="HC HOSPITAL",font=("Helevetica",50,"bold"),fill="white")


            my_canvas3.create_text(87,150,text=" Name:",font=("Helevetica",35,"bold"),fill="red4")
            my_canvas3.create_text(80,150,text=" Name:",font=("Helevetica",35,"bold"),fill="white")

            txtsname=Entry(root3,font=("Helevetica",30,"bold"),width=12,bd=5,fg="red4")
            txtsname.place(x=187,y=120)

            my_canvas3.create_text(687,150,text="Patient no:",font=("Helevetica",35,"bold"),fill="red4")
            my_canvas3.create_text(680,150,text="Patient no:",font=("Helevetica",35,"bold"),fill="white")

            txtspn=Entry(root3,font=("Helevetica",30,"bold"),width=5,bd=5,fg="red4")
            txtspn.place(x=807,y=120)

            my_canvas3.create_text(207,250,text="Medical records:",font=("Helevetica",35,"bold"),fill="red4")
            my_canvas3.create_text(200,250,text="Medical records:",font=("Helevetica",35,"bold"),fill="white")

            txtarea1=Text(root3,font=('arial',30,'bold'),height=6,width=40,bd=8,relief=GROOVE,wrap='word',fg="red4")#wrap is used for the complete word which goes to new line
            txtarea1.place(x=40,y=280)

            srch1=PhotoImage(file="search1.png")
            srchbtn1=Button(root3,bd=5,image=srch1,command=find).place(x=470,y=580)

            cls2=PhotoImage(file="exit2.png")
            clsbtn2=Button(root3,bd=5,image=cls2,command=exit3).place(x=570,y=580)

            

            rpt1=PhotoImage(file="repeat.png")
            rptbtn1=Button(root3,image=rpt1,bd=5,command=repeat1).place(x=370,y=580)
            root3.mainloop()

           
         root.destroy()
         root1=Tk()
         root1.resizable(0,0)
         photo1=PhotoImage(file ="iconmed1.png")
         root1.iconphoto(False, photo1)

         appheight1=667
         appwidth1=1000

         screenwidth1=root1.winfo_screenwidth()
         screenheight1=root1.winfo_screenheight()

         x1=(screenwidth1/2)-(appwidth1/2)
         y1=(screenheight1/2)-(appheight1/2)

         root1.geometry(f'{appwidth1}x{appheight1}+{int(x1)}+{int(y1)}')
         root1.title("HC HOSPITAL")
         bg1=PhotoImage(file="bg.png")
         my_canvas1=Canvas(root1,width=1000,height=667)
         my_canvas1.pack(fill="both",expand=True)


         my_canvas1.create_image(0,0,image=bg1,anchor='nw')

         my_canvas1.create_text(507,50,text="HC HOSPITAL",font=("Helevetica",50,"bold"),fill="black")
         my_canvas1.create_text(500,50,text="HC HOSPITAL",font=("Helevetica",50,"bold"),fill="white")

         srch=PhotoImage(file="search.png")
         srchbtn=Button(root1,bd=5,image=srch,command=search).place(x=150,y=220)

         profile=PhotoImage(file="profile.png")
         prfibtn=Button(root1,bd=5,image=profile,command=add).place(x=650,y=220)

         cls=PhotoImage(file="exit1.png")
         clsbtn=Button(root1,bd=5,image=cls,command=exit1).place(x=450,y=550)

         my_canvas1.create_text(260,470,text="Search",font=("Helevetica",35,"bold"),fill="red4")
         my_canvas1.create_text(253,470,text="Search",font=("Helevetica",35,"bold"),fill="white")

         my_canvas1.create_text(760,470,text="Add",font=("Helevetica",35,"bold"),fill="red4")
         my_canvas1.create_text(753,470,text="Add",font=("Helevetica",35,"bold"),fill="white")
 






         root1.mainloop()
         
      else:
         messagebox.showerror("ERROR","Username or Password is incorrect")
   
   
   
   
   


root=Tk()
root.resizable(0,0)
photo=PhotoImage(file ="iconmed1.png")
root.iconphoto(False, photo)

appheight=667
appwidth=1000

screenwidth=root.winfo_screenwidth()
screenheight=root.winfo_screenheight()

x=(screenwidth/2)-(appwidth/2)
y=(screenheight/2)-(appheight/2)

root.geometry(f'{appwidth}x{appheight}+{int(x)}+{int(y)}')


root.title("HC HOSPITAL")
bgimage=PhotoImage(file="bg.png")




#Create a Canvas
my_canvas=Canvas(root,width=1000,height=667)
my_canvas.pack(fill="both",expand=True)


my_canvas.create_image(0,0,image=bgimage,anchor='nw')

my_canvas.create_text(507,50,text="HC HOSPITAL",font=("Helevetica",50,"bold"),fill="black")
my_canvas.create_text(500,50,text="HC HOSPITAL",font=("Helevetica",50,"bold"),fill="white")


my_canvas.create_text(257,200,text="Enter the username:",font=("Helevetica",35,"bold"),fill="red4")
my_canvas.create_text(250,200,text="Enter the username:",font=("Helevetica",35,"bold"),fill="white")


txtuser=Entry(root,font=("Helevetica",30,"bold"),width=17,bd=5,fg="red4")
txtuser.place(x=500,y=172)

my_canvas.create_text(257,300,text="Enter the password:",font=("Helevetica",35,"bold"),fill="red4")
my_canvas.create_text(250,300,text="Enter the password:",font=("Helevetica",35,"bold"),fill="white")


password=StringVar()
txtpwd=Entry(root,textvariable=password,show="*",font=("Helevetica",30,"bold"),width=17,bd=5,fg="red4")
txtpwd.place(x=500,y=272)


eye=PhotoImage(file="eye.png")
eyebutton=Button(root,image=eye,bd=5,command=unhide)
eyebutton.place(x=900,y=272)

ceye=PhotoImage(file="eye1.png")
ceyebutton=Button(root,image=ceye,bd=5,command=hide)
ceyebutton.place(x=900,y=352)

login=PhotoImage(file="login.png")
lgnbutton=Button(root,image=login,borderwidth=0,command=lgn).place(x=270,y=550)

exitimg=PhotoImage(file="exit.png")
extbtn=Button(root,image=exitimg,borderwidth=0,command=exitf).place(x=570,y=550)

root.mainloop()
