import random
import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
from sklearn import datasets


# Problem - 1 (Part - 1)
def Dice_Stair_1(total_runs):
    Sixty_Plus = []
    for i in range(total_runs):
        step = 0
        for j in range(250):
            dice = np.random.randint(1, 6)
            # print(dice)
            if step == 0:
                if dice == 1 or dice == 2:
                    continue
            if dice == 1 or dice == 2:
                step -= 1
            elif dice == 3 or dice == 5 or dice == 4:
                step += 1

            while dice == 6:
                dice = random.randint(1, 6)
                # print(dice)
                if step == 0:
                    if dice == 1 or dice == 2:
                        break
                if dice == 1 or dice == 2:
                    step -= 1
                elif dice == 3 or dice == 5 or dice == 4:
                    step += 1
                # print("6 ", end=', ')
            # print("Step = ", step, "Dice = ", dice)

        if step > 60:
            Sixty_Plus.append(1)
        else:
            Sixty_Plus.append(0)
    print("We Moved above Sixty Step = ",
          Sixty_Plus.count(1), " AND ", "We are Less Than Sixty Steps = ", Sixty_Plus.count(0))
    print("Probability ({}) Trials) = ".format(total_runs), Sixty_Plus.count(1) / 1000)


# Dice_Stair_1(1000)


# Problem - 1 (Part - 2)
# With Custom Number Of Throws
def Dice_Stair_2(throws, total_runs):
    Sixty_Plus = []
    for _ in range(total_runs):
        step = 0
        for j in range(throws):
            dice = np.random.randint(1, 6)
            # print(dice)
            if step == 0:
                if dice == 1 or dice == 2:
                    continue
            if dice == 1 or dice == 2:
                step -= 1
            elif dice == 3 or dice == 5 or dice == 4:
                step += 1

            while dice == 6:
                dice = random.randint(1, 6)
                # print(dice)
                if step == 0:
                    if dice == 1 or dice == 2:
                        break
                if dice == 1 or dice == 2:
                    step -= 1
                elif dice == 3 or dice == 5 or dice == 4:
                    step += 1
                # print("6 ", end=', ')
            # print("Step = ", step, "Dice = ", dice)
        if step > 60:
            Sixty_Plus.append(1)
        else:
            Sixty_Plus.append(0)
    print("We Moved above Sixty Step = ", Sixty_Plus.count(1), " AND ",
          "We are Less Than Sixty Steps = ", Sixty_Plus.count(0))
    print("Probability ({}) Trials) = ".format(total_runs), Sixty_Plus.count(1) / 1000)


# Dice_Stair_2(250, 1000)


# Problem - 1 (Part - 3)
# With Probability Distribution
def Dice_Stair_3(throws, weights, total_runs):
    Sixty_Plus = []
    for i in range(total_runs):
        dice_v = []
        step = 0
        for j in range(throws):
            dice = random.choices(range(1, 7), weights=weights)
            dice = dice[0]
            # print(dice)
            if step == 0:
                if dice == 1 or dice == 2:
                    dice_v.append(dice)
                    continue
            if dice == 1 or dice == 2:
                step -= 1
            elif dice == 3 or dice == 5 or dice == 4:
                step += 1

            while dice == 6:
                dice = random.randint(1, 6)
                # print(dice)
                if step == 0:
                    if dice == 1 or dice == 2:
                        break
                if dice == 1 or dice == 2:
                    step -= 1
                elif dice == 3 or dice == 5 or dice == 4:
                    step += 1
        if step > 60:
            Sixty_Plus.append(1)
        else:
            Sixty_Plus.append(0)

    print("We Moved above Sixty Step = ", Sixty_Plus.count(1), " AND ",
          "We are Less Than Sixty Steps = ", Sixty_Plus.count(0))
    print("Probability ({}) Trials) = ".format(total_runs), Sixty_Plus.count(1) / 1000)


probabilities = [0.2, 0.3, 0.2, 0.1, 0.1, 0.1]


# Dice_Stair_3(250, probabilities, 1000)


# For Probabilities We Would use random seed in order to get same values of dies at every outcome
# After applying weights to every number of dice the probability
# of getting to step more than 60 is reduced to 0 in 1000 trail runs with 250 throws of dice in each trial_run






# Data-Generation For Linear Regression

def Data_Generation_For_Linear_Regression(no_of_rows, no_of_attributes):
    error = norm.rvs(0, 0.25, no_of_rows)
    # print(error)
    features = []
    for v in range(no_of_attributes):
        x = norm.rvs(0, 1, no_of_rows)
        x = x[:, np.newaxis]
        if v == 0:
            features = x
        else:
            features = np.c_[x, features]
    print(features)

    y = []
    for value in features:
        summation = 0
        for w in range(0, len(value)):
            print(value[w])
            summation = summation + (1 / (w + 2)) * value[w]
            print(summation)
        y.append(summation)
    y = y + error - 1
    cols = []
    for i in range(no_of_attributes):
        cols.append(i)
    data_set = pd.DataFrame(features, columns=cols)
    data_set["y"] = y
    print(data_set.head())
    data_set.to_csv("Linear_Regression_Dataset.csv")



# Data_Generation_For_Logistic_Regression(1000, 2)

def Data_Generation_For_Logistic_Regression(no_of_rows, no_of_attributes):
    features = []
    for v in range(no_of_attributes):
        x = norm.rvs(0, 1, no_of_rows)
        x = x[:, np.newaxis]
        if v == 0:
            features = x
        else:
            features = np.c_[x, features]
    print(features)
    y = []
    for value in features:
        summation = 1
        z = 0
        for w in range(0, len(value)):
            print(value[w])
            summation = summation + ((w + 2) * value[w])
            z = 1 / (1 + np.exp(-summation))
        y.append(1 if z >= 0.5 else 0)

    cols = []
    for i in range(no_of_attributes):
        cols.append(i)
    data_set = pd.DataFrame(features, columns=cols)
    data_set["y"] = y
    print(data_set.head())
    data_set.to_csv("Logistic_Regression_Dataset.csv")


# Data_Generation_For_K_Means(1000, 2)

def Data_Generation_For_K_Means(no_of_values, features):
    x, y = datasets.make_blobs(no_of_values, features, random_state=0, centers=3)
    cols = []
    for i in range(features):
        cols.append(i)
    data_set = pd.DataFrame(x, columns=cols)
    data_set["y"] = y
    data_set.to_csv("Data_Set_K_Means.csv")





# Linear Regression Using Gradient Descent
def Linear_Regression_Using_Batch_Gradient_Descent(lr, weights, epochs, x, y):
    costs = []
    for _ in range(epochs):
        prediction = np.dot(x, weights)
        error = prediction - y
        cost = 1 / (len(x)) * np.dot(error.T, error)
        costs.append(cost)
        weights = weights - (lr * (1 / len(x)) * np.dot(x.T, error))
    return weights, costs


def MSE(y, predicted):
    error = y - predicted
    return 1 / (len(y)) * np.dot(error.T, error)


np.random.seed(123)
data = pd.read_csv("Linear_Regression_Dataset.csv")
v = len(data.columns)
X = data.iloc[:, 1:v - 1].values
thetas = np.random.rand(len(X[0]) + 1)

# Appending 1 for intercept purpose
X = np.c_[np.ones(X.shape[0]), X]
Y = data.iloc[:, v - 1].values

# Splitting Data_Sets
val = len(X) // 3
X_train = X[val:]
X_test = X[: val]
Y_train = Y[val:]
Y_test = Y[: val]

theta_, past_cost = Linear_Regression_Using_Batch_Gradient_Descent(0.021, thetas, 1000, X_train, Y_train)
print(past_cost)
print(theta_)

# Plot the cost function...
plt.title('Cost Function')
plt.xlabel('No. of iterations')
plt.ylabel('Cost')
plt.plot(past_cost)
plt.show()

predictions = []
c = theta_[0]
for i in X_test:
    s = 0
    for j in range(0, len(i) - 1):
        # print(j)
        s = s + (theta_[j + 1] * i[j + 1])
    s += c
    predictions.append(s)

print(predictions)
print(Y_test)
print("MSE : ", MSE(Y_test, predictions))







# Logistic Regression Using Gradient Descent
def Logistic_Regression_Using_Gradient_Descent(lr, weights, epochs, x, y):
    costs = []
    for _ in range(epochs):
        prediction = np.dot(x, weights)
        sigmoid = 1 / (1 + np.exp(-prediction))
        error = sigmoid - y
        cost = (-y) * np.log(sigmoid) - (1 - y) * np.log(1 - sigmoid)
        cost = sum(cost) / len(x)
        costs.append(cost)
        weights = weights - (lr * (1 / len(x)) * np.dot(x.T, error))
    return weights, costs


def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / len(actual) * 100.0


np.random.seed(123)
data = pd.read_csv("Logistic_Regression_Dataset.csv")
v = len(data.columns)
X = data.iloc[:, 1:v - 1].values
# thetas = np.random.rand(len(X[0]))
thetas = np.zeros(len(X[0]))
Y = data.iloc[:, v - 1].values

# Splitting Data_Sets
val = len(X) // 3
X_train = X[val:]
X_test = X[: val]
Y_train = Y[val:]
Y_test = Y[: val]

theta_, past_cost = Logistic_Regression_Using_Gradient_Descent(0.25, thetas, 1000, X_train, Y_train)
print(past_cost)
print(theta_)

# Plot the cost function...
plt.title('Cost Function')
plt.xlabel('No. of iterations')
plt.ylabel('Cost')
plt.plot(past_cost)
plt.show()

predictions = []
for i in X_test:
    s = 0
    for j in range(0, len(i)):
        # print(j)
        s = s + (theta_[j] * i[j])
    z = round(1 / (1 + np.exp(-s)))
    predictions.append(z)
print(predictions)
print(Y_test)
print("Accuracy = ", accuracy_metric(Y_test, predictions))






# Logistic Regression Using L1 and L2 Regularization
def Logistic_Regression_Using_Gradient_Descent(lr, weights, epochs, x, y):
    l1 = 0.4
    l2 = 1 - l1
    costs = []
    for _ in range(epochs):
        prediction = np.dot(x, weights)
        sigmoid = 1 / (1 + np.exp(-prediction))
        error = sigmoid - y
        cost = (-y) * np.log(sigmoid) - (1 - y) * np.log(1 - sigmoid)
        cost = sum(cost) / len(x)
        costs.append(cost)
        weights = weights - (lr * (x.T.dot(error) + l1 * np.sign(weights) + l2 * 2 * weights) * 1 / len(x))
    return weights, costs


def accuracy_metric(actual, predicted):
    correct = 0
    for value in range(len(actual)):
        if actual[value] == predicted[value]:
            correct += 1
    return correct / len(actual) * 100.0


np.random.seed(123)
data = pd.read_csv("Logistic_Regression_Dataset.csv")
v = len(data.columns)
X = data.iloc[:, 1:v - 1].values
# thetas = np.random.rand(len(X[0]))
thetas = np.zeros(len(X[0]))
Y = data.iloc[:, v - 1].values

# Splitting Data_Sets
val = len(X) // 3
X_train = X[val:]
X_test = X[: val]
Y_train = Y[val:]
Y_test = Y[: val]

theta_, past_cost = Logistic_Regression_Using_Gradient_Descent(0.025, thetas, 1000, X_train, Y_train)
print(past_cost)
print(theta_)

# Plot the cost function...
plt.title('Cost Function')
plt.xlabel('No. of iterations')
plt.ylabel('Cost')
plt.plot(past_cost)
plt.show()

predictions = []
for i in X_test:
    s = 0
    for j in range(0, len(i)):
        # print(j)
        s = s + (theta_[j] * i[j])
    z = round(1 / (1 + np.exp(-s)))
    predictions.append(z)
print(predictions)
print(Y_test)
print("Accuracy = ", accuracy_metric(Y_test, predictions))

# Linear Regression Using L1_L2_Reguarization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Linear Regression Using L1 and L2 Regularization
def L1_L2_Regularization_Linear_Regression(x, y, epochs, lr, weight):
    l1 = 0.4
    l2 = 1 - l1
    costs = []
    for _ in range(epochs):
        prediction = np.dot(x, weight)
        error = prediction - y
        cost = 1 / (len(x)) * np.dot(error.T, error)
        costs.append(cost)
        weight = weight - (lr * (x.T.dot(error) + l1 * np.sign(weight) + l2 * 2 * weight) * 1 / len(x))
        print(weight)
    return costs, weight


def MSE(y, predicted):
    error = y - predicted
    return 1 / (len(y)) * np.dot(error.T, error)


np.random.seed(123)
data = pd.read_csv("Linear_Regression_Dataset.csv")
v = len(data.columns)
X = data.iloc[:, 1:v - 1].values
thetas = np.random.randn(len(X[0]) + 1)
print(thetas)
# Appending 1 for intercept purpose
X = np.c_[np.ones(X.shape[0]), X]
Y = data.iloc[:, v - 1].values

# Splitting Data_Sets
val = len(X) // 3
X_train = X[val:]
X_test = X[: val]
Y_train = Y[val:]
Y_test = Y[: val]
cost_val, weights = L1_L2_Regularization_Linear_Regression(X_train, Y_train, 1000, 0.025, thetas)
plt.title('Cost Function')
plt.xlabel('No. of iterations')
plt.ylabel('Cost')
plt.plot(cost_val)
plt.show()

predictions = []
c = weights[0]
for i in X_test:
    s = 0
    for j in range(0, len(i) - 1):
        # print(j)
        s = s + (weights[j + 1] * i[j + 1])
    s += c
    predictions.append(s)

print(predictions)
print(Y_test)
print("MSE : ", MSE(Y_test, predictions))






# K - Means Using Random Centroids From Scratch
def K_Means(x, no_of_clusters):
    centroids = np.array([]).reshape(len(x[0]), 0)
    # print(centroids)
    for i in range(no_of_clusters):
        random_val = random.randint(0, len(x) - 1)
        centroids = np.c_[centroids, x[random_val]]
    print(centroids)
    distance = euclidean_distance(centroids, no_of_clusters, len(x), x)
    plt.scatter(x[:, 0], x[:, 1], c='maroon')
    plt.show()
    color = ['red', 'blue', 'green', 'black', 'purple', 'orange', 'brown', 'pink', 'neon']
    if len(x[0]) == 2:
        for k in range(no_of_clusters):
            plt.scatter(x=distance[k][:, 0], y=distance[k][:, 1], c=color[k])
        plt.scatter(centroids[0, :], centroids[1, :], color='yellow')
        plt.show()
    for va in distance.keys():
        print("cluster {} -----> {}".format(va, distance[va]))
    return centroids, distance


def euclidean_distance(centroids, no_of_clusters, length, x):
    euclidean = np.array([]).reshape(length, 0)
    for i in range(no_of_clusters):
        distance = np.sum((x - centroids[:, i]) ** 2, axis=1)
        euclidean = np.c_[euclidean, distance]

    # print(euclidean)
    index = np.argmin(euclidean, axis=1)
    # print(index)
    distances = {}
    for k in range(no_of_clusters):
        distances[k] = np.array([]).reshape(len(x[0]), 0)
    for i in range(length):
        distances[index[i]] = np.c_[distances[index[i]], x[i]]
    for k in range(no_of_clusters):
        distances[k] = distances[k].T
    return distances


def weighted_sum_of_squares(x):
    weighted_sum_squares = []
    for va in range(1, 8):
        centroids, distance = K_Means(x, va)
        weighted_sum_square = 0
        for k in range(va):
            weighted_sum_square += np.sum((distance[k] - centroids[:, k]) ** 2)
        weighted_sum_squares.append(weighted_sum_square)

    plt.plot(weighted_sum_squares)
    plt.show()


data = pd.read_csv("Data_Set_K_Means.csv")
val = len(data.columns)
X = data.iloc[:, 1: val - 1].values
Y = data.iloc[:, val - 1].values
# print(len(X[0]))
# K_Means(X, 3)
# weighted_sum_of_squares(X)