from tkinter.font import names

import numpy as np

random_3D_array = np.random.randint(10, 100, size=(3, 3))
print(random_3D_array)

w, v = np.linalg.eig(random_3D_array)

print("\nPrinting the Eigen values of the given square array:\n",w)
print("\nPrinting Right eigenvectors of the given square array:\n",v)

combined  = np.vstack((w,v))

np.savetxt('eigen.csv', combined,delimiter=',')