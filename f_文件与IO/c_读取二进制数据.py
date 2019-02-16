
if __name__ == '__main__':
    with open('f_文件与IO/data.bin', 'rb') as f:  # 读取txt是'rt'模式
        data = f.read()

    with open('f_文件与IO/data.bin', 'wb') as f:
        f.write(b'Hello world')

    # @ todo


# 对固定大小的记录进行迭代
if __name__ == '__main__':
    from functools import partial
    RECORD_SIZE = 32

    with open('f_文件与IO/data.bin', 'rb') as f:
        records = iter(partial(f.read, RECORD_SIZE), b'')
        for r in records:
            print(r)

# 将二级制数据读取到可变缓冲区中
if __name__ == '__main__':
    import os.path
    def read_into_buffer(filename):
        buf = bytearray(os.path.getsize(filename))
        with open(filename, 'rb') as f:
            f.readinto(buf)
        return buf
