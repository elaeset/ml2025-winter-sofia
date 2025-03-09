import numpy as np
from sklearn.neighbors import KNeighborsRegressor as kr
from sklearn.metrics import precision_score, recall_score

def scikit():
    try:
        input_N = int(input('Please input a positive integer N: '))
        print('N is', input_N)
        if input_N <= 0:
            raise ValueError('N must be a positive')

        X, Y = [], []
        for i in range(input_N):
            x = float(input(f"Enter x (either 0 or 1) for point {i+1}: "))
            y = float(input(f"Enter y (either 0 or 1) for point {i+1}: "))
            X.append(x)
            Y.append(y)
        
        X = np.array(X)
        Y = np.array(Y)

        print(X)
        print(Y)
        
        precision = precision_score(X, Y)
        recall = recall_score(X, Y)
    
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")

    except ValueError as error:
        print(f'input error:{error}')

scikit()
