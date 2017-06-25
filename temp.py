# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

from tkinter import *
from tkinter.messagebox import *

flag_child_classif = False
flag_child_claster = False
flag_child_search_rules = False

def show_hide_child_classif(event):
    global flag_child_classif
    
    if (flag_child_classif == False):
        flag_child_classif = True
        child_classif.deiconify()
        root.withdraw()
    else:
        flag_child_classif = False
        child_classif.withdraw()
        root.deiconify()


def show_hide_child_claster(event):
    global flag_child_claster
    
    if (flag_child_claster == False):
        flag_child_claster = True
        child_claster.deiconify()
        root.withdraw()
    else:
        flag_child_claster = False
        child_claster.withdraw()
        root.deiconify()
    
def show_hide_child_search_rules(event):
    global flag_child_search_rules
    
    if (flag_child_search_rules == False):
        flag_child_search_rules = True
        child_search_rules.deiconify()
        root.withdraw()
    else:
        flag_child_search_rules = False
        child_search_rules.withdraw()
        root.deiconify()


root = Tk()
root.title("Главное окно")
root.geometry("400x200")

btn1 = Button(root, text="Классификация")
btn1.bind("<Button-1>", show_hide_child_classif)
btn1.pack(fill=X)

btn2 = Button(root, text="Кластеризация")
btn2.bind("<Button-1>", show_hide_child_claster)
btn2.pack(fill=X)

btn3 = Button(root, text="Поиск ассоциативных правил")
btn3.bind("<Button-1>", show_hide_child_search_rules)
btn3.pack(fill=X)



child_classif = Toplevel(root)
child_classif.title("Классификация")
child_classif.geometry("400x200")
child_classif.withdraw()

child_classif_btn1 = Button(child_classif, text="Метод классификации 1")
child_classif_btn1.pack(fill=X)

child_classif_btn2 = Button(child_classif, text="Метод классификации 2")
child_classif_btn2.pack(fill=X)

child_classif_btn3 = Button(child_classif, text="Метод классификации 3")
child_classif_btn3.pack(fill=X)

child_classif_btn4 = Button(child_classif, text="Назад")
child_classif_btn4.bind("<Button-1>", show_hide_child_classif)
child_classif_btn4.pack(fill=X)



child_claster = Toplevel(root)
child_claster.title("Класстеризация")
child_claster.geometry("400x200")
child_claster.withdraw()

child_claster_btn1 = Button(child_claster, text="Метод класстеризация 1")
child_claster_btn1.pack(fill=X)

child_claster_btn2 = Button(child_claster, text="Метод класстеризация 2")
child_claster_btn2.pack(fill=X)

child_claster_btn3 = Button(child_claster, text="Метод класстеризация 3")
child_claster_btn3.pack(fill=X)

child_claster_btn4 = Button(child_claster, text="Назад")
child_claster_btn4.bind("<Button-1>", show_hide_child_claster)
child_claster_btn4.pack(fill=X)



child_search_rules = Toplevel(root)
child_search_rules.title("Поиск ассоциативных правил")
child_search_rules.geometry("400x200")
child_search_rules.withdraw()

child_search_rules_btn1 = Button(child_search_rules, text="Метод поиск ассоциативных правил 3")
child_search_rules_btn1.pack(fill=X)

child_search_rules_btn2 = Button(child_search_rules, text="Метод поиск ассоциативных правил 3")
child_search_rules_btn2.pack(fill=X)

child_search_rules_btn3 = Button(child_search_rules, text="Метод поиск ассоциативных правил 3")
child_search_rules_btn3.pack(fill=X)

child_search_rules_btn4 = Button(child_search_rules, text="Назад")
child_search_rules_btn4.bind("<Button-1>", show_hide_child_search_rules)
child_search_rules_btn4.pack(fill=X)

root.mainloop()

#child = Toplevel(root)
#child.title("Дочернее окно")
#child.geometry("400x200")    
#child.withdraw()

#btn2 = Button(child, text="Кнопка")
#btn2.bind("<Button-1>", show_hide)
#btn2.pack()







