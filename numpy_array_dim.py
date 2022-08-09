import numpy as np

# rank = ndim = dimension

# a2=np.arange(8).reshape(2,2,2)
a2 = np.array([[[[1,2],[3,4]],[[5,6],[7,8]],[[5,6],[7,8]],[[5,6],[7,8]]],[[[1,2],[3,4]],[[5,6],[7,8]],[[5,6],[7,8]],[[5,6],[7,8]]]])
print(a2.ndim)
print(a2.shape)
print(a2.size)
a = np.random.randn(4,3,3,2)
print(a.shape)

arr = np.array([1, 2, 3])
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr.ndim)
print(arr.shape)