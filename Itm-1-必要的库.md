## NumPy
科学计算：多维数组、高级数学函数等  
在skleran中，`NumPy数组`是基本数据结构，所用到的数据都必须转化成NumPy数组。NumPy核心概念：`ndarray类`，其元素必须是同一类型。  
```python
In[2]: import numpy as np
In[3]: x = np.array([[1, 2, 3], [10, 20 ,40]])
In[4]: x
Out[4]: 
array([[ 1,  2,  3],
       [10, 20, 40]])
```
## Scipy
科学计算函数集合：线性代数高级程序、统计分布等。利用其实现算法。其中scipy.sparse给出`稀疏矩阵`。用以保存大部分元素是0的二维数组。  
```python
In[5]: from scipy import sparse
  ...: eye = np.eye(4)
  ...: eye
Out[5]: 
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])
```
转为CSR(CompressedSparseRowformat)格式
```python
In[6]: sparse_matrix = sparse.csr_matrix(eye)
In[7]: sparse_matrix
Out[7]: 
<4x4 sparse matrix of type '<class 'numpy.float64'>'
	with 4 stored elements in Compressed Sparse Row format>
In[8]: "{}".format(sparse_matrix)
Out[8]: '  (0, 0)\t1.0\n  (1, 1)\t1.0\n  (2, 2)\t1.0\n  (3, 3)\t1.0'
```
COO(Coordinate)格式，创建同一矩阵。 
```python
In[9]: date = np.ones(4)
  ...: row_indices = np.arange(4)
  ...: col_indices = np.arange(4)
In[10]: eye_coo = sparse.coo_matrix(date, (row_indices, col_indices))
   ...: eye_coo
Out[10]: 
<1x4 sparse matrix of type '<class 'numpy.float64'>'
	with 4 stored elements in COOrdinate format>
In[11]: "{}".format(eye_coo)
Out[11]: '  (0, 0)\t1.0\n  (0, 1)\t1.0\n  (0, 2)\t1.0\n  (0, 3)\t1.0'
```
## matplotlib
科学绘图：可视化。
_占位符_
## pandas
处理分析数据。基于`DateFrame`数据结构（类似表格）
_占位符_
