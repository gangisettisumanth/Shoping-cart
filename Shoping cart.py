from tkinter import *

import mysql.connector

db= mysql.connector.connect(host='localhost', user='root', password='', db='sample')

cursor = db.cursor()

def calculate():

    product_tot.set (product_price.get()* product_qty.get())

def add():

    id=product_id.get()

    name=product_name.get()

    price = product_price.get()

    qty = product_qty.get()

    tot =product_tot.get()

    cursor.execute('insert into shopitems values (%s, %s, %s, %s, %s)',[id,name,price,qty, tot])

    db.commit()


def view():

    id= product_id.get()

    cursor.execute('select * from shopitems where id=%s',[id])

    data =cursor.fetchone()

    product_name.set(data[1])

    product_price.set(data[2])

    product_qty.set(data[3])

    product_tot.set(data[4])


def update():

    id= product_id.get()

    price = product_price.get()

    qty = product_qty.get()

    tot = product_tot.get()

    cursor.execute('update shopitems set price=%s, qty=%s, tot=%s where id=%s' ,[price,qty, tot,id])

    db.commit()


def delete():

    id=product_id.get()

    cursor.execute('delete from shopitems where id=%s',[id])

    db.commit()

def clear():

    product_id.set('')

    product_name.set('')

    product_price.set('')

    product_qty.set('')

    product_tot.set('')


def overall():

    global viewpage

    viewpage = Toplevel(obj)


    viewpage.geometry('900x500')

    viewpage.title('Product Details')

    viewpage.configure(bg='Lightblue')

    cursor.execute('select * from shopitems')

    data= cursor.fetchall()

    rows = len(data)

    cols = len(data[0])

    Label(viewpage, text='Product Id', font=('calibri',15, 'bold'), bg='lightblue').grid(row=0,column=0)
    Label(viewpage, text='Product Name', font=('calibri', 15, 'bold'), bg='Lightblue').grid(row=0,column=1)

    Label(viewpage, text='Product Price', font=('calibri' ,15, 'bold'), bg='lightblue').grid(row=0,column=2)

    Label(viewpage, text='Product Qty', font=('calibri', 15, 'bold'), bg='Lightblue').grid(row=0,column=3)

    Label(viewpage, text="Total Price", font=('calibri', 15, 'bold'), bg='lightblue').grid(row=0,column=4)

    for i in range (rows):

        for j in range(cols):

            s=Entry(viewpage, font=("calibri",13))
            s.grid(row=i + 1, column=j)
            s.insert(END, data[i][j])

obj = Tk()

obj.geometry('650x500')

obj.title('Access Control Matrix')

obj.configure(bg='Lightgreen')

Label (obj, text='Products Entry', font=('calibri',20), fg='green'). place (x=240,y=18)


product_id_label = Label (obj, text='Product ID', font=('calibri',17), bg='lightgreen')

product_id_label.place(x=130,y=70)

product_id= StringVar()

product_id_entry = Entry(obj, textvariable=product_id, font=('calibri',15))

product_id_entry.place(x=290,y=70)


product_name_label = Label (obj, text='Product Name', font=('calibri',17), bg='lightgreen')

product_name_label.place(x=130,y=120)

product_name= StringVar()

product_name_entry = Entry(obj, textvariable=product_name, font=('calibri',15))

product_name_entry.place(x=290,y=120)


product_price_label = Label (obj, text='Product Price', font=('calibri',17), bg='lightgreen')

product_price_label.place(x=130,y=170)

product_price= IntVar()

product_price_entry = Entry(obj, textvariable=product_price, font=('calibri',15))

product_price_entry.place(x=290,y=170)


product_qty_label = Label (obj, text='Product Qty', font=('calibri',17), bg='lightgreen')

product_qty_label.place(x=130,y=220)

product_qty= IntVar()

product_qty_entry = Entry(obj, textvariable=product_qty, font=('calibri',15))

product_qty_entry.place(x=290,y=220)


product_tot_label = Label (obj, text='Total Price', font=('calibri',17), bg='lightgreen')

product_tot_label.place(x=130,y=270)

product_tot= IntVar()

product_tot_entry = Entry(obj, textvariable=product_tot, font=('calibri',15))

product_tot_entry.place(x=290,y=270)

but_cal=Button(obj,text='Calculate',command=calculate,font=('calibri',11),bg='gray',fg='white',width='8',height='1')
but_cal.place(x=500,y=220)

but_add=Button(obj,text='ADD',command=add,font=('calibri',15),bg='gray',fg='white',width='10',height='1')
but_add.place(x=130,y=350)

but_view=Button(obj,text='  VIEW',command=view,font=('calibri',15),bg='gray',fg='white',width='10',height='1')
but_view.place(x=260,y=350)

but_upd=Button(obj,text='UPDATE',command=update,font=('calibri',15),bg='gray',fg='white',width='10',height='1')
but_upd.place(x=390,y=350)

but_del=Button(obj,text='DELETE',command=delete,font=('calibri',15),bg='gray',fg='white',width='10',height='1')
but_del.place(x=130,y=410)

but_clr=Button(obj,text='CLEAR',command=clear,font=('calibri',15),bg='gray',fg='white',width='10',height='1')
but_clr.place(x=260,y=410)

but_ovr=Button(obj,text='OVERALL',command=overall,font=('calibri',15),bg='gray',fg='white',width='10',height='1')
but_ovr.place(x=390,y=410)

obj.mainloop()