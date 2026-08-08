import numpy as np

# 1. Find index of value 5 using where().
'''a= np.array([1,2,3,4,5,6])
print (np.where(a==5)[0])
'''
#2. Find all even numbers.
'''a= np.array([1,2,3,4,5,6])
print(np.where(a%2==0)[0]) # gives index
b=np.where(a%2==0) #gives array elements
print (a[b])'''


#3. Find numbers greater than 10
'''a= np.array([1,2,3,4,5,6])
print(np.where(a%2==0)[0]) # gives index
b=np.where(a%2==0) #gives array elements
print (a[b])'''


#4. Search multiple occurrences.
import numpy as np
a = np.array([1, 2, 3, 2, 4, 2, 5])
print(np.where(a==2))

#5. Find negative values.
import numpy as np
a = np.array([-9, -5, -3, 0, 2, 6, 8])
print(np.searchsorted(a, -4))

#6.Use searchsorted() on a sorted array.

import numpy as np
a = np.array([1, 3, 5, 7, 9])
print(np.searchsorted(a, 5))

#7. Search Insertion index of 15
import numpy as np
a = np.array([1, 5, 10, 20, 25])
print(np.searchsorted(a, 15))


#8.Find indices divisible by 3.
a = np.array([1, 5, 10,9, 20, 25])
print(np.where(a%3==0))

#9. Compare left vs right searchsorted.
a = np.array([1, 3, 5, 5, 5, 7, 9])

print(np.searchsorted(a, 5, side='left'))
print(np.searchsorted(a, 5, side='right'))