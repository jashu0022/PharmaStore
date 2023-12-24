from tkinter import *
from tkinter import ttk
from docxtpl import DocxTemplate
import pickle
import os
import random
import datetime


master1 = None

product = {}
order = {}

def restoring():
    global product, order

    with open('data/product.pkl', 'rb') as handle:
        l = pickle.load(handle)

        for i in l:
            product[i[0]] = Product_Window()
            product[i[0]].restoring_pro( i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11] )




    with open('data/order.pkl', 'rb') as hand:
        l1 = pickle.load(hand)

        for j in l1:
            order[j[0]] = Order()
            order[j[0]].restoring_orders( j[1], j[2], j[3], j[4], j[5], j[6], j[7])

    hand.close()

    print(order)

def saving():
    global product, order

    l = []
    l1 = []
    for i in product:
        l.append([i , product[i].name , product[i].id ,product[i].address, product[i].brand , product[i].type , product[i].dose , product[i].weight, product[i].quan , product[i].mrp, product[i].pack ,product[i].exp ])

    for j in order:
        l1.append([j,order[j].idno,  order[j].name, order[j].num , order[j].mail, order[j].addr, order[j].prod_det, order[j].amt])

    with open('data/product.pkl', 'wb') as handle:
        pickle.dump(l, handle)
    handle.close()

    with open('data/order.pkl', 'wb') as hand:
        pickle.dump(l1, hand)
    hand.close()


class Restore:
    def __init__(self, master):
        restoring()
        Main_Window(master)


class Product_Window:
    def adding_product_win(self, name ):
        self.win = Toplevel()
        self.win.protocol("WM_DELETE_WINDOW", self.on_toplevel_clos)
        self.win.geometry('{}x{}'.format(900, self.win.winfo_screenheight()-100))
        self.win.state('zoomed')

        image = PhotoImage(file='images\\images.png')
        self.win.iconphoto(False, image)



        Label(self.win, text='Add product', font=('Comic Sans MS', 25)).place(x=400, y=10)
        self.win.title('Add Product ')



        Label(self.win, text='   ', font=('Comic Sans MS', 15)).grid(row=0, pady=20)

        for i in range(11, 16, 2):
            Label(self.win, text='  :', font=('Comic Sans MS', 15)).grid(row=i, column=5)

        for i in range(1,16,2 ):
            Label(self.win,text='  :' ,font=('Comic Sans MS', 15 )).grid(row=i, column=1)

        for i in range(1,16,2 ):
            Label(self.win,text='    ' ,font=('Comic Sans MS', 15 )).grid(row=i, column=3, padx=20)

        for i in range(2,20,2 ):
            Label(self.win,text='   ' ).grid(row=i, pady=4)

        self.name = name
        Label(self.win, text= 'product name',  font=('Comic Sans MS', 15)).grid(row=1)
        Label(self.win, text= self.name, font=('Comic Sans MS', 15, 'bold') ).grid(row=1, column=2, sticky='nsew')

        Label(self.win, text= 'Product id ',  font=('Comic Sans MS', 15, )).grid(row=3)
        id = Entry(self.win,  font=('Comic Sans MS', 15,))
        id.grid(row=3, column=2)


        Label(self.win, text='manufacturer \n address',  font=('Comic Sans MS', 15,)).grid(row=5)
        address = Entry(self.win,  font=('Comic Sans MS', 15,))
        address.grid(row=5, column=2)


        Label(self.win, text= 'Brand name ',  font=('Comic Sans MS', 15, )).grid(row=7)
        brand = Entry(self.win, font=('Comic Sans MS', 15,))
        brand.grid(row=7,column=2)


        Label(self.win, text= 'Product type ',  font=('Comic Sans MS', 15, )).grid(row=9)
        type = Entry(self.win , font=('Comic Sans MS', 15,))
        type.grid(row=9,column=2)


        Label(self.win, text= 'Product dose',  font=('Comic Sans MS', 15, )).grid(row=11)
        dose = Entry(self.win,  font=('Comic Sans MS', 15,))
        dose.grid(row=11, column=2)


        Label(self.win, text= 'Net quantity',  font=('Comic Sans MS', 15, )).grid(row=13)
        weight = Entry(self.win,  font=('Comic Sans MS', 15,))
        weight.grid(row=13, column=2)


        Label(self.win, text='quantity',  font=('Comic Sans MS', 15,)).grid(row=15)
        quan = Entry(self.win,  font=('Comic Sans MS', 15,))
        quan.grid(row=15, column=2)


        Label(self.win, text='product mrp', font=('Comic Sans MS', 15,)).grid(row=11, column=4)
        mrp = Entry(self.win,  font=('Comic Sans MS', 15,))
        mrp.grid(row=11, column=6)


        Label(self.win, text='packing date',  font=('Comic Sans MS', 15,)).grid(row=13, column=4)
        pack = Entry(self.win,  font=('Comic Sans MS', 15,))
        pack.grid(row=13, column=6)


        Label(self.win, text='expiary date ',  font=('Comic Sans MS', 15,)).grid(row=15, column=4)
        exp = Entry(self.win,  font=('Comic Sans MS', 15,))
        exp.grid(row=15, column=6)


        add = Button(self.win, text='ADD', font=('Comic Sans MS', 15,), command= lambda : self.on_added(id, address, brand, type, dose, weight , quan, mrp, pack, exp))
        add.grid(row=17, column=6, sticky='nesw')
        dele = Button(self.win, text='EXIT', font=('Comic Sans MS', 15,), command= lambda :self.on_toplevel_clos())
        dele.grid(row=19, column=6, sticky='nesw')

    def update_window(self):
        self.up_window = Toplevel()
        self.up_window.protocol("WM_DELETE_WINDOW", self.on_toplevel_up_close)
        self.up_window.geometry('{}x{}'.format(900, self.up_window.winfo_screenheight() - 100))
        self.up_window.state('zoomed')

        image = PhotoImage(file='images\\images.png')
        self.up_window.iconphoto(False, image)


        Label(self.up_window, text='Update product', font=('Comic Sans MS', 25)).place(x=400, y=10)
        self.up_window.title('Update Product ')

        Label(self.up_window, text='   ', font=('Comic Sans MS', 15)).grid(row=0, pady=20)

        for i in range(11, 16, 2):
            Label(self.up_window, text='  :', font=('Comic Sans MS', 15)).grid(row=i, column=5)

        for i in range(1, 16, 2):
            Label(self.up_window, text='  :', font=('Comic Sans MS', 15)).grid(row=i, column=1)

        for i in range(1, 16, 2):
            Label(self.up_window, text='    ', font=('Comic Sans MS', 15)).grid(row=i, column=3, padx=20)

        for i in range(2, 20, 2):
            Label(self.up_window, text='   ').grid(row=i, pady=4)


        Label(self.up_window, text='product name', font=('Comic Sans MS', 15)).grid(row=1)
        Label(self.up_window, text=self.name, font=('Comic Sans MS', 15, 'bold')).grid(row=1, column=2, sticky='nsew')

        Label(self.up_window, text='Product id ', font=('Comic Sans MS', 15,)).grid(row=3)
        id = Entry(self.up_window, font=('Comic Sans MS', 15,))
        id.insert(1, self.id)
        id.grid(row=3, column=2)

        Label(self.up_window, text='manufacturer \n address', font=('Comic Sans MS', 15,)).grid(row=5)
        address = Entry(self.up_window, font=('Comic Sans MS', 15,))
        address.insert(1, self.address)
        address.grid(row=5, column=2)

        Label(self.up_window, text='Brand name ', font=('Comic Sans MS', 15,)).grid(row=7)
        brand = Entry(self.up_window, font=('Comic Sans MS', 15,))
        brand.insert(1, self.brand)
        brand.grid(row=7, column=2)

        Label(self.up_window, text='Product type ', font=('Comic Sans MS', 15,)).grid(row=9)
        type = Entry(self.up_window, font=('Comic Sans MS', 15,))
        type.insert(1, self.type)
        type.grid(row=9, column=2)

        Label(self.up_window, text='Product dose', font=('Comic Sans MS', 15,)).grid(row=11)
        dose = Entry(self.up_window, font=('Comic Sans MS', 15,))
        dose.insert(1, self.dose)
        dose.grid(row=11, column=2)

        Label(self.up_window, text='Net quantity', font=('Comic Sans MS', 15,)).grid(row=13)
        weight = Entry(self.up_window, font=('Comic Sans MS', 15,))
        weight.insert(1,self.weight)
        weight.grid(row=13, column=2)

        Label(self.up_window, text='quantity', font=('Comic Sans MS', 15,)).grid(row=15)
        quan = Entry(self.up_window, font=('Comic Sans MS', 15,))
        quan.insert(1, self.quan)
        quan.grid(row=15, column=2)

        Label(self.up_window, text='product mrp', font=('Comic Sans MS', 15,)).grid(row=11, column=4)
        mrp = Entry(self.up_window, font=('Comic Sans MS', 15,))
        mrp.insert(1,self.mrp)
        mrp.grid(row=11, column=6)

        Label(self.up_window, text='packing date', font=('Comic Sans MS', 15,)).grid(row=13, column=4)
        pack = Entry(self.up_window, font=('Comic Sans MS', 15,))
        pack.insert(1, self.pack)
        pack.grid(row=13, column=6)

        Label(self.up_window, text='expiary date ', font=('Comic Sans MS', 15,)).grid(row=15, column=4)
        exp = Entry(self.up_window, font=('Comic Sans MS', 15,))
        exp.insert(1, self.exp)
        exp.grid(row=15, column=6)



        update = Button(self.up_window, text='UPDATE', font=('Comic Sans MS', 15,),command=lambda: self.on_update(id, address, brand, type, dose, weight, quan, mrp, pack,exp))
        update.grid(row=17, column=6, sticky='nesw')


    def view_product(self):
        self.view = Toplevel()
        self.view.protocol("WM_DELETE_WINDOW", self.on_toplevel_clo)
        self.view.geometry('{}x{}'.format(900, self.view.winfo_screenheight() - 100))
        self.view.state('zoomed')

        image = PhotoImage(file='images\\images.png')
        self.view.iconphoto(False, image)

        Label(self.view, text='product Details', font=('Comic Sans MS', 25)).place(x=400, y=10)
        self.view.title('Product Details')


        Label(self.view, text='   ', font=('Comic Sans MS', 15)).grid(row=0, pady=20)

        for i in range(11, 16, 2):
            Label(self.view, text='  :', font=('Comic Sans MS', 15)).grid(row=i, column=5)

        for i in range(1, 16, 2):
            Label(self.view, text='  :', font=('Comic Sans MS', 15)).grid(row=i, column=1)

        for i in range(1, 16, 2):
            Label(self.view, text='    ', font=('Comic Sans MS', 15)).grid(row=i, column=3, padx=20)

        for i in range(2, 20, 2):
            Label(self.view, text='   ').grid(row=i, pady=4)


        Label(self.view, text='product name', font=('Comic Sans MS', 15)).grid(row=1)
        Label(self.view, text=self.name, font=('Comic Sans MS', 15, 'bold')).grid(row=1, column=2, sticky='nsew')

        Label(self.view, text='Product id ', font=('Comic Sans MS', 15,)).grid(row=3)
        Label(self.view, text=self.id,font=('Comic Sans MS', 15,)).grid(row=3, column=2)

        Label(self.view, text='manufacturer \n address', font=('Comic Sans MS', 15,)).grid(row=5)
        Label(self.view, text=self.address, font=('Comic Sans MS', 15,)).grid(row=5, column=2)

        Label(self.view, text='Brand name ', font=('Comic Sans MS', 15,)).grid(row=7)
        Label(self.view, text=self.brand, font=('Comic Sans MS', 15,)).grid(row=7, column=2)

        Label(self.view, text='Product type ', font=('Comic Sans MS', 15,)).grid(row=9)
        Label(self.view, text=self.type, font=('Comic Sans MS', 15,)).grid(row=9, column=2)

        Label(self.view, text='Product dose', font=('Comic Sans MS', 15,)).grid(row=11)
        Label(self.view, text=self.dose, font=('Comic Sans MS', 15,)).grid(row=11, column=2)

        Label(self.view, text='Net quantity', font=('Comic Sans MS', 15,)).grid(row=13)
        Label(self.view, text=self.weight, font=('Comic Sans MS', 15,)).grid(row=13, column=2)

        Label(self.view, text='quantity', font=('Comic Sans MS', 15,)).grid(row=15)
        Label(self.view,text= self.quan, font=('Comic Sans MS', 15,)).grid(row=15, column=2)

        Label(self.view, text='product mrp', font=('Comic Sans MS', 15,)).grid(row=11, column=4)
        Label(self.view,text=self.mrp, font=('Comic Sans MS', 15,)).grid(row=11, column=6)

        Label(self.view, text='packing date', font=('Comic Sans MS', 15,)).grid(row=13, column=4)
        Label(self.view, text=self.pack, font=('Comic Sans MS', 15,)).grid(row=13, column=6)

        Label(self.view, text='expiary date ', font=('Comic Sans MS', 15,)).grid(row=15, column=4)
        Label(self.view, text=self.exp, font=('Comic Sans MS', 15,)).grid(row=15, column=6)

        dele = Button(self.view, text='EXIT', font=('Comic Sans MS', 15,), command=lambda: self.on_toplevel_clo())
        dele.grid(row=19, column=6, sticky='nesw')


    def on_toplevel_up_close(self):
        Main_Window(master1)
        self.up_window.withdraw()


    def on_toplevel_clos(self):
        global product
        del product[self.name]
        Main_Window(master1)
        self.win.withdraw()


    def on_toplevel_clo(self):
        Main_Window(master1)
        self.view.withdraw()


    def on_added(self, id, address, brand, type, dose, weight , quan, mrp, pack, exp):
        self.id = id.get()
        self.address = address.get()
        self.brand = brand.get()
        self.type = type.get()
        self.dose = dose.get()
        self.weight = weight.get()
        self.quan = quan.get()
        self.mrp = mrp.get()
        self.pack = pack.get()
        self.exp = exp.get()
        Main_Window(master1)
        self.win.withdraw()

        saving()

    def on_update(self, id, address, brand, type, dose, weight , quan, mrp, pack, exp):
            self.id = id.get()
            self.address = address.get()
            self.brand = brand.get()
            self.type = type.get()
            self.dose = dose.get()
            self.weight = weight.get()
            self.quan = quan.get()
            self.mrp = mrp.get()
            self.pack = pack.get()
            self.exp = exp.get()
            Main_Window(master1)
            self.up_window.withdraw()


    def restoring_pro(self, name , id, address, brand, type, dose, weight , quan, mrp, pack, exp):
        self.name = name
        self.id = id
        self.address = address
        self.brand = brand
        self.type = type
        self.dose = dose
        self.weight = weight
        self.quan = quan
        self.mrp = mrp
        self.pack = pack
        self.exp = exp

class Customer:
    def cust(self, name , num, mail, addr):
        self.name = name
        self.num = num
        self.mail = mail
        self.addr = addr

    def get_cust(self):
        return self.name, self.num, self.mail, self.addr

class Order(Customer):
    def ordering_pro_win(self, num , name ):
        global product
        self.prod_det = []
        self.amt = float(0)

        self.or_win = Toplevel()
        self.or_win.protocol("WM_DELETE_WINDOW", self.on_top_close)

        image = PhotoImage(file='images\\images.png')
        self.or_win.iconphoto(False, image)

        self.or_win.title('Place Order')

        self.idno = num
        self.cu_name = name.get()
        frame = Frame(self.or_win)
        frame.pack(padx=30, pady=5)


        self.or_win.state('zoom')

        Label(frame, text=' ', font=('Comic Sans MS', 25)).grid(row=0, column=0, columnspan=6, pady=20)
        Label(frame, text=f" Order id   : {self.idno}",  font=('Comic Sans MS', 25)).grid(row=0, column=0, columnspan=6)

        for i in range(1, 5):
            Label(frame, text=' ', font=('Comic Sans MS', 12)).grid(row=i, column=4, padx=7)

        for i in range(1,5):
            Label(frame, text='  :', font=('Comic Sans MS', 12)).grid(row=i, column=1)

        Label(frame, text='customer name ', font=('Comic Sans MS', 12)).grid(row=1, column=0, pady=2)
        en1 = Entry(frame, font=('Comic Sans MS', 12))
        en1.grid(row=1, column=2)

        en1.insert(1, self.cu_name)

        Label(frame, text='mobile number', font=('Comic Sans MS', 12)).grid(row=2, column=0, pady=2)
        en2 = Entry(frame, font=('Comic Sans MS', 12))
        en2.grid(row=2, column=2)

        Label(frame, text='Email id ', font=('Comic Sans MS', 12)).grid(row=3, column=0, pady=2)
        en3 = Entry(frame, font=('Comic Sans MS', 12))
        en3.grid(row=3, column=2)

        Label(frame, text='customer adress', font=('Comic Sans MS', 12)).grid(row=4, column=0, pady=2)
        en4 = Entry(frame, font=('Comic Sans MS', 12))
        en4.grid(row=4, column=2)




        Label(frame, text='product name ', font=('Comic Sans MS', 12)).grid(row=1, column= 5, pady=2)
        en5 = Entry(frame, font=('Comic Sans MS', 12))
        en5.grid(row=2, column=5, pady=2)
        Label(frame, text='Quantity ', font=('Comic Sans MS', 12)).grid(row=3, column=5, pady=2)
        en6 = Spinbox(frame, from_=0,to=1000,font=('Comic Sans MS', 12))
        en6.grid(row=4, column=5, pady=2)



        tree = ttk.Treeview(frame, columns=('qty', 'prod', 'mrp', 'total'), show='headings', height=16)
        tree.heading('qty', text='Qty')
        tree.heading('prod', text='Product ')
        tree.heading('mrp', text='mrp')
        tree.heading('total', text='Total')

        tree.grid(row=6, column=0, columnspan=6, padx=10, pady=10)

        but = Button(frame, text='Add Product ', font=('Comic Sans MS', 12), command=lambda: self.add_to_tree(en5, en6 , tree))
        but.grid(row=5, column=5)

        Label(frame, text=f'Total amount :{self.amt} /-',font=('Comic Sans MS', 15)).grid(row=7, column=5, sticky='e')

        but1 = Button(frame, text='Place Order  ', font=('Comic Sans MS', 12), command= lambda :self.on_odress( en1, en2, en3, en4))
        but1.grid(row=8, column=0, columnspan=6, sticky='nesw')

        self.frame = frame

    def view_order(self):
        self.v_or_win = Toplevel()


        self.v_or_win.protocol("WM_DELETE_WINDOW", self.on_view_close)

        self.v_or_win.state('zoom')
        frame = Frame(self.v_or_win)
        frame.pack(pady=10, padx=30)

        Label(frame, text='    ', font=('Comic Sans MS', 15)).grid(row=0, column=0, columnspan=7, padx=20, pady=20)
        Label(frame, text= f'ORDER ID : {self.idno}',  font=('Comic Sans MS', 17)).grid(row=0, column=0, columnspan=7)
        Label(frame, text='customer Details ', font=('Comic Sans MS', 15)).grid(row=1, column=0, columnspan=2, sticky='e')

        name, num, mail, addr = super().get_cust()

        Label(frame, text='Name' , font=('Comic Sans MS', 12)).grid(row=2, sticky='e')
        Label(frame, text=name , font=('Comic Sans MS', 12)).grid(row=2, column=1)

        Label(frame, text='mobile', font=('Comic Sans MS', 12)).grid(row=3, sticky='e')
        Label(frame, text=num, font=('Comic Sans MS', 12)).grid(row=3, column=1)

        Label(frame, text='Email' , font=('Comic Sans MS', 12)).grid(row=4, sticky='e')
        Label(frame, text=mail, font=('Comic Sans MS', 12)).grid(row=4, column=1)

        Label(frame, text='adress', font=('Comic Sans MS', 12)).grid(row=5, sticky='e')
        Label(frame, text=addr, font=('Comic Sans MS', 12)).grid(row=5, column=1)

        Label(frame, text='Order Details ', font=('Comic Sans MS', 15)).grid(row=6, column=0, columnspan=2, sticky='e')

        k=0

        Label(frame, text='Quantity', font=('Comic Sans MS', 15, 'bold')).grid(row=7, column=1, padx=5)
        Label(frame, text='product  name ', font=('Comic Sans MS', 15, 'bold')).grid(row=7, column=2, padx=7)
        Label(frame, text='product mrp', font=('Comic Sans MS', 15, 'bold')).grid(row=7, column=3, padx=5)
        Label(frame, text='amount', font=('Comic Sans MS', 15, 'bold')).grid(row=7, column=4, padx=5)


        for i in range(8, 8+len(self.prod_det)):
                Label(frame, text=self.prod_det[i-8][0], font=('Comic Sans MS', 15)).grid(row=i, column=1, padx=5)
                Label(frame, text=self.prod_det[i-8][1], font=('Comic Sans MS', 15)).grid(row=i, column=2, padx=7)
                Label(frame, text=self.prod_det[i-8][2], font=('Comic Sans MS', 15)).grid(row=i, column=3, padx=5)
                Label(frame, text=self.prod_det[i-8][3], font=('Comic Sans MS', 15)).grid(row=i, column=4, padx=5)
                k=i
        k=k+1
        Label(frame, text='', font=('Comic Sans MS', 15)).grid(row=k, column=1, columnspan=4)

        k = k + 1
        Label(frame, text=f'Total amt  : {self.amt}/-',  font=('Comic Sans MS', 15)).grid(row=k, column=4, columnspan=2)

        k = k + 1
        but = Button(frame, text='Generate invoice', font=('Comic Sans MS', 15), command=lambda : self.generate_invoice())
        but.grid(row=k, column=4, sticky='nesw')

        k = k + 1
        but2 = Button(frame, text='EXIT', font=('Comic Sans MS', 15), command= lambda :self.on_view_close())
        but2.grid(row=k, column=4, sticky='nesw')

    def on_click_generate_invoice(self):
        doc = DocxTemplate('invoice.docx')
        doc.render({"name":self.name, "numb":self.num, "mail":self.mail, "ad": self.addr, "invoice":self.prod_det, "amount":self.amt, "idn":self.idno} )
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        downloads_dir = downloads_dir + '/' +f'{self.name}-{self.idno}-invoice.docx'
        doc.save(downloads_dir)

    def generate_invoice(self):
        doc = DocxTemplate('invoice.docx')
        doc.render({"name":self.name, "numb":self.num, "mail":self.mail, "ad": self.addr, "invoice":self.prod_det, "amount":self.amt, "idn":self.idno} )
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        downloads_dir = downloads_dir + '/' + f'{self.name}-{self.idno}-invoice.docx'
        doc.save(downloads_dir)


        Main_Window(master1)
        self.v_or_win.withdraw()


    def add_to_tree(self,  pro, quan, tree):
        global product
        if pro.get() in product:
            product[pro.get()].quan = str(int(product[pro.get()].quan) - int(quan.get()))
            tree.insert('', 0, values=[quan.get(), pro.get(), product[pro.get()].mrp, int(quan.get()) * float(product[pro.get()].mrp)])
            self.prod_det.append([quan.get(), pro.get(), product[pro.get()].mrp, int(quan.get()) * float(product[pro.get()].mrp)])
            self.amt = self.amt + int(quan.get()) * float(product[pro.get()].mrp)
            Label(self.frame, text=f'Total amount :{self.amt} /-', font=('Comic Sans MS', 15)).grid(row=7, column=5,sticky='e')
            pro.delete(0, END)
            quan.delete(0, END)
            quan.insert(0, '0')
        else:
            pro.delete(0, END)
            quan.delete(0, END)
            quan.insert(0, '0')
            return

    def on_odress(self, name , num, mail, addr):
        super().cust(name.get() , num.get(), mail.get(), addr.get())

        Main_Window(master1)
        self.or_win.withdraw()
        saving()


    def on_top_close(self):
        global order
        for i in self.prod_det:
            product[i[1]].quan = str(int(product[i[1]].quan) + int(i[0]))
        del order[self.idno]
        Main_Window(master1)
        self.or_win.withdraw()

    def restoring_orders(self, idno, name, num, mail, addr, pro_det, amt):
        self.idno = idno
        super().cust(name, num, mail, addr)
        self.prod_det = pro_det
        self.amt = amt


    def on_view_close(self):

        Main_Window(master1)
        self.v_or_win.withdraw()

    def on_view_close_generate(self):
        self.generate_invoice()


        Main_Window(master1)
        self.v_or_win.withdraw()
        

class Main_Window:
    def __init__(self, master):
        saving()
        global master1
        master1 = self.master = master

        self.toplevel = Toplevel(self.master)
        self.toplevel.protocol("WM_DELETE_WINDOW", self.on_toplevel_close)
        self.toplevel.geometry('{}x{}'.format(self.toplevel.winfo_screenwidth() - 50, self.toplevel.winfo_screenheight() - 50))

        # icon
        image1 = PhotoImage(file='images\\images.png')
        self.toplevel.iconphoto(False, image1)

        # title
        self.toplevel.title('main menu')

        # window zoom
        self.toplevel.state('zoomed')

        x = self.toplevel.winfo_screenwidth()
        y = self.toplevel.winfo_screenheight() // 2

        # image
        self.image = PhotoImage(file='images\\pharmacy.png')
        Label(self.toplevel, image=self.image, width=x, height=y).place(x=1, y=10)

        # spaces
        Label(self.toplevel, text='  ').grid(row=0, pady=self.toplevel.winfo_screenwidth() / 7)
        Label(self.toplevel, text='       ').grid(row=1, padx=30)

        # add product
        Label(self.toplevel, text='Add product').grid(row=1, column=1)
        self.label1 = Entry(self.toplevel)
        self.label1.grid(row=2, column=1)
        self.butt1 = Button(self.toplevel, text='add', width=10, height=1, command=lambda: self.add_product(self.label1))
        self.butt1.grid(row=2, column=2, padx=7)

        Label(self.toplevel, text='       ').grid(row=3, pady=10)

        # view product
        Label(self.toplevel, text='view product').grid(row=4, column=1)
        self.label2 = Entry(self.toplevel)
        self.label2.grid(row=5, column=1)
        self.butt2 = Button(self.toplevel, text='view', width=10, height=1, command= lambda : self.view_product(self.label2))
        self.butt2.grid(row=5, column=2, padx=7)

        # update product
        Label(self.toplevel, text='       ').grid(row=1, column=3, padx=130)
        Label(self.toplevel, text='update product').grid(row=1, column=4)
        self.label3 = Entry(self.toplevel)
        self.label3.grid(row=2, column=4)
        self.butt3 = Button(self.toplevel, text='update', width=10, height=1, command= lambda : self.up_product(self.label3))
        self.butt3.grid(row=2, column=5, padx=7)

        # delete product
        Label(self.toplevel, text='delete product').grid(row=4, column=4)
        self.label4 = Entry(self.toplevel)
        self.label4.grid(row=5, column=4)
        self.butt4 = Button(self.toplevel, text='delete', width=10, height=1, command=lambda: self.del_product(self.label4))
        self.butt4.grid(row=5, column=5, padx=7)

        # generate invoice
        Label(self.toplevel, text='       ').grid(row=6, pady=10)
        Label(self.toplevel, text='generate invoice').grid(row=7, column=4)
        self.label5 = Entry(self.toplevel)
        self.label5.grid(row=8, column=4)
        self.butt5 = Button(self.toplevel, text='Generate', width=10, height=1, command=lambda :self.on_generate_invoice())
        self.butt5.grid(row=8, column=5, padx=7)

        #place order
        Label(self.toplevel, text='       ').grid(row=1,column=6, padx=130)
        Label(self.toplevel, text='place order\n enter customer name ').grid(row=1, column=7)
        self.label6 = Entry(self.toplevel)
        self.label6.grid(row=2, column=7)
        self.butt6 = Button(self.toplevel, text='order', width=10, height=1, command= lambda :self.order_product(self.label6))
        self.butt6.grid(row=2, column=8, padx=7)

        #view order
        Label(self.toplevel, text='       ').grid(row=3, pady=10)
        Label(self.toplevel, text='view order').grid(row=4, column=7)
        self.label7 = Entry(self.toplevel)
        self.label7.grid(row=5, column=7)
        self.butt7 = Button(self.toplevel, text='view', width=10, height=1, command=lambda :self.on_view_order(self.label7))
        self.butt7.grid(row=5, column=8, padx=7)

    def on_view_order(self, idn):
        global order
        idno = idn.get()
        idn.delete(0, END)
        if idno  == '':
            return
        elif idno in order:
            order[idno].view_order()
            self.toplevel.withdraw()
        else :
            return


    def on_generate_invoice(self):
        idn = self.label5.get()
        self.label5.delete(0, END)
        if idn in order:
            order[idn].on_click_generate_invoice()
        else:
            return

    def add_product(self,name):
        global product
        self.name = name
        self.name = self.name.get()
        self.label1.delete(0, END)
        if self.name == '':
            return
        else:
            product[self.name] = Product_Window()
            product[self.name].adding_product_win(self.name)
            self.toplevel.withdraw()

    def up_product(self, name):
        global product
        self.name = name.get()
        self.label3.delete(0, END)
        if self.name == '':
            return
        else:
            product[self.name].update_window()
            self.toplevel.withdraw()

    def order_product(self, name):
        global order
        Name = name.get()
        self.or_num = self.ran_num()
        if Name == '':
            name.delete(0, END)
            return
        else:
            order[self.or_num] = Order()
            order[self.or_num].ordering_pro_win(self.or_num, name)
            self.toplevel.withdraw()

    def ran_num(self):
        now = datetime.datetime.now()
        x = random.randint(0, 10)
        return str(now.strftime("%d%m%y%H%M%S")) + str(x)

    def view_product(self, name):
        global product
        self.name = name
        self.name = self.name.get()
        self.label2.delete(0, END)
        if self.name == '':
            return
        else:
            product[self.name].view_product()
            self.toplevel.withdraw()

    def del_product(self, name):
        global product
        self.name = name
        self.name = self.name.get()
        self.label4.delete(0, END)
        if self.name == '':
            return
        else:
            pop = Toplevel()
            pop.geometry('{}x{}+{}+{}'.format(400, 200, self.toplevel.winfo_screenwidth() // 2 - 200, self.toplevel.winfo_screenheight() // 2 - 100))
            pop.overrideredirect(True)
            pop.config(background='#8c8c89')
            if self.name in product:
                del product[self.name]
                Label(pop, text='product successfully deleted ', background='#8c8c89', font=('Comic Sans MS', 15, 'bold')).place(x=60, y=60)
            else:
                Label(pop, text='No such product Found \n re-enter product name ', background='#8c8c89', font=('Comic Sans MS', 15, 'bold')).place(x=75, y=60)
        pop.after(2000,lambda :pop.withdraw())

    def on_toplevel_close(self):
        pop = Toplevel()
        pop.geometry('{}x{}+{}+{}'.format(400, 200, self.toplevel.winfo_screenwidth() // 2 - 200, self.toplevel.winfo_screenheight() // 2 - 100))
        pop.overrideredirect(True)
        pop.config(background='#8c8c89')
        Label(pop, text='Do you want exit?', background='#8c8c89', font=('Comic Sans MS', 15, 'bold')).place(x=20, y=35)
        butt1 = Button(pop, text='yes', background='#8c8c89', font=('Comic Sans MS', 10), width=7, command=lambda: self.master.destroy())
        butt1.place(x=245, y=160)
        butt2 = Button(pop, text='no', background='#8c8c89', font=('Comic Sans MS', 10), width=7, command=lambda: pop.withdraw())
        butt2.place(x=320, y=160)
        saving()

