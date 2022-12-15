import sqlite3
from sqlite3 import Cursor
from tkinter import *
import random
#cоздание бд
with sqlite3.connect("passport.db") as db:
    cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS passport(
id integer PRIMARY KEY,
name text NOT NULL,
surname text NOT NULL,
tries integer);""")
#регистрация пользователя, запись имени, фамилии, id
def regist():
    passid = random.randint(100000, 999999)
    entry_box = Entry()
    entry_box.insert(0, passid)
    entry_box.place(x=50, y=20, width=100, height=25)
    newname = name_input.get()
    newsurname = surname_input.get()
    newid = entry_box.get()
    cursor.execute("""INSERT INTO passport(id,name,surname,tries)
    VALUES(?, ?, ?, ?)""",(newid,newname, newsurname))
    db.commit()
#создание первого окна
window = Tk()
window.title("PASSPORT TABLE")
window.geometry("1000x500")
window["bg"] = "#a49eba"

label = Label(text="Ваш id, сохраните")
label.place(x=50, y=50, width=100, height=25)

label = Label(text="Введите данные для регистрации")
label.place(x=410, y=100, width=200, height=50)

label = Label(text="Имя")
label.place(x=300, y=200, width=125, height=25)


label = Label(text="Фамилия")
label.place(x=600, y=200, width=125, height=25)

name_input = Entry()
name_input.place(x=300, y=250, width=125, height=25)

surname_input = Entry()
surname_input.place(x=600, y=250, width=125, height=25)
#кликабельная кнопка ссылающая на функцию regist
button_ins = Button(text="Зарегестрировать",command=regist, font="georgia 8")
button_ins.place(x=350, y=400, width=120, height=25)
button_ins.size()
button_ins["bg"] = "#948eab"
button_ins["activebackground"] = "#7f7994"
#окно проверки присутствия id в бд
def check_place():
    #экзамен гаи
    def examen():
        #все реализовано через if, после одной ошибки экзамен не сдан
        def resh():
            if select1.get() == "Только с места установки дорожного знака «Начало населенного пункта» на белом фоне" and select2.get() == "Допускается только при доставке грузов к торговым и другим предприятиям, расположенным непосредственно у тротуаров или пешеходных дорожек, если отсутствуют другие возможности подъезда." and select3.get() == "Только совместно с ближним или дальним светом фар." and select4.get() == "Только мотоциклы без бокового прицепа." and select5.get() == "50 км/ч":
                label8 = Label(test,text="Молодец,ты сдал!!!!")
                label8.place(x=350, y=300)
                label8["fg"] = "green"
            else:
                label9 = Label(test, text="К сожалению ты не сдал(((")
                label9.place(x=350, y=300)
                label9["fg"] = "red"
        #withdraw скрывает окна
        exam.withdraw()
        test= Tk()
        test.title("test")
        test.geometry("800x500")
        label3 = Label(test,text="Где начинают действовать требования Правил, относящиеся к населенным пунктам?")
        label3.place(x=10, y=50)
        select1 = StringVar(test)
        select1.set("Выберите ответ из предложенных")
        option1 = OptionMenu(test,select1,"Только с места установки дорожного знака «Начало населенного пункта» на белом фоне","С места установки дорожного знака с названием населенного пункта на белом или синем фоне","В начале застроенной территории, непосредственно прилегающей к дороге")
        option1.place(x=550, y=50)
        label4 = Label(test, text="Допускается ли движение автомобилей по тротуарам\n или пешеходным дорожкам?")
        label4.place(x=10, y=100)
        select2 = StringVar(test)
        select2.set("Выберите ответ из предложенных")
        option2 = OptionMenu(test, select2,"Допускается", "Допускается только при доставке грузов к торговым и другим предприятиям, расположенным непосредственно у тротуаров или пешеходных дорожек, если отсутствуют другие возможности подъезда.","Не допускается")
        option2.place(x=550, y=100)
 # Допускается
# Допускается только при доставке грузов к торговым и другим предприятиям, расположенным непосредственно у тротуаров или пешеходных дорожек, если отсутствуют другие возможности подъезда. pr
# Не допускается
        label5 = Label(test, text="При движении в условиях недостаточной видимости можно использовать\n противотуманные фары:")
        label5.place(x=10, y=150)
        select3 = StringVar(test)
        select3.set("Выберите ответ из предложенных")
        option3 = OptionMenu(test, select3,"Только отдельно от ближнего  или дальнего света фар.","Только совместно с ближним или дальним светом фар.","Как отдельно, так и совместно с ближним или дальним светом  фар.")
        option3.place(x=550, y=150)
        # Только отдельно от ближнего  или дальнего света фар.
        # Только совместно с ближним или дальним светом фар. pr
        # Как отдельно, так и совместно с ближним или дальним светом  фар.
        label6 = Label(test, text="Какие из перечисленных транспортных средств разрешается эксплуатировать\n без медицинской аптечки?")
        label6.place(x=10, y=200)
        select4 = StringVar(test)
        select4.set("Выберите ответ из предложенных")
        option4 = OptionMenu(test, select4,"Автомобили.","Все мотоциклы.","Только мотоциклы без бокового прицепа.")
        option4.place(x=550, y=200)
        # Автомобили.
        #  Все мотоциклы.
        # Только мотоциклы без бокового прицепа. pr
        label7 = Label(test, text="С какой максимальной скоростью разрешается продолжить движение при\n буксировке неисправного механического транспортного средства?")
        label7.place(x=10, y=250)
        select5 = StringVar(test)
        select5.set("Выберите ответ из предложенных")
        option5 = OptionMenu(test, select5,"50 км/ч","70 км/ч","90 км/ч")
        option5.place(x=550, y=250)
        # 50 км/ч.pr
        # 70 км/ч.
        # 90 км/ч
        button_test = Button(test, text="Завершить", command=resh, font="georgia 8")
        button_test.place(x=350, y=350)
    def checking():
        #проверяет на наличе в бд
        checks = passex.get()
        cursor.execute(f"SELECT * FROM passport WHERE id = '{checks}'")
        if not cursor.fetchone():
         label1 = Label(exam,text="Вас нет в базе!!!")
         label1.place(x=200, y=50, width=125, height=25)
         label1["fg"] = "red"
         button_exam["state"]="disabled"
        else:
            label2 = Label(exam, text="Всё отлично!!!")
            label2.place(x=200, y=50, width=125, height=25)
            label2["fg"] = "green"
            button_exam["state"] = "active"

    window.withdraw()
    exam = Tk()
    exam.title("exam")
    exam.geometry("500x500")
    label = Label(exam, text="Введите ваш id")
    label.place(x=200, y=250, width=125, height=25)
    passex = Entry(exam)
    passex.place(x=200, y=200, width=125, height=25)

    button_exam = Button(exam, text="Начать экзамен",command=examen, font="georgia 8")
    button_exam["state"]="disabled"
    button_exam.place(x=200, y=300, width=120, height=25)
    button_check = Button(exam, text="Проверить id",command=checking, font="georgia 8")
    button_check.place(x=200, y=150, width=120, height=25)


button_ins = Button(text="Дальше",command=check_place, font="georgia 8")
button_ins.place(x=550, y=400, width=120, height=25)
button_ins.size()
button_ins["bg"] = "#948eab"
button_ins["activebackground"] = "#7f7994"

window.mainloop()

db.close()