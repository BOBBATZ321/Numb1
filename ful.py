import math
from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.geometry("720x480+500+100")
window.resizable(False, False)
window.title("Calculadora de mierda")
window.config(background="#FFE4B5" )
expression = ""

result = StringVar()
expression_field = Entry(textvariable=result, font=("Arial Black", 10), state=DISABLED)
expression_field.grid(columnspan=6, ipadx=150,  ipady=10, column=2)
expression_field.insert(0, "Добро пожаловать в изобретение века!!!")




lb = Label(text="История: \n", font=("Arial Black", 11) )
lb.place(x=10, y= 320)

def dl_store():
    global lb
    r = "История: \n"
    lb.config(text= r + "")

bt = Button(text="Стереть \n историю", font=("Bahnschrift SemiLight Condensed", 14),  command=dl_store)
bt.place(x=12, y= 253)



# expression_field.pack()
# expression_field.bind('',lambda expression_field:"break"if expression_field.keysym not in(list("1234567890-.")+['BackSpace','Delete','Left','Right'])else"")

lbl = Label(text="Бабенко Петр 49гр")
lbl.grid(column=0, row=0)

def press_num(num):
    global expression
    expression += str(num)
    result.set(expression)

def delete():
    global expression
    expression = expression[0:-1]
    result.set(expression)

def procent():
    global expression
    total = str((eval(expression)) / 100)
    result.set(total)
    r = "История: \n"
    lb.config(text=r + "%" + expression + "=" + total)
    expression = total

# def ravnopress():
#     try:
#         global expression
#         r = "="
#         total = str(eval(expression))
#         result.set(r + total)
#         expression = total
#     except:
#         result.set("Вы Ошибка!")
#         expression = ""
def ravnopress():
    try:
        global expression
        res = result.get()
        total = str(eval(res))
        result.set(total)
        r = "История: \n"
        lb.config(text = r + expression + "="  +  total)
        expression = total
    except:
        result.set("Вы Ошибка!")
        expression = ""

def reset():
    global expression
    total = ""
    result.set(total)
    expression = total

def fac():
    global expression
    total = str(math.factorial(eval(expression)))
    result.set(total)
    r = "История: \n"
    lb.config(text=r + "x!" + expression + "=" + total)
    expression = total

def log():
    global expression
    total = str(math.log10(eval(expression)))
    result.set(total)
    r = "История: \n"
    lb.config(text=r + "log!" + expression + "=" + total)
    expression = total

def ln():
    global expression
    total = str(math.log(eval(expression)))
    result.set(total)
    r = "История: \n"
    lb.config(text=r + "ln!" + expression + "=" + total)
    expression = total

def coren():
    global expression
    total = str(math.sqrt(eval(expression)))
    result.set(total)
    r = "История: \n"
    lb.config(text=r + "√" + expression + "=" + total)
    expression = total

# def сtan():
#     global expression
#     total = str(math.(int(expression)))
#     result.set(total)
#     expression = total???????????????????????????

def clicked():

        def sin():
            global expression
            total = str(math.sin(eval(expression)))
            result.set(total)
            r = "История: \n"
            lb.config(text=r + "Sin!" + expression + "=" + total)
            expression = total

        def cos():
            global expression
            total = str(math.cos(eval(expression)))
            result.set(total)
            r = "История: \n"
            lb.config(text=r + "Cos!" + expression + "=" + total)
            expression = total

        def tan():
            global expression
            total = str(math.tan(eval(expression)))
            result.set(total)
            r = "История: \n"
            lb.config(text=r + "Tan!" + expression + "=" + total)
            expression = total

        def pi():
            global expression
            total = str(3.14159265359)
            result.set(total)
            r = "История: \n"
            lb.config(text=r + "π" + "=" + total)
            expression = total

        def mod():
            global expression
            total = str(math.modf(eval(expression)))
            result.set(total)
            r = "История: \n"
            lb.config(text=r + "Остаток от деления: " + expression + " = " + total)
            expression = total

        def trun():
            global expression
            total = str(math.trunc(eval(expression)))
            result.set(total)
            r = "История: \n"
            lb.config(text=r + "Округление числа: " + expression + " до целого = " + total)
            expression = total

        def exp():
            global expression
            total = str(math.exp(eval(expression)))
            result.set(total)
            expression = total
            r = "История: \n"
            lb.config(text=r + "E" + expression + " = " + total)
            expression = total



        lbl = Label(text="Help me!!!")
        lbl.grid(row=0, column=1)

        mod1 = Button(text="MOD", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15),command= mod)
        mod1.config(background="#C0C0C0")
        mod1.grid(row=6, column=3)

        trun1 = Button(text="Trun", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15),
                         command= trun)
        trun1.config(background="#C0C0C0")
        trun1.grid(row=6, column=4)

        e = Button(text="E", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15),
                         command=exp)
        e.config(background="#C0C0C0")
        e.grid(row=6, column=5)

        # button4 = Button(text="4", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15),
        #                  command=lambda: press_num(4))
        # button4.config(background="#C0C0C0")
        # button4.grid(row=7, column=3)
        #
        # button5 = Button(text="5", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15),
        #                  command=lambda: press_num(5))
        # button5.config(background="#C0C0C0")
        # button5.grid(row=7, column=4)
        #
        # button6 = Button(text="6", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15),
        #                  command=lambda: press_num(6))
        # button6.config(background="#C0C0C0")
        # button6.grid(row=7, column=5)
        #
        # button7 = Button(text="7", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15),
        #                  command=lambda: press_num(7))
        # button7.config(background="#C0C0C0")
        # button7.grid(row=6, column=3)
        #
        # button8 = Button(text="8", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15),
        #                  command=lambda: press_num(8))
        # button8.config(background="#C0C0C0")
        # button8.grid(row=6, column=4)
        #
        # button9 = Button(text="9", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15),
        #                  command=lambda: press_num(9))
        # button9.config(background="#C0C0C0")
        # button9.grid(row=6, column=5)

        sin = Button(text="Sin", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command=sin)
        sin.config(background="#C0C0C0")
        sin.grid(row=2, column=1)

        cos = Button(text="Cos", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command=cos)
        cos.config(background="#C0C0C0")
        cos.grid(row=3, column=1)

        tan = Button(text="Tan", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command=tan)
        tan.config(background="#C0C0C0")
        tan.grid(row=4, column=1)

        pi = Button(text="π", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command=pi)
        pi.config(background="#C0C0C0")
        pi.grid(row=3, column=0)

        # button0 = Button(text="0", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command=lambda: press_num(0))
        # button0.config(background="#C0C0C0")
        # button0.grid(row=9, column=3)

button1 = Button(text = "1", height=1, width=5,font=("Arial Black", 12), command=lambda: press_num(1))
button1.config(background="#F5FFFA")
button1.grid(row=4, column=3)

button2 = Button(text = "2", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num(2))
button2.config(background="#F5FFFA")
button2.grid(row=4, column=4)

button3 = Button(text = "3", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num(3))
button3.config(background="#F5FFFA")
button3.grid(row=4, column=5)

button4 = Button(text = "4", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num(4))
button4.config(background="#F5FFFA")
button4.grid(row=3, column=3)

button5 = Button(text = "5", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num(5))
button5.config(background="#F5FFFA")
button5.grid(row=3, column=4)

button6 = Button(text = "6", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num(6))
button6.config(background="#F5FFFA")
button6.grid(row=3, column=5)

button7 = Button(text = "7", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num(7))
button7.config(background="#F5FFFA")
button7.grid(row=2, column=3)

button8 = Button(text = "8", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num(8))
button8.config(background="#F5FFFA")
button8.grid(row=2, column=4)

button9 = Button(text = "9", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num(9))
button9.config(background="#F5FFFA")
button9.grid(row=2, column=5)

button0 = Button(text = "0", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num(0))
button0.config(background="#F5FFFA")
button0.grid(row=5, column=3)

plus = Button(text = "+", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num("+"))
plus.config(background="#C0C0C0")
plus.grid(row=5, column=6)

minus = Button(text = "-", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num("-"))
minus.config(background="#C0C0C0")
minus.grid(row=4, column=6)

ravno = Button(text = "=", height=1, width=5, font=("Arial Black", 12), command=ravnopress)
ravno.config(background="#C0C0C0")
ravno.grid(row=5, column=5)

umn = Button(text = "*", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num("*"))
umn.config(background="#C0C0C0")
umn.grid(row=3, column=6)

delen = Button(text = "/", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num("/"))
delen.config(background="#C0C0C0")
delen.grid(row=2, column=6)

tohcka = Button(text = ".", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num("."))
tohcka.config(background="#F5FFFA")
tohcka.grid(row=5, column=4)

reset = Button(text = "C", height=1, width=5, font=("Arial Black", 12), command=reset)
reset.config(background="#C0C0C0")
reset.grid(row=1, column=6)

skobga1 = Button(text = ")", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num(")"))
skobga1.config(background="#C0C0C0")
skobga1.grid(row=1, column=4)

skobga2 = Button(text = "(", height=1, width=5, font=("Arial Black", 12), command=lambda: press_num("("))
skobga2.config(background="#C0C0C0")
skobga2.grid(row=1, column=3)

Dele = Button(text = "<-", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command=delete)
Dele.config(background="#C0C0C0")
Dele.grid(row=1, column=7)

procent = Button(text = "%", height=1, width=5, font=("Arial Black", 12), command=procent)
procent.config(background="#C0C0C0")
procent.grid(row=1, column=5)

stepen = Button(text = "x^", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command = lambda : press_num("**"))
stepen.config(background="#C0C0C0")
stepen.grid(row=5, column=2)

factorial = Button(text = "x!", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command = fac)
factorial.config(background="#C0C0C0")
factorial.grid(row=1, column=2)

logor10 = Button(text = "log", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command = log)
logor10.config(background="#C0C0C0")
logor10.grid(row=3, column=2)

logor = Button(text = "ln", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command = ln)
logor.config(background="#C0C0C0")
logor.grid(row=2, column=2)

coren = Button(text = "√", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command = coren)
coren.config(background="#C0C0C0")
coren.grid(row=4, column=2)

close = Button(text="CLOSE", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command= lambda: window.destroy())
close.config(background="#C0C0C0")
close.grid(row=3, column=7)

boot = Button(window,text="BOOT", height=1, width=5, font=("Bahnschrift SemiLight Condensed", 15), command = clicked)
boot.config(background="#C0C0C0")
boot.grid(row=2, column=7)

def radian():
    acrual_radio = selected.get()
    umn = 1
    if acrual_radio == 1:
        umn = (3.1416 / 180)
    elif acrual_radio == 2:
        umn = (180 / 3.1416)

    global expression
    total = str(eval(expression) * umn)
    result.set(total)
    expression = total

selected = IntVar()
rad1 = Radiobutton(window,text='Радианы', value=1, variable=selected)
rad2 = Radiobutton(window,text='градусы', value=2, variable=selected)
rad3 = Radiobutton(window,text='Блокировка \n перевода', value=3, variable=selected)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=7, row=4)

vd = Button(text="Перевод", height= 2, width= 7, command= radian)
vd.grid(row=2, column=0 )

# c = Combobox(text="fuc")
# c.grid(row=0, column=0)

window.mainloop()

