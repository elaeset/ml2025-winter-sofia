import numpy as np
from sklearn.neighbors import KNeighborsRegressor as kr
from sklearn.metrics import accuracy_score

def knnClassifier():
    try:
        input_N = int(input('Please input a positive integer N: '))
        print('N is', input_N)
        if input_N <= 0:
            raise ValueError('N must be a positive')

        X, Y = [], []
        for i in range(input_N):
            x = float(input(f"Enter x (a real number) for point {i+1}: "))
            y = int(input(f"Enter y (non-negative integer) for point {i+1}: "))
            if y < 0:
                raise ValueError('y must be a non-negative integer')
            
            X.append(x)
            Y.append(y)
        
        X_pretrain = np.array(X)
        Y_pretrain = np.array(Y)

        X_train = X_pretrain.reshape(-1, 1)
        Y_train = Y_pretrain.reshape(-1, 1).astype(int)

        print(X_train)
        print(Y_train)

        input_M = int(input('Please input a positive integer M: '))
        print('M is', input_M)
        if input_M <= 0:
            raise ValueError('M must be a positive')
        
        X2, Y2 = [], []
        for i in range(input_M):
            x2 = float(input(f"Enter x (a real number) for point {i+1}: "))
            y2 = int(input(f"Enter y (non-negative integer) for point {i+1}: "))
            if y2 < 0:
                raise ValueError('y must be a non-negative integer')
            
            X2.append(x2)
            Y2.append(y2)
        
        X_pretest = np.array(X2)
        Y_pretest = np.array(Y2)

        X_test = X_pretest.reshape(-1, 1)
        Y_test = Y_pretest.reshape(-1, 1).astype(int)

        print(X_test)
        print(Y_test)

        best_k = 1
        best_accuracy = 0.0

        for k in range(1, 11):
            knn = kr(n_neighbors=k)
            knn.fit(X_train, Y_train)
            Y_pred = knn.predict(X_test)
            accuracy = accuracy_score(Y_test, Y_pred)
            print(f"k = {k}, Accuracy = {accuracy:.4f}")
        
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k
    
        print(f"Best k: {best_k} with Accuracy: {best_accuracy:.4f}")


    except ValueError as error:
        print(f'input error:{error}')

knnClassifier()
