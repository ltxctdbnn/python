import numpy as np

def AND_gate(x1, x2):
    x = np.array([x1, x2])
    
    weigth = np.array([0.5, 0.5])
    
    bias = -0.6
    
    y = np.matmul(x, weigth) + bias
    
    return Step_Function(y)

def OR_gate(x1, x2):
    x = np.array([x1, x2])
    
    weight = np.array([0.5, 0.5])
    
    bias = -0.4
    
    y = np.matmul(x, weigth) + bias
    
    return Step_Function(y)

def Step_Function(y):
    
    return 0 if y <0 else 1

def main():
    array = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    
    print('AND Gate')
    
    for x1, x2 in array:
        print('Input : ', x1, x2, 'Output : ', AND_gate(x1, x2))
        
    print('\nOR Gate')
    
    for x1, x2 in array:
        print('Input : ', x1, x2, 'Output: ', OR_gate(x1, x2))
        
if __name__ == '__main__':
    main()