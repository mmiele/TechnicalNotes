### Method:1 ###
for i in range(1,20,2):
    print(('*'*i).center(20))
for sp in range(3):
    print(('||').center(20))
print(('\====/').center(20))


### Method: 2 ###
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
import numpy as np
x = np.arange(7,16)
y = np.arange(1,18,2)
z = np.column_stack((x[::-1],y))
for i,j in z:
    print(' '*i+'*'*j)
for r in range(3):
    print(' '*13,'||')
print(' '*12, end = '\====/')
print('')