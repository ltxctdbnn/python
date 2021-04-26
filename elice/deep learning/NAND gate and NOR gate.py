import numpy as np

def NAND_gate(x1, x2):
    x= np.array([x1, x2])
    
    weight = np.array([0.5, 0.5])
    
    bias = 0.6
    
    y = -1 * np.matmul(x, weight) + bias
    
    return Step_Function(y)

def NOR_gate(x1, x2):
    x = np.array([x1, x2])
    
    weight = np.array([0.5, 0.5])
    
    bias = 0.4
    
    y = -1 * np.matmul(x, weight) + bias
    
    return Step_Function(y)

def Step_Function(y):
    
    return 0 if y < 0 else 1

def main():
    array = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    
    print('NAND Gate')
    
    for x1, x2 in array:
        print('Input : ', x1, x2, 'Output : ', NAND_gate(x1, x2))
        
    print('NOR Gate')
    
    for x1, x2 in array:
        print('Input : ', x1, x2, 'Output : ', NOR_gate(x1, x2))
        
if __name__ == '__main__':
    main()