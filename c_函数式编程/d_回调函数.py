
# 这是一个简单回调函数的例子
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    def _onpress(event):
        print('click')

    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event', _onpress)

    '''
    _onpress就是一个回调函数，就是在画布中鼠标点击一下，
    如果捕获到了button_press_event时间，那么久调用_onpress，并且见这个事件的event对象输入给_onpress
    '''