"""
Test in xmas_tree.py
"""

class XmasTree(object):

    """ Shows how to use numpy package.

        .. remarks::
            The class `XmasTree` creates 3 Xmas trees
            with different shapes and colors.

    """

    def xmas_tree_1(self):

        """ Builds a simple tree. """

        for i in range(1,20,2):
            print(('*'*i).center(20))
        for sp in range(3):
            print(('||').center(20))
        print(('\====/').center(20))


    def xmas_tree_2(self):

        """ Builds a more colorful tree. """

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


    def xmas_tree_3(self):

        """ Builds a simple tree. """

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
    ''' Main function,
        It displays the menu. Then enter a loop until the user exit.
    '''
    tree = XmasTree()

    tree.xmas_tree_1()
    tree.xmas_tree_2()
    tree.xmas_tree_3()


if __name__ == "__main__":
    main()
