# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
#######################################################################
##КЛАССИФИКАЦИЯ
#######################################################################
import classification.C_4_5.tree as с45
import classification.Naive_Bayes_Classifier.BayesScratch.bayes_classifier as bayes
import classification.k_Nearest_Neighbors.knn as knn
import clustering.Hierarchical_clustering.hclust as hc
import clustering.Hierarchical_clustering.hierarchical_clustering_plot as hc_plot
import clustering.DBSCAN.plot_dbscan as dbscan
import clustering.BIRCH.birch_clustering as birch
import clustering.mean_shift.plot_mean_shift as mean_shift
import input_output.io as io
import classification.Stochastic_Gradient_Descent.sgd as sgd
import utils.text_processing as text_proc
#import associative_rules.apriori_tid.apriori as apriori_tid
#import classification.Linear_Least_Squares_Classifier.LLS as lls
import clustering.Affinity_Propagation.AffinityPropagation as aff_p
import clustering.k_means.k_means as kmen
from tkinter import *
from tkinter.messagebox import *
from associative_rules.apriori_tid.apriori import *

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
    print("=========================================================")

#######################################################################
##КЛАСТЕРИЗАЦИЯ
#######################################################################

def mean_shift_run(event):
    oformlenie()
    print("Mean Shift")
    oformlenie()
    mean_shift.run(txter_claster.get())
    oformlenie_end()

def affinity_propagation_run(event) :
    oformlenie()
    aff_p.compute_affinity_propagation("clustering\\Affinity_Propagation\\input_data.txt")
    oformlenie()
    oformlenie_end()

def dbscan_run(event):
    oformlenie()
    dbscan.dbscan_run("clustering\\DBSCAN\\input_data.txt")
    oformlenie()
    oformlenie_end()

def k_means_run(event):
    oformlenie()
    kmen.run()
    oformlenie()
    #запуск стартера, т.к. в нем есть подключение к бд
 #   dir = os.path.abspath(os.curdir)+"//clustering//k_means//run_data.sh 1"
 #   os.popen(dir)#"run_data.sh", cwd=r"C/1/ProjectOfDataMining/classification/Linear_Least_Squares_Classifierr")
    oformlenie_end()

def hierarchical_clustering_run(event):
    oformlenie()
    print("Hierarchical clustering")
    hc_plot.run("clustering\\Hierarchical_clustering\\input_data.txt")
    oformlenie_end()

def birch_run(event):
    oformlenie()
    print("BIRCH clustering")
    birch.run("clustering\\BIRCH\\input_data.txt")
    oformlenie_end()

#######################################################################
##АССОЦИАТИВНЫЕ ПРАВИЛА
#######################################################################

def run_apriori_tid(event):
    oformlenie()
    print("Apriori TID")
    oformlenie()
    data_iter = dataFromFile('associative_rules/apriori_tid/tesco.csv')
    items, rules = runApriori(data_iter, 0.5, 0.05)
    printResults(items, rules)

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
    
def lls_run(event):
    oformlenie()
    print("LLS")
    oformlenie()
    #запуск стартера, т.к. в нем есть подключение к бд
   # dir = os.path.abspath(os.curdir)+"//classification//Linear_Least_Squares_Classifier//run_data.sh 1"
   # os.popen(dir)#"run_data.sh", cwd=r"C/1/ProjectOfDataMining/classification/Linear_Least_Squares_Classifierr")
    
    oformlenie_end()    

def sgd_run(event):
    oformlenie()
    print("Stochastic Gradient Descent")
    sgd.run("")
    oformlenie_end()

def bayes_run(event):
    oformlenie()
    print("Naive Bayes Algorithm")
    bayes.main("classification/Naive_Bayes_Classifier/BayesScratch/pima-indians-diabetes.csv")
    oformlenie_end()

def knn_run(event):
    oformlenie()
    print("k-Nearest Neighbors")
    knn.main()   
    oformlenie_end()

def exit_prog(event):
    exit(0);
		
#########
# Скрыть/показать текстовое поле для пути к файлу с данными.
# Осуществляется с помощью RadioButton-виджетов
#########

def show_entry_claster():
    if radioItem_claster.get() == 2:
        txter_claster.grid_remove()
        lab_claster.grid_remove()
    else:
        lab_claster.grid(row=2, column=1)
        txter_claster.grid(row=2, column=2)
		
def show_entry_classif():
    if radioItem_classif.get() == 2:
        txter_classif.grid_remove()
        lab_classif.grid_remove()
    else:
        lab_classif.grid(row=2, column=1)
        txter_classif.grid(row=2, column=2)
		
def show_entry_search_rules():
    if radioItem_search_rules.get() == 2:
        txter_search_rules.grid_remove()
        lab_search_rules.grid_remove()
    else:
        lab_search_rules.grid(row=2, column=1)
        txter_search_rules.grid(row=2, column=2)
		
root = Tk()
root.title("Главное окно")
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
child_classif.bind("<Destroy>", exit_prog);
child_classif.withdraw()

radioItem_classif = IntVar()
radioItem_classif.set(1)

radCsv_classif = Radiobutton(child_classif, text="Считать с csv-файла", variable=radioItem_classif, value=0, command=show_entry_classif)
radCsv_classif.grid(row=1, column=0, sticky=W)

radInternet_classif = Radiobutton(child_classif, text="Считать с интернета", variable=radioItem_classif, value=1, command=show_entry_classif)
radInternet_classif.grid(row=2, column=0, sticky=W)

radRandom_classif = Radiobutton(child_classif, text="Генерировать случайно", variable=radioItem_classif, value=2, command=show_entry_classif)
radRandom_classif.grid(row=3, column=0, sticky=W)

lab_classif = Label(child_classif, text="Путь: ")
lab_classif.grid(row=2, column=1)
txter_classif = Entry(child_classif, width=20)
txter_classif.grid(row=2, column=2)

child_classif_btn1 = Button(child_classif, text="C 4.5", width=50)
child_classif_btn1.bind("<Button-1>", С_4_5_run)
child_classif_btn1.grid(row=4, column=0, columnspan=3)

child_classif_btn2 = Button(child_classif, text="k Nearest Neighbors")
child_classif_btn2.bind("<Button-1>", knn_run)
child_classif_btn2.grid(row=5, column=0, columnspan=3, sticky=W+N+S+E)

child_classif_btn3 = Button(child_classif, text="Linear Least Squares Classifier")
child_classif_btn3.bind("<Button-1>", lls_run)
child_classif_btn3.grid(row=6, column=0, columnspan=3, sticky=W+N+S+E)

child_classif_btn5 = Button(child_classif, text="Naive Bayes Classifier")
child_classif_btn5.bind("<Button-1>", bayes_run)
child_classif_btn5.grid(row=7, column=0, columnspan=3, sticky=W+N+S+E)

child_classif_btn6 = Button(child_classif, text="Алгоритм опорных векторов")
child_classif_btn6.grid(row=8, column=0, columnspan=3, sticky=W+N+S+E)

child_classif_btn7 = Button(child_classif, text="Алгоритм Роккио")
child_classif_btn7.grid(row=9, column=0, columnspan=3, sticky=W+N+S+E)

child_classif_btn8 = Button(child_classif, text="Stochastic Gradient Descent")
child_classif_btn8.bind("<Button-1>", sgd_run)
child_classif_btn8.grid(row=10, column=0, columnspan=3, sticky=W+N+S+E)

child_classif_btn4 = Button(child_classif, text="Назад")
child_classif_btn4.bind("<Button-1>", show_hide_child_classif)
child_classif_btn4.grid(row=11, column=0, columnspan=3, sticky=W+N+S+E)

child_claster = Toplevel(root)
child_claster.title("Кластеризация")
child_claster.bind("<Destroy>", exit_prog);
child_claster.withdraw()

radioItem_claster = IntVar()
radioItem_claster.set(1)

radCsv_claster = Radiobutton(child_claster, text="Считать с csv-файла", variable=radioItem_claster, value=0, command=show_entry_claster)
radCsv_claster.grid(row=1, column=0, sticky=W)

radInternet_claster = Radiobutton(child_claster, text="Считать с интернета", variable=radioItem_claster, value=1, command=show_entry_claster)
radInternet_claster.grid(row=2, column=0, sticky=W)

radRandom_claster = Radiobutton(child_claster, text="Генерировать случайно", variable=radioItem_claster, value=2, command=show_entry_claster)
radRandom_claster.grid(row=3, column=0, sticky=W)

lab_claster = Label(child_claster, text="Путь: ")
lab_claster.grid(row=2, column=1)
txter_claster = Entry(child_claster, width=20)
txter_claster.grid(row=2, column=2)

child_claster_btn1 = Button(child_claster, text="Mean Shift", width=50)
child_claster_btn1.bind("<Button-1>", mean_shift_run)
child_claster_btn1.grid(row=4, column=0, columnspan=3)

child_claster_btn2 = Button(child_claster, text="K-means")
child_claster_btn2.bind("<Button-1>", k_means_run)
child_claster_btn2.grid(row=5, column=0, columnspan=3, sticky=W+N+S+E)

child_claster_btn3 = Button(child_claster, text="Hierarchical clustering")
child_claster_btn3.bind("<Button-1>", hierarchical_clustering_run)
child_claster_btn3.grid(row=6, column=0, columnspan=3, sticky=W+N+S+E)

child_claster_btn5 = Button(child_claster, text="DBSCAN")
child_claster_btn5.bind("<Button-1>", dbscan_run)
child_claster_btn5.grid(row=7, column=0, columnspan=3, sticky=W+N+S+E)

child_claster_btn7 = Button(child_claster, text="BIRCH")
child_claster_btn7.bind("<Button-1>", birch_run)
child_claster_btn7.grid(row=8, column=0, columnspan=3, sticky=W+N+S+E)

child_claster_btn6 = Button(child_claster, text="Affinity Propagation")
child_claster_btn6.bind("<Button-1>", affinity_propagation_run)
child_claster_btn6.grid(row=9, column=0, columnspan=3, sticky=W+N+S+E)

child_claster_btn4 = Button(child_claster, text="Назад")
child_claster_btn4.bind("<Button-1>", show_hide_child_claster)
child_claster_btn4.grid(row=10, column=0, columnspan=3, sticky=W+N+S+E)

child_search_rules = Toplevel(root)
child_search_rules.title("Поиск ассоциативных правил")
child_search_rules.bind("<Destroy>", exit_prog);
child_search_rules.withdraw()

radioItem_search_rules = IntVar()
radioItem_search_rules.set(1)

radCsv_search_rules = Radiobutton(child_search_rules, text="Считать с csv-файла", variable=radioItem_search_rules, value=0, command=show_entry_search_rules)
radCsv_search_rules.grid(row=1, column=0, sticky=W)

radInternet_search_rules = Radiobutton(child_search_rules, text="Считать с интернета", variable=radioItem_search_rules, value=1, command=show_entry_search_rules)
radInternet_search_rules.grid(row=2, column=0, sticky=W)

radRandom_search_rules = Radiobutton(child_search_rules, text="Генерировать случайно", variable=radioItem_search_rules, value=2, command=show_entry_search_rules)
radRandom_search_rules.grid(row=3, column=0, sticky=W)

lab_search_rules = Label(child_search_rules, text="Путь: ")
lab_search_rules.grid(row=2, column=1)
txter_search_rules = Entry(child_search_rules, width=20)
txter_search_rules.grid(row=2, column=2)

child_search_rules_btn1 = Button(child_search_rules, text="Apriori Hybrid", width=50)
child_search_rules_btn1.grid(row=4, column=0, columnspan=3)

child_search_rules_btn2 = Button(child_search_rules, text="ID3")
child_search_rules_btn2.grid(row=5, column=0, columnspan=3, sticky=W+N+S+E)

child_search_rules_btn3 = Button(child_search_rules, text="Apriori TID")
child_search_rules_btn3.bind("<Button-1>", run_apriori_tid)
child_search_rules_btn3.grid(row=6, column=0, columnspan=3, sticky=W+N+S+E)

child_search_rules_btn4 = Button(child_search_rules, text="Назад")
child_search_rules_btn4.bind("<Button-1>", show_hide_child_search_rules)
child_search_rules_btn4.grid(row=7, column=0, columnspan=3, sticky=W+N+S+E)

root.mainloop()
