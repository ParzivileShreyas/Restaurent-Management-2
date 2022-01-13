from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")

text_Input = StringVar()
operator =""
Tops = Frame(root, width = 1600, height = 50,bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800, height = 700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300, height = 700,relief=SUNKEN)
f2.pack(side=RIGHT)
#==============================TIME==============================
localtime=time.asctime(time.localtime(time.time()))#Date Time Function
#==============================INFO==============================
lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Management System", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblDateTime = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblDateTime.grid(row=1,column=0)
#===========================CALCULATOR==========================

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoF = float(Fries.get())
    CoD = float(Drinks.get())
    CoChapati = float(Chapati.get())
    CoBurger = float(Burger.get())
    CoSoups = float(Soups.get())
    CoIceCream = float(IceCream.get())

    CostofFries = CoF * 70
    CostofDrinks = CoD * 90
    CostofChapati = CoChapati * 60
    CostofBurger = CoBurger * 120
    CostofSoups = CoSoups * 50
    CostofIceCream = CoIceCream * 110

    CostofMeal = "Rs", str('%.2f' % (CostofFries+CostofDrinks+CostofChapati+CostofBurger+CostofSoups+CostofIceCream))

    PayTax = ((CostofFries+CostofDrinks+CostofChapati+CostofBurger+CostofSoups+CostofIceCream) * 0.2)

    TotalCost = (CostofFries+CostofDrinks+CostofChapati+CostofBurger+CostofSoups+CostofIceCream)
    Ser_Charge = (CostofFries+CostofDrinks+CostofChapati+CostofBurger+CostofSoups+CostofIceCream) / 99
    Service = "Rs", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs", str('%.2f' % (PayTax+TotalCost+Ser_Charge))
    PaidTax = "Rs", str('%.2f' % PayTax)    
    Service_Charges.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Chapati.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charges.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Soups.set("")
    IceCream.set("")

txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input,bd=30, insertwidth=4, bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="7", bg="powder blue",command=lambda: btnClick(7)) .grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="8", bg="powder blue",command=lambda: btnClick(8)) .grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="9", bg="powder blue",command=lambda: btnClick(9)) .grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="+", bg="powder blue",command=lambda: btnClick("+")) .grid(row=2,column=3)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="4", bg="powder blue",command=lambda: btnClick(4)) .grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="5", bg="powder blue",command=lambda: btnClick(5)) .grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="6", bg="powder blue",command=lambda: btnClick(6)) .grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="-", bg="powder blue",command=lambda: btnClick("-")) .grid(row=3,column=3)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="1", bg="powder blue",command=lambda: btnClick(1)) .grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="2", bg="powder blue",command=lambda: btnClick(2)) .grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="3", bg="powder blue",command=lambda: btnClick(3)) .grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="*", bg="powder blue",command=lambda: btnClick("*")) .grid(row=4,column=3)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="0", bg="powder blue",command=lambda: btnClick(0)) .grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="C", bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="=", bg="powder blue", command=btnEqualsInput).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="/", bg="powder blue",command=lambda: btnClick("/")) .grid(row=5,column=3)

#----------------------------------------------------------------------------Restaurant info 1 ------------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Chapati = StringVar()
SubTotal = StringVar()
Total= StringVar()
Service_Charges = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Soups = StringVar()
IceCream = StringVar()
fries=StringVar()
drinks=StringVar()
chapati=StringVar()
burger=StringVar()
soups=StringVar()
icecreams=StringVar()
menu=StringVar()

lblReference = Label(f1,font=('arial', 16, 'bold') , text="Reference", bd=16, anchor='w')
lblReference.grid(row=0, column=0)
txtReference=Entry(f1,font=('arial', 16, 'bold') , textvariable=rand, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtReference.grid(row=0, column=1)

lblFries = Label(f1,font=('arial', 16, 'bold') , text="Large Fries", bd=16, anchor='w')
lblFries.grid(row=1, column=0)
txtFries=Entry(f1,font=('arial', 16, 'bold') , textvariable=Fries, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtFries.grid(row=1, column=1)

lblBurger = Label(f1,font=('arial', 16, 'bold') , text="Burger", bd=16, anchor='w')
lblBurger.grid(row=2, column=0)
txtBurger=Entry(f1,font=('arial', 16, 'bold') , textvariable=Burger, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtBurger.grid(row=2, column=1)

lblChapati = Label(f1,font=('arial', 16, 'bold') , text="Chapati", bd=16, anchor='w')
lblChapati.grid(row=3, column=0)
txtChapati=Entry(f1,font=('arial', 16, 'bold') , textvariable=Chapati, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtChapati.grid(row=3, column=1)

lblSoups = Label(f1,font=('arial', 16, 'bold') , text="Soups ", bd=16, anchor='w')
lblSoups .grid(row=4, column=0)
txtSoups =Entry(f1,font=('arial', 16, 'bold') , textvariable=Soups , bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtSoups .grid(row=4, column=1)

lblIceCream = Label(f1,font=('arial', 16, 'bold') , text="IceCream", bd=16, anchor='w')
lblIceCream.grid(row=5, column=0)
txtIceCream=Entry(f1,font=('arial', 16, 'bold') , textvariable=IceCream , bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtIceCream.grid(row=5, column=1)

#----------------------------------------------------------------------------Restaurant info 2------------------------------------------------------------------------------------------

lblDrinks = Label(f1,font=('arial', 16, 'bold') , text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1,font=('arial', 16, 'bold') , textvariable=Drinks, bd=10, insertwidth=4, bg="#ffffff", justify = "right")
txtDrinks.grid(row=0, column=3)

lblCost = Label(f1,font=('arial', 16, 'bold') , text="Cost", bd=16, anchor='w')
lblCost .grid(row=1, column=2)
txtCost=Entry(f1,font=('arial', 16, 'bold') , textvariable=Cost, bd=10, insertwidth=4, bg="#ffffff", justify = "right")
txtCost.grid(row=1, column=3)

lblService = Label(f1,font=('arial', 16, 'bold') , text="Service", bd=16, anchor='w')
lblService.grid(row=2, column=2)
txtService=Entry(f1,font=('arial', 16, 'bold') , textvariable=Service_Charges, bd=10, insertwidth=4, bg="#ffffff", justify = "right")
txtService.grid(row=2, column=3)

lblStateTax = Label(f1,font=('arial', 16, 'bold') , text="State Tax", bd=16, anchor='w')
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1,font=('arial', 16, 'bold') , textvariable=Tax, bd=10, insertwidth=4, bg="#ffffff", justify = "right")
txtStateTax.grid(row=3, column=3)

lblSubTotal = Label(f1,font=('arial', 16, 'bold') , text="SubTotal ", bd=16, anchor='w')
lblSubTotal .grid(row=4, column=2)
txtSubTotal=Entry(f1,font=('arial', 16, 'bold') , textvariable=SubTotal , bd=10, insertwidth=4, bg="#ffffff", justify = "right")
txtSubTotal .grid(row=4, column=3)

lblTotalCost = Label(f1,font=('arial', 16, 'bold') , text="TotalCost", bd=16, anchor='w')
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1,font=('arial', 16, 'bold') , textvariable=Total , bd=10, insertwidth=4, bg="#ffffff", justify = "right")
txtTotalCost.grid(row=5, column=3)

lblmenu = Label(f1,font=('arial', 16, 'bold') , text="MENU")
lblmenu.grid(row=0, column=4)

lblfries = Label(f1,font=('arial', 16, 'bold') , text="Fries=70")
lblfries.grid(row=1, column=4)

lbldrinks = Label(f1,font=('arial', 16, 'bold') , text="Drinks=90")
lbldrinks.grid(row=2, column=4)

lblchapati = Label(f1,font=('arial', 16, 'bold') , text="Chapati=60")
lblchapati.grid(row=3, column=4)

lblburger = Label(f1,font=('arial', 16, 'bold') , text="Burger=120")
lblburger.grid(row=4, column=4)

lblsoups = Label(f1,font=('arial', 16, 'bold') , text="Soups=50")
lblsoups.grid(row=5, column=4)

lblicecreams = Label(f1,font=('arial', 16, 'bold') , text="IceCreams=110")
lblicecreams.grid(row=6, column=4)

#============================================Buttons=============================================================================================
btnTotal = Button(f1,padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold') , width=10, text="Total", bg="powder blue", command = Ref).grid(row=7,column=1)

btnReset = Button(f1,padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold') , width=10, text="Reset", bg="powder blue", command = Reset).grid(row=7,column=2)

btnqExit = Button(f1,padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold') , width=10, text="Exit", bg="powder blue", command = qExit).grid(row=7,column=3)

root.mainloop()
