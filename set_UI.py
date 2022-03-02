from tkinter import *
from PIL import Image, ImageDraw
import PIL


class Window:

    Cwidth = 100
    Cheight = 100

    def __init__(self, width, height, title="MyWindow", icon=r"resources/images.ico" ):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        self.top_frame = Frame(self.root, width=self.Cwidth, height=self.Cheight)
        self.left_frame = Frame(self.root)
        self.right_frame = LabelFrame(self.root, text="Цифры")
        self.var = IntVar()
        self.var.set(0)
        self.r0 = Radiobutton(self.right_frame, text='0', variable=self.var, value=0)
        self.r1 = Radiobutton(self.right_frame, text='1', variable=self.var, value=1)
        self.r2 = Radiobutton(self.right_frame, text='2', variable=self.var, value=2)
        self.r3 = Radiobutton(self.right_frame, text='3', variable=self.var, value=3)
        self.r4 = Radiobutton(self.right_frame, text='4', variable=self.var, value=4)
        self.r5 = Radiobutton(self.right_frame, text='5', variable=self.var, value=5)
        self.r6 = Radiobutton(self.right_frame, text='6', variable=self.var, value=6)
        self.r7 = Radiobutton(self.right_frame, text='7', variable=self.var, value=7)
        self.r8 = Radiobutton(self.right_frame, text='8', variable=self.var, value=8)
        self.r9 = Radiobutton(self.right_frame, text='9', variable=self.var, value=9)
        self.cv = Canvas(self.top_frame, width=self.Cwidth, height=self.Cheight, bg='white')
        self.image = PIL.Image.new("RGB", (width, height))
        self.draw = ImageDraw.Draw(self.image)
        self.penSize_slider = 3
        self.buttonRecognize = Button(self.left_frame, text="Распознать", width=20)
        self.buttonTeach = Button(self.left_frame, text="Обучить", width=20)
        self.buttonSave = Button(self.left_frame, text="Сохранить веса", width=20)
        self.buttonError = Button(self.left_frame, text="Ошибка", width=20)
        self.buttonClear = Button(self.left_frame, text="Очистить", command=self.clear, width=20)
        self.lbl1 = Label(self.top_frame, text=" ", font="Arial 10", fg="black")
        self.lbl2 = Label(self.top_frame, text=" ", font="Arial 9", width=15)
        if icon:
            self.root.iconbitmap(icon)

    def draw_widgets(self):
        self.cv.bind("<B1-Motion>", self.paint)
        self.cv.pack(side=LEFT)
        self.right_frame.pack(anchor=NE, side=RIGHT, expand="yes", fill=Y)
        self.top_frame.pack(side=TOP, fill=Y, pady=20, padx=20)
        self.left_frame.pack(side=TOP, fill=Y, pady=20, padx=20, ipady=10)
        self.r0.pack(side=TOP)
        self.r1.pack(side=TOP)
        self.r2.pack(side=TOP)
        self.r3.pack(side=TOP)
        self.r4.pack(side=TOP)
        self.r5.pack(side=TOP)
        self.r6.pack(side=TOP)
        self.r7.pack(side=TOP)
        self.r8.pack(side=TOP)
        self.r9.pack(side=TOP)
        self.lbl1.pack(side=TOP, pady=10)
        self.lbl2.pack(side=TOP)
        self.buttonRecognize.pack()
        self.buttonTeach.pack()
        self.buttonError.pack()
        self.buttonClear.pack()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.cv.create_oval(x1, y1, x2, y2, fill="black", width=self.penSize_slider)
        self.draw.line([x1, y1, x2, y2], fill="black", width=self.penSize_slider)

    def clear(self):
        self.cv.delete("all")
        self.draw.rectangle((0, 0, self.Cwidth, self.Cheight), fill=(255, 255, 255, 255))