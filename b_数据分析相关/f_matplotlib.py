

import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, MultipleLocator, FuncFormatter, FixedFormatter
import numpy as np

# 大的，fig和axes
if __name__ == '__main__':
    # import matplotlib
    # matplotlib.rcParams # 保存默认的参数

    # 1、生成fig
    fig = plt.figure(
        num=1,
        figsize=(9, 8),
        dpi=None,
        facecolor='white',
        edgecolor='white',
        frameon=True,
        clear=False,  # 如果同名，就删去原来的内容
        # FigureClass
    )
    fig.show()

    # 2、生成ax
    ax = fig.add_axes(
        [0.1, 0.1, 0.8, 0.8],   # [left, bottom, width, height] 0-1的小数
        projection='rectilinear', # ['aitoff' | 'hammer' | 'lambert' | 'mollweide' | 'polar' | 'rectilinear'], optional其他坐标系
        # 坐标投射，aitoff地球坐标，hammer另一个地球坐标，lambert圆形的坐标，mollweide地球坐标，polar是极坐标，rectilinear笛卡尔坐标系
        # polar=False,  # If True, equivalent to projection='polar'.
    )


# 边框相关，spines, locator, formatter, tickline, ticklable
if __name__ == '__main__':
    fig, ax = plt.subplots()
    # 准备
    ax.set_xlim(-0.5,100.5)
    ax.set_ylim(-0.5, 100.5)

    # 2.1 spine边线，会影响到ticklines
    ax.spines['top'].set_color('red')
    ax.spines['top'].set_lw(2)
    # ax.spines['top'].set_visible(False)

    # 2.2 Locator:grid和tick的位置，分为major和minor
    xAxis = ax.get_xaxis()

    xMajorLocator = FixedLocator(np.arange(-0.5,100.5,1))
    xAxis.set_major_locator(xMajorLocator)
    xAxis.grid(True, 'major', color='black', linestyle='solid', linewidth=0.5, zorder=1)

    # tick分为ticklable和tickline
    # ticklable是文字标签
    for tickLabel in xAxis.get_ticklabels():
        tickLabel.set_visible(False)

    # ticklines是那些小点点
    for tickline in xAxis.get_ticklines():
        tickline.set_visible(False)

    # 2.3 formattor是ticklable显示的文字的内容，就是一个数字和str对应的函数，或者是一个字符串的list
    # ---------这个是FixedFormatter
    # majorFormatter = FixedFormatter(['09:30','10:30','13:00','14:00','15:00',])
    # XAxis.set_major_formatter(majorFormatter)
    # ---------这个是funcFormatter
    # def _price_formatter_func(num, pos=None):
    #     return '%0.2f' % num
    # xFormatter = FuncFormatter(_price_formatter_func)
    # xAxis.set_major_formatter(xFormatter)

    fig.canvas.draw_idle()


# 4 Shapes and collections
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.path as mpath
    import matplotlib.lines as mlines
    import matplotlib.patches as mpatches
    from matplotlib.collections import PatchCollection


    def label(xy, text):
        y = xy[1] - 0.15  # shift y-value for label so that it's below the artist
        plt.text(xy[0], y, text, ha="center", family='sans-serif', size=14)


    fig, ax = plt.subplots()
    # create 3x3 grid to plot the artists
    grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T

    patches = []

    # add a circle
    # mpatches.Circle?
    circle = mpatches.Circle(
        [0.2, 0.2],
        0.1,
        ec="none"
    )
    patches.append(circle)
    label(grid[0], "Circle")

    # add a rectangle
    rect = mpatches.Rectangle(grid[1] - [0.025, 0.05], 0.05, 0.1, ec="none")
    patches.append(rect)
    label(grid[1], "Rectangle")

    # add a wedge
    wedge = mpatches.Wedge(grid[2], 0.1, 30, 270, ec="none")
    patches.append(wedge)
    label(grid[2], "Wedge")

    # add a Polygon
    polygon = mpatches.RegularPolygon(grid[3], 5, 0.1)
    patches.append(polygon)
    label(grid[3], "Polygon")

    # add an ellipse
    ellipse = mpatches.Ellipse(grid[4], 0.2, 0.1)
    patches.append(ellipse)
    label(grid[4], "Ellipse")

    # add an arrow
    arrow = mpatches.Arrow(grid[5, 0] - 0.05, grid[5, 1] - 0.05, 0.1, 0.1,
                           width=0.1)
    patches.append(arrow)
    label(grid[5], "Arrow")

    # add a path patch
    Path = mpath.Path
    path_data = [
        (Path.MOVETO, [0.018, -0.11]),
        (Path.CURVE4, [-0.031, -0.051]),
        (Path.CURVE4, [-0.115, 0.073]),
        (Path.CURVE4, [-0.03, 0.073]),
        (Path.LINETO, [-0.011, 0.039]),
        (Path.CURVE4, [0.043, 0.121]),
        (Path.CURVE4, [0.075, -0.005]),
        (Path.CURVE4, [0.035, -0.027]),
        (Path.CLOSEPOLY, [0.018, -0.11])]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts + grid[6], codes)
    patch = mpatches.PathPatch(path)
    patches.append(patch)
    label(grid[6], "PathPatch")

    # add a fancy box
    fancybox = mpatches.FancyBboxPatch(
        grid[7] - [0.025, 0.05], 0.05, 0.1,
        boxstyle=mpatches.BoxStyle("Round", pad=0.02))
    patches.append(fancybox)
    label(grid[7], "FancyBboxPatch")

    # add a line
    x, y = np.array([[-0.06, 0.0, 0.1], [0.05, -0.05, 0.05]])
    line = mlines.Line2D(x + grid[8, 0], y + grid[8, 1], lw=5., alpha=0.3)
    label(grid[8], "Line2D")

    colors = np.linspace(0, 1, len(patches))
    collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
    collection.set_array(np.array(colors))
    ax.add_collection(collection)
    ax.add_line(line)

    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()

    plt.show()


# 5 table
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    fig = plt.figure(figsize=(9, 9), facecolor='white')
    ax = fig.add_axes([0.00, 0.00, 1, 1], facecolor='white', zorder=0)

    # -----------------------------生成table----------------------------------------------------------------------------
    # 用celltext来生成，celltext是一个矩阵，里面放text
    # plt.table?
    cell_text = [['●']*51]*51  # float也可以
    table = plt.table(cellText=cell_text,
                      cellLoc='center',
                      # colWidths=[0.0196,]*10,
                      # rowLabels=['1']*4, rowColours=['red']*4, rowLoc='left',
                      # colLabels=['2']*6, colColours=['yellow']*6, colLoc='center',
                      loc='center'  # 表格所在位置
                      )
    fig.show()
    del fig, ax, table

    # 用cellColours来生成
    cell_color = [['yellow']*3,
                  ['red'] * 3,
                  ['green'] * 3,]
    table2 = plt.table(cellColours=cell_color, cellLoc='center',
                      loc='center')


    fig.show()

    # --------------------------------------单个操作单元格---------------------------------------------------------------
    for i in range(51):
        for j in range(51):
            table.get_celld()[i,j].set_height(0.0196)
            table.get_celld()[i, j].set_width(0.0196)
            table.get_celld()[i, j].set_lw(0.2)
    # dir(table.get_celld()[0, 0])
    fig.canvas.draw_idle()

    # --------------------------------------操作表格属性-----------------------------------------------------------------
    table.scale(1.2, 1.2)
    # dir(table)

table.get_celld()[0, 0].get = '2'

table.get_celld()[0, 0].get_text()._text = '1'
