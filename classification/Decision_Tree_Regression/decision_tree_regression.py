
# Import the necessary modules and libraries
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from numpy import array


def run(data):
    # Create a random dataset
    rng = np.random.RandomState(1)
    X = np.sort(5 * rng.rand(80, 1), axis=0)
    y = np.sin(X).ravel()
    y[::5] += 3 * (0.5 - rng.rand(16))
    y_array =[]
    x_array = []
    text_array = data.split('\n')
    for line in text_array :
        line_arr = [float(i) for i in line.split(' ')]
        x_array.append(line_arr[0])
        y_array.append(line_arr[1])
    # Fit regression model
    X = np.vstack(array(x_array))
    y = array(y_array)
    regr_1 = DecisionTreeRegressor(max_depth=2)
    regr_2 = DecisionTreeRegressor(max_depth=5)
    regr_1.fit(X, y)
    regr_2.fit(X, y)

    # Predict
    X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
    y_1 = regr_1.predict(X_test)
    y_2 = regr_2.predict(X_test)

    # Plot the results
    plt.figure()
    plt.scatter(X, y, s=20, edgecolor="black",
                c="darkorange", label="data")
    plt.plot(X_test, y_1, color="cornflowerblue",
             label="max_depth=2", linewidth=2)
    plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
    plt.xlabel("data")
    plt.ylabel("target")
    plt.title("Decision Tree Regression")
    plt.legend()
    plt.show()