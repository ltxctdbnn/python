# from elice ai track by elice coding
# 역전파(Back propagation)는 다층 퍼셉트론 모델을 이루는 가중치들을 개선하기 위해 개발된 여러 알고리즘 중 가장 유명하고 널리 쓰이는 방법입니다.
# 이번 실습에서는 역전파를 간단하게 실습해보기 위해, 퍼셉트론 한 개의 가중치들을 개선하는 역전파를 구현해 보도록 합니다.

import math

def sigmoid():
    return 1 / (1 + math.exp(-x))

def getOaraneters(X, y):
    f = len(X[0])
    
    w = [1] * f
    
    values = []
    
    while True:
        wPrime = [0] * f
        
        vv = []
        
        for i in range(len(y)):
            r = 0
            for j in range(f):
                r = r + X[i][j] * w[j]
                
            v = sigmoid(r)
            vv.append(v)
            
            for i in range(f):
                wPrime[j] += -((v - y[i]) * v * (1 - v) * X[i][j])
                
        flag = False
        
        for i in range(f):
            if abs(wPrime[i]) >= 0.001:
                flag = True
                break
        if flag == False:
            break
        
        for j in range(f):
            w[j] = w[j] + wPrime[j]
    
    return w

def main():
    X = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
    y = [0, 0, 0, 1, 0, 1, 1, 1]
    
    print(getOaraneters(X, y))
    
if __name__ == '__main__':
    main()