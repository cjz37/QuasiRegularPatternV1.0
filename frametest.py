"""
模型错误
5_5_1_3
6_1_1_2
"""
from tkinter import *
from tkinter import ttk
import image6_3_1_1 as im
from PIL import Image, ImageTk
# import threading  # 多线程


photo = None
img = None


def draw():
    return


def callback():
    print("~被调用了~")


def cmb1event(event):
    if "图案样式1" == cmb1.get():
        print("1")
    elif "图案样式2" == cmb1.get():
        print("2")
    elif "图案样式3" == cmb1.get():
        print("3")
    elif "图案样式..." == cmb1.get():
        print("more")


def cmb2event(event):
    if "切割模式1" == cmb1.get():
        print("1")
    elif "切割模式2" == cmb1.get():
        print("2")
    elif "切割模式3" == cmb1.get():
        print("3")
    elif "切割模式..." == cmb1.get():
        print("more")


def get_value(v=0):
    for key in scales.keys():
        param[key] = scales[key]['value'].get()

    paramVar.set(f"q:{param['q']}, s:{param['s']}, xmin:{param['xmin']}, ymin:{param['ymin']}")


def action():
    q = param['q']
    s = param['s']
    w = Ew.get().strip()
    xmin = param['xmin']
    ymin = param['ymin']
    if w:
        w = int(w)
        if w < 0 or w > 1080:
            tip.config(text='图像大小无效')
        else:
            tip.config(text='')
            im.draw(q, s, w, xmin, ymin)
    else:
        tip.config(text='请输入图像大小')

    savename = "6_3_1_1 {} {}pi".format(q, s)
    filename = 'images/' + savename + '.png'

    global photo
    global img
    img = Image.open('images/temp.png')
    photo = ImageTk.PhotoImage(img)
    imgLabel = Label(img_area, image=photo, width=600, height=600)
    imgLabel.grid(row=0, column=0)
    # t = threading.Thread(target=im.draw(q, s, w, xmin, ymin))  # 使用线程显示图片，不干扰滑块的调整
    # t.start()
    # qrp_img = PhotoImage(file="images/temp.png")
    # imgLabel = Label(img_area, image=qrp_img)
    # imgLabel.grid(row=0, column=0)


root = Tk()
root.title('图形生成')
root.geometry('1000x600+100+20')
root.resizable(False, False)

# 菜单栏
menubar = Menu(root)
chapter2menu = Menu(menubar, tearoff=False)
chapter2menu.add_command(label="moudel1", command=callback)  # command=?
chapter2menu.add_command(label="moudel2", command=callback)
chapter2menu.add_command(label="moudel...", command=callback)
menubar.add_cascade(label="第二章", menu=chapter2menu)

chapter3menu = Menu(menubar, tearoff=False)
chapter3menu.add_command(label="moudel1", command=callback)  # command=?
chapter3menu.add_command(label="moudel2", command=callback)
chapter3menu.add_command(label="moudel...", command=callback)
menubar.add_cascade(label="第三章", menu=chapter3menu)

chapter4menu = Menu(menubar, tearoff=False)
chapter4menu.add_command(label="moudel1", command=callback)  # command=?
chapter4menu.add_command(label="moudel2", command=callback)
chapter4menu.add_command(label="moudel...", command=callback)
menubar.add_cascade(label="第四章", menu=chapter4menu)

chapter5menu = Menu(menubar, tearoff=False)
chapter5menu.add_command(label="moudel1", command=callback)  # command=?
chapter5menu.add_command(label="moudel2", command=callback)
chapter5menu.add_command(label="moudel...", command=callback)
menubar.add_cascade(label="第五章", menu=chapter5menu)

chapter6menu = Menu(menubar, tearoff=False)
chapter6menu.add_command(label="moudel1", command=callback)  # command=?
chapter6menu.add_command(label="moudel2", command=callback)
chapter6menu.add_command(label="moudel...", command=callback)
menubar.add_cascade(label="第六章", menu=chapter6menu)

root.config(menu=menubar)

frm = Frame(root)
frm.pack()

# 左侧区域
img_area = Frame(frm, width=700, height=600)
qrp_img = PhotoImage(file="images/clear.png")
imgLabel = Label(img_area, image=qrp_img, width=600, height=600)
imgLabel.grid(row=0, column=0)
img_area.pack(side=LEFT)

# 右侧区域
param_area = Frame(frm, width=300, height=600)
Label(param_area, text='第二章:', font=('华文行楷', 20, 'italic')).grid(row=0, column=0, pady=18)
Label(param_area, text='分支1', font=('华文行楷', 20, 'italic')).grid(row=0, column=1)
# 滑块
param = {}
v = IntVar()
scales = {'q': {'range': (1, 36), 'value': IntVar(), 'pos': 1, 'describe': "迭代次数"},
          's': {'range': (1, 128), 'value': IntVar(), 'pos': 2, 'describe': "图案密度"},
          # 'w': {'range': (0, 600), 'value': IntVar(), 'pos': 3, 'describe': "图像大小"},
          'xmin': {'range': (-600, 600), 'value': IntVar(), 'pos': 3, 'describe': "中心X坐标偏移"},
          'ymin': {'range': (-600, 600), 'value': IntVar(), 'pos': 4, 'describe': "中心Y坐标偏移"}}
for k, v in scales.items():
    Label(param_area, text=v['describe'], font=('华文行楷', 12)).grid(row=v['pos'], column=0, padx=30)
    scales[k]['target'] = Scale(param_area, variable=v['value'], from_=v['range'][0], to=v['range'][1],
                                orient=HORIZONTAL, length=200, command=get_value)
    scales[k]['target'].grid(row=v['pos'], column=1, columnspan=2)

    # 初始化滑块
    if 1 == v['pos']:
        v['value'].set(3)
    elif 2 == v['pos']:
        v['value'].set(12)
    # elif 3 == v['pos']:
    #     v['value'].set(600)
    elif 3 == v['pos']:
        v['value'].set(0)
    elif 4 == v['pos']:
        v['value'].set(0)

paramVar = StringVar()
get_value()
# Label(root, text="参数信息:").grid(row=6, column=1, pady=18)
# Label(root, textvariable=paramVar).grid(row=6, column=2)

Label(param_area, text='图像大小', font=('华文行楷', 12)).grid(row=5, column=0, pady=18)
Ew = Entry(param_area)
Ew.grid(row=5, column=1)

# 下拉列表
cmb1 = ttk.Combobox(param_area)
Label(param_area, text="图案样式:", font=('华文行楷', 12)).grid(row=7, column=1)
cmb1.grid(row=8, column=1, pady=5)
cmb1['value'] = ('图案样式1', '图案样式2', '图案样式3', '图案样式...')
cmb1.current(0)

cmb2 = ttk.Combobox(param_area)
Label(param_area, text="切割模式:", font=('华文行楷', 12)).grid(row=9, column=1)
cmb2.grid(row=10, column=1, pady=5)
cmb2['value'] = ('切割模式1', '切割模式2', '切割模式3', '切割模式...')
cmb2.current(0)

cmb1.bind("<<ComboboxSelected>>", cmb1event)
cmb2.bind("<<ComboboxSelected>>", cmb2event)

tip = Label(param_area, font=('华文行楷', 12))
tip.grid(row=8, column=0)

btn1 = Button(param_area, text='生成', font=('华文行楷', 12), width='10', command=action)
btn1.grid(row=9, column=0)

btn2 = Button(param_area, text='保存', font=('华文行楷', 12), width='10', command=action)
btn2.grid(row=10, column=0)

param_area.pack(side=RIGHT)

root.mainloop()
