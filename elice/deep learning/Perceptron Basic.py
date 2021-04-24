def Perceptron(x1, x2, w1, w2):
    bias = -1
    output = (x1 * w1 + w2 * x2 + bias)
    y = 1 if output > 0 else 0
    
    return output, y

def input_func():
    # 비 오는 여부(비가 온다 : 1 / 비가 오지 않는다 : 0)
    x_1 =  int(input("x1 : 비가 오는 여부(1 or 0)을 입력하세요."))
    
    # 여자친구가 만나자고 하는 여부(만나자고 한다 : 1 / 만나자고 하지 않는다 : 0)
    x_2 =  int(input("x2 : 여친이 만나자고 하는 여부(1 or 0)을 입력하세요."))
    
    # 비를 좋아하는 정도의 값(비를 싫어한다 -5 ~ 5 비를 좋아한다)
    w_1 =  int(input("w1 : 비를 좋아하는 정도 값(-5 ~ 5)을 입력하세요."))
    
    # 여자친구를 좋아하는 정도의 값(여자친구를 싫어한다 -5 ~ 5 비를 좋아한다)
    w_2 =  int(input("w2 : 여친을 좋아하는 정도 값(-5 ~ 5)을 입력하세요."))
    
    return x1, x2, w1, w2

def main():
    x1, x2, w1, w2 = input_func()
    result, go_out = Perceptron(x1, x2, w1, w2)
    
    if go_out > 0:
        print("외출 여부 : %d\n ==> 외출한다!" % go_out)
    else:
        print("외출 여부 : %d\n ==> 외출하지 않는다!" % go_out)
        
if __name__ == '__main__':
    main()