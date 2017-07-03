# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 04:09:09 2017

@author: K
"""
#import clustering.k_means.k_means as km

import classification.C_4_5.tree as с45
#import classification.Linear_Least_Squares_Classifier.LLS as lls
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
    print("=========================================================")

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


def k_means_run(event):
    oformlenie()
    print("K-means")
    oformlenie()
    #запуск стартера, т.к. в нем есть подключение к бд
 #   dir = os.path.abspath(os.curdir)+"//clustering//k_means//run_data.sh 1"
 #   os.popen(dir)#"run_data.sh", cwd=r"C/1/ProjectOfDataMining/classification/Linear_Least_Squares_Classifierr")
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
    
def lls_run(event):
    oformlenie()
    print("LLS")
    oformlenie()
    #запуск стартера, т.к. в нем есть подключение к бд
   # dir = os.path.abspath(os.curdir)+"//classification//Linear_Least_Squares_Classifier//run_data.sh 1"
   # os.popen(dir)#"run_data.sh", cwd=r"C/1/ProjectOfDataMining/classification/Linear_Least_Squares_Classifierr")
    
    oformlenie_end()    
    

def exit_prog(event):
    exit(0);
		