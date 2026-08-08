import numpy as np

#1. 1.Create two 1D arrays and join them.
'''a= np.array([1,2])
b=np.array([3,4])
c=np.concatenate((a,b))
print (c)
'''

#2. Join three arrays into one.
'''
a,b= np.array([1,2],[3,5])
c=([7,8])
d= np.concatenate((a,b,c))
print (d)'''

#3. Join two 2D arrays row-wise (axis=0).
'''
a=np.array([[1,2],[3,5]])
b=np.array([[4,8],[9,7]])
c=np.concatenate((a,b),axis=0)
#OR
c1=np.vstack((a,b))
print (c)
print (c1)'''

#4. Join two 2D arrays column-wise (axis=1).
'''a=np.array([[1,2],[3,5]])
b=np.array([[4,8],[9,7]])
c=np.concatenate((a,b),axis=1)
#OR
c1=np.hstack((a,b))
print (c)
print (c1)
'''
#5. Use stack on two 2-D arrays
'''a=np.array([[1,2],[3,5]])
b=np.array([[4,8],[9,7]])
c=np.stack((a,b),axis=1)
print (c)
'''

#6.Create two student score arrays and merge them.

student1 = np.array([85, 90])   # [Math, Science]
student2 = np.array([78, 88])   # [Math, Science]
##use Vstack

