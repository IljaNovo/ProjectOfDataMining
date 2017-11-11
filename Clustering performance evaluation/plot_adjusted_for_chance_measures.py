import numpy as np
import matplotlib.pyplot as plt
from time import time
from sklearn import metrics


def read_Excel(var_vivoda):
    wb = load_workbook('data.xlsx')
    sheet = wb.get_sheet_by_name('sheetname')
#    print("#################################################")
#    print(sheet['C7'].value)
#    print(sheet['C8'].value)
    
#    print(sheet['D7'].value)
#    print(sheet['D8'].value)
    
#    print(sheet['E7'].value)
#    print(sheet['E8'].value)
#    print("#################################################")
    centers =[[float(sheet['C7'].value),float(sheet['C8'].value)],[float(sheet['D7'].value),float(sheet['D8'].value)],[float(sheet['E7'].value),float(sheet['E8'].value)]]
    #n_samples = sheet['E10'].value
    
    #print ("!!!!!!!!!!")
    #print (n_samples)
    
    #i=0
    #2X, y = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6) #генерация случайных чисел
 
    #func(var_vivoda,X,y)

def uniform_labelings_scores(score_func, n_samples, n_clusters_range,
                             fixed_n_classes=None, n_runs=5, seed=42):
    """Compute score for 2 random uniform cluster labelings.

    Both random labelings have the same number of clusters for each value
    possible value in ``n_clusters_range``.

    When fixed_n_classes is not None the first labeling is considered a ground
    truth class assignment with fixed number of classes.
    """
    random_labels = np.random.RandomState(seed).randint
    scores = np.zeros((len(n_clusters_range), n_runs))

    if fixed_n_classes is not None:
        labels_a = random_labels(low=0, high=fixed_n_classes, size=n_samples)

    for i, k in enumerate(n_clusters_range):
        for j in range(n_runs):
            if fixed_n_classes is None:
                labels_a = random_labels(low=0, high=k, size=n_samples)
            labels_b = random_labels(low=0, high=k, size=n_samples)
            scores[i, j] = score_func(labels_a, labels_b)
    return scores

score_funcs = [
    metrics.adjusted_rand_score,
    metrics.v_measure_score,
    metrics.adjusted_mutual_info_score,
    metrics.mutual_info_score,
]

#####################################################################################
##значения по умолчанию
def func(var_vivoda):
    n_samples = 100
    n_clusters_range = np.linspace(2, n_samples, 10).astype(np.int)
    
    plt.figure(1)
    
    plots = []
    names = []
    for score_func in score_funcs:
        print("Computing %s for %d values of n_clusters and n_samples=%d"
              % (score_func.__name__, len(n_clusters_range), n_samples))
    
        t0 = time()
        scores = uniform_labelings_scores(score_func, n_samples, n_clusters_range)
        print("done in %0.3fs" % (time() - t0))
        plots.append(plt.errorbar(
            n_clusters_range, np.median(scores, axis=1), scores.std(axis=1))[0])
        names.append(score_func.__name__)
    
    plt.title("Clustering measures for 2 random uniform labelings\n"
              "with equal number of clusters")
    plt.xlabel('Number of clusters (Number of samples is fixed to %d)' % n_samples)
    plt.ylabel('Score value')
    plt.legend(plots, names)
    plt.ylim(ymin=-0.05, ymax=1.05)
    n_samples = 1000
    n_clusters_range = np.linspace(2, 100, 10).astype(np.int)
    n_classes = 10
    
    plt.figure(2)

# 2 independent random clusterings with equal cluster number
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
        uniform_labelings_scores(100, 100, n_clusters_range,
                             fixed_n_classes=None, n_runs=5, seed=42)
        #read_RANDOM(b)
        print("1!")
    
    if(a==2):
        read_Excel(b)



    
    # Random labeling with varying n_clusters against ground class labels
    # with fixed number of clusters
    
    
    
    plots = []
    names = []
    for score_func in score_funcs:
        print("Computing %s for %d values of n_clusters and n_samples=%d"
              % (score_func.__name__, len(n_clusters_range), n_samples))
    
        t0 = time()
        scores = uniform_labelings_scores(score_func, n_samples, n_clusters_range,
                                          fixed_n_classes=n_classes)
        print("done in %0.3fs" % (time() - t0))
        plots.append(plt.errorbar(
            n_clusters_range, scores.mean(axis=1), scores.std(axis=1))[0])
        names.append(score_func.__name__)
    
    plt.title("Clustering measures for random uniform labeling\n"
              "against reference assignment with %d classes" % n_classes)
    plt.xlabel('Number of clusters (Number of samples is fixed to %d)' % n_samples)
    plt.ylabel('Score value')
    plt.ylim(ymin=-0.05, ymax=1.05)
    plt.legend(plots, names)
    plt.show()

if __name__ == "__main__":
	main()