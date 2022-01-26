from cgitb import text
from email import message
from tkinter import *
from tkinter import messagebox
from turtle import width
import Pyautogui
import sys

def action():
    #播报提示
    message = messagebox.showinfo(title='Message', message='确定要执行操作吗？')
    print(message)

    #获取输入框内容
    data = entry.get().strip()
    Pyautogui.work(data)
    while True:
        Pyautogui.work(data)

def exit():
    #退出
    sys.exit(0)


#施工中...
def actWin():
    root = Tk()
    root.geometry('150x100+800+400')
    root.resizable(False,False)
    root.title('状态')
    Label(root, text = '正在执行中', font = ('黑体',13)).grid(padx=30, pady=70)
    root.mainloop()

if __name__ == '__main__':
    
    #实例化Tk
    root = Tk()
    

    #设置位置和大小
    root.geometry('500x300+800+400')

    #是否可拉伸窗口
    root.resizable(False,False)

    #设置标题
    root.title('自动化微信回复')

    #设置标签，grid --> 设置网格
    Label(root, text = '请输入语句: ', font = ('黑体',13)).grid(padx=30, pady=70)
    Label(root, text = '     Created by BinL', font = ('黑体',10)).grid(row=3, column=2,pady=80)
    Label(root, text = 'Ver 0.0.1', font = ('黑体',10)).grid(row=3, column=0)

    #输入框
    entry = Entry(root, width=40)
    entry.grid(row=0,column=1,columnspan=2)


    #按钮1
    button1 = Button(root, text = '运行', width=10, command=action)
    button1.grid(row=2,column=0)


    #施工中...
    #按钮2
    button2 = Button(root, text = '终止', width=10)
    button2.grid(row=2,column=1)

    #按钮3
    button3 = Button(root, text = '退出', width=10, command=exit)
    button3.grid(row=2,column=2,padx=30)


    #循环弹窗
    root.mainloop()