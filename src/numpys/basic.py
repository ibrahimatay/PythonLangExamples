import numpy as np

a = np.arange(6)
print(a) # [0 1 2 3 4 5]

a = np.arange(1, 10, 1)
print(a) # [1 2 3 4 5 6 7 8 9]

a2 = a[np.newaxis, :]
print(a2) # [[1 2 3 4 5 6 7 8 9]]

a = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
])

print('sort {0}'.format(np.sort(a)))

print(a[1]) # [5, 6, 7, 8]

vector2 = np.zeros(6,)
print(vector2)