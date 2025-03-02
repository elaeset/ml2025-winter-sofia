import numpy as np
from sklearn.neighbors import KNeighborsRegressor as kr

def knn():
    try:
        input_N = int(input('Please input a positive integer N: '))
        print('N is', input_N)
        if input_N <= 0:
            raise ValueError('N must be a positive')

        input_k = int(input('Please input a positive integer k and make sure k<N: '))
        print('k is', input_k)
        if input_k <= 0:
            raise ValueError('k must be a positive')
    
        if input_k > input_N:
            print("Error: k cannot be greater than N.")
            return
    
        X, Y = [], []
        for i in range(input_N):
            x = float(input(f"Enter x for point {i+1}: "))
            y = float(input(f"Enter y for point {i+1}: "))
            X.append([x])
            Y.append(y)
        
        X = np.array(X)
        Y = np.array(Y)

        print(X)
        print(Y)

        input_X = float(input('please input a X value for prediction: '))

        neigh = kr(n_neighbors=input_k)
        neigh.fit(X,Y)
        predict = neigh.predict([[input_X]])

        print(f'The Y value predicted is:{predict}')

    except ValueError as error:
        print(f'input error:{error}')

knn()
