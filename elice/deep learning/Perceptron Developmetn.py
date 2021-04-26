def main():
    x = [1, 2, 3, 4]
    w = [1, 2, 3, 4]
    b = -2
    
    output, y = perceptron(w, x, b)
    
    print('output : ', output)
    print('y : ', y)
    
def perceptron(w, x, b):
    output = 0
    
    for i in range(0, len(x)):
        output = (w[i] * x[i]) + output
        
    output = output + b
    
    y = 1 if output > 0 else 0
    
    return output, y

if __name__ == '__main__':
    main()