# -*- coding: utf-8 -*-
"""
===================================
Demo of DBSCAN clustering algorithm
===================================

Finds core samples of high density and expands clusters from them.

"""

import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import input_output.io as io
from numpy import array

def dbscan_run(X, eps_, min_samples_):
    print(__doc__)
    ##############################################################################
    # Generate sample data
    centers = [[1, 1], [-1, -1], [1, -1]]
    #text = io.Input.local_read_text_file(inputFilePath)
    #input_array = text.split('\n')

    # This operation need for labels_true generating for metrics printing
    useless_data, labels_true = make_blobs(n_samples=len(X), centers=centers, cluster_std=0.4,random_state=0)
    #with open("input_data.txt", 'w', encoding='utf-8') as file2:
    #    for line in X:
    #        file2.write(str(line) + "\n")

    #float_array = []
    #for line in input_array:
    #    float_line = [float(i) for i in line.split(' ')]
    #    float_array.append(float_line)
    #X = array(float_array)

    X = StandardScaler().fit_transform(X)

    ##############################################################################
    # Compute DBSCAN
    db = DBSCAN(eps=eps_, min_samples=min_samples_).fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    print('Estimated number of clusters: %d' % n_clusters_)
    print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    print("Adjusted Rand Index: %0.3f"
          % metrics.adjusted_rand_score(labels_true, labels))
    print("Adjusted Mutual Information: %0.3f"
          % metrics.adjusted_mutual_info_score(labels_true, labels))
    #print("Silhouette Coefficient: %0.3f"
    #      % metrics.silhouette_score(X, labels))

    ##############################################################################
    # Plot result
    import matplotlib.pyplot as plt

    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

        class_member_mask = (labels == k)

        xy = X[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=14)

        xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=6)

    io.Output.write_to_txt_file_two_value("!Results/clustering_DBSCAN_result.txt", X, labels)
    plt.title('Estimated number of clusters: %d' % n_clusters_)

    fig = plt.gcf()
    fig.canvas.set_window_title('[Result] DBSCAN clustering')
    plt.show()
