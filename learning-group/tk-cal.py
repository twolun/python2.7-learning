# -*- coding: utf-8 -*-
from Tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print e.get()

b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(master, "User name:", 10)
password = makeentry(master, "Password:", 10, show="*")
content = StringVar()
entry = Entry(master, text=caption, textvariable=content)

text = content.get()
content.set(text)

# root = Tk()
# def key(event):
#     print "pressed", repr(event.char)
#
# def callback(event):
#     frame.focus_set()
#     print "clicked at", event.x, event.y
#
# frame = Frame(root, width=100, height=100)
# frame.bind("<Key>", key)
# frame.bind("<Button-1>", callback)
# frame.pack()
#
# root.mainloop()

#-------------------二输入规则计算器--------------------
#Author：哈士奇说喵(第一次署名有点怕)

# from Tkinter import *
# import difflib
# #主框架部分
# root = Tk()
# root.title('乞丐版规则器0.0')
# root.geometry()
# Label_root=Label(root,text='规则运算(根框架)',font=('宋体',15))
#
# #-----------------------定义规则------------------------
#
# def Plus(a,b):
#     return round(a+b, 2)
#
# def Sub(a,b):
#     return round(a-b,2)
#
# def Mult(a,b):
#     return round(a*b, 2)
#
# def Div(a,b):
#     return round(a/b, 2)
#
# def P_str(a,b):
#     return a+b
#
# def Rep(a,b):
#     return difflib.SequenceMatcher(None,a,b).ratio()
#     #difflib可以看看其中的定义，计算匹配率的
#
# #还可以继续增加规则函数，只要是两输入的参数都可以
# #----------------------触发函数-----------------------
#
# def Answ():#规则函数
#
#     if lb.get(lb.curselection()).encode('utf-8') == '加':
#         Ans.insert(END,'规则:+ ->'+str(Plus(float(var_first.get()),float(var_second.get()))))
#     if lb.get(lb.curselection()).encode('utf-8')=='减':
#         Ans.insert(END,'规则:- ->'+str(Sub(float(var_first.get()),float(var_second.get()))))
#     if lb.get(lb.curselection()).encode('utf-8')=='乘':
#         Ans.insert(END,'规则:x ->'+str(Mult(float(var_first.get()),float(var_second.get()))))
#     if lb.get(lb.curselection()).encode('utf-8')=='除':
#         Ans.insert(END,'规则:/ ->'+str(Div(float(var_first.get()),float(var_second.get()))))
#     if lb.get(lb.curselection()).encode('utf-8')=='字符串连接':
#         Ans.insert(END,'规则：字符串连接 ->' +P_str(var_first.get(),var_second.get()).encode('utf-8'))
#     if lb.get(lb.curselection()).encode('utf-8')=='字符串相似度':
#         Ans.insert(END,'规则:字符串相似度 ->'+str(Rep(var_first.get(),var_second.get())))
#
#     #添加规则后定义规则函数
#
# def Clea():#清空函数
#     input_num_first.delete(0,END)#这里entry的delect用0
#     input_num_second.delete(0,END)
#     Ans.delete(0,END)#text中的用0.0
#
#
# #----------------------输入选择框架--------------------
# frame_input = Frame(root)
# Label_input=Label(frame_input, text='(输入和选择框架)', font=('',15))
# var_first = StringVar()
# var_second = StringVar()
# input_num_first = Entry(frame_input, textvariable=var_first)
# input_num_second = Entry(frame_input, textvariable=var_second)
#
# #---------------------选择运算规则---------------------
# #还可以添加其他规则
#
# lb = Listbox(frame_input,height=4)
# list_item=['加', '减', '乘', '除','字符串连接','字符串相似度']
# for i in list_item:
#     lb.insert(END,i)
#
# #---------------------计算结果框架---------------------
# frame_output = Frame(root)
# Label_output=Label(frame_output, text='(计算结果框架)', font=('',15))
# Ans = Listbox(frame_output, height=1,width=30)#text也可以，Listbox好处在于换行
#
#
# #-----------------------Button-----------------------
#
# calc = Button(frame_output,text='计算', command=Answ)
# cle = Button(frame_output,text='清除', command=Clea)
#
#
# #---------------------滑动Scrollbar-------------------
# scr1 = Scrollbar(frame_input)
# lb.configure(yscrollcommand = scr1.set)
# scr1['command']=lb.yview
#
# scr2 = Scrollbar(frame_output)
# Ans.configure(yscrollcommand = scr2.set)
# scr2['command']=Ans.yview
#
#
# #-------------------------布局------------------------
# #布局写在一块容易排版，可能我low了吧
# Label_root.pack(side=TOP)
# frame_input.pack(side=TOP)
# Label_input.pack(side=LEFT)
#
# input_num_first.pack(side=LEFT)
# lb.pack(side=LEFT)
# scr1.pack(side=LEFT,fill=Y)
# input_num_second.pack(side=RIGHT)
#
# frame_output.pack(side=TOP)
# Label_output.pack(side=LEFT)
# calc.pack(side=LEFT)
# cle.pack(side=LEFT)
# Ans.pack(side=LEFT)
# scr2.pack(side=LEFT,fill=Y)
#
# #-------------------root.mainloop()------------------
#
# root.mainloop()

#
# label1 = Label(master, text="First").grid(row=0, sticky=W)
# label2 = Label(master, text="Second").grid(row=1, sticky=W)
#
# e1 = Entry(master)
# e2 = Entry(master)
#
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# master.mainloop()

# root = Tk()
#
# def callback():
#     print "called the callback!"

# create a toolbar
# toolbar = Frame(root)
#
# b = Button(toolbar, text="new", width=6, command=callback)
# b.pack(side=LEFT, padx=2, pady=2)
#
# b = Button(toolbar, text="open", width=6, command=callback)
# b.pack(side=LEFT, padx=2, pady=2)
#
# toolbar.pack(side=TOP, fill=X)
# status = Label(toolbar, text="", bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)
#
# mainloop()

# def callback():
#     print "called the callback!"
#
# root = Tk()
#
# # create a menu
# menu = Menu(root)
# root.config(menu=menu)
#
# filemenu = Menu(menu)
# menu.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="New", command=callback)
# filemenu.add_command(label="Open...", command=callback)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=callback)
#
# helpmenu = Menu(menu)
# menu.add_cascade(label="Help", menu=helpmenu)
# helpmenu.add_command(label="About...", command=callback)
#
# mainloop()

# root = Tk()
#
# def key(event):
#     print "pressed", repr(event.char)
#
# def callback(event):
#     frame.focus_set()
#     print "clicked at", event.x, event.y
#
# frame = Frame(root, width=100, height=100)
# frame.bind("<Key>", key)
# frame.bind("<Button-2>", callback)
# frame.pack()
#
# root.mainloop()

# root = Tk()
# w = Label(root, text='hello, world')
# w.pack()
# root.mainloop()

# class App(Frame):
#     def __init__(self, master, **kw):
#         self.frame = Frame(master, height=320, width=320)
#         self.frame.pack_propagate(0)
#         self.frame.pack()
#     #     Frame.__init__(self, master)
#     #     self.config(height=320, width=320)
#     #     self.grid_propagate(0)
#     #     self.pack()
#
#         self.button = Button(self.frame, text='QUIT', fg='red', command=self.frame.quit)
#         self.button.pack( expand=1, side=LEFT)
#         self.hi_there = Button(self.frame, text='Hello', command=self.say_hi)
#         self.hi_there.pack(side=LEFT)
#
#     def say_hi(self):
#         print 'hi there, everyone'
#         self.frame.configure(height=640, width=320)
#         self.hi_there.configure(text='red')
#
#
# root = Tk()
# app = App(root)
# root.mainloop()
# root.destroy()

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.create_widgets()
#
#     def say_hi(self):
#         print 'hi there, everyone'
#
#     def create_widgets(self):
#         self.QUIT = Button(self)
#         self.QUIT['text'] = 'QUIT'
#         self.QUIT['fg'] = 'red'
#         self.QUIT['command'] = self.quit
#
#         self.QUIT.pack({'side': 'left'})
#         #
#         self.hi_there = Button(self)
#         self.hi_there['text'] = 'Hello'
#         self.hi_there['command'] = self.say_hi
#         #
#         self.hi_there.pack({'side': 'left'})
#
#
#
#
# root = Tk()
# app = Application(master=root)
# app.mainloop()
# root.destroy()


