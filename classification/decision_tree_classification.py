# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
import random


def dtc_run(data, plot_step):
    if (data is None):
        data = datasets.load_iris()
        i = 0
        for row in data.data:
            j = 0
            for el in row:
                data.data[i, j] = random.uniform(0.1, 9.9)
                j = j + 1
            i = i + 1
    # Parameters
    n_classes = 3
    plot_colors = "ryb"

    for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3],
                                    [1, 2], [1, 3], [2, 3]]):
        # We only take the two corresponding features
        X = data.data[:, pair]
        y = data.target

        # Train
        clf = DecisionTreeClassifier().fit(X, y)

        # Plot the decision boundary
        plt.subplot(2, 3, pairidx + 1)

        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                             np.arange(y_min, y_max, plot_step))
        plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)

        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        cs = plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu)

        plt.xlabel(data.feature_names[pair[0]])
        plt.ylabel(data.feature_names[pair[1]])

        # Plot the training points
        for i, color in zip(range(n_classes), plot_colors):
            idx = np.where(y == i)
            plt.scatter(X[idx, 0], X[idx, 1], c=color, label=data.target_names[i],
                        cmap=plt.cm.RdYlBu, edgecolor='black', s=15)

    plt.suptitle("Decision surface of a decision tree using paired features")
    plt.legend(loc='lower right', borderpad=0, handletextpad=0)
    plt.axis("tight")
    plt.savefig('!Results/classification_DTC_result.png', bbox_inches='tight')
    fig = plt.gcf()
    fig.canvas.set_window_title('[Result] Decision Tree classification')
    plt.show()