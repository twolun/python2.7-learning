# -*- coding: utf-8 -*-
'''
1. 输入框，支持鼠标点击及键盘混合输入
2. 输入框，支持鼠标点击退格及键盘退格
3. 自自定义，字符串连接操作
4. 有待完善功能, +/-/*//数据类型验证
'''
from Tkinter import *

class CalButton:
    def __init__(self, frame, n, fn):
        self.frame = frame
        self.value = n
        self.fn = fn
        self.button = Button(frame, text=n, command=self.get_value)

    def get_value(self):
        self.fn(self.value)

def key(event):
    print "pressed", repr(event.char)

class Calculator(Frame):
    def __init__(self, master, **kw):
        self.frame = Frame(master, height=480, width=320)
        self.frame.pack_propagate(0)
        self.frame.pack()
        self.cal_init()


    def cal_init(self):
        self.op_label = Label(self.frame, text="Op")
        self.op_label.grid(row=1)
        Label(self.frame, text="result").grid(row=3)

        self.entry3 = Entry(self.frame)
        op = Label(self.frame, text="", height=2)   #占位用

        op.grid(row=5, column=1)
        self.entry3.grid(row=3, column=1)

        self.entry1_init()
        self.op_init()
        self.entry2_init()
        self.button_init()

        # 计算，清除按钮
        cal_button = Button(self.frame, text='计算', command=self.cal_fun)
        clear_button = Button(self.frame, text='清除', command=self.clear_fun)
        zw_button = Button(self.frame, text='C', command=self.clear_step)
        cal_button.grid(row=10, column=0)
        clear_button.grid(row=10, column=1)
        zw_button.grid(row=10, column=2)

    def entry1_init(self):
        Label(self.frame, text="Num1").grid(row=0)
        self.entry1 = Entry(self.frame)
        self.entry1.grid(row=0, column=1)
        self.entry1.focus_set()
        self.entry1.bind('<FocusIn>', self.entry1_focusin)

    def entry1_focusin(self, event):
        self.entry = '1'

    def entry2_init(self):
        Label(self.frame, text="Num2").grid(row=2)
        self.entry2 = Entry(self.frame)
        self.entry2.grid(row=2, column=1)
        self.entry2.bind('<FocusIn>', self.entry2_focusin)

    def entry2_focusin(self, event):
        self.entry = '2'

    def op_init(self):
        self.op_list = Listbox(self.frame, height=2)
        # self.op_list.configure(height=5)
        for item in ['+', '-', '*', '/', '字符串连接']:
            self.op_list.insert(END, item)
        self.op_list.grid(row=1, column=1)
        # self.op_list.bind("<Key>", self.key_press)
        # self.op_list.bind("<Button-1>", self.set_focus)
        # self.op_list.activate(0)

    def button_init(self):
        num1 = self.create_button(1)
        num2 = self.create_button(2)
        num3 = self.create_button(3)
        num4 = self.create_button(4)
        num5 = self.create_button(5)
        num5 = self.create_button(6)
        num5 = self.create_button(7)
        num5 = self.create_button(8)
        num5 = self.create_button(9)

    def create_button(self, n):
        num = CalButton(self.frame, n, self.get_button_value)
        if(1 <= n <= 3 ):
            row = 6
            column = n - 1
        if(4 <= n <= 6):
            row = 7
            column = n - 4
        if( 7 <= n <= 9):
            row = 8
            column = n - 7
        num.button.grid(row=row, column=column)
        return num.button

    def get_button_value(self, value):
        if self.entry == '1':
            self.entry1.insert(END, value)
        if self.entry == '2':
            self.entry2.insert(END, value)
        print value

    def select_op(self):
        print 1111

    def cal_fun(self):
        self.op = self.op_list.get(ACTIVE)
        entry1 = self.entry1.get()
        entry2 = self.entry2.get()
        if not entry2:
            return False
        if self.op == '+':
            res = self.plus(entry1, entry2)
        if self.op == '-':
            res = self.sub(entry1, entry2)
        if self.op == '*':
            res = self.mult(entry1, entry2)
        if self.op == '/':
            res = self.div(entry1, entry2)
        if self.op.encode('utf-8') == '字符串连接':
            res = self.str_plus(entry1, entry2)
        else:
            pass

        self.entry3.delete(0, END)      # 先清空
        self.entry3.insert(END, res)
        # print self.op_list.curselection()
        # self.op_list.see(2)


    def plus(self, a, b):
        return float(a) + float(b)

    def sub(self, a, b):
        return float(a) - float(b)

    def mult(self, a, b):
        return float(a) * float(b)

    def div(self, a, b):
        return round(float(a) / float(b))

    def str_plus(self, a, b):
        return a + b

    def clear_fun(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.op = '+'
        self.op_list.see(0)
        self.op_list.activate(0)
        self.entry1.focus_set()

    def clear_step(self):
        if self.entry == '1':
            value_len = len(self.entry1.get())
            self.entry1.delete(value_len - 1, END)
        if self.entry == '2':
            value_len = len(self.entry2.get())
            self.entry2.delete(value_len - 1, END)

    def key_press(self, event):
        print repr(event.char)

    def set_focus(self, event):
        self.frame.focus_set()
        print self.op_list.get(ACTIVE)
        print self.op_list.curselection()
        self.op_label.configure(text='Op('+self.op_list.get(ACTIVE)+')')


root = Tk()
app = Calculator(root)

root.mainloop()
root.destroy()

