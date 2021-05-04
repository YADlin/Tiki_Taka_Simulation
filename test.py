import numpy as np

P1 = np.array([300, 290])
P2 = np.array([500, 200])
P3 = np.array([800, 200])
P4 = np.array([1000, 290])
P5 = np.array([500, 380])
P6 = np.array([300, 380])

P = np.array([P1, P2, P3, P4, P5, P6])
P = np.transpose(P)
c = np.random.randint(0, 2)
i = np.shape(P)
print(i[0])
