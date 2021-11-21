import numpy as np

mat = np.arange(0, 100).reshape((10,10))
filtered_list = mat > 50

my_list = mat[filtered_list]
print(my_list)