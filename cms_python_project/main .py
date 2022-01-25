from tkinter import*
from tkinter import filedialog,messagebox
import random
import time
import requests
from PIL import Image, ImageTk
from database import Database #importing Database class from database.py file


mydb=Database('CmsDatabase.db')
#Functions
def menu():
    root5=Toplevel(root)
    root5.title("Menu")
    root5.config(bg='yellow')
    root5.geometry('700x800')
    image1 = Image.open("menuimg.png")
    resized_Menuimage= image1.resize((700,800), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(resized_Menuimage)

    label1 = Label(root5,image=test)
    label1.image = test
    label1.place(x=0, y=0)


def settings():
    root4=Toplevel(root)
    root4.title("Settings")
    root4.config(bg='#006666')
    root4.geometry('620x620+50+50')
    def selectitem(event):#Returns the index of selected item
     try:
      global selected_item
      index=listbox.curselection()[0]
      selected_item=listbox.get(index)
      print(selected_item[1])
     except IndexError:
        print('Item not present')

    
    def Update():
     
     def Update_db():
         
         mydb.update(selected_item[0],U_name.get(),U_Phn.get(),selected_item[3],selected_item[4],selected_item[5])
         addtolist()

     LabelName=Label(root4,text="Name :").place(x=470,y=80)
     U_name=Entry(root4,font=('helvetica',12,'bold'),bd=3,width=14)
     U_name.place(x=470,y=110)
     U_name.insert(END,selected_item[1])

     LabelPhn=Label(root4,text="Phn no. :").place(x=470,y=150)
     U_Phn=Entry(root4,font=('helvetica',12,'bold'),bd=3,width=14)
     U_Phn.place(x=470,y=180)
     U_Phn.insert(END,selected_item[2])

     save_Butt=Button(root4,bg="#222222",fg='white',bd=0,padx=20,height=1,text="Save ",command=Update_db)
     save_Butt.place(x=530,y=250)

     

    

    
    def DeleteFromDb():
        mydb.remove(selected_item[0])
        addtolist()

    def addtolist():#Add's data to listbox1
     listbox.delete(0,END)
     for data in mydb.fetch():
        listbox.insert(END,data)
        print(data)
    # lst = [(nameDetail,phnumberDetails,subtotalofItems+50,date,billnumber),

    def insertToDB():#insert data into Db
      mydb.insert(nameDetail,phnumberDetails,subtotalofItems+50,date,billnumber)  
    
    listbox=Listbox(root4,bg='#272727',width=70,height=35,foreground='grey',borderwidth=0)
    listbox.place(x=10,y=20)
    listbox.bind('<<ListboxSelect>>',selectitem)#runs 'selectitem' and pass the selected items details
    update_Butt=Button(root4,bg="#222222",fg='white',bd=0,padx=40,height=1,text="Update ",command=Update)
    update_Butt.place(x=470,y=20)

    delete_Butt=Button(root4,bg="#222222",fg='white',bd=0,padx=40,height=1,text="Delete ",command=DeleteFromDb)
    delete_Butt.place(x=470,y=50)
    
    addtolist()#
    insertToDB()
    addtolist()
    
    
    
    

def reset():
    textReceipt.delete(1.0,END)
    e_burger.set('0')
    e_chickenBurger.set('0')
    e_classicBurger.set('0')
    e_cheeseToast.set('0')
    e_vegWrap.set('0')
    e_garlicBread.set('0')
    e_eggwrap.set('0')
    e_munchOnNachos.set('0')
    e_vegRoll.set('0')

    e_alphonsoShake.set('0')
    e_assamTea.set('0')
    e_hotCoffee.set('0')
    e_coldCoffee.set('0')
    e_cafeMocha.set('0')
    e_cafeLatte.set('0')
    e_cafeAmericano.set('0')
    e_cafeFrappe.set('0')
    e_cokoShake.set('0')

    e_blackForestCake.set('0')
    e_dutchTruffleCake.set('0')
    e_pineaplleCake.set('0')
    e_chocoLavaCake.set('0')
    e_cupcake.set('0')
    e_chocolateCookies.set('0')
    e_donuts.set('0')
    e_monsterCookie.set('0')
    e_brownies.set('0')

    textburger.config(state=DISABLED)
    textchickenBurger.config(state=DISABLED)
    textclassicBurger.config(state=DISABLED)
    textcheeseToast.config(state=DISABLED)
    textvegWrap.config(state=DISABLED)
    textgarlicBread.config(state=DISABLED)
    texteggwrap.config(state=DISABLED)
    textmunchOnNachos.config(state=DISABLED)
    textvegRoll.config(state=DISABLED)

    textalphansoShake.config(state=DISABLED)
    textassamTea.config(state=DISABLED)
    texthotCoffee.config(state=DISABLED)
    textcoldcoffee.config(state=DISABLED)
    textcafeMocha.config(state=DISABLED)
    textcafeLatte.config(state=DISABLED)
    textcafeAmericano.config(state=DISABLED)
    textcafeFrappe.config(state=DISABLED)
    textcokoShake.config(state=DISABLED)

    textblackForestCake.config(state=DISABLED)
    textdutchTruffleCake.config(state=DISABLED)
    textpineaplleCake.config(state=DISABLED)
    textchocoLavaCake.config(state=DISABLED)
    textcupcake.config(state=DISABLED)
    textchocolateCookies.config(state=DISABLED)
    textdonuts.config(state=DISABLED)
    textmonsterCookie.config(state=DISABLED)
    textbrownies.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    CostofFoodvar.set('')
    Costofdrinksvar.set('')
    Costofdesertsvar.set('')
    SubTotalvar.set('')
    ServiceTaxvar.set('')
    TotalCostvar.set('')

def send():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        def send_msg():
            message=textarea.get(1.0,END)
            number=numberfield.get()
            auth='69aKjNuGCeOzZ1BYn234LoXFfcJRUw0l5Aiy8DkgptvVx7mdHrCK7FYGyHNVQTc8kMfbW09djUv3iSEu'
            url='https://www.fast2sms.com/dev/bulk'

            params={
                'authorization':auth,
                'message':message,
                'numbers':number,
                'sender-id':'FSTSMS',
                'route':'p',
                'language':'english'
            }
            response=requests.get(url,params=params)
            dic=response.json()
            result=dic.get('return')
            if result==True:
                messagebox.showinfo('Send Successfully','Message sent succesfully')

            else:
                messagebox.showerror('Error','Something went wrong')

        root2=Toplevel(root)

        root2.title("Send Bill")
        root2.config(bg='#006666')
        root2.geometry('485x620+50+50')

        logoImage=PhotoImage(file=r'sender.png')
        label=Label(root2,image=logoImage,bg='#006666')
        label.pack(pady=5)

        numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='#006666',fg='white')
        numberLabel.pack(pady=5)

        numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
        numberfield.pack(pady=5)

        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='#006666', fg='white')
        billLabel.pack(pady=5)

        textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')

        if CostofFoodvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n')
        if Costofdrinksvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n')
        if Costofdesertsvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems + 50}Rs\n')

        sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='#006666',bd=7,relief=GROOVE
                          ,command=send_msg).pack(pady=5)
       
    
       

def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        def save_custmer_details():
            global nameDetail, phnumberDetails
            
            nameDetail=namefield.get()
            phnumberDetails=phnumberfield.get()
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        
            if(url!=None):
                bill_data=textReceipt.get(1.0,END)
                url.write(bill_data)
                url.close()
                messagebox.showinfo('Information','Your Bill Is Succesfully Saved')
            root3.destroy()  
            
        print('123')
        root3=Toplevel(root)
        root3.geometry('485x620+50+50')
        root3.title('customer details')
        root3.config(bg='#006666')
        
        nameLabel=Label(root3,text='Name',font=('arial',18,'bold underline'),bg='#006666',fg='white')
        nameLabel.pack(pady=5)

        namefield=Entry(root3,font=('helvetica',22,'bold'),bd=3,width=24)
        namefield.pack(pady=5)

        phnumberLabel=Label(root3,text='phone Number',font=('arial',18,'bold underline'),bg='#006666',fg='white')
        phnumberLabel.pack(pady=5)

        phnumberfield=Entry(root3,font=('helvetica',22,'bold'),bd=3,width=24)
        phnumberfield.pack(pady=5)

        nextButton=Button(root3,text='NEXT',font=('arial',19,'bold'),bg='white',fg='#006666',bd=7,relief=GROOVE
                                ,command=save_custmer_details).pack(pady=5) 
          
        
        
       

def receipt():
    global billnumber,date
    if CostofFoodvar.get() != '' or Costofdesertsvar.get() != '' or Costofdrinksvar.get() != '':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END,'***************************************************************\n')
        if e_burger.get()!='0':
            textReceipt.insert(END,f'Roti\t\t\t{int(e_burger.get())*10}\n\n')

        if e_chickenBurger.get()!='0':
            textReceipt.insert(END,f'Daal\t\t\t{int(e_chickenBurger.get())*60}\n\n')

        if e_classicBurger.get() != '0':
            textReceipt.insert(END, f'Sabji:\t\t\t{int(e_classicBurger.get()) * 50}\n\n')    

        if e_cheeseToast.get()!='0':
            textReceipt.insert(END,f'Fish\t\t\t{int(e_cheeseToast.get())*100}\n\n')

        if e_vegWrap.get() != '0':
            textReceipt.insert(END, f'Kebab:\t\t\t{int(e_vegWrap.get()) * 40}\n\n')    

        if e_garlicBread.get() != '0':
            textReceipt.insert(END, f'Chawal:\t\t\t{int(e_garlicBread.get()) * 30}\n\n')

        if e_eggwrap.get() != '0':
            textReceipt.insert(END, f'Mutton:\t\t\t{int(e_eggwrap.get()) * 120}\n\n')

        if e_munchOnNachos.get() != '0':
            textReceipt.insert(END, f'Paneer:\t\t\t{int(e_munchOnNachos.get()) * 100}\n\n')        

        if e_vegRoll.get() != '0':
            textReceipt.insert(END, f'Chicken:\t\t\t{int(e_vegRoll.get()) * 120}\n\n')


        if e_alphonsoShake.get() != '0':
            textReceipt.insert(END, f'Lassi:\t\t\t{int(e_alphonsoShake.get()) * 50}\n\n')

        if e_assamTea.get() != '0':
            textReceipt.insert(END, f'Coffee:\t\t\t{int(e_assamTea.get()) * 40}\n\n')

        if e_hotCoffee.get() != '0':
            textReceipt.insert(END, f'Faluda:\t\t\t{int(e_hotCoffee.get()) * 80}\n\n')

        if e_cafeMocha.get() != '0':
            textReceipt.insert(END, f'Shikanji:\t\t\t{int(e_cafeMocha.get()) * 30}\n\n')

        if e_cafeLatte.get() != '0':
            textReceipt.insert(END, f'Jaljeera:\t\t\t{int(e_cafeLatte.get()) * 40}\n\n')

        if e_coldCoffee.get() != '0':
            textReceipt.insert(END, f'Roohafza:\t\t\t{int(e_coldCoffee.get()) * 60}\n\n')

        if e_cafeAmericano.get() != '0':
            textReceipt.insert(END, f'Masala Chai:\t\t\t{int(e_cafeAmericano.get()) * 20}\n\n')

        if e_cafeFrappe.get() != '0':
            textReceipt.insert(END, f'Badam Milk:\t\t\t{int(e_cafeFrappe.get()) * 50}\n\n')

        if e_cokoShake.get() != '0':
            textReceipt.insert(END, f'Cold Drinks:\t\t\t{int(e_cokoShake.get()) * 80}\n\n')

        if e_dutchTruffleCake.get() != '0':
            textReceipt.insert(END, f'Oreo:\t\t\t{int(e_dutchTruffleCake.get()) * 400}\n\n')

        if e_pineaplleCake.get() != '0':
            textReceipt.insert(END, f'Apple:\t\t\t{int(e_pineaplleCake.get()) * 300}\n\n')

        if e_blackForestCake.get() != '0':
            textReceipt.insert(END, f'Kitkat:\t\t\t{int(e_blackForestCake.get()) * 500}\n\n')

        if e_cupcake.get() != '0':
            textReceipt.insert(END, f'Banana:\t\t\t{int(e_cupcake.get()) * 450}\n\n')

        if e_chocolateCookies.get() != '0':
            textReceipt.insert(END, f'Brownie:\t\t\t{int(e_chocolateCookies.get()) * 800}\n\n')

        if e_donuts.get() != '0':
            textReceipt.insert(END, f'Pineapple:\t\t\t{int(e_donuts.get()) * 620}\n\n')

        if e_monsterCookie.get() != '0':
            textReceipt.insert(END, f'Chocolate:\t\t\t{int(e_monsterCookie.get()) * 700}\n\n')

        if e_brownies.get() != '0':
            textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_brownies.get()) * 550}\n\n')

        if e_chocoLavaCake.get() != '0':
            textReceipt.insert(END, f'Vanilla:\t\t\t{int(e_chocoLavaCake.get()) * 550}\n\n')

        textReceipt.insert(END,'***************************************************************\n')
        if CostofFoodvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
        if Costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if Costofdesertsvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
        textReceipt.insert(END,'***************************************************************\n')

    else:
        messagebox.showerror('Error','No Item Is selected')
                   

def totalcost():
    global priceofFood,priceofDrinks,priceofCakes,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_burger.get())
        item2=int(e_chickenBurger.get())
        item3=int(e_cheeseToast.get())
        item4 = int(e_classicBurger.get())
        item5 = int(e_vegWrap.get())
        item6 = int(e_garlicBread.get())
        item7 = int(e_eggwrap.get())
        item8 = int(e_munchOnNachos.get())
        item9 = int(e_vegRoll.get())

        item10 = int(e_alphonsoShake.get())
        item11 = int(e_assamTea.get())
        item12 = int(e_hotCoffee.get())
        item13 = int(e_cafeMocha.get())
        item14 = int(e_cafeLatte.get())
        item15 = int(e_coldCoffee.get())
        item16 = int(e_cafeAmericano.get())
        item17 = int(e_cafeFrappe.get())
        item18 = int(e_cokoShake.get())

        item19 = int(e_dutchTruffleCake.get())
        item20 = int(e_pineaplleCake.get())
        item21 = int(e_blackForestCake.get())
        item22 = int(e_chocoLavaCake.get())
        item23 = int(e_cupcake.get())
        item24 = int(e_chocolateCookies.get())
        item25 = int(e_donuts.get())
        item26 = int(e_monsterCookie.get())
        item27 = int(e_brownies.get())

        priceofFood=(item1*10)+(item2*60)+(item3*100)+(item4*50)+ (item5*40) + (item6 * 30) + (item7 * 120) \
                    + (item8 * 100) + (item9 * 120)

        priceofDrinks=(item10*50)+(item11*40)+ (item12 * 80) + (item13 * 30) + (item14 * 40) + (item15 * 60) \
                      + (item16 * 20) + (item17 * 50) + (item18 * 80)

        priceofCakes=(item19*400)+(item20*300)+ (item21 * 500) + (item22 * 550) + (item23 * 450) + (item24 * 800) \
                     + (item25 * 620) + (item26 * 700) + (item27 * 550)

        CostofFoodvar.set(str(priceofFood)+ ' Rs')
        Costofdrinksvar.set(str(priceofDrinks)+ ' Rs')
        Costofdesertsvar.set(str(priceofCakes)+ ' Rs')

        subtotalofItems=priceofFood+priceofDrinks+priceofCakes
        SubTotalvar.set(str(subtotalofItems)+' Rs')

        ServiceTaxvar.set('50 Rs')

        tottalcost=subtotalofItems+50
        TotalCostvar.set(str(tottalcost)+' Rs')

    else:
        messagebox.showerror('Error','No Item Is selected')


def burger():
    if var1.get()==1:
        textburger.config(state=NORMAL)
        textburger.delete(0,END)
        textburger.focus()
    else:
        textburger.config(state=DISABLED)
        e_burger.set('0')

def chickenBurger():
    if var2.get()==1:
        textchickenBurger.config(state=NORMAL)
        textchickenBurger.delete(0,END)
        textchickenBurger.focus()

    else:
        textchickenBurger.config(state=DISABLED)
        e_chickenBurger.set('0')

def cheeseToast():
    if var3.get()==1:
        textcheeseToast.config(state=NORMAL)
        textcheeseToast.delete(0,END)
        textcheeseToast.focus()

    else:
        textcheeseToast.config(state=DISABLED)
        e_cheeseToast.set('0')

def classicBurger():
    if var4.get() == 1:
        textclassicBurger.config(state=NORMAL)
        textclassicBurger.focus()
        textclassicBurger.delete(0, END)
    elif var4.get() == 0:
        textclassicBurger.config(state=DISABLED)
        e_classicBurger.set('0')


def eggWrap():
    if var5.get() == 1:
        texteggwrap.config(state=NORMAL)
        texteggwrap.focus()
        texteggwrap.delete(0, END)
    elif var5.get() == 0:
        texteggwrap.config(state=DISABLED)
        e_eggwrap.set('0')


def vegRoll():
    if var6.get() == 1:
        textvegRoll.config(state=NORMAL)
        textvegRoll.focus()
        textvegRoll.delete(0, END)
    elif var6.get() == 0:
        textvegRoll.config(state=DISABLED)
        e_vegRoll.set('0')


def munchOnNachos():
    if var7.get() == 1:
        textmunchOnNachos.config(state=NORMAL)
        textmunchOnNachos.focus()
        textmunchOnNachos.delete(0, END)
    elif var7.get() == 0:
        textmunchOnNachos.config(state=DISABLED)
        e_munchOnNachos.set('0')


def garlicBread():
    if var8.get() == 1:
        textgarlicBread.config(state=NORMAL)
        textgarlicBread.focus()
        textgarlicBread.delete(0, END)
    elif var8.get() == 0:
        textgarlicBread.config(state=DISABLED)
        e_garlicBread.set('0')


def vegWrap():
    if var9.get() == 1:
        textvegWrap.config(state=NORMAL)
        textvegWrap.focus()
        textvegWrap.delete(0, END)
    elif var9.get() == 0:
        textvegWrap.config(state=DISABLED)
        e_vegWrap.set('0')


def alphansoShake():
    if var10.get() == 1:
        textalphansoShake.config(state=NORMAL)
        textalphansoShake.focus()
        textalphansoShake.delete(0, END)
    elif var10.get() == 0:
        textalphansoShake.config(state=DISABLED)
        e_alphonsoShake.set('0')


def assamTea():
    if var11.get() == 1:
        textassamTea.config(state=NORMAL)
        textassamTea.focus()
        textassamTea.delete(0, END)
    elif var11.get() == 0:
        textassamTea.config(state=DISABLED)
        e_assamTea.set('0')


def cafeFrappe():
    if var12.get() == 1:
        textcafeFrappe.config(state=NORMAL)
        textcafeFrappe.focus()
        textcafeFrappe.delete(0, END)
    elif var12.get() == 0:
        textcafeFrappe.config(state=DISABLED)
        e_hotCoffee.set('0')


def cafeMocha():
    if var13.get() == 1:
        textcafeMocha.config(state=NORMAL)
        textcafeMocha.focus()
        textcafeMocha.delete(0, END)
    elif var13.get() == 0:
        textcafeMocha.config(state=DISABLED)
        e_cafeMocha.set('0')


def hotCoffee():
    if var14.get() == 1:
        texthotCoffee.config(state=NORMAL)
        texthotCoffee.focus()
        texthotCoffee.delete(0, END)
    elif var14.get() == 0:
        texthotCoffee.config(state=DISABLED)
        e_hotCoffee.set('0')


def coldCoffee():
    if var15.get() == 1:
        textcoldcoffee.config(state=NORMAL)
        textcoldcoffee.focus()
        textcoldcoffee.delete(0, END)
    elif var15.get() == 0:
        textcoldcoffee.config(state=DISABLED)
        e_coldCoffee.set('0')


def cafeAmericano():
    if var16.get() == 1:
        textcafeAmericano.config(state=NORMAL)
        textcafeAmericano.focus()
        textcafeAmericano.delete(0, END)
    elif var16.get() == 0:
        textcafeAmericano.config(state=DISABLED)
        e_cafeAmericano.set('0')


def cafeLatte():
    if var17.get() == 1:
        textcafeLatte.config(state=NORMAL)
        textcafeLatte.focus()
        textcafeLatte.delete(0, END)
    elif var17.get() == 0:
        textcafeLatte.config(state=DISABLED)
        e_cafeFrappe.set('0')


def cokoShake():
    if var18.get() == 1:
        textcokoShake.config(state=NORMAL)
        textcokoShake.focus()
        textcokoShake.delete(0, END)
    elif var18.get() == 0:
        textcokoShake.config(state=DISABLED)
        e_cokoShake.set('0')


def blackForestCake():
    if var19.get() == 1:
        textblackForestCake.config(state=NORMAL)
        textblackForestCake.focus()
        textblackForestCake.delete(0, END)
    elif var19.get() == 0:
        textblackForestCake.config(state=DISABLED)
        e_blackForestCake.set('0')


def dutchTruffleCake():
    if var20.get() == 1:
        textdutchTruffleCake.config(state=NORMAL)
        textdutchTruffleCake.focus()
        textdutchTruffleCake.delete(0, END)
    elif var20.get() == 0:
        textdutchTruffleCake.config(state=DISABLED)
        e_dutchTruffleCake.set('0')


def pineaplleCake():
    if var21.get() == 1:
        textpineaplleCake.config(state=NORMAL)
        textpineaplleCake.focus()
        textpineaplleCake.delete(0, END)
    elif var21.get() == 0:
        textpineaplleCake.config(state=DISABLED)
        e_pineaplleCake.set('0')


def chocoLavaCake():
    if var22.get() == 1:
        textchocoLavaCake.config(state=NORMAL)
        textchocoLavaCake.focus()
        textchocoLavaCake.delete(0, END)
    elif var22.get() == 0:
        textchocoLavaCake.config(state=DISABLED)
        e_chocoLavaCake.set('0')


def cupcake():
    if var23.get() == 1:
        textcupcake.config(state=NORMAL)
        textcupcake.focus()
        textcupcake.delete(0, END)
    elif var23.get() == 0:
        textcupcake.config(state=DISABLED)
        e_cupcake.set('0')


def chocolateCookies():
    if var24.get() == 1:
        textchocolateCookies.config(state=NORMAL)
        textchocolateCookies.focus()
        textchocolateCookies.delete(0, END)
    elif var24.get() == 0:
        textchocolateCookies.config(state=DISABLED)
        e_chocolateCookies.set('0')


def donuts():
    if var25.get() == 1:
        textdonuts.config(state=NORMAL)
        textdonuts.focus()
        textdonuts.delete(0, END)
    elif var25.get() == 0:
        textdonuts.config(state=DISABLED)
        e_donuts.set('0')


def monsterCookie():
    if var26.get() == 1:
        textmonsterCookie.config(state=NORMAL)
        textmonsterCookie.focus()
        textmonsterCookie.delete(0, END)
    elif var26.get() == 0:
        textmonsterCookie.config(state=DISABLED)
        e_monsterCookie.set('0')


def brownies():
    if var27.get() == 1:
        textbrownies.config(state=NORMAL)
        textbrownies.focus()
        textbrownies.delete(0, END)
    elif var27.get() == 0:
        textbrownies.config(state=DISABLED)
        e_brownies.set('0')




root=Tk() #"root" is object of Tk class
root.geometry('1520x690+0+0') #widthx height +distance from x and y axis
root.resizable(0,0) # disable minimize maximize button
root.title('Cafe Managment System')#titlee of page
root.config(bg='#006666')#udate anything with congig-bg

#frame1_heading

topFrame=Frame(root,bd=10,relief=RIDGE,bg='#006666')
topFrame.pack(side=TOP)
labellTitle=Label(topFrame,text='Cafe Managment System', font=('arial',30,'bold'), fg='yellow',bg='#006666',width=51,bd=9)
labellTitle.grid(row=0,column=1)
img= (Image.open("setting_2.png"))
#img= PhotoImage(file = r"setting_2.png")
iconmenu = PhotoImage(file = r"menu_2.png")
iconsettings=PhotoImage(file=r'setting_2.png')

buttonSettings=Button(topFrame,text='Settings',font=('arial',14,'bold'),fg='white',bg='#006666',bd=3,padx=5,image = iconsettings,command=settings)
buttonSettings.grid(row=0,column=2)
buttonMenu=Button(topFrame,text='Menu',font=('arial',14,'bold'),fg='white',bg='#006666',bd=3,padx=5,image=iconmenu,command=menu )
buttonMenu.grid(row=0,column=0)

#frame2_products
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='#006666')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg="#006666")
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE, fg='#006666')
foodFrame.pack(side=LEFT)

drinkFrame=LabelFrame(menuFrame,text='Drink',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='#006666')
drinkFrame.pack(side=LEFT)

desertsFrame=LabelFrame(menuFrame,text='Derserts',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='#006666')
desertsFrame.pack(side=LEFT) 

#frame3_rightframes

rightFrame=Frame(root,bd=15,relief=RIDGE, bg='#006666')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE, bg='#006666')
calculatorFrame.pack()

recieptFarme=Frame(rightFrame,bd=4,relief=RIDGE, bg='#006666')
recieptFarme.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE, bg='#006666')
buttonFrame.pack()

#variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

#check box variales

e_burger=StringVar()
e_chickenBurger=StringVar()
e_classicBurger=StringVar()
e_cheeseToast=StringVar()
e_vegWrap=StringVar()
e_garlicBread=StringVar()
e_eggwrap=StringVar()
e_munchOnNachos=StringVar()
e_vegRoll=StringVar()

e_alphonsoShake=StringVar()
e_assamTea=StringVar()
e_hotCoffee=StringVar()
e_coldCoffee=StringVar()
e_cafeMocha=StringVar()
e_cafeLatte=StringVar()
e_cafeAmericano=StringVar()
e_cafeFrappe=StringVar()
e_cokoShake=StringVar()

e_blackForestCake=StringVar()
e_dutchTruffleCake=StringVar()
e_pineaplleCake=StringVar()
e_chocoLavaCake=StringVar()
e_cupcake=StringVar()
e_chocolateCookies=StringVar()
e_donuts=StringVar()
e_monsterCookie=StringVar()
e_brownies=StringVar()

CostofFoodvar=StringVar()
Costofdrinksvar=StringVar()
Costofdesertsvar=StringVar()
SubTotalvar=StringVar()
ServiceTaxvar=StringVar()
TotalCostvar=StringVar()

#checkbox intialization

e_burger.set('0')
e_chickenBurger.set('0')
e_classicBurger.set('0')
e_cheeseToast.set('0')
e_vegWrap.set('0')
e_garlicBread.set('0')
e_eggwrap.set('0')
e_munchOnNachos.set('0')
e_vegRoll.set('0')

e_alphonsoShake.set('0')
e_assamTea.set('0')
e_hotCoffee.set('0')
e_coldCoffee.set('0')
e_cafeMocha.set('0')
e_cafeLatte.set('0')
e_cafeAmericano.set('0')
e_cafeFrappe.set('0')
e_cokoShake.set('0')

e_blackForestCake.set('0')
e_dutchTruffleCake.set('0')
e_pineaplleCake.set('0')
e_chocoLavaCake.set('0')
e_cupcake.set('0')
e_chocolateCookies.set('0')
e_donuts.set('0')
e_monsterCookie.set('0')
e_brownies.set('0')

##food check buttons

burger=Checkbutton(foodFrame,text='Burger',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=burger)
burger.grid(row=0,column=0,sticky=W)

chickenBurger=Checkbutton(foodFrame,text='Chicken Burger',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=chickenBurger)
chickenBurger.grid(row=1,column=0,sticky=W)

classicBurger=Checkbutton(foodFrame,text='Classic Burger',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=classicBurger)
classicBurger.grid(row=2,column=0,sticky=W)

cheeseToast=Checkbutton(foodFrame,text='Cheese Toast',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=cheeseToast)
cheeseToast.grid(row=3,column=0,sticky=W)

vegWrap=Checkbutton(foodFrame,text='Veg Wrap',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=vegWrap)
vegWrap.grid(row=4,column=0,sticky=W)

garlicBread=Checkbutton(foodFrame,text='Garlic Bread',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=garlicBread)
garlicBread.grid(row=5,column=0,sticky=W)

eggWrap=Checkbutton(foodFrame,text='Egg Wrap',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=eggWrap)
eggWrap.grid(row=6,column=0,sticky=W)

munchOnNachos=Checkbutton(foodFrame,text='Munch-On Nachos',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=munchOnNachos)
munchOnNachos.grid(row=7,column=0,sticky=W)

vegRoll=Checkbutton(foodFrame,text='Veg Roll',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=vegRoll)
vegRoll.grid(row=8,column=0,sticky=W)

#entry fields for food items

textburger=Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_burger)
textburger.grid(row=0,column=1)

textchickenBurger=Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_chickenBurger)
textchickenBurger.grid(row=1,column=1)

textclassicBurger=Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_classicBurger)
textclassicBurger.grid(row=2,column=1)

textcheeseToast=Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_cheeseToast)
textcheeseToast.grid(row=3,column=1)

textvegWrap=Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_vegWrap)
textvegWrap.grid(row=4,column=1)

textgarlicBread=Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_garlicBread)
textgarlicBread.grid(row=5,column=1)

texteggwrap=Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_eggwrap)
texteggwrap.grid(row=6,column=1)

textmunchOnNachos=Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_munchOnNachos)
textmunchOnNachos.grid(row=7,column=1)

textvegRoll=Entry(foodFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_vegRoll)
textvegRoll.grid(row=8,column=1)


#drinks

alphansoShake=Checkbutton(drinkFrame,text='Alphonso Shake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=alphansoShake)
alphansoShake.grid(row=0,column=0,sticky=W)

assamTea=Checkbutton(drinkFrame,text='Assam Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=assamTea)
assamTea.grid(row=1,column=0,sticky=W)

hotCoffee=Checkbutton(drinkFrame,text='Hot Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=hotCoffee)
hotCoffee.grid(row=2,column=0,sticky=W)

coldCoffee=Checkbutton(drinkFrame,text='Cold Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=coldCoffee)
coldCoffee.grid(row=3,column=0,sticky=W)

cafeMocha=Checkbutton(drinkFrame,text='Cafe Mocha',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=cafeMocha)
cafeMocha.grid(row=4,column=0,sticky=W)

cafeLatte=Checkbutton(drinkFrame,text='Cafe latte',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=cafeLatte)
cafeLatte.grid(row=5,column=0,sticky=W)

cafeAmericano=Checkbutton(drinkFrame,text='Café Americano',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=cafeAmericano)
cafeAmericano.grid(row=6,column=0,sticky=W)

cafeFrappe=Checkbutton(drinkFrame,text='Café Frappe',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=cafeFrappe)
cafeFrappe.grid(row=7,column=0,sticky=W)

cokoShake=Checkbutton(drinkFrame,text='Cocoa shake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=cokoShake)
cokoShake.grid(row=8,column=0,sticky=W)

#checkboxes of  drinks

textalphansoShake=Entry(drinkFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_alphonsoShake)
textalphansoShake.grid(row=0,column=1)

textassamTea=Entry(drinkFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_assamTea)
textassamTea.grid(row=1,column=1)

texthotCoffee=Entry(drinkFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_hotCoffee)
texthotCoffee.grid(row=2,column=1)

textcoldcoffee=Entry(drinkFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_coldCoffee)
textcoldcoffee.grid(row=3,column=1)

textcafeMocha=Entry(drinkFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_cafeMocha)
textcafeMocha.grid(row=4,column=1)

textcafeLatte=Entry(drinkFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_cafeLatte)
textcafeLatte.grid(row=5,column=1)

textcafeAmericano=Entry(drinkFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_cafeAmericano)
textcafeAmericano.grid(row=6,column=1)

textcafeFrappe=Entry(drinkFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_cafeFrappe)
textcafeFrappe.grid(row=7,column=1)

textcokoShake=Entry(drinkFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_cokoShake)
textcokoShake.grid(row=8,column=1)

#deserts

blackForestCake=Checkbutton(desertsFrame,text='Black Forest Cake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=blackForestCake)
blackForestCake.grid(row=0,column=0,sticky=W)

dutchTruffleCake=Checkbutton(desertsFrame,text='Dutch Truffle Cake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=dutchTruffleCake)
dutchTruffleCake.grid(row=1,column=0,sticky=W)

pineaplleCake=Checkbutton(desertsFrame,text='Pineapple Cake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=pineaplleCake)
pineaplleCake.grid(row=2,column=0,sticky=W)

chocoLavaCake=Checkbutton(desertsFrame,text='Choco Lava Cake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=chocoLavaCake)
chocoLavaCake.grid(row=3,column=0,sticky=W)

cupcake=Checkbutton(desertsFrame,text='Cupcake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=cupcake)
cupcake.grid(row=4,column=0,sticky=W)

chocolateCookies=Checkbutton(desertsFrame,text='Chocolate Cookies',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=chocolateCookies)
chocolateCookies.grid(row=5,column=0,sticky=W)

donuts=Checkbutton(desertsFrame,text='Donuts',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=donuts)
donuts.grid(row=6,column=0,sticky=W)

monsterCookie=Checkbutton(desertsFrame,text='Monster Cookies',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=monsterCookie)
monsterCookie.grid(row=7,column=0,sticky=W)

brownies=Checkbutton(desertsFrame,text='brownies',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=brownies)
brownies.grid(row=8,column=0,sticky=W)

#deserts checkboxes
textblackForestCake=Entry(desertsFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_blackForestCake)
textblackForestCake.grid(row=0,column=1)

textdutchTruffleCake=Entry(desertsFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_dutchTruffleCake)
textdutchTruffleCake.grid(row=1,column=1)

textpineaplleCake=Entry(desertsFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_pineaplleCake)
textpineaplleCake.grid(row=2,column=1)

textchocoLavaCake=Entry(desertsFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_chocoLavaCake)
textchocoLavaCake.grid(row=3,column=1)

textcupcake=Entry(desertsFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_cupcake)
textcupcake.grid(row=4,column=1)

textchocolateCookies=Entry(desertsFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_chocolateCookies)
textchocolateCookies.grid(row=5,column=1)

textdonuts=Entry(desertsFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_donuts)
textdonuts.grid(row=6,column=1)

textmonsterCookie=Entry(desertsFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_monsterCookie)
textmonsterCookie.grid(row=7,column=1)

textbrownies=Entry(desertsFrame, font=('arial',18,'bold'),bd=7,width=6, state=DISABLED,textvariable=e_brownies)
textbrownies.grid(row=8,column=1)


#costlabels and entry fields

labelCostofFood=Label(costFrame,text="cost of food",font=('arial',16,'bold'), bg='#006666',fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',18,'bold'),bd=6, width=14, state='readonly',textvariable=CostofFoodvar)
textCostofFood.grid(row=0,column=1,padx=41)

labelCostofdrinks=Label(costFrame,text="cost of Drinks",font=('arial',16,'bold'), bg='#006666',fg='white')
labelCostofdrinks.grid(row=1,column=0)

textCostofdrinks=Entry(costFrame,font=('arial',18,'bold'),bd=6, width=14, state='readonly',textvariable=Costofdrinksvar)
textCostofdrinks.grid(row=1,column=1,padx=41)

labelCostofdeserts=Label(costFrame,text="cost of Deserts",font=('arial',16,'bold'), bg='#006666',fg='white')
labelCostofdeserts.grid(row=2,column=0,)

textCostofdeserts=Entry(costFrame,font=('arial',18,'bold'),bd=6, width=14, state='readonly',textvariable=Costofdesertsvar)
textCostofdeserts.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text="sub Total",font=('arial',16,'bold'), bg='#006666',fg='white')
labelSubTotal.grid(row=0,column=2,)

textSubTotal=Entry(costFrame,font=('arial',18,'bold'),bd=6, width=14, state='readonly',textvariable=SubTotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text="Service text",font=('arial',16,'bold'), bg='#006666',fg='white')
labelServiceTax.grid(row=1,column=2,)

textServiceTax=Entry(costFrame,font=('arial',18,'bold'),bd=6, width=14, state='readonly',textvariable=ServiceTaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='#006666',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',18,'bold'),bd=6,width=14, state='readonly',textvariable=TotalCostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='#006666',bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='#006666',bd=3,padx=5,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='#006666',bd=3,padx=5,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='#006666',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='#006666',bd=3,padx=5,command=reset)
buttonReset.grid(row=0,column=4,)

#textarea for receipt

textReceipt=Text(recieptFarme,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#calculator

operator='' #7+9
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''


calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='#006666',bd=6,width=6,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='#006666',bd=6,width=6,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='#006666',bd=6,width=6
               ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='#006666',bd=6,width=6
                  ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='#006666',bd=6,width=6
               ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='#006666',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='#006666',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='#006666',bd=6,width=6
                   ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='#006666',bd=6,width=6
               ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='#006666',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='#006666',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='#006666',bd=6,width=6
                  ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='#006666',bd=6,width=6,
                 command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='#006666',bd=6,width=6
                   ,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='#006666',bd=6,width=6
               ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='#006666',bd=6,width=6,
                 command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)
root.mainloop()#will keep our window on loop - continously open
