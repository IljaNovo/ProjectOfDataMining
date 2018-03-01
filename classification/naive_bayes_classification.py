# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
import random

def bayes_run(data, plot_step):
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
	plot_colors = "bry"

	X = data.data[:, :2]
	y = data.target

	# Shuffle
	idx = np.arange(X.shape[0])
	np.random.seed(13)
	np.random.shuffle(idx)
	X = X[idx]
	y = y[idx]

	# Train
	clf = GaussianNB().fit(X, y)

	x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
	y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
	xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
						 np.arange(y_min, y_max, plot_step))

	Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
	Z = Z.reshape(xx.shape)
	cs = plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

	plt.axis()

	# Plot the training points
	for i, color in zip(range(n_classes), plot_colors):
		idx = np.where(y == i)
		plt.scatter(X[idx, 0], X[idx, 1], c=color,
					label=data.target_names[i],
					cmap=plt.cm.Paired)
	plt.axis()

	plt.legend(loc="upper left")
	fig = plt.gcf()
	fig.canvas.set_window_title('[Result] Naive Bayes classification')
	plt.savefig('!Results/classification_Naive_Bayes_result.png', bbox_inches='tight')

	plt.show()