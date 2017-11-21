# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth

import input_output.io as io


def run_mean_shift(X, bandwidth):
    
    # The following bandwidth can be automatically detected using
    if(bandwidth == None):
        bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    print("number of estimated clusters : %d" % n_clusters_)

    # #############################################################################
    # Plot result
    import matplotlib.pyplot as plt
    from itertools import cycle

    plt.figure(1)
    plt.clf()

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]
        plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    io.Output.write_to_txt_file_two_value("C:/Results/clustering_MS_result.txt", X, labels)

    fig = plt.gcf()
    fig.canvas.set_window_title('[Result] Mean Shift clustering')
    plt.savefig('!Results/Clustering_Mean_Shift_result.png', bbox_inches='tight') #сохранение графика
    plt.show()
    