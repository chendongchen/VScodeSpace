
import matplotlib.pyplot as plt
import numpy as np
import math 


## 基础性质
# NumPy的数组类被调用ndarray。它也被别名所知 array。请注意，numpy.array这与标准Python库类不同array.array，后者只处理一维数组并提供较少的功能。ndarray对象更重要的属性是：

# ndarray.ndim - 数组的轴（维度）的个数。在Python世界中，维度的数量被称为rank。
# ndarray.shape - 数组的维度。这是一个整数的元组，表示每个维度中数组的大小。对于有 n 行和 m 列的矩阵，shape 将是 (n,m)。因此，shape 元组的长度就是rank或维度的个数 ndim。
# ndarray.size - 数组元素的总数。这等于 shape 的元素的乘积。
# ndarray.dtype - 一个描述数组中元素类型的对象。可以使用标准的Python类型创建或指定dtype。另外NumPy提供它自己的类型。例如numpy.int32、numpy.int16和numpy.float64。
# ndarray.itemsize - 数组中每个元素的字节大小。例如，元素为 float64 类型的数组的 itemsize 为8（=64/8），而 complex32 类型的数组的 itemsize 为4（=32/8）。它等于 ndarray.dtype.itemsize 。
# ndarray.data - 该缓冲区包含数组的实际元素。通常，我们不需要使用此属性，因为我们将使用索引访问数组中的元素
# 

# This is the example

# a = np.arange(15).reshape(3,5)
# print(a, a.shape, a.ndim, a.dtype.name, a.itemsize, a.size, type(a))


## 数组创建

# 有几种方法可以创建数组。

# 例如，你可以使用array函数从常规Python列表或元组中创建数组。得到的数组的类型是从Python列表中元素的类型推导出来的。

# a=np.array([0,1,2,3,4,5])
# print(a)
# print(a.dtype)

# b=np.array([1.2, 3.5, 20.9])
# print(b)
# print(b.dtype)

# 也可以在创建时显式指定数组的类型：

# 创建一个复数对象
# c = np.array( [ [ 1, 2 ], [ 3, 4 ] ], dtype = complex )
# print( c )

# 通常，数组的元素最初是未知的，但它的大小是已知的。
# 因此，NumPy提供了几个函数来创建具有初始占位符内容的数组。这就减少了数组增长的必要，因为数组增长的操作花费很大。
# 函数zeros创建一个由0组成的数组，
# 函数 ones创建一个完整的数组，
# 函数empty 创建一个数组，其初始内容是随机的，取决于内存的状态。
# 默认情况下，创建的数组的dtype是 float64 类型的。

# print(np.zeros( (3, 4 ) ), np.ones( (2, 3, 4 ), dtype=np.int16), np.empty( (3, 4 ) ) )

# 为了创建数字组成的数组，NumPy提供了一个类似于range的函数，该函数返回数组而不是列表。给定范围，并给定步长
# 当arange与浮点参数一起使用时，由于有限的浮点精度，通常不可能预测所获得的元素的数量。
# 出于这个原因，通常最好使用linspace函数来接收我们想要的元素数量的函数，而不是步长（step）：给定元素个数

# print( np.arange( 10, 30, 5 ) )
# #  array([10, 15, 20, 25])
# print( np.arange( 0, 2, 0.3 ) )                # it accepts float arguments
# #  array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])
# np.linspace( 0, 2, 9 )                 # 9 numbers from 0 to 2
# # array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])
# x = np.linspace( 0, 2*math.pi, 100 )        # useful to evaluate function at lots of points
# f = np.sin(x)

# plt.plot(x, f)       # Plot the sine of each x point
# plt.show()                  # Display 

# 打印数组
# a = np.arange(36)
# print(a)
# print( a.reshape(6, 6) )
# print( a.reshape(2, 3, 6) )
# # reshape 不会改变数组
# print( a )

## 基本操作 

# 数组上的算术运算符会应用到 元素 级别。下面是创建一个新数组并填充结果的示例：

# a = np.array( [20, 30, 40, 50] )
# b = np.arange( 4 )
# print( str(a) + "+" + str(b) + "=" + str( a+b ) )
# print( str(b) + "**2 = " + str( b**2 ) )
# print( "10*np.sin( a ) = " + str(10*np.sin( a )) )

# # 要执行矩阵乘法运算可使用 @ or dot, 与矩阵语言相似。

# print( a @ b)
# print( a.dot( b ) )

# 对于不同类型的数组进行操作，结果数组向上转换为更精确的数组

# a = np.ones( (2, 3), dtype = int ) 
# b = np.random.random( (2, 3))
# c = a + b
# print( a.dtype, b.dtype, c.dtype)

# # int32 float64 float64

# 许多一元操作，例如计算数组中所有元素的总和，都是作为ndarray类的方法实现的。

# a = np.random.random( (12, 33) )
# print( a, a.sum(), a.max(), a.min())

## 通函数

# NumPy提供熟悉的数学函数，例如sin，cos和exp。在NumPy中，这些被称为“通函数”（ufunc）。
# 在NumPy中，这些函数在数组上按元素进行运算，产生一个数组作为输出。

# A = np.arange(10)
# print(np.sin(A), np.exp(A), np.sqrt(A))

# 另见这些通函数
# all， any， apply_along_axis， argmax， argmin， argsort， average， 
# bincount， ceil， clip， conj， corrcoef， cov， cross， cumprod， cumsum， 
# diff， dot， floor， inner， INV ， lexsort， max， maximum， 
# mean， median， min， minimum， nonzero， outer， prod， re， round， 
# sort， std， sum， trace， transpose， var， vdot， vectorize， where


## 索引、切片和迭代
# 一维的数组可以进行索引、切片和迭代操作的，就像 列表 和其他Python序列类型一样。
# 地址起点是0

# a = np.arange(10)**3
# print( a )
# print( a[2] )
# print( a[2:4] ) # 2：4 的所有元素

# 多维的数组每个轴可以有一个索引。这些索引以逗号​​分隔的元组给出：
# ：表示全部
# 三个点（ ... ）表示产生完整索引元组所需的冒号。例如，如果 x 是rank为5的数组（即，它具有5个轴），则


# 1,2,...] 相当于 x[1,2,:,:,:]，
# 迭代对多维数组进行 迭代（Iterating） 是相对于第一个轴完成的：如果想要对数组中的每个元素执行操作，可以使用flat属性，该属性是数组的所有元素的迭代器：
# b = np.random.random((4, 5))
# print( b )
# for row in b:
#      print(row)
# # 但是，如果想要对数组中的每个元素执行操作，可以使用flat属性，该属性是数组的所有元素的迭代器：

# for element in b.flat:
#      print(element)

# this is for testing environment of packages 

# x = np.linspace(0, 200, 1000)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()                  # Display 

a = np.arange(10)
b = a
if a is b:
     print("true")
