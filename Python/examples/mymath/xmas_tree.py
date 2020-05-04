'''
.. module:: xmas_tree
    :platform: OS X
    :synopsis: Shows how to use important data types

.. note::
    It shows how to use numpy

    How to run it:
        In a terminal winodow at the command prompt enter: > python xmas-tree.py.
        Enter the operation selection, then the first and second operand.

.. moduleauthor:: Michael <milexm@gmail.com>

'''
# import numpy as np

# Method:1
def xmas_tree_1():
    for i in range(1,20,2):
        print(('*'*i).center(20))
    for sp in range(3):
        print(('||').center(20))
    print(('\====/').center(20))


### Method: 2 ###
def xmas_tree_2():
    b = 34
    c = 0
    while b > 0 and c < 33 :
            print('\33[1;32;48m'+' '*b+'*'+'*'*c+'\33[0m')
            b -= 1
            c += 2
    for r in range(3):
        print(' '*33,'||')
    print(' '*32, end = '\====/')
    print('')

### Method:3 ###
def xmas_tree_3():
    x = np.arange(7,16)
    y = np.arange(1,18,2)
    z = np.column_stack((x[::-1],y))
    for i,j in z:
        print(' '*i+'*'*j)
    for r in range(3):
        print(' '*13,'||')
    print(' '*12, end = '\====/')
    print('')


def main():
    xmas_tree_1()
    xmas_tree_2()
    xmas_tree_3()

if __name__ == "__main__":
    main()
