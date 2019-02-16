
# 下面是一个插值的例子
if __name__ == '__main__':
    import sys
    sys.path.append('D:\\py36 projects\\quant-research')
    import talib as ta

    # 数据准备
    from tools.data import fetch
    df = fetch.index_one('000001.SH', endTime='2010-12-31') # 短一点，避免卡
    # 计算DEA指标
    df['DIFF'], df['DEA'], df['MACD'] = ta.MACD(df['CLOSE'])
    df.dropna(axis=0, inplace=True)
    df['MACD'] = df['MACD'] * 2
    from tools.backtest import signal
    # 生成买卖标记
    signal.up_cross(df, fastLine='DIFF', slowLine='DEA') # 多了一列signal
    signal.signal_transform_single(df,signalCol='signal',at_once=False,mode='long',zhisun=-0.05)

    # 插值的语法
    dfNeed = df.reset_index()[['CLOSE', 'poChg']]
    from scipy.interpolate import interp1d

    # 1、先将样本点输入inter1d，得到一个函数，需要输入x轴的序列和y轴序列
    interp_f = interp1d(
        dfNeed.loc[dfNeed['poChg'] != 0.0, 'CLOSE'].index.tolist(),
        dfNeed.loc[dfNeed['poChg'] != 0.0, 'CLOSE'].tolist()
    )

    # 2、生成一列用来保存插值后的结果，首先输入x轴的值，
    dfNeed['interpLinear'] = 0.0
    dfNeed.loc[
    dfNeed.loc[dfNeed['poChg'] != 0.0, 'poChg'].index[0]:(
        dfNeed.loc[dfNeed['poChg'] != 0.0, 'poChg'].index[-1]),
    'interpLinear'
    ] \
        = range(
        dfNeed.loc[dfNeed['poChg'] != 0.0, 'poChg'].index[0],
        (dfNeed.loc[dfNeed['poChg'] != 0.0, 'poChg'].index[-1] + 1)
    )

    # 3、然后用apply(interp_f)将x的值转换成y的值
    dfNeed.loc[dfNeed['interpLinear'] != 0.0, 'interpLinear'] \
        = dfNeed.loc[dfNeed['interpLinear'] != 0.0, 'interpLinear'].apply(interp_f)


# 下面是回归的例子
if __name__ == '__main__':
    import sys
    sys.path.append('D:\\py36 projects\\quant-research')
    from tools.data import fetch # 这句是可以跑通的，只是pycharm报错而已
    df = fetch.stock_all(fields='DATETIME, CODE, OPEN, HIGH, LOW, CLOSE',endTime='2005-01-31')

    # 这个是仅次于用矩阵求逆最快的运算，但是功能比较单一
    from scipy.stats import linregress
    linrst = linregress(df[['OPEN', 'HIGH', 'LOW']],df['CLOSE'],)

    # @todo 总结以下其他回归的用法
    # 下面是statmodels的
    import statsmodels.api as sm
    x = sm.add_constant(df['OPEN'])
    y = df['CLOSE']
    linmodel = sm.OLS(y,x).fit()
    linmodel.summary()

    # 没有截距
    x = df['OPEN']
    y = df['CLOSE']
    linmodel = sm.OLS(y,x).fit()
    linmodel.summary()