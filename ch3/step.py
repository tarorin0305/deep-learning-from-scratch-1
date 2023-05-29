import numpy as np
import matplotlib.pyplot as plt

# implement step function
def step_function(x):
    return np.array(x > 0, dtype=int)

# implement sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

# x = np.arange(-5.0, 5.0, 0.1) # create data
# y = step_function(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1) # set y axis range
# plt.show()

# define function that execute sigmoid function
def execute_sigmoid():
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1) # set y axis range
    plt.show()

# create multi-dimensional array
def multi_dimensional_array():
    A = np.array([1, 2, 3, 4])
    print(A)
    print(np.ndim(A)) # get dimension of array
    print(A.shape) # get shape of array
    print(A.shape[0]) # get first element of shape of array

    B = np.array([[1, 2], [3, 4], [5, 6]])
    print(B)
    print(np.ndim(B)) # get dimension of array
    print(B.shape) # get shape of array

# define function that calculates multi dimensional array
def calculate_multi_dimensional_array():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    # print(np.dot(A, B)) # calculate multi dimensional array

    C = np.array([[1, 2, 3], [4, 5, 6]])
    D = np.array([[1, 2], [3, 4], [5, 6]])
    # print(np.dot(C, D)) # calculate multi dimensional array

    X = np.array([1, 2])
    W = np.array([[1, 3, 5], [2, 4, 6]])
    Y = np.dot(X, W)
    print(X.shape)
    print(W.shape)
    print(Y)
    print(Y.shape)

# define function that calculates multi dimensional array with bias
def calculate_multi_dimensional_array_with_bias():
    X = np.array([1.0, 0.5]) # input
    W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]) # weight1
    B1 = np.array([0.1, 0.2, 0.3]) # bias1

    print(W1.shape)
    print(X.shape)
    print(B1.shape)

    A1 = np.dot(X, W1) + B1 # calculate multi dimensional array
    print(A1)

if __name__ == '__main__':
    calculate_multi_dimensional_array_with_bias()
