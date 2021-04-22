# from elice ai track by elice coding
# Gradient descent 알고리즘은 손실 함수(loss function)의 미분값인 gradient를 이용해 모델에게 맞는 최적의 가중치(weight), 즉 손실 함수의 값을 최소화하는 가중치를 구할 수 있는 알고리즘입니다.
# 이번 실습에서는 Gradient descent 알고리즘을 직접 구현한 후, 이를 이용해 데이터를 가장 잘 설명하는 선형 회귀 직선의 기울기와 y절편, 즉 선형 회귀 모델에게 맞는 최적의 가중치를 찾아보겠습니다.

import numpy as np

def linear_model(w0, w1, X):
    f_x = w0 + w1 * X
    
    return f_x

def Loss(f_x, y):
    ls = np.mean(np.square(y - f_x))
    
    return ls

def gradient_descent(w0, w1, X, y):
    gradient0 = 2 * np.mean((y - (w0 + w1 * X)) * (-1))
    gradient1 = 2 * np.mean((y - (w0 + w1 * X)) * (-1 * X))
    
    return np.array([gradient0, gradient1])

def main():
    X = np.array([1, 2, 3, 4]).reshape((-1, 1))
    y = np.array([3.1, 4.9, 7.2, 8.9]).reshape((-1, 1))
    
    w0 = 0
    w1 = 0
    
    lr = 0.001
    
    for i in range(1000):
        gd = gradient_descent(w0, w1, X, y)
        
        w0 = w0 - lr * gd[0]
        w1 = w1 - lr * gd[1]
        
        if (i % 100 == 0):
            loss = Loss(linear_model(w0, w1, X), y)
            
            print("{}번째 loss : {}".format(i, loss))
            print("{}번째 w0, w1 : {}, {}".format(i, w0, w1), "\n")
            
        return w0, w1
    
if __name__ == '__main__':
    main()