#Programming 101
#week13
#discussion 1

def func1(a):
    a=2
def func2(b):
    b['test']=2
def func3():
    c={}
    c['test']=10
def func4():
    global d
    d=2
def func5():
    e=10
    return e

#Case 1
a=0
func1(a)
print('case 1: a=',a)

#Case 2
b={}
func2(b)
print('case 2: b=',b)

#Case 3
c={}
func3()
print('case 3: c=',c)

#Case 4
d=0
func4()
print('case 4: d=',d)

#Case 5
e=0
e=func5()
print('case 5: e=',e)
