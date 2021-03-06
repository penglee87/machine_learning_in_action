>>> import numpy as np

>>> xnums =np.arange(4)
>>> ynums =np.arange(5)
>>> data_list= np.meshgrid(xnums,ynums)
>>> type(data_list)
<class 'list'>
>>> type(data_list[0])
<class 'numpy.ndarray'>
>>> data_list[0].shape
(5, 4)
>>> data_list[1].shape
(5, 4)
>>> data_list
[array([[0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3]]), array([[0, 0, 0, 0],
       [1, 1, 1, 1],
       [2, 2, 2, 2],
       [3, 3, 3, 3],
       [4, 4, 4, 4]])]
>>> x,y =data_list
>>> x
array([[0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3]])
>>> y
array([[0, 0, 0, 0],
       [1, 1, 1, 1],
       [2, 2, 2, 2],
       [3, 3, 3, 3],
       [4, 4, 4, 4]])
>>> x.ravel()
array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3])
>>> x.ravel().shape
(20,)
>>> y.ravel()
array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])
>>> np.array([x.ravel(), y.ravel()])
array([[0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
       [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]])
>>> np.array([x.ravel(), y.ravel()]).T
array([[0, 0],
       [1, 0],
       [2, 0],
       [3, 0],
       [0, 1],
       [1, 1],
       [2, 1],
       [3, 1],
       [0, 2],
       [1, 2],
       [2, 2],
       [3, 2],
       [0, 3],
       [1, 3],
       [2, 3],
       [3, 3],
       [0, 4],
       [1, 4],
       [2, 4],
       [3, 4]])
>>> np.c_[x.ravel(), y.ravel()]
array([[0, 0],
       [1, 0],
       [2, 0],
       [3, 0],
       [0, 1],
       [1, 1],
       [2, 1],
       [3, 1],
       [0, 2],
       [1, 2],
       [2, 2],
       [3, 2],
       [0, 3],
       [1, 3],
       [2, 3],
       [3, 3],
       [0, 4],
       [1, 4],
       [2, 4],
       [3, 4]])
>>> np.c_[x.ravel(), y.ravel()].shape
(20, 2)
>>> np.c_[x.ravel(), y.ravel()][:,0]
array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3])
>>> np.c_[x.ravel(), y.ravel()][:,0].shape
(20,)
>>> np.c_[x.ravel(), y.ravel()][:,0].reshape(x.shape)
array([[0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3]])
>>> 