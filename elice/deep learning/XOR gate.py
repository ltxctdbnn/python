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

def NAND_gate(x1, x2):
    x= np.array([x1, x2])
    
    weight = np.array([0.5, 0.5])
    
    bias = 0.6
    
    y = -1 * np.matmul(x, weight) + bias
    
    return Step_Function(y)

def Step_Function(y):
    
    return 0 if y < 0 else 1

def XOR_gate(x1, x2):
    
    return AND_gate(NAND_gate(x1, x2), OR_gate(x1, x2))

def main():
    array = np.array([[0,0], [0,1], [1,0], [1,1]])
    
    print('XOR Gate')
    
    for x1, x2 in array:
        print('Input : ', x1, x2, 'Output : ', XOR_gate(x1, x2))
        
if __name__ == '__main__':
    main()