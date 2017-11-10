import numpy as np
import numpy as np
import openpyxl
import xlrd
import csv
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from sklearn.datasets import load_iris
from sklearn.datasets.samples_generator import make_blobs  #импорт библиотеки для генерации
from openpyxl import load_workbook
from sklearn.tree import DecisionTreeClassifier


#значения по умолчанию
cel_0_1 = 0
cel_1_1 = 1

cel_2_1 = 0
cel_2_2 = 2

cel_3_1 = 0
cel_3_3 = 3

cel_4_1 = 1
cel_4_3 = 2

cel_5_1 = 1
cel_5_3 = 3

cel_6_1 = 2
cel_6_3 = 3


def read_Excel(b):
    wb = load_workbook('data.xlsx')
    sheet = wb.get_sheet_by_name('sheetname')

    #n_samples = sheet['E10'].value
    
    #print ("!!!!!!!!!!")
    print (n_samples)
    
    func(var_vivoda,X,y)
    mass = [[sheet['B12'].value,sheet['C12'].value], [sheet['B13'].value,sheet['C13'].value],[sheet['B14'].value,sheet['C14'].value],[sheet['B15'].value,sheet['C15'].value],[sheet['B16'].value,sheet['C16'].value],[sheet['B17'].value,sheet['C17'].value]]
    return mass
 
def read_RANDOM(var_vivoda, var_vvoda): #только для этого метода, т.к. странная генерация данных 
    # Parameters1
    n_classes = 3
    plot_colors = "bry"
    plot_step = 0.02
    
    func(var_vivoda, n_classes, plot_colors, plot_step, var_vvoda)


def func(var_vivoda, n_classes, plot_colors, plot_step, var_vvoda):
    
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("List_1") 
    
    
    # Load data
    iris = load_iris()   #подгрузка бд из интернета, судя по документации
                    
    if(var_vvoda == 2):                
        mass = read_Excel(var_vivoda) #чтение из Excel
    if(var_vvoda == 1):
        mass = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]] #стандартные параметры
        
        
    #здесь так же подставляются значения из Excel. Поэтому такие разные имена ячеек
    for pairidx, pair in enumerate(mass):
    
        if var_vvoda==1:
            # автоматическая генерация значений
            X = iris.data[:, pair]
            y = iris.target
            
        
    
        # Train
        clf = DecisionTreeClassifier().fit(X, y)
    
        # Plot the decision boundary
        plt.subplot(2, 3, pairidx + 1)
    
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                             np.arange(y_min, y_max, plot_step))
    
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    
        plt.xlabel(iris.feature_names[pair[0]])
        plt.ylabel(iris.feature_names[pair[1]])
        plt.axis("tight")
    
        # Plot the training points
        for i, color in zip(range(n_classes), plot_colors):
            idx = np.where(y == i)
            plt.scatter(X[idx, 0], X[idx, 1], c=color, label=iris.target_names[i],
                        cmap=plt.cm.Paired)
            
            if var_vivoda == 2: #если установлен вывод в Excel
                for x in range(len(X)):
                    sheet1.write(x+3,1,float(X[x,0]))
                    
                for x in range(len(X)):
                    sheet1.write(x+3,1,float(X[x,1]))
            
    
        plt.axis("tight")
    
    plt.suptitle("Decision surface of a decision tree using paired features")
    plt.legend()
    book.save("Raport.xls")
    plt.show()
##############################################################################    
def Excel_result(X,y,cluster_centers):
       
    print("DEBUG!!!")
    book = xlwt.Workbook(encoding="utf-8")
    
    sheet1 = book.add_sheet("List_1") 
    
    sheet1.write(2,0, "Координата точки на графике Х*")
    sheet1.write(2,1, "Координата точки на графике Y*")
    sheet1.write(2,4, "Координата центра найденного класстера Х*")
    sheet1.write(2,5, "Координата центра найденного класстера Y*")
    
    for x in range(len(y)):
        sheet1.write(x+3,1,float(X[x,1]))
    #---------------------------------------
    for x in range(len(y)):
        sheet1.write(x+3,0,float(X[x,0]))
    
    #---------------------------------------
    for i in range(len(cluster_centers)):
        for j in range(len(cluster_centers[i])):
            #print(i,j)
            sheet1.write(i+3,j+3,cluster_centers[i,j])
    #print(range(len(cluster_centers)))
    print("DEBUG!!!")
     
    book.save("Raport.xls")
    
    
##############################################################################
##############################################################################
def main():
    print("Sposob vvoda")
    print("1 - Random")
    print("2 - Excel")
    print("3 - sait")
    
    print("Sposob vvoda =")

    a = int(input())
    print("Sposob vvoda =",a)
    
    print("-----------------------------------")
    print("Sposob vivoda")
    print("1 - graphic")
    print("2 - Excel")
    
    print("Sposob vivoda =")
    
    b = 10 + int(input())
    print("Sposob vivoda =", b)

    if a==1:
        read_RANDOM(b,a)
        print("1!")
    
    if(a==2):
        read_Excel(b)

    func()
if __name__ == "__main__":
	main()