import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets.samples_generator import make_blobs
import input_output.io as io
from numpy import array

def run_mean_shift(X, bandwidth):
    # #############################################################################
    # Generate sample data
    #centers = [[1, 1], [-1, -1], [1, -1]]
    #text = io.Input.local_read_text_file(inputFilePath)
    #input_array = text.split('\n')
    #float_array = []
    #for line in input_array:
    #    float_line = [float(i) for i in line.split(' ')]
    #    float_array.append(float_line)
    #X = array(float_array)
    #X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
    #with open("input_data.txt", 'w', encoding='utf-8') as file2:
    #    for line in X:
    #        file2.write(str(line) + "\n")
    # #############################################################################
    # Compute clustering with MeanShift

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
    io.Output.write_to_txt_file_two_value("!Results/clustering_MS_result.txt", X, labels)

    fig = plt.gcf()
    fig.canvas.set_window_title('[Result] Mean Shift clustering')
    plt.show()