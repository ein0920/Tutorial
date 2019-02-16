
import pandas as pd
import numpy as np
np.set_printoptions(precision=4)


# 1、生成，类名称ndarray，生成是函数是array
if __name__ == '__main__':
    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    arr2 = np.array(data2, dtype=np.int8)

    # 两个属性，维数和形状
    arr2.ndim
    arr2.shape

    # 根据形状生成
    np.zeros(10)  # zeros_like是输入一个ndarray
    np.zeros((3, 6))
    np.empty((2, 3, 2))

    # range的ndarray版
    np.arange(15)


# 随机数生成
if __name__ == '__main__':
    samples = np.random.normal(size=(4, 4))  # 正态分布，loc是均值，scale是标准差，size=None默认返回一个数
    samples = np.random.randn(4, 5)  # 返回4行5列的标准正态分布
    samples = np.random.rand(3, 2)  # 返回3行2列的0-1的均匀分布
    samples = np.random.randint(low=1, high=10, size=(4, 6))  # 返回4行6列的下限为1，上限为10（不含）的随机整数分布
    samples = np.random.permutation(samples)  # 将samples打乱顺序，如果输入的是x的话，那么输出打乱顺序后的np.arange(x)
    np.random.shuffle(samples)  # 将samples打乱顺序
    samples = np.random.binomial(n=10, p=0.02, size=(4, 5))  # 二项分布
    samples = np.random.beta(a=4, b=6, size=(4, 5))  # beta分布
    samples = np.random.chisquare(df=0.95, size=(4, 5))  # 卡方分布
    samples = np.random.gamma(shape=2.0, size=(4, 5))  # gamma分布
    samples = np.random.uniform()  # 0-1均匀分布


# 数据类型，ndarray是同构的。生成的时候可以指定dtype
if __name__ == '__main__':
    int_array = np.arange(10)
    calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float32)
    new_int_array = int_array.astype(calibers.dtype)


# 3、索引和切片，切片是一个view，不是copy
if __name__ == '__main__':
    # 3.1 int和切片
    arr = np.arange(10)
    arr
    arr[5]
    arr[5:8]
    arr[5:8] = 12

    # 3.2 二维索引
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    arr2d[2]

    arr2d[0][2]
    arr2d[0, 2]

    arr2d[1, :2]
    arr2d[2, :1]

    # 3.3 布尔索引
    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    data = np.random.randn(7, 4)
    # 对于2维数组，输入一维的布尔索引就相当于选定行，
    data[names == 'Bob']
    # 对于2维数组，布尔索引和切片混合
    data[names == 'Bob', 2:]

    names != 'Bob'
    data[-(names == 'Bob')]  # 布尔前面加- 相当于not

    # 两个布尔的and or 是 & |
    mask = (names == 'Bob') | (names == 'Will')

    # 也可以二维布尔数组，索引的结果变成一维数组。
    data[data < 0]
    data[data < 0] = 0

    # 3.4 花式索引，花式索引不是view，是一个copy
    # 花式所以就是在[]输入一个[4, 3, 0, 6]之类的整数数组，
    arr = np.empty((8, 4))
    for i in range(8):
        arr[i] = i
    arr[[4, 3, 0, 6]]
    arr[[-3, -5, -7]]

    # 输入二维的也可以
    # more on reshape in Chapter 12
    arr = np.arange(32).reshape((8, 4))
    arr[[1, 5, 7, 2], [0, 3, 1, 2]]  # 最终选出的元素是(1,0)(5,3)(7,1)(2,2)四个点
    # 如果需要是方形区域
    arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]
    arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]  # pd也有ix


# np的矩阵计算和标量运算
if __name__ == '__main__':
    arr = np.array([[1., 2., 3.], [4., 5., 6.]])

    # 标量运算
    arr * arr
    arr + arr
    arr - arr
    arr / arr
    5 * arr # 和[1,2,3] * 5不同

    # 矩阵运算
    arr.T # 转置

    # 点乘
    x = np.array([[1., 2., 3.], [4., 5., 6.]])
    y = np.array([[6., 23.], [-1, 7], [8, 9]])
    x.dot(y)  # equivalently np.dot(x, y)

    # 线性代数计算库
    from numpy.linalg import inv
    X = np.random.randn(5, 5)
    mat = X.T.dot(X)
    inv(mat)  # 求逆
    # 详细函数见书110页


# 元素级函数
if __name__ == '__main__':
    # 5.1 ufunc一元元素级函数
    arr = np.arange(10)

    # 一些ufunc顶级函数
    np.abs(arr)
    np.isnan(arr)
    np.isfinite(arr)
    np.isinf(arr)

    # 5.2 二元ufunc元素级函数
    np.add(arr, arr)

    # 5.3 np.where
    arr = np.random.randn(4, 4)

    np.where(arr > 0, 2, -2) + 1
    np.where(arr > 0, 2, arr)  # set only positive values to 2

    cond1 = np.random.randn(4, 4)  # cond1和cond2是两个布尔数组，这样写只是不想让程序报错，
    cond2 = np.random.randn(4, 4)

    np.where(cond1 & cond2, 0,
             np.where(cond1, 1,
                      np.where(cond2, 2, 3)))


# 聚合函数
if __name__ == '__main__':
    # 5.4 数学和统计方法，聚合函数
    arr = np.random.randn(5, 4)  # 5行4列，axis=1就是返回5个数。
    arr.mean()  # 整个数组求均值
    np.mean(arr)

    arr.mean(axis=1)  # 不同同轴元素之间的运算，
    # axis = 1 如下所示
    # 4 <------ |ˉ| |ˉ| |ˉ| |ˉ|
    # 4 <------ | | | | | | | |
    # 4 <------ | | | | | | | |
    # 4 <------ | | | | | | | |
    # 4 <------ |_| |_| |_| |_|
    # axis = 0 如下所示
    # 4   4   4  4
    # ^   ^   ^  ^
    # |   |   |  |
    # |二 二 二 二|
    # |二 二 二 二|
    # |二 二 二 二|
    # |二 二 二 二|

    # 当布尔型数据用于上述方法时，True被强制转换成1
    bools = np.array([False, False, True, False])
    bools.any()  # 对于bool数组来说是否存在True
    bools.all()  # 对于bool数组来说是否全True


# 5.5 排序
if __name__ == '__main__':
    # 就地排序，改变自身，ndarray的方法
    large_arr = np.random.randn(1000)
    large_arr.sort()
    large_arr[int(0.05 * len(large_arr))]  # 5% quantile

    arr = np.random.randn(5, 3)
    arr.sort(1)  # 对位置1的行排序，其他不变，会改变数组的相对位置。

    # 用np.sort()排序是产生副本


# 集合运算
if __name__ == '__main__':
    # 5.6 唯一和集合逻辑
    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    np.unique(names)  # 取唯一后进行排序

    # 集合的函数
    values = np.array([6, 0, 0, 3, 2, 5, 6])
    np.in1d(values, [2, 3, 6])  # values的每个元素是否在[2, 3, 6]中。
    # 返回array([ True, False, False,  True,  True, False,  True], dtype=bool)
    np.unique(values)  # 唯一元素
    np.intersect1d(values, values)  # 交集
    np.union1d(values, values)  # 并集
    np.setdiff1d(values, values)  # 前-后的差集
    np.setxor1d(values, values)  # 对称差。


# 二、np的高级应用
# 1、判断ndarray的数据类型
if __name__ == '__main__':
    ints = np.ones(10, dtype=np.uint16)
    floats = np.ones(10, dtype=np.float32)
    np.issubdtype(ints.dtype, np.integer)  # 判断数据类型
    np.issubdtype(floats.dtype, np.floating)

    np.float64.mro()  # np.float64所有的父类


# 2、重塑
if __name__ == '__main__':
    # 2.1折叠
    arr = np.arange(8)
    arr.reshape((4, 2))  # 变成4行2列的结构，不接收inplace参数
    arr = np.arange(15)
    arr.reshape((5, -1))  # 填-1的那个维度自动计算

    other_arr = np.ones((3, 5))
    arr.reshape(other_arr.shape)  # 根据其他数组的形状来重塑

    # 2.2 拉平
    arr = np.arange(15).reshape((5, 3))
    arr.ravel()  # 拉平，不创建副本
    arr.flatten()  # 创建副本
    arr = np.arange(12).reshape((3, 4))
    arr.ravel()
    arr.ravel('F') # 默认是C顺序，F顺序列优先


# 3、数组的合并和拆分
if __name__ == '__main__':
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[7, 8, 9], [10, 11, 12]])
    np.concatenate([arr1, arr2], axis=0)  # 上下连接
    np.concatenate([arr1, arr2], axis=1)  # 左右连接

    np.vstack((arr1, arr2))  # 上下连接，vertical
    np.hstack((arr1, arr2))  # 左右连接，horizonal

    # 堆叠辅助
    arr = np.arange(6)
    arr1 = arr.reshape((3, 2))
    arr2 = np.random.randn(3, 2)
    np.r_[arr1, arr2]  # 行堆叠
    np.c_[np.r_[arr1, arr2], arr]  # 列堆叠，如果

    # 将切片翻译成数组
    np.c_[1:6, -10:-5]

    # 分拆
    arr = np.random.randn(5, 2)
    first, second, third = np.split(arr, [2, 3])  # 分别是ary[:2]，ary[2:3]，ary[3:]


# 4、元素的重复操作
if __name__ == '__main__':
    arr = np.arange(3)
    arr.repeat(3)  # 重复 array([0, 0, 0, 1, 1, 1, 2, 2, 2])，每个重复三次
    arr.repeat([2, 3, 4])  # 不同元素重复次数不一样

    # 多维数组的复制
    arr = np.random.randn(2, 2)
    arr.repeat(2, axis=0)  # 分组行，每个复制成两倍
    arr.repeat([2, 3], axis=0)  # 第一行复制两次，第二行复制3次
    arr.repeat([2, 3], axis=1)  # 第一列复制两次，第二列复制3次

    # tile 铺瓷砖，一块一块复制
    arr
    np.tile(arr, 2)  # 水平铺设
    np.tile(arr, (2, 1))  # 两行一列地铺设
    np.tile(arr, (3, 2))  # 3行2列地铺设

    # 花式索引的等价函数，take和put
    # 花式索引就是输入一个list of int 来引用对应行的数据，布尔索引是布尔的数组来索引
    arr = np.arange(10) * 100
    inds = [7, 1, 2, 6]

    arr[inds]
    arr.take(inds)  # 效果是一样的，

    arr.put(inds, 42)  # put是会改变arr，意思是将inds表示的元素变成42，42放到inds表示的元素中
    arr.put(inds, [40, 41, 42, 43])

    # 二维数组，索引列，axis=1
    inds = [2, 0, 2, 1]
    arr = np.random.randn(2, 4)
    arr.take(inds, axis=1)


# 5、广播
if __name__ == '__main__':
    # 广播就是不同形状的数组之间的算术运算的执行方式。最简单就是和标量相乘
    arr = np.arange(5)
    arr * 4  # 每个元素都乘以4，

    # A二维 - B一维，B默认是一行的，所以就是才行上广播，A的每行都减去B
    arr = np.random.randn(4, 3)
    arr.mean(0)  # 相当于axis=0
    demeaned = arr - arr.mean(0)
    demeaned.mean(0)

    # 如果需要在列上广播，那么就要reshape一下
    arr - np.array([1, 1, 1, 1]).reshape(4, 1)

    row_means = arr.mean(1)  # 即使是这样计算下来，等到的一维还是默认是行，所以不能广播
    demeaned = arr - row_means.reshape((4, 1))


# 6、ufunc元素级函数的高级应用
if __name__ == '__main__':
    # 一维的情况
    arr = np.arange(10)
    np.add.reduce(arr)  # 求和，就是约简运算的意思
    arr.sum()  # 也是求和

    # 二维的情况
    arr = np.random.randn(5, 5)
    arr[::2].sort(1)  # 排序是就地排序

    # 自定义ufunc
    def add_elements(x, y):
        return x + y

    add_them = np.frompyfunc(add_elements, 2, 1)
    add_them(np.arange(8), np.arange(8))


# 7、随机数生成
if __name__ == '__main__':
    # -----------------------------random 模块-----------------------------------------------
    import random
    random.random() # 用于生成一个0到1的随机符点数: 0 <= n < 1.0 ，均匀分布

    random.uniform(10, 20) # 生成10-20之间的随机数，a <= n <= b，均匀分布
    random.uniform(20, 10) # 不必后大于前

    random.randint(3,39) #用于生成一个指定范围内的整数。均匀分布
    random.randint(20, 10)  # 该语句是错误的。下限必须小于上限。

    random.randrange(10, 100, 2)# 结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。

    random.choice("学习Python") # 在可迭代对象中获得随机的元素

    p = ["Python", "is", "powerful", "simple", "and so on..."] # random.shuffle(x[, random])，用于将一个列表中的元素打乱。
    random.shuffle(p) # 对p进行修改

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
    slice = random.sample(list, 5)  # 从list中随机获取5个元素，作为一个片断返回

    # -----------------------------numpy.random 模块-----------------------------------------------
    import numpy as np
    np.random.rand(10)  # 用于生成[0.0, 1.0)之间的随机浮点数，当没有参数时，返回一个随机浮点数，
    np.random.rand(3,5)

    np.random.randn(10)  # 该函数返回一个样本，具有标准正态分布。

    np.random.randint(10, size=8)  # np.random.randint(low[, high, size]) 返回随机的整数，位于半开区间 [low, high)。

    arr = np.arange(10)
    np.random.shuffle(arr) # 将序列的所有元素随机排序
    np.random.choice() # numpy.random.choice()可以从序列(字符串、列表、元组等)中随机选取，返回一个列表，元组或字符串的随机项。

    np.random.permutation(10) # np.random.permutation(x)返回一个随机排列

    # 其他分布
    np.random.normal() # API: normal(loc=0.0, scale=1.0, size=None) loc：均值，scale：标准差，size：抽取样本的size
    np.random.binomial() # numpy.random.RandomState.binomial(n, p, size=None)表示对一个二项分布进行采样,s为成功次数
