import numpy as np
import sklearn.neural_network import MLPClassifier
import warnings
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt

def visualize(clf, X, Y):
    X_ = []
    Y_ = []
    colors = []
    shapes = []

    plt.figure(figsize=(6, 6))

    for x, y in zip(X, Y):
        X_.append(x[1])
        Y_.append(x[0])
        if y == 0:
            colors.append('b')
        else:
            colors.append('r')

        if clf.predict([x])[0] == y:
            shapes.append('o')
        else:
            shapes.append('x')

    for x, y in zip(X, Y):
        c = '#87CEFA'
        if clf.predict([x])[0] == 1:
            c = '#fab387'
        plt.scatter(x[1], x[0], marker='s', c=c, s=1200, edgecolors='none')

    for _s, c, _x, _y in zip(shapes, colors, X_, Y_):
        plt.scatter(_x, _y, marker=_s, c=c, s=200)
    plt.show()
    
warnings.filterwarnings(action='ignore')

np.random.seed(100)

def read_data(filename):
    
    X = []
    Y = []
    
    with open(filename) as fp:
        N, M = fp.readline().split()
        N = int(N)
        M = int(M)
        
        for i in range(N):
            line = fp.readline().split()
            for j in range(M):
                X.append([i, j])
                Y.append(int(line[j]))
    
    X = np.array(X)
    Y = np.array(Y)
    
    return (X, Y)

def train_MLP_classifier(X, Y):
    
    clf = MLPClassifier(hidden_layer_sizes=(50,50))
    
    clf.fit(X, Y)
    
    return clf

def report_clf_stats(clf, X, Y):
    
    hit = 0
    miss = 0
    
    for x, y in zip(X, Y):
        if clf.predict([x])[0] == y:
            hit += 1
        else:
            miss += 1
    
    score = (hit / len(X))*100
    
    print("Accuracy: %.1lf%% (%d hit / %d miss)" % (score, hit, miss))
    
def main():
    
    X_train, Y_train = read_data('Multi Layer Perceptron Basic Data/train.txt')
    
    X_test, Y_test = read_data('Multi Layer Perceptron Basic Data/test.txt')
    
    clf = train_MLP_classifier(X_train, Y_train)
    
    score = report_clf_stats(clf, X_test, Y_test)
    
    visualize(clf, X_test, Y_test)

if __name__ == "__main__":
    main()