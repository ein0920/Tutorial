

# listbox
if __name__ == '__main__1':
    # 教程 http://www.runoob.com/python/python-gui-tkinter.html
    import tkinter as tk  # 导入 Tkinter 库

    root = tk.Tk()  # 创建窗口对象，相当于生成一个窗口用以承载各种组件

    # 创建两个列表
    li = ['C', 'python', 'php', 'html', 'SQL', 'java']
    movie = ['CSS', 'jQuery', 'Bootstrap']

    # 创建两个列表组件，并且放到root中
    listb = tk.Listbox(root)
    listb2 = tk.Listbox(root)
    listb3 = tk.Listbox(root)
    # 第一个小部件插入数据
    for item in li:
        listb.insert(0, item)
        listb3.insert(0, item)

    for item in movie:  # 第二个小部件插入数据
        listb2.insert(0, item)

    # 将小部件放置到主窗口中，不同组件堆起来
    listb.pack()
    listb2.pack()
    listb3.pack()

    # 进入消息循环
    root.mainloop()


if __name__ == '__main__':
    pass

# 编写菜单
if __name__ =='__main__2':
    from tkinter import *

    top = Tk()
    top.wm_title("菜单")
    top.geometry("400x300+300+100")

    # 创建一个菜单项，类似于导航栏
    menubar = Menu(top)

    # 创建菜单项
    fmenu1 = Menu(top)
    for item in ['新建', '打开', '保存', '另存为']:
        # 如果该菜单时顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单项。
        fmenu1.add_command(label=item)

    fmenu2 = Menu(top)
    for item in ['复制', '粘贴', '剪切']:
        fmenu2.add_command(label=item)

    fmenu3 = Menu(top)
    for item in ['默认视图', '新式视图']:
        fmenu3.add_command(label=item)

    fmenu4 = Menu(top)
    for item in ["版权信息", "其他说明"]:
        fmenu4.add_command(label=item)

    # add_cascade 的一个很重要的属性就是 menu 属性，它指明了要把那个菜单级联到该菜单项上，
    # 当然，还必不可少的就是 label 属性，用于指定该菜单项的名称
    menubar.add_cascade(label="文件", menu=fmenu1)
    menubar.add_cascade(label="编辑", menu=fmenu2)
    menubar.add_cascade(label="视图", menu=fmenu3)
    menubar.add_cascade(label="关于", menu=fmenu4)

    # 最后可以用窗口的 menu 属性指定我们使用哪一个作为它的顶层菜单
    top['menu'] = menubar
    top.mainloop()
