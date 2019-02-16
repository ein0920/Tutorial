
# 将文本写入类似于文件的对象上
if __name__ == '__main__':
    import io
    # s相当于一个虚拟的txt文件
    s = io.StringIO()

    s.write('Hello World\n')
    print('This is a test', file=s)

    s.getvalue()

    # 也可以像txt那样的读取
    s = io.StringIO('Hello\nWorld\n')
    s.read(4)  # 读完出来就没有了，相当于pop
    s.read()
    s.read()

    # io.StringIO只能进行文本的处理，二进制要使用io.BytesIO
