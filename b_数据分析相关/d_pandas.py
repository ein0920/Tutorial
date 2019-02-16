
import pandas as pd
import numpy as np
import datetime as dt
from dateutil.parser import parse

# 这个是Series的生成例子
if __name__ == '__main__':
    obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])  # 输入一维list
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}  # 输入dict，key成为index
    obj4 = pd.Series(sdata)


# 这个是df的生成例子
if __name__ == '__main__':
    # 输入dict ，key作为columns
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = pd.DataFrame(data)
    frame2 =pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                       index=['one', 'two', 'three', 'four', 'five'])
    frame2['debt'] = np.arange(5.)
    val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])  # 用series给df赋值的时候会精确匹配，不用pd.concat
    frame2['debt'] = val

    # 输入二维ndarry的时候就是行列对应
    data = np.arange(24).reshape(4, 6)
    frame3 = pd.DataFrame(data)  # 输入二维ndarry的时候就是行列对应
    # 行1 array([[0, 1, 2, 3, 4, 5],
    # 行2       [6, 7, 8, 9, 10, 11],
    # 行3       [12, 13, 14, 15, 16, 17],
    # 行4       [18, 19, 20, 21, 22, 23]])


# 一些属性
if __name__ == '__main__':
    obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])  # 输入一维list
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = pd.DataFrame(data)

    obj2.index
    obj2.values
    obj2.name = 'population'  # Series的名字
    obj2.index.name = 'state'  # index的名字

    frame.values
    frame.index
    frame.columns
    frame.index.name
    frame.columns.name


# index类
# 一维index
if __name__ == '__main__':
    obj = pd.Series(range(5), index=['a', 'b', 'c', 'd', 'b'])
    index1 = obj.index
    index1[1:]  # 一维index可以像tuple那么用绝对位置来索引和切片，且不可修改

    index2 = pd.Index([3, 4, 6, 1])  # 还可以直接生成index，不从Series中取出

    # ------------------------------------------1.1一些常用函数----------------------------------------------------------
    index1.append(index2)  # 两个index连起来，组成一个新的index
    index1.difference(index2)  # 差集
    index1.intersection(index2)  # 交集
    index1.union(index2)  # 并集
    index1.equals(index2)  # 是否相等
    index1.isin(index2)  # 典型的isin函数，index的各个指是否包含在参数中。
    index1.delete(0)  # 删去绝对位置为0的index，返回副本
    index1.insert(0, '8')  # 在绝对位置插入目标，返回副本
    index1.is_monotonic_increasing  # index是否单调递增
    index1.is_monotonic_decreasing
    index1.is_unique  # index是否唯一
    index1.unique()  # 返回唯一的数组

    # ------------------------------------------1.2其他方法--------------------------------------------------------------
    # key就是需要具体某个index的值，axis就是横向或者纵向，loc就是绝对位置
    index1.tolist()  # 变成list
    index1.value_counts()  # 对index不同值进行技术。
    index1.get_loc('b')  # 输入值输出loc（绝对位置）

    index2.idxmin()  # index里面最小的那个的loc
    index2.idxmax()  # index里面最小的那个的loc
    index2.idxsort()  # index由小到大排列对应的loc

    index2.astype(dtype=str)  # 转变类型

    index1.delete(0)  # 按照位置删去
    # index1.drop(2) # 不知道什么回事

    index1.dtype  # 返回index的数据类型

    index1.drop_duplicates()  # 去重
    index1.duplicated()  # 返回一个ndarray，告诉那个是重复的，重复的是True
    index1.get_duplicates()  # 返回重复的那些

    index1.factorize()  # 也不知道是干嘛的

    index1.fillna(0)  # 就是fillna

    index1.flags  # 一些事件标志，不知道是干嘛的

    index1.format()  # 将index变成str输出

    index1.get_indexer()  # 不知道是干嘛的

    index1.get_slice_bound()  # 不知道是干嘛的

    index2.get_value(obj, 1)  # 不清楚
    index1.get_values()  # 就是把值取出来


# 二维index
if __name__ == '__main__':
    import sys
    sys.path.append('D:\\py36 projects\\quant-research')
    from tools.data import fetch  # 这句是可以跑通的，只是pycharm报错而已
    df = fetch.stock_all(fields='不复权',endTime='2005-01-31')

    index3 = df.index  # pandas.indexes.multi.MultiIndex
    df.columns  # columns也是一个index对象

    #### 2.1 二维特殊的方法
    index3.get_loc((dt.datetime(2005, 1, 5), u'000001.SZ'))  # 输入某个index，返回loc
    index3.get_level_values(1)  # 取出第二层级的index


# 重新索引
if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'],
                       fill_value=0, method='ffill')  # 改变存储的顺序，如果不存在则空值，可以ffill等方法

    frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                      columns=['Ohio', 'Texas', 'California'])
    states = ['Texas', 'Utah', 'California']
    frame.reindex(columns=states)  # 可以对columns就行reindex，

    # 或者用ix来reindex，效果一样
    frame.ix[['a', 'b', 'c', 'd'], states]


# 丢弃
if __name__ == '__main__':
    data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
                     columns=['one', 'two', 'three', 'four'])
    data.drop(['Colorado', 'Ohio'])
    data.drop('two', axis=1)  # drop列的时候要axis=1，删去某一轴的元素，axis=1就是一列作为一轴
    del data['Colorado']  # 丢弃行


# series索引
if __name__ == '__main__':
    # ---------------------------------------------1.1一维---------------------------------------------------------------
    obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
    obj['b']  # 可以用标签来索引
    obj[['b', 'a', 'd']]
    obj['b':'c']  # 可以用标签的切片，此时含头含尾

    obj[1]  # 也可以用loc来索引
    obj[2:4]  # 此时含头不含尾

    # ---------------------------------------------1.2二维--------------------------------------------------------------
    import sys
    sys.path.append('D:\\py36 projects\\quant-research')
    from tools.data import fetch  # 这句是可以跑通的，只是pycharm报错而已

    df = fetch.stock_all(fields='不复权', endTime='2005-01-31')
    obj2 = df['OPEN']
    obj2['2005-01-04']
    # 这样不能直接用年或年月
    obj2['2005']
    obj2['000001.SZ']


# dataframe索引
if __name__ == '__main__':
    import sys
    sys.path.append('D:\\py36 projects\\quant-research')
    from tools.data import fetch  # 这句是可以跑通的，只是pycharm报错而已
    # -------------------------------------一维--------------------------------------------------------------------------
    # --------------2.1.1[]索引，不能用来同时索引行列，只能行或者列---------------------------------------------------------
    data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
                     columns=['one', 'two', 'three', 'four'])

    # 标签，列，不能行列同时
    data['two']  # 标签是索引列的
    data[['three', 'one']]  # slice也可以
    data['Colorado']  # 不能索引行，报错
    data['Colorado', 'one']  # 不能行列同时索引

    # loc，行，不能行列同时
    data[:2]  # loc及slice是用来索引行的
    data[2, 3]  # 不能行列同时索引

    # 布尔，行，不能行列同时
    data[[True, True, False, True]]  # 一维的布尔数组是用来行的
    data[[True, True, False, True], [True, True, False, True]]  # 不能行列同时索引

    data[data < 5]  # 二维布尔数组全索引，其他没选定的是Nan


    # --------------2.1.2一维，ix索引，行列都可以，速度最慢，慎用 ----------------------------------------------------------
    # 标签，行列均可
    data.ix['Colorado']  # 可以只索引行，标签
    data.ix['Colorado':, ['two', 'three']]  # 也可以行列同时，行在前，列在后，可以用切片
    data.ix[:, ['two', 'three']]  # 可以只索引列，
    # loc，行列均可
    data.ix[2:]  # 可以只索引行，loc
    data.ix[2, 3]  # 行列均可
    data.ix[:, 2]  # 只索引列
    data.ix[['Colorado', 'Utah'], [3, 0, 1]]  # 前后都可以用loc和标签
    # 布尔，行列均可
    data.ix[data.three > 5, [True, True, False, True]]  # 前后都可以用布尔数组，但是不能带不同的index

    # --------------2.1.3 一维，loc，行列都可以---------------------------------------------------------------------------
    # 标签，行列均可，但是不能loc
    data.loc['Colorado', ['two', 'three']]  # loc只能用标签来索引，不能用loc
    data.loc['Colorado':]  # 只索引行，可以用切片
    data.loc[:, ['two', 'three']]  # 只索引列

    # loc要使用.iloc
    data.iloc[1, 2]  # iloc只能用loc来索引，行列都可以
    data.iloc[2]  # 只索引行
    data.iloc[:, 3]  # 只索引列
    data.iloc[4:8, 3]  # 行列皆可

    # 布尔,loc和iloc都可以用布尔，行列均可
    data.loc[[True, True, False, True]]
    data.iloc[[True, True, False, True]]
    data.loc[[True, True, False, True], [True, True, False, True]]  # 行列均可

    # --------------2.1.4一维，at，取标量--------------------------------------------------------------------------------
    # 标签，只能取标量
    data.at['Ohio', 'two']  # 只能用来那标量，行列标签都要才能索引，只能用标签
    data.at['Ohio']  # 不能只写行标签，
    # loc要用iat
    data.iat[1, 2]  # 只能用来那标量，行列loc都要才能索引，只能用loc

    # 一维，xs，速度最快，功能单一
    # 标签，只索引行或者列，不能行列都索引
    data.xs('Ohio')  # 可以所以行，不能用loc，不能用切片
    data.xs('one', axis=1)  # 也可以索引列，但是要axis=1
    data.xs('Ohio', 'one', axis=0)  # 不能都索引
    # loc，不能用loc，需要icol和irow，尽量少用，用iloc
    data.icol(1)
    data.irow(1)


    # ----------------------------2.2二维，只关心标签，不管loc，loc见一维--------------------------------------------------
    # --------------2.2.1二维Series ------------------------------------------------------------------------------------
    data = pd.Series(np.random.randn(10),
                  index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                         [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
    data['b']
    data['b':'c']

    df = fetch.stock_all(fields='不复权', endTime='2005-01-31')

    # --------------二维，[]，同上，标签是列，loc是行，布尔是行-------------------------------------------------------------
    # 二维的[]索引行只能用切片，可以只有一个level，而且可以用日期的切片
    df[parse('2005-01-04'):]
    df['2005-01-04':]
    # 但是不能只用年月或者年
    df['2005-01':]

    # --------------2.2.2二维，ix----------------------------------------------------------------------------------------
    df.ix['2005-01-04']  # 可以只索引level0，datetime可以用'2005-01-04'代替
    df.ix['2005']  # ix不能只用年
    df.ix['2005-01-04', ['OPEN', 'HIGH']]  # 可以只用level=0的标签，datetime可以用'2005-01-04'代替
    df.ix[('2005-01-04', '000001.SZ'), ['OPEN', 'HIGH']]  # 可以行列同时索引，level0和level1同时输入，不能用切片，datetime可以用'2005-01-04'代替
    # 索引不能只索引level1，这个也不行df.ix[(slice(None),'000001.SZ'),slice(None)]

    # --------------2.2.3二维loc，对于标签来说，用法和ix基本一直，但是可以只索引level1---------------------------------------
    df.loc['2005-01-04']  # 可以只索引level0
    df.loc['2005-01']  # loc可以只用年月
    df.loc['2005-01-04', ['OPEN', 'HIGH']]
    df.loc['2005-01', ['OPEN', 'HIGH']]  # 两个并用都可以只有年月
    df.loc[['2005-01-04', '000001.SZ'], ['OPEN', 'HIGH']]
    df.loc[('2005-01-04', '000001.SZ'), ['OPEN', 'HIGH']]

    df.loc[(slice(None), '000001.SZ'), slice(None)]  # 可以通过这个方法来只索引level1，下面两个都不行
    # df.loc[[:,u'000001.SZ'],['OPEN','HIGH']] # 也不能只索引level1，报错
    df.loc['000001.SZ']  # 也不能只索引level1

    # --------------2.2.4二维at，at不能只索引level0或level1，只能同时索引取出标量-------------------------------------------
    df.at['2005-01-04', 'OPEN']

    # --------------2.2.5二维xs，但是只能整行整列取------------------------------------------------------------------------
    df.xs('2005-01-04')  # 可以只索引level0
    df.xs('2005-01')  # 不能只用年月
    df.xs(u'000001.SZ', level=1)  # 可以只索引level1
    df.xs(('2005-01-04', u'000001.SZ'))  # 当然也可以level0和level一起

    # ----------------------------3、重复的索引，两个都拿出来--------------------------------------------------------------
    df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
    df.ix['b']  # 两个都拿出来，返回一个Series，单个的话则是返回标量

    #----------------------------4、整数索引的问题，容易和loc混淆---------------------------------------------------------
    # 对于非rangeIndex，标签是标签，loc是loc
    obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
    obj['b']  # 可以用标签来索引
    obj[['b', 'a', 'd']]
    obj['b':'c']  # 可以用标签的切片，此时含头含尾

    obj[-1]  # 也可以用loc来索引
    obj[2:4]  # 此时含头不含尾
    # 对于rangeIndex来说，输入数字就是标签，不调用loc
    ser = pd.Series(np.arange(3.))
    ser[-1]
    # 只有iloc等才使用调用loc

    # ----------------------------5、反索引，逆向索引，返回index----------------------------------------------------------
    obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
    obj[obj == 1.0].index[0]  # 取index
    obj.index.get_loc(obj[obj == 1.0].index[0])  # 取loc


# 数据透视表
if __name__ == '__main__':
    tips = pd.read_csv('D:\\py36 projects\\Tutorial\\b_数据分析相关\\tips.csv',engine='python')
    tips['tip_pct'] = tips['tip'] / tips['total_bill']
    # Pivot tables就像excel的数据透视表那样，所做的操作的就是按照index进行分类聚合，默认的聚合方法是求平均，
    # 具体就是如果是想知道Female和Male分别总共花了多少钱，那么聚合列就是total_bill，分组key就是sex
    # 同样，如果想知道女性吸烟者（两个标准），那么分组key就是sex和smoker。
    # 行和列其实在统计上来说是没有区别的，只是显示上有区别而已。
    tips.pivot_table(index=['sex', 'smoker'])
    # 本来是
    #      total_bill   tip     sex smoker   day    time  size   tip_pct
    # 0         16.99  1.01  Female     No   Sun  Dinner     2  0.059447
    # 1         10.34  1.66    Male     No   Sun  Dinner     3  0.160542
    # 2         21.01  3.50    Male     No   Sun  Dinner     3  0.166587
    # 3         23.68  3.31    Male     No   Sun  Dinner     2  0.139780
    # 4         24.59  3.61  Female     No   Sun  Dinner     4  0.146808
    # 5         25.29  4.71    Male     No   Sun  Dinner     4  0.186240

    # Pivot tables的结果是，分组key['sex', 'smoker']移入index，如果组合聚合
    #                    size       tip   tip_pct  total_bill
    # sex    smoker
    # Female No      2.592593  2.773519  0.156921   18.105185
    #        Yes     2.242424  2.931515  0.182150   17.977879
    # Male   No      2.711340  3.113402  0.160669   19.791237
    #        Yes     2.500000  3.051167  0.152771   22.284500

    # ['tip_pct', 'size']是需要聚合的列，
    tips.pivot_table(['tip_pct', 'size'], index=['sex', 'day'],
                     columns='smoker')
    #               tip_pct                size
    # smoker             No       Yes        No       Yes
    # sex    day
    # Female Fri   0.165296  0.209129  2.500000  2.000000
    #        Sat   0.147993  0.163817  2.307692  2.200000
    #        Sun   0.165710  0.237075  3.071429  2.500000
    #        Thur  0.155971  0.163073  2.480000  2.428571
    # Male   Fri   0.138005  0.144730  2.000000  2.125000
    #        Sat   0.162132  0.139067  2.656250  2.629630
    #        Sun   0.158291  0.173964  2.883721  2.600000
    #        Thur  0.165706  0.164417  2.500000  2.300000


# stack()和unstack()
if __name__ == '__main__':
    # 一个index和columns都是一层的df变成一个两层index的Series
    data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                     index=pd.Index(['Ohio', 'Colorado'], name='state'),
                     columns=pd.Index(['one', 'two', 'three'], name='number'))
    result = data.stack()
    # 相反操作
    result.unstack()
    result.unstack(0)  # 一般情况下是内层被移走，指定level可以让外层index被移走。
    result.unstack('state')  # 一般情况下是内层被移走，指定level可以让外层index被移走。指定名字也可以

    # unstack会引入缺失数据，stack会忽略缺失数据，dropna=False可以强制不忽略。
    s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
    data2 = pd.concat([s1, s2], keys=['one', 'two'])
    data2.unstack()
    data2.unstack().stack(dropna=False)  #
