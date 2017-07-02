# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import clustering.mean_shift.mean_shift_runner as msr
import classification.C_4_5.tree as с45
#import clustering.kmeans.kmeans as k_means #подключение k-means

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


def oformlenie():
    print("=========================================================")

def oformlenie_end():
    print("====================End of execution=====================")

#######################################################################
##КЛАСТЕРИЗАЦИЯ
#######################################################################

def mean_shift_run(event):
    oformlenie()
    print("Mean Shift")
    oformlenie()
    if __name__ == '__main__':
        msr.run()
    oformlenie_end()

        
#def k_means_run(event):
#    if __name__ == '__main__':
#        k_means.run() 

#######################################################################
##КЛАССИФИКАЦИЯ
#######################################################################
def С_4_5_run(event):
    oformlenie()
    print("C 4.5")
    oformlenie()
    if __name__ == '__main__':
        с45.run_decision_tree()   
    oformlenie_end()

def exit_prog(event):
    exit(0);
		
root = Tk()
root.title("Главное окно")
root.geometry("400x200")
root.bind("<Destroy>", exit_prog);

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
child_classif.bind("<Destroy>", exit_prog);
child_classif.withdraw()

child_classif_btn1 = Button(child_classif, text="C 4.5")
child_classif_btn1.bind("<Button-1>", С_4_5_run)
child_classif_btn1.pack(fill=X)

child_classif_btn2 = Button(child_classif, text="k Nearest Neighbors")
child_classif_btn2.pack(fill=X)

child_classif_btn3 = Button(child_classif, text="Linear Least Squares Classifier")
child_classif_btn3.pack(fill=X)

child_classif_btn5 = Button(child_classif, text="Naive Bayes Classifier")
child_classif_btn5.pack(fill=X)

child_classif_btn6 = Button(child_classif, text="Алгоритм опорных векторов")
child_classif_btn6.pack(fill=X)

child_classif_btn7 = Button(child_classif, text="Алгоритм Роккио")
child_classif_btn7.pack(fill=X)

child_classif_btn4 = Button(child_classif, text="Назад")
child_classif_btn4.bind("<Button-1>", show_hide_child_classif)
child_classif_btn4.pack(fill=X)



child_claster = Toplevel(root)
child_claster.title("Класстеризация")
child_claster.geometry("400x200")
child_claster.bind("<Destroy>", exit_prog);
child_claster.withdraw()

child_claster_btn1 = Button(child_claster, text="Mean Shift")
child_claster_btn1.bind("<Button-1>", mean_shift_run)
child_claster_btn1.pack(fill=X)

child_claster_btn2 = Button(child_claster, text="K-means")
#child_claster_btn1.bind("<Button-1>", k_means_run)
child_claster_btn2.pack(fill=X)

child_claster_btn3 = Button(child_claster, text="Hierarchical clustering")
child_claster_btn3.pack(fill=X)

child_claster_btn5 = Button(child_claster, text="DBSCAN")
child_claster_btn5.pack(fill=X)

child_claster_btn6 = Button(child_claster, text="Affinity Propagation")
child_claster_btn6.pack(fill=X)

child_claster_btn4 = Button(child_claster, text="Назад")
child_claster_btn4.bind("<Button-1>", show_hide_child_claster)
child_claster_btn4.pack(fill=X)



child_search_rules = Toplevel(root)
child_search_rules.title("Поиск ассоциативных правил")
child_search_rules.geometry("400x200")
child_search_rules.bind("<Destroy>", exit_prog);
child_search_rules.withdraw()

child_search_rules_btn1 = Button(child_search_rules, text="Apriori Hybrid")
child_search_rules_btn1.pack(fill=X)

child_search_rules_btn2 = Button(child_search_rules, text="ID3")
child_search_rules_btn2.pack(fill=X)

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







