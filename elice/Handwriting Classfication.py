import numpy as np
import random
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
import warnings

warnings.filterwarnings(action='ignore')

np.random.seed(100)

def load_data(X, Y):
    
    X_train = X[:1600]
    Y_train = Y[:1600]
    
    X_test = X[1600:]
    Y_test = Y[1600:]
    
    return X_train, Y_train, X_test, Y_test

def train_MLP_classifier(X, Y):
    
    clf = MLPClassifier(hidden_layer_sizes=(160,240))
    
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
    
    digits = load_digits()
    
    X = digits.data
    Y = digits.target
    
    X_train, Y_train, X_test, Y_test = load_data(X, Y)
    
    clf = train_MLP_classifier(X_train, Y_train)
    
    score = report_clf_stats(clf, X_test, Y_test)
    
    return score

if __name__ == "__main__":
    main()