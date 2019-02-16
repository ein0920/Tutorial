

# 处理路径名，os.path
if __name__ == '__main__':
    import os
    path = 'f_文件与IO/somefile.txt'
    os.path.basename(path)
    os.path.dirname(path)
    os.path.join('tmp', 'data', os.path.basename(path))

    path = '~/somefile.txt'
    os.path.expanduser(path)  # 变成用户目录下的文件路径
    os.path.split(path)


# 检测文件是否存在
if __name__ == '__main__':
    import os
    os.path.exists('f_文件与IO/somefile.txt')
    os.path.exists('somefile.txt')

    os.path.isfile('f_文件与IO/somefile.txt')
    os.path.isdir('f_文件与IO/')
    os.path.isdir('f_文件与IO')

    # 文件的元数据
    os.path.getsize('f_文件与IO/somefile.txt')
    os.path.getmtime('f_文件与IO/somefile.txt')
    import time
    time.ctime(os.path.getmtime('f_文件与IO/somefile.txt'))


# 返回文件夹中所有的文件名的list
if __name__ == '__main__':
    import os
    files = os.listdir(r'C:\py36 projects\Tutorial')  # 列出文件夹内的所有文件的文件名

    # 拿到目录下所有的文件
    names = [name for name in os.listdir('C:\py36 projects\Tutorial')
             if os.path.isfile(os.path.join('C:\py36 projects\Tutorial', name))]

    # 拿到目录下所有文件夹
    dirnames = [name for name in os.listdir('C:\py36 projects\Tutorial')
                if os.path.isdir(os.path.join('C:\py36 projects\Tutorial', name))]

    # 可以用endswith等来匹配
    pyfiles = [name for name in os.listdir('C:\py36 projects\Tutorial')
               if name.endswith('.py')]

    # 文件名匹配
    import glob
    pyfiles = glob.glob('C:\py36 projects\Tutorial\*.py')

    from fnmatch import fnmatch
    pyfiles = [name for name in os.listdir('C:\py36 projects\Tutorial')
               if fnmatch(name, '*.py')]

    # 还可以得到文件相关的元数据
    import os
    import os.path
    import glob

    name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]


# os.walk
if __name__ == '__main__':
    '''
    top -- 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
    root 所指的是当前正在遍历的这个文件夹的本身的地址
    dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    topdown --可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)。
                如果 topdown 参数为 True，walk 会遍历top文件夹，与top 文件夹中每一个子目录。
    onerror -- 可选，需要一个 callable 对象，当 walk 需要异常时，会调用。
    followlinks -- 可选，如果为 True，则会遍历目录下的快捷方式(linux 下是软连接 symbolic link )实际所指的目录(默认关闭)，
                        如果为 False，则优先遍历 top 的子目录。
    '''
    import os
    walkrst = os.walk('C:\py36 projects\Tutorial')
    for root, dirs, files in walkrst:
        print(root, dirs, files)

    next(walkrst)