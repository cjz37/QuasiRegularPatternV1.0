"""
模型错误
5_5_1_3
6_1_1_2
"""
from tkinter import *
import image6_1_2_1 as im


def action():
    q = Eq.get().strip()
    s = Es.get().strip()
    w = Ew.get().strip()
    xmin = Exmin.get().strip()
    ymin = Eymin.get().strip()
    if q and s and w and xmin and ymin:
        q = float(q)
        s = int(s)
        w = int(w)
        xmin = int(xmin)
        ymin = int(ymin)
        if q < 0 or s < 0 or w < 0 or q > 36 or s > 128 or w > 1080:
            tip.config(text='wrong')
        else:
            tip.config(text='')
            im.draw(q, s, w, xmin, ymin)
    else:
        tip.config(text='no enter')


if __name__ == '__main__':
    root = Tk()
    root.geometry('420x220+720+370')
    root.resizable(False, False)
    root.title('图形生成')

    tip = Label(root, font=('黑体', 15))
    tip.grid(row=0, column=1)
    Label(root, text='  Q', font=('黑体', 15)).grid(row=1, column=0)
    Label(root, text='  Scale', font=('黑体', 15)).grid(row=2, column=0)
    Label(root, text='  Width', font=('黑体', 15)).grid(row=3, column=0)
    Label(root, text='  Xmin', font=('黑体', 15)).grid(row=4, column=0)
    Label(root, text='  Ymin', font=('黑体', 15)).grid(row=5, column=0)
    Label(root, text='  图片按S保存，按Esc关闭', font=('黑体', 15)).grid(row=6, column=0)

    Eq = Entry(root)
    Eq.grid(row=1, column=1)
    Es = Entry(root)
    Es.grid(row=2, column=1)
    Ew = Entry(root)
    Ew.grid(row=3, column=1)
    Exmin = Entry(root)
    Exmin.grid(row=4, column=1)
    Eymin = Entry(root)
    Eymin.grid(row=5, column=1)

    btn = Button(root, text='运行', width='10', command=action)
    btn.grid(row=6, column=1)

    root.mainloop()
