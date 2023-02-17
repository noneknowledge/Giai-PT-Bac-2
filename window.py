from tkinter import *


def btn_clicked():
    print("Button Clicked")

def tiepAction():
    hesoA.set("")
    hesoB.set("")
    ketqua.set("")
    print("repeat")


def giaiAction():
    try:
        a = float(hesoA.get())
        b = float(hesoB.get())
        if a==0 and b==0:
            ketqua.set("Vo so nghiem")
        elif a==0 and b!=0:
            ketqua.set("Vo nghiem")
        else: 
            ketqua.set("x = "+str(-b/a))
    except:
        try:
            a = float(hesoA.get())
            x = float(ketqua.get())
            hesoB.set("B = " +str(a*x))
        except:
            try:
                b = float(hesoB.get())
                x = float(ketqua.get())
                if x==0 and b==0:
                    hesoA.set("Vo so nghiem")
                elif x==0 and b!=0:
                    hesoA.set("Vo nghiem")
                else: 
                    hesoA.set("A = "+str(-b/x))
            except:
                hesoA.set("")
                hesoB.set("")
                ketqua.set("Nhap lai he so A và he so B")



window = Tk()
hesoA = StringVar()
hesoB = StringVar()
ketqua = StringVar()


window.geometry("974x617")
window.configure(bg = "#4d4944")
canvas = Canvas(
    window,
    bg = "#4d4944",
    height = 617,
    width = 974,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = giaiAction,#giai
    relief = "flat")

b0.place(
    x = 362, y = 484,
    width = 250,
    height = 99)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = window.quit, #thoat
    relief = "flat")

b1.place(
    x = 652, y = 487,
    width = 250,
    height = 99)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = tiepAction, #tiep
    relief = "flat")

b2.place(
    x = 50, y = 487,
    width = 250,
    height = 99)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    476.0, 244.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    563.5, 153.5,
    image = entry0_img)

entry0 = Entry(
    textvariable=hesoA,
    font = "Helvetica 24", 
    bd = 0,
    bg = "#deeeea",
    highlightthickness = 0)

entry0.place(
    x = 314, y = 117,
    width = 499,
    height = 71)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    563.5, 262.5,
    image = entry1_img)

entry1 = Entry(
    textvariable=hesoB,
    font = "Helvetica 24", 
    bd = 0,
    bg = "#deeeea",
    highlightthickness = 0)

entry1.place(
    x = 314, y = 226,
    width = 499,
    height = 71)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    563.5, 371.5,
    image = entry2_img)

entry2 = Entry(
    textvariable=ketqua,
    font = "Helvetica 24", 
    bd = 0,
    bg = "#96c7c1",
    highlightthickness = 0)

entry2.place(
    x = 314, y = 335,
    width = 499,
    height = 71)

window.resizable(False, False)
window.mainloop()
