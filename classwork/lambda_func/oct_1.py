import math 
L = [100, 101, 102, 100, 55, 101, 55]
X = L.copy()

def modL1():
    iter = 0
    for i in L:
        print(iter, i, L.count(i))

        if L.count(i) > 1: 
            X.remove(i)
        iter += 1
import copy
copy.deepcopy(L)



# main() is a special function that controls how a program is executed.

alist = [2, 4, 7, 9, 11]
def f7():
    global alist
    print(alist)
    alist = alist * 2
    mysum = sum(alist)
    return mysum **0.5


def changeList(L: list):
    for i in range(len(L)):
        L.append(i)

    return L

print('################# output')


def main():
    print('starting my program')
    return f7()

if __name__ == "__main__":
    print('Only executed when the script is ran not called')
    ans = main()
    print(ans)
else:
    print('executed from the else part')
    myvar = [100, 101, 102]
    import math

    print(changeList(myvar))
