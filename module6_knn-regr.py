import numpy as np

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
    
        points = []
        for i in range(input_N):
            x, y = map(float, input(f"Enter x and y for point {i+1} (separated by space): ").split())
            points.append((x, y))
        
        points = np.array(points)
        print(points)

        input_X = float(input('please input a X value for prediction: '))

        distances = np.abs(points[:,0]-input_X)

        nearest_indices = np.argsort(distances)[:input_X]

        predict = np.mean(points[nearest_indices, 1])

        print(f'The Y value predicted is:{predict}')

    except ValueError as error:
        print(f'input error:{error}')

knn()
