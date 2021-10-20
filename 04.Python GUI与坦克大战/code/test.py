from tkinter import *
# 引入 messagebox 消息弹窗
from tkinter import messagebox
import tkinter

# 这里需要通过引入 tkinter；直接写TK() 会报错
root = tkinter.Tk()

btn = Button(root)
btn["text"] = "点击"
btn.pack()


def huhuhu(e):  # 事件对象
    messagebox.showinfo("Message:", "测试成功")
    print("芜湖")


btn.bind("<Button-1>", huhuhu)

root.mainloop()  # 进入事件循环
