def subtract(x1, x2):
    return x1 - x2                     
def addition(x1, x2):
    return x1 + x2                     
def product(x1, x2):
    return x1 * x2
def division(x1, x2):
    return x1 / x2
op=""
while op != "0":
    print("運算方法功能選單")
    print("0:離開程式")
    print("1:加法")
    print("2:減法")
    print("3:乘法")
    print("4:除法")
    op = (input("請輸入0/1/2/3/4: "))
    if op == "0":
        print("離開程式")
    elif op.isdecimal():
            try:
                a = float(input("a = "))
                b = float(input("b = "))
                if op == "1":
                    print("a + b = ", addition(a, b))   
                elif op == "2":
                    print("a - b = ", subtract(a, b))   
                elif op == "3":
                    print("a * b = ", product(a, b))
                elif op == "4":
                    if b!=0:
                        print("a / b =", division(a, b))
                    elif b==0:
                        print("b不可為0")
            except ValueError:
                print("請輸入阿拉伯數字")
    else:
        print("輸入的並非選項之一")
