import time as time
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets.samples_generator import make_swiss_roll
from numpy import array
import input_output.io as io

def run(X, n_clusters):
    # #############################################################################
    # Generate data (swiss roll dataset)
    #text = io.Input.local_read_text_file(inputFilePath)
    #input_array = text.split('\n')
    #n_samples = len(input_array)
    #noise = 0.05
    #X, _ = make_swiss_roll(n_samples, noise)
    #with open("input_data.txt", 'w', encoding='utf-8') as file2:
    #    for line in X:
    #        file2.write(str(line) + "\n")
    #float_array = []
    #for line in input_array:
    #    float_line = [float(i) for i in line.split(' ')]
    #    float_array.append(float_line)
    #X = array(float_array)
    # Make it thinner
    X[:, 1] *= .5

    # #############################################################################
    # Compute clustering
    print("Compute unstructured hierarchical clustering...")
    st = time.time()
    ward = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward').fit(X)
    elapsed_time = time.time() - st
    label = ward.labels_
    print("Elapsed time: %.2fs" % elapsed_time)
    print("Number of points: %i" % label.size)

    # #############################################################################
    # Plot result
    fig = plt.figure()
    ax = p3.Axes3D(fig)
    ax.view_init(7, -80)
    for l in np.unique(label):
        ax.scatter(X[label == l, 0], X[label == l, 1], X[label == l, 2],
                   color=plt.cm.jet(np.float(l) / np.max(label + 1)),
                   s=20, edgecolor='k')
    plt.title('Without connectivity constraints (time %.2fs)' % elapsed_time)
    io.Output.write_to_txt_file_two_value("!Results/clustering_HC_without_constraints_result.txt", X, label)



    # #############################################################################
    # Define the structure A of the data. Here a 10 nearest neighbors
    from sklearn.neighbors import kneighbors_graph
    connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)

    # #############################################################################
    # Compute clustering
    print("Compute structured hierarchical clustering...")
    st = time.time()
    ward = AgglomerativeClustering(n_clusters=n_clusters, connectivity=connectivity,
                                   linkage='ward').fit(X)
    elapsed_time = time.time() - st
    label = ward.labels_
    print("Elapsed time: %.2fs" % elapsed_time)
    print("Number of points: %i" % label.size)

    # #############################################################################
    # Plot result
    fig = plt.figure()
    ax = p3.Axes3D(fig)
    ax.view_init(7, -80)
    for l in np.unique(label):
        ax.scatter(X[label == l, 0], X[label == l, 1], X[label == l, 2],
                   color=plt.cm.jet(float(l) / np.max(label + 1)),
                   s=20, edgecolor='k')
    plt.title('With connectivity constraints (time %.2fs)' % elapsed_time)
    io.Output.write_to_txt_file_two_value("!Results/clustering_HC_with_constraints_result.txt", X, label)

    plt.show()