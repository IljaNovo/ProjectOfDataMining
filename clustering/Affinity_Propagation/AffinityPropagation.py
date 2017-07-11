from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from itertools import cycle


def compute_affinity_propagation(data):
    # DATA FILLING
    if len(data)==0:
        centers = [[1, 1], [-1, -1], [1, -1]]
        n_sampes = 300
        cluster_std = 1
        random_state = 0
    else:
        centers, n_sampes, cluster_std, random_state = process_data(data)
    X, labels_true = make_blobs(n_samples=int(n_sampes), centers=centers, cluster_std=int(cluster_std), random_state=int(random_state))
    af = AffinityPropagation(preference=-50).fit(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_
    n_clusters_ = len(cluster_centers_indices)
    print('Estimated number of clusters: %d' % n_clusters_)
    print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
    print("Adjusted Mutual Information: %0.3f" % metrics.adjusted_mutual_info_score(labels_true, labels))
    print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels, metric='sqeuclidean'))
    plt.close('all')
    plt.figure(1)
    plt.clf()
    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        class_members = labels == k
        cluster_center = X[cluster_centers_indices[k]]
        plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)
        for x in X[class_members]:
            plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()

def process_data(data) :
    first_row = data[0].split()
    second_row = data[1].split()
    centers = []
    center = []
    for item in first_row :
        center.append(int(item))
        if(len(center)== 2) :
            centers.append(center)
            center = []
    n_sampes = second_row[0]
    cluster_std = second_row[1]
    random_state = second_row[2]
    return centers,n_sampes,cluster_std,random_state