
# 序列化python对象，将json那样将对象保存在硬盘中
if __name__ == '__main__':
    import pickle
    data = [1,2,3,4,5]
    f = open('f_文件与IO/python_data', 'wb')
    pickle.dump(data, f)

    s = pickle.dumps(data)  # 将对象转变成字符串

    f.close()

    # 恢复文件
    f = open('f_文件与IO/python_data', 'rb')
    data1 = pickle.load(f)

    data2 = pickle.loads(s)

    # --------
    import pickle
    f = open('f_文件与IO/python_data1', 'wb')
    pickle.dump([1,2,3,4], f)
    pickle.dump('hello', f)
    pickle.dump({'Apple', 'Pear', 'Banana'}, f)
    f.close()

    f = open('f_文件与IO/python_data1', 'rb')
    pickle.load(f)


# 可以将一个执行中的类实例序列话
if __name__ == '__main__':
    from f_文件与IO import countdown
    c = countdown.Countdown(30)

    f = open('f_文件与IO/cstate.p', 'wb')
    import pickle
    pickle.dump(c, f)
    f.close()

    # 关闭后打开
    import pickle
    f = open('f_文件与IO/cstate.p', 'rb')
    pickle.load(f)


'''
长期储存最好使用json、XML等标准化格式
'''