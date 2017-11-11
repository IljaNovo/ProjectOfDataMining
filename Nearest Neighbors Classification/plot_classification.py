#================================
#Nearest Neighbors Classification
#================================

import numpy as np
import xlwt
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

##############################################################################
def read_RANDOM(var_vivoda): #Генерация данных рандомного значения
    n_neighbors = 15
    
    # import some data to play with
    iris = datasets.load_iris()
    
    # we only take the first two features. We could avoid this ugly
    # slicing by using a two-dim dataset
    X = iris.data[:, :2]
    y = iris.target
    
    h = .02  # step size in the mesh
    
    # Create color maps
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
    func(cmap_bold,cmap_light,h,X,y,n_neighbors,var_vivoda)                            

##############################################################################                            
def func(cmap_bold,cmap_light,h,X,y,n_neighbors,var_vivoda): #функция вычисляет кластеры.                          
    for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
        clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
        clf.fit(X, y)
    
        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, x_max]x[y_min, y_max].
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    
        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        
        if var_vivoda==11:
            Plot_result(xx,yy,Z,X,y,n_neighbors,cmap_light,cmap_bold)
    
##############################################################################
def Plot_result(xx,yy,Z,X,y,n_neighbors,cmap_light,cmap_bold):
    for weights in ['uniform', 'distance']:
        
        plt.figure()
        plt.pcolormesh(xx, yy, Z, cmap=cmap_light)  #отрисовать области
    
        # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,  #отрисовать точки
                    edgecolor='k', s=20)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.title("3-Class classification (k = %i, weights = '%s')"
                  % (n_neighbors, weights))

    plt.show()
##############################################################################    
def Excel_result():
       
    print("DEBUG!!!")
    book = xlwt.Workbook(encoding="utf-8")

    # Добавить лист в книгу 
    '''
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
            sheet1.write(i+3,j+3,cluster_centers[i,j])
    print("DEBUG!!!")
    '''
    
        
     
    book.save("Raport.xls")      
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
        read_RANDOM(b)
    
    if(a==2):
        read_Excel(b)

if __name__ == "__main__":
	main()    
