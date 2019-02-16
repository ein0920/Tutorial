
# 字符串格式化 %
if __name__ == '__main__':
    pass


# 字符串格式化 .format
if __name__ == '__main__':
    # Format方法和%的格式化字符串是类似的，%对应的是{}。Format输出的还是字符串
    # {}里面输入位置，对应format中的顺序
    '{0},{1}'.format('kzc', 18)  # 'kzc,18'
    '{},{}'.format('kzc', 18)  # 'kzc,18'
    '{1},{0},{1}'.format('kzc', 18)  # 'kzc,18'

    # {}里面放标识，对应format里面的参数
    '{name},{age}'.format(name='kzc', age=18)  # 'kzc,18'

    # 格式限定符，用:开启
    '{num:>8}'.format(num='189')  # 结果：'     189'。解释：^、<、>分别是居中、左对齐、右对齐，后面带宽度。8是长度
    '{:0>8}'.format('189')  # 填充0
    '{:.2f}'.format(321.33545)  # 保留2位，四舍五入
    '{:b}'.format(17)  # 17变成二进制。b、d、o、x分别是二进制、十进制、八进制、十六进制。
    '{:,}'.format(1234567890)  # 变成，分割的数字格式

    # just，对齐
    if __name__ == '__main__':
        text = 'hello world'
        text.ljust(20)
        text.rjust(20, '-')
        text.center(20, '*')

        format(text, '>20')  # 右对齐，挤到右边
        format(text, '^20')
        format(text, '=>20s')  # 右对齐，填充=，作为字符串

        # format可用于其他类型的数据
        x = 1.2345
        format(x, '>10')
        format(x, '^10.2f')


# f字符串
if __name__ == '__main__':
    # python3.6中开始有f-string

    name = "Eric"
    age = 74
    f'Hello, {name}. You are {age}.'

    # 由于f字符串是在运行时进行渲染的，因此可以将任何有效的Python表达式放入其中。
    f"{2 * 37}"
    f"{name.lower()} is funny." # 可以调用函数

    # 多行字符串，多行字符串组要括起来，或者用\来分割
    profession = 'comedian'
    affiliation = 'Monty Python'
    message = (f"Hi {name}. "
               "You are a {profession}. "
               "You were in {affiliation}.")
    another = f"Hi {name}. " \
              f"You are a {profession}. " \
              f"You were in {affiliation}."

    # 可以在表达式中使用各种类型的引号。只要确保在表达式中使用的f-字符串外部没有使用相同类型的引号即可。
    f"{'Eric Idle'}"
    f'{"Eric Idle"}'
    f"""Eric Idle"""
    f"The \"comedian\" is {name}, aged {age}." # 相同类型的引号需要用\

    # 在f-string中使用字典
    comedian = {'name': 'Eric Idle', 'age': 74}
    f"The comedian is {comedian['name']}, aged {comedian['age']}."
    # 这个会报错，如果在字典键周围使用与在f字符串外部使用相同类型的引号，则第一个字典键开头的引号将被解释为字符串的结尾。
    # f'The comedian is {comedian['name']}, aged {comedian['age']}.'

    # 使用大括号
    f"{{74}}"
    f"{{{{74}}}}"


# 字符串的自带方法
if __name__ == '__main__':

    val = 'a,b,  guido'
    a = 'abc'
    b = 'aaabbccddddd'
    strList = ['a', 'b', 'c']
    # 替换，分开
    val.split(',') # 将val用','分割开，返回list
    val.partition(',') # 将val分成三个部分，('a', ',', 'b,  guido')。第一次出现，如果没有找到则返回('a,b,  guido', '', '')
    'df\ted\td'.expandtabs() # 将tab字符换成空格，默认换成8个空格，
    '---'.join(strList) # 将输入list之间用'---'连接，返回str

    # ----------------strip---------------------------------------------------------------------------------------------
    # 空白的去除
    s = ' hello world \n'
    s.strip()
    s.lstrip()
    s.rstrip()

    # 字符去除
    t = '-------hello========'
    t.lstrip('-')
    t.rstrip('=')
    t.strip('-=')

    # 不会去除中间的
    s = ' hello   world   \n'
    s.strip()
    val.strip() # 去掉val中所用指定字符，默认空格
    val.strip('a') # 去掉'a'
    val.rstrip('o') # 删去右边'o'字符，默认空格
    val.lstrip() # 左边的
    val.replace(',','--') # 将','替换成'--'，可以输入开始结束位置

    # 大小写相关---------------------------------------------------------------------------------------------------------
    val.lower() # 同时也是类方法，不是实例化也可以用
    val.upper()
    val.swapcase() # 大写变小写，小写变大写

    'abc,dfg'.title() # 'Abc,Dfg'
    'abc,dfg'.capitalize() # 首字符大写，copy. 'Abc,dfg'

    # 定位相关
    'guido' in val # 'guido'是否在val中，返回TF
    val.index(',') # ','中在val中第一个出现的loc，找不到的话返回异常。可以输入开始结束位置
    val.find(',') # 和index差不多，找不到返回-1
    val.rfind(',') # ','中在val中最后一个出现的loc，找不到的话返回异常。可以输入开始结束位置

    # 填充相关
    a.center(12,'-') # 返回一个长度为12的str，其中a在在中间，其他用'-'来填充
    a.ljust(12) # 同上，a在左边，右边填充
    a.rjust(12) # 同上
    val.zfill(23) #  '000000000000a,b,  guido'
    b.count('aa',0,5) # 统计b中0:5出现'aa'的次数

    # 判断字符开头和结尾
    a.endswith('c',0,4) # a[0:4]是否以'c'结尾，TF
    a.startswith('c',0,4) # a[0:4]是否以'c'开头，TF

    val.isalnum() # 是否全为数字，is开头的顾名思义


# translate @todo 未弄清楚怎么用的字符串方法
if __name__ == '__main__':
    s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'
    print(s)

    # (a) Remapping whitespace
    remap = {
        ord('\t'): ' ',
        ord('\f'): ' ',
        ord('\r'): None  # Deleted
    }

    a = s.translate(remap)


# format_map方法
if __name__ == '__main__':
    name = 'Guido'
    n = 37

    s = '{name} has {n} messages.'
    print(s.format_map(vars()))
    vars()  # object类的所有属性，也就是当前程序所有变量

    # format_map接受一个dict作为输入，应该右s的插入变量名的字符串形式作为key的dict
    s.format_map({'name':'Guido', 'n':89})

    # 在处理缺失问题上，可以修改dict，做一个__missing__方法
    class safesub(dict):  # 如果缺失的时候，则调用这个魔术方法
        def __missing__(self, key):
            return '{%s}' % key

