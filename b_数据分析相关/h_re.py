

# re.match
if __name__ == '__main__':
    '''
    re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
    1、参数描述
    参数	    | 描述
    ————————+———————————————————————————————————————————————————————————————————————————————————————————————————————————
    pattern	| 匹配的正则表达式
    string	| 要匹配的字符串。
    flags	| 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志

    2、flags的描述
    修饰符	| 描述
    ————————+———————————————————————————————————————————————————————————————————————————————————————————————————————————
    re.I	| 使匹配对大小写不敏感
    re.L	| 做本地化识别（locale-aware）匹配
    re.M	| 多行匹配，影响 ^ 和 $
    re.S	| 使 . 匹配包括换行在内的所有字符
    re.U	| 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
    re.X	| 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

    3、方法
    匹配对象方法	    | 描述
    ————————————————+———————————————————————————————————————————————————————————————————————————————————————————————————
    group(num=0)	| 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
    groups()	    | 返回一个包含所有小组字符串的tuple，从 1 到 所含的小组号。
    span()          | 返回开始和结束位置的tuple
    '''

    import re

    #
    a = re.match('www', 'www.runoob.com')
    a.span()
    b = re.match('run', 'www.runoob.com')  # 返回None

    # group方法
    line = "Cats are smarter than dogs"

    matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

    if matchObj:
        print("matchObj.group() : ", matchObj.group())
        print("matchObj.group(1) : ", matchObj.group(1))
        print("matchObj.group(2) : ", matchObj.group(2))
    else:
        print("No match!!")


# re.search
if __name__ == '__main__':
    '''
    re.search 扫描整个字符串并返回第一个成功的匹配。

    1、函数参数说明：
    参数	    | 描述
    ————————+———————————————————————————————————————————————————————————————————————————————————————————————————————————
    pattern	| 匹配的正则表达式
    string	| 要匹配的字符串。
    flags	| 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

    2、
    匹配对象方法	    | 描述
    ————————————————+———————————————————————————————————————————————————————————————————————————————————————————————————
    group(num=0)	| 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
    groups()	    | 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。

    '''

    import re

    # 和match不同之处在于不用在第一个字符开始
    print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
    print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

    # group方法
    line = "Cats are smarter than dogs";

    searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

    if searchObj:
        print("searchObj.group() : ", searchObj.group())
        print("searchObj.group(1) : ", searchObj.group(1))
        print("searchObj.group(2) : ", searchObj.group(2))
    else:
        print("Nothing found!!")


# re.sub
if __name__ == '__main__':
    '''
    re.sub用于替换字符串中的匹配项。

    参数	    | 描述
    ————————+———————————————————————————————————————————————————————————————————————————————————————————————————————————
    pattern | 正则中的模式字符串。
    repl    | 替换的字符串，也可为一个函数。
    string  | 要被查找替换的原始字符串。
    count   | 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
    '''

    import re

    phone = "2004-959-559 # 这是一个国外电话号码"

    # 删除字符串中的 Python注释
    num = re.sub(r'#.*$', "", phone)
    print("电话号码是: ", num)

    # 删除非数字(-)的字符串
    num = re.sub(r'\D', "", phone)
    print("电话号码是 : ", num)

    # repl参数是分组名字-------------------------------------------------------------------------------------------------
    import re

    # Some sample text
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

    # (a) Simple substitution
    print(datepat.sub(r'\3-\1-\2', text))

    # repl 参数是一个函数------------------------------------------------------------------------------------------------
    # 将匹配的数字乘以 2
    def double(matched):
        value = int(matched.group('value'))  # 回调函数的输入上一个匹配对象，需要用.group来调用匹配的字符串
        return str(value * 2)

    s = 'A23G4HFD567'
    print(re.sub('(?P<value>\d+)', double, s))

    # 第二个例子
    # (b) Replacement function
    from calendar import month_abbr

    def change_date(m):
        mon_name = month_abbr[int(m.group(1))]
        return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


    print(datepat.sub(change_date, text))


# re.findall和re.finditer
if __name__ == '__main__':
    '''
    和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

    参数	    | 描述
    ————————+———————————————————————————————————————————————————————————————————————————————————————————————————————————
    pattern	| 匹配的正则表达式
    string	| 要匹配的字符串。
    flags	| 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
    '''
    import re

    m = re.findall('\d+', 'one12twothree34four')

    # re.finditer
    it = re.finditer(r"\d+", "12a32bc43jf3")
    for match in it:
        print(match.group())


# re.match, re.search和re.findall分组的区别
if __name__ == '__main__':
    import re
    text = 'hello blue go go hello'
    rst = re.match(r'\b\w+\b\s+\w+\b', text)
    rst.group()

    all = re.findall(r'\b\w+\b\s+\w+\b', text)  # 已经匹配上的就略过了
    all

    # 有分组的
    s = 'hello blue go go hello'
    rst = re.match(r'\b(\w+)\b\s+(\w+)\b', s)
    rst.group()

    p = re.compile(r'\b(\w+)\b\s+(\w+)\b')
    all = re.findall(p, s)  # findall对应多个分组的处理就是用tuple将多个分组的匹配存起来
    all

    # 后向引用的
    s = 'hello blue go go hello'
    rst = re.match(r'\b(\w+)\b\s+\1\b', s)  # \1不是代替(\w+)，而是说要和前面的(\w+)匹配到一模一样的内容才行，所以重头开始没有匹配
    rst.group()

    rst = re.search(r'\b(\w+)\b\s+\1\b', s)  # 因为\1需要和之前的组匹配到一模一样的，所以匹配到'go go'
    rst.group()

    s = 'hello blue go go hello'
    all = re.findall(r'\b(\w+)\b\s+\1\b', s)  # findall返回的结果是指保存组的结果，\1不作为组返回
    all


# re.split
if __name__ == '__main__':
    '''
    split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：

    参数	    | 描述
    ————————+———————————————————————————————————————————————————————————————————————————————————————————————————————————
    pattern	| 匹配的正则表达式
    string	| 要匹配的字符串。
    maxsplit| 分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
    flags	|标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
    '''

    import re

    line = 'asdf fjdk; afed, fjek,asdf,      foo'

    # (a) Splitting on space, comma, and semicolon
    parts = re.split(r'[;,\s]\s*', line)
    print(parts)

    # (b) Splitting with a capture group
    fields = re.split(r'(;|,|\s)\s*', line)
    print(fields)

    # (c) Rebuilding a string using fields above
    values = fields[::2]
    delimiters = fields[1::2]
    delimiters.append('')
    print('value =', values)
    print('delimiters =', delimiters)
    newline = ''.join(v + d for v, d in zip(values, delimiters))
    print('newline =', newline)

    # (d) Splitting using a non-capture group
    parts = re.split(r'(?:,|;|\s)\s*', line)
    print(parts)


# re.compile
if __name__ == '__main__':
    '''
    compile 函数用于编译正则表达式，生成一个正则表达式(Pattern)对象，供前面的函数使用，match, search, findall, finditer, split

    参数	    | 描述
    ————————+———————————————————————————————————————————————————————————————————————————————————————————————————————————
    pattern | 正则中的模式字符串。
    flags	| 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
    '''

    # -----------------------------match和search------------------------------------------------------------------------
    import re

    # 第一步生成一个pattern对象，然后pattern来match或者search
    pattern = re.compile('\d+')
    m = pattern.match('one12twothree34four')
    m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
    m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
    m.group(0)
    m.start(0)
    m.end(0)
    m.span()

    # -----------------------------findall------------------------------------------------------------------------------
    '''
    参数	    | 描述
    ————————+———————————————————————————————————————————————————————————————————————————————————————————————————————————
    string  | 待匹配的字符串。
    pos     | 可选参数，指定字符串的起始位置，默认为 0。
    endpos  | 可选参数，指定字符串的结束位置，默认为字符串的长度。
    '''
    import re

    pattern = re.compile(r'\d+')  # 查找数字
    result1 = pattern.findall('runoob 123 google 456')
    result2 = pattern.findall('run88oob123google456', 0, 10)


# 正则表达式模式pattern1：单个字符和量词
if __name__ == '__main__':
    # -------------------------------------单个字符----------------------------------------------------------------------
    '''
    实例	        | 描述
    ————————————+———————————————————————————————————————————————————————————————————————————————————————————————————————
    python	    | 匹配 "python".
    ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    字符类
    实例	        | 描述
    ————————————+———————————————————————————————————————————————————————————————————————————————————————————————————————
    [Pp]ython	| 匹配 "Python" 或 "python"
    rub[ye]	    | 匹配 "ruby" 或 "rube"
    [123]       | 匹配 "1" 或 "2" 或 "3"
    [aeiou]	    | 匹配中括号内的任意一个字母
    [0-9]	    | 匹配任何数字。类似于 [0123456789]
    [a-z]	    | 匹配任何小写字母
    [A-Z]	    | 匹配任何大写字母
    [a-zA-Z0-9]	| 匹配任何字母及数字
    [^aeiou]	| 除了aeiou字母以外的所有字符
    [^0-9]	    | 匹配除了数字外的字符
    ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    特殊字符类
    实例	        | 描述
    ————————————+———————————————————————————————————————————————————————————————————————————————————————————————————————
    .	        | 匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
    \d	        | 匹配一个数字字符。等价于 [0-9]。
    \D	        | 匹配一个非数字字符。等价于 [^0-9]。
    \w	        | 匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
    \W	        | 匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。
    \s	        | 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
    \S	        | 匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
    ————————————+———————————————————————————————————————————————————————————————————————————————————————————————————————
    \f	        | 匹配换页符。
    \t	        | 匹配制表符。
    \n	        | 匹配换行符。
    \r	        | 匹配回车符。
    \v	        | 匹配垂直制表符。
    \h	        | 匹配水平空白符。
    '''

    import re

    # 例子1
    text = "foo    bar\t baz  \tqux"  # \t就是tab
    re.split('\s+', text)

    # -----------------------------------------量词---------------------------------------------------------------------

    '''
    表示数量的模式
    模式	        | 描述
    ————————————+———————————————————————————————————————————————————————————————————————————————————————————————————————
    re*	        | 匹配0个或多个的表达式。
    re+         | 匹配1个或多个的表达式。
    re?         | 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
    re{n}       | 精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
    re{n,}      | 匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。
                | "o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
    re{n, m}    | 匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
    '''

    import re

    # 注意pattern的分块
    pattern = '\d{3,4}[.-]?'
    text = '705-251-2302'
    re.findall(pattern, text)

    # 例子2
    text = """Dave dave@google.com
    Steve steve@gmail.com
    Rob rob@gmail.com
    Ryan ryan@yahoo.com
    """
    pattern = '[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

    # 例子3
    pattern = '\d{3}-?\d{3}-?\d{4}'
    text = '705-251-2302'
    re.findall(pattern, text)

    # 例子4，匹配不了
    pattern = '(\d{3,4}[.-]?)+'
    text = '705-251-2302'
    re.match(pattern, text)

    # 例子5可用
    pattern = r'(\d{3}[.-]?){2}\d{4}'
    text = '705-251-2302'
    re.match(pattern, text)

    pattern = '\d{3}'
    text = '123'
    re.findall(pattern, text)


# 定位符^、$、\b，\B
if __name__ == '__main__':

    import re

    # ^匹配一行文本开始处的文本
    lines = ["Hello world.", "hello world.", "ni hao", "Hello Tom"]
    results = []
    for line in lines:
        if re.findall(r"^H", line):  # 找行开头的H
            results.append(line)
    print(results)  # ['Hello world.', 'Hello Tom']

    # $匹配一行文本结束处的文本
    lines = ["Hello world.", "hello world.", "ni hao", "Hello Tom"]
    results = []
    for line in lines:
        if re.findall(r"m$", line):  # 找结尾的m
            results.append(line)
    print(results)  # ['Hello Tom']

    # \b匹配一个单词(不含空格的字符串)边界，即字与空格间的位置
    text = "apple took itake tattle tabled tax yed temperate"
    print(re.findall(r"\bta.*\b", text))  # ta开头的最长子句子 ['tattle tabled tax yed temperate']
    print(re.findall(r"\bta\S*?\b", text))  # ta开头的单词       ['tattle', 'tabled', 'tax']
    print(re.findall(r"\bta\S*?ed\b", text))  # ta开头ed结尾的单词 ['tabled']

    # \B非单词边界的
    text = "phone phoneplus iphone telephone telegram"
    # 从text中找出iphone telephone单词
    words = text.split()
    results = []
    for word in words:
        if re.findall(r"\Bphone", word):
            results.append(word)
    print(results)  # ['iphone', 'telephone']

    # @ todo不知道支持\Q \E否
    text = 'I have a $dsde'
    re.findall('\Q$\E', text)


# 分组、后向引用
if __name__ == '__main__':
    # ---------------------------------------()分组---------------------------------------------------------------------
    import re

    text = 'This is some text -- with punctuation.'
    # word starting with 't' then another word
    regex = re.compile(r'(\bt\w+)\W+(\w+)')  # 这里包括两个组，
    print('Pattern               :', regex.pattern)

    match = regex.search(text)  # 只返回一个匹配，一个匹配里面有两个分组，对应两个括号
    print('Entire match          :', match.group(0))
    print('Word starting with "t":', match.group(1))
    print('Word after "t" word   :', match.group(2))
    match.group(3)

    # 例子2
    s = 'age:13,name:Tom;age:18,name:John'
    p = re.compile(r'age:(\d+),name:(\w+)')
    it = re.finditer(p, s)
    print('【Output】')
    for m in it:
        print('------')
        print(m.group())
        print(m.group(0))
        print(m.group(1))
        print(m.group(2))

    # ------------------------忽略某个分组-------------------------------------------------------------------------------
    s = 'age:13,name:Tom'
    p1 = re.compile(r'age:(\d+),name:(\w+)')
    print('【Output】')
    # 不忽略分组
    print(re.findall(p1, s))

    # 忽略分组：(?:)
    p2 = re.compile(r'age:(?:\d+),name:(\w+)')
    print(re.findall(p2, s))
    rst = p2.match(s)
    rst.group(0)
    rst.group(1)  # 只有这个group，前一个括号被忽略了，可以加快匹配速度

    # ------------------------后向引用-------------------------------------------------------------------------------
    # 所谓后向引用，就是对前面出现过的分组再一次引用，使用默认的分组名称进行后向引用：\1,\2,\3...（注：从1开始）
    # 匹配字符串中连续出现的两个相同的单词
    import re
    text = 'hello blue go go hello'
    rst = re.match(r'\b\w+\b\s+\w+\b', text)
    rst.group()

    all = re.findall(r'\b\w+\b\s+\w+\b', text)  # 已经匹配上的就略过了
    all

    # 有分组的
    s = 'hello blue go go hello'
    rst = re.match(r'\b(\w+)\b\s+(\w+)\b', s)
    rst.group()

    p = re.compile(r'\b(\w+)\b\s+(\w+)\b')
    all = re.findall(p, s)  # findall对应多个分组的处理就是用tuple将多个分组的匹配存起来
    all

    # 后向引用的
    s = 'hello blue go go hello'
    rst = re.match(r'\b(\w+)\b\s+\1\b', s)  # \1不是代替(\w+)，而是说要和前面的(\w+)匹配到一模一样的内容才行，所以重头开始没有匹配
    rst.group()

    rst = re.search(r'\b(\w+)\b\s+\1\b', s)  # 因为\1需要和之前的组匹配到一模一样的，所以匹配到'go go'
    rst.group()

    s = 'hello blue go go hello'
    all = re.findall(r'\b(\w+)\b\s+\1\b', s)  # findall返回的结果是指保存组的结果，\1不作为组返回
    all


    # ------------------------自定义名称分组的后向引用--------------------------------------------------------------------
    # python正则可以对分组自定义名称，然后可以使用自定义名称进行后向引用，
    # 使用自定义分组名称比使用默认分组名称更加清晰、更容易让人理解。
    # 对分组自定义名称的方法：(?P<myname>exp)
    # 后向引用的方式：(?P=myname)
    s = 'hello blue go go hello'
    p = re.compile(r'\b(?P<my_group1>\w+)\b\s+(?P=my_group1)\b')  # (?P<my_group1>\w+)命名的格式
    print('【Output】')
    print(re.findall(p, s))

    # -------------------------嵌套分组----------------------------------------------------------------------------------
    s = '2017-07-10 20:00'
    p = re.compile(r'(((\d{4})-\d{2})-\d{2}) (\d{2}):(\d{2})')
    re.findall(p, s)
    # 输出：
    # [('2017-07-10','2017-07','2017','20','00')]

    se = re.search(p, s)
    print(se.group())
    print(se.group(0))
    print(se.group(1))
    print(se.group(2))
    print(se.group(3))
    print(se.group(4))
    print(se.group(5))
    # 可以看出，分组的序号是以左小括号'('从左到右的顺序为准的。


# 模式flags
if __name__ == '__main__':
    import re
    help(re)

    # DOTALL, S
    # 使"."匹配包括"\n"在内的所有字符（"."默认是不能匹配"\n“的），
    p = r'me.com'
    print(re.findall(p, 'me.com'))
    print(re.findall(p, 'me\ncom'))
    print(re.findall(p, 'me\ncom', re.DOTALL))
    print(re.findall(p, 'me\ncom', re.S))
    # 注：使用re.S模式时，正则表达式不能是编译后的正则（re.compile()函数），否则会出错。
    # 使用re.S模式时，"^"字符变为文档开始符而不再是行开始符，"$"字符变为文档结束符而不再是行结束符。

    # IGNORECASE, I
    # # 使匹配对大小写不敏感，举例：
    p = r'a'
    print(re.findall(p, 'A'))
    print(re.findall(p, 'A', re.IGNORECASE))
    print(re.findall(p, 'A', re.I))

    # LOCALE, L
    # 本地化匹配，使用了该编译标志后，\w,\W,\b,\B,\s,\S等字符的含义就和本地化有关了。

    # MULTILINE, M
    # 开启多行匹配，影响"^"和"$"。举例：
    s = """
aa bb cc
bb aa
aa ccd
    """
    p1 = r'^aa'
    p2 = r'cc$'

    print(re.findall(p1, s))
    print(re.findall(p1, s, re.M))

    print(re.findall(p2, s))
    print(re.findall(p2, s, re.M))

    # VERBOSE, X
    # 开启正则的多行写法，使之更清晰。举例：
    p = r"""
    \d{3,4}
    -?
    \d{7,8}
    """
    tel = '010-12345678'

    print(re.findall(p, tel))
    print(re.findall(p, tel, re.X))

    # UNICODE, U
    # 以unicode编码进行匹配，比如用'\s'匹配中文全角的空格符：\u3000，不加该编译标志和加该编译标志的效果对比如下：
    s = '\u3000'
    p = r'\s'
    print(re.findall(p, s))
    print(re.findall(p, s, re.U))

    # 如何同时使用多个编译标志？
    # 有时候可能同时要用到多种编译标志，比如我既想在匹配的时候忽略大小写，又想让"."匹配换行符号"\n"，前面的方式貌似不行了，那怎么办呢？
    # 方法：在正则的任意位置加上这句即可：(?iLmsux)
    s = 'Abc\ncom'
    p = r'(?is)abc.com'  # 注：编译标志(?is)可以加在正则的任意位置，这里加在了末尾
    print(re.findall(p, s))
    re.findall(p, s, re.I|re.S)  # 这样前面就不用加(?is)


# 元字符
if __name__ == '__main__':
    '''
    元字符：所谓元字符，指的是那些不仅仅可以表示字符本身含义、并且还可以表示其他特殊含义的字符。正则中的元字符主要有如下这些：
    . ^ $ * + ? { } [ ]  | ( )
    要在正则中匹配元字符本身，需要使用转义符号，比如如果要匹配"+"符号，则在正则中要写成："\+".
    '''

    # -------------------[]---------------------------------------------------------------------------------------------
    '''
    (1) 常用来指定一个字符集，如[abc]匹配：a或b或c
    (2) 元字符在"[]"中不起所用，比如：[a+]匹配：a或+
        但注意：在方括号中要匹配转义符“”本身，要用："\\"；要匹配方括号开头的"^"符本身，要用："^"；要匹配"-"字符，需要用："\-"
    (3) 补集匹配：[^a]，匹配非a的一个字符
    (4) 匹配连续字符：[a-zA-Z0-9]，匹配大小写英文字母和数字
    '''

    # -------------------^和$---------------------------------------------------------------------------------------------
    '''
    ^匹配行首，在MULTILINE模式中，直接匹配字符串中的每一个换行。
    $匹配行尾，行尾是指：字符串尾，或一个换行字符后的任何位置。
    '''

    # -------------------*,+,?---------------------------------------------------------------------------------------------
    '''
    *匹配行尾，行尾是指：字符串尾，或一个换行字符后的任何位置。
    +匹配前一个字符或子表达式出现1次或多次。
    ?匹配前一个字符或子表达式出现1次或0次。还可以表示非贪婪匹配
    '''
    # ?还表示非贪婪匹配
    import re

    # 贪婪模式，会尽量多地去匹配
    r1 = re.compile(r'ab+')
    s1 = 'abbb'
    print(re.findall(r1, s1))

    # 非贪婪模式，会尽量少地去匹配
    r2 = re.compile(r'ab+?')
    s2 = 'abbb'
    print(re.findall(r2, s2))


# 字符组
if __name__ == '__main__':
    import re
    # 就是用方括号来匹配，例如[0-9]就是匹配一个0-9之间的数字，[a-fA-F0-9]是匹配一个十六位数字
    # 取反就是[^aeiou]就是脱字符

    # ---------------------------差集和并集------------------------------------------------------------------------------
    # 并集
    r'[0-3[6-9]]'
    # 差集
    r'[a-z&&[^m-r]]'



# 量词————贪心，懒惰和占有
if __name__ == '__main__':
    import re

    # 贪心，首次尝试匹配整个字符串，如果失败则退回一个字符（回溯）再匹配。
    text = 'abcdacsdnd'
    pattern = r'a.*d'
    rst = re.search(pattern, text)
    rst.group()

    # 固定次数{}
    '''
    模式	        | 描述
    ————————————+———————————————————————————————————————————————————————————————————————————————————————————————————————
    {n}	        | 匹配n次。
    {n,}        | 匹配n次或多次。
    {n,m}       | 匹配n次到m次
    '''


    # 懒惰, 从目标的起始位置开始尝试寻找匹配，每次检查一个字符，寻找要匹配的内容，最后尝试整个字符串
    text = 'abcdacsdnd'
    pattern = r'a.*?d'
    re.findall(pattern, text)

    # 占有 @ todo
    text = 'abcdacsdnd'
    pattern = r'a.*+d'
    re.findall(pattern, text)

    '''
    模式	        | 描述
    ————————————+———————————————————————————————————————————————————————————————————————————————————————————————————————
    ??	        | 懒惰匹配零次或一次。
    +?          | 懒惰匹配一次或多次。
    *?          | 懒惰匹配零次或多次
    {n}?        | 懒惰匹配n次。
    {n,}?       | 懒惰匹配n次或多次。
    {n,m}?      | 懒惰匹配n次到m次
    '''




# unicode匹配
if __name__ == '__main__':
    pass


# 各种零宽断言，环视
if __name__ == '__main__':
    # 零宽断言分为四种：正预测先行断言、正回顾后发断言、负预测先行断言、负回顾后发断言，不同的断言匹配的位置不同

    # -----------------------正预测先行断言：(?=exp)---------------------------------------------------------------------
    # 匹配一个位置（但结果不包含此位置）之前的文本内容，这个位置满足正则exp，举例：匹配出字符串s中以ing结尾的单词的前半部分：
    import re
    s = "I'm singing while you're dancing."
    p = re.compile(r'\b\w+(?=ing\b)')
    print(re.findall(p, s))  # 不返回括号内的
    rst = re.search(p, s)  #

    # -----------------------正回顾后发断言：(?<=exp)---------------------------------------------------------------------
    # 匹配一个位置（但结果不包含此位置）之后的文本，这个位置满足正则exp，举例：匹配出字符串s中以do开头的单词的后半部分：
    s = "doing done do todo"
    p = re.compile(r'(?<=\bdo)\w+\b')
    print(re.findall(p, s))

    # -----------------------负预测先行断言：(?!exp) 前向搜索否定模式------------------------------------------------------
    # 匹配一个位置（但结果不包含此位置）之前的文本，此位置不能满足正则exp，举例：匹配出字符串s中不以ing结尾的单词的前半部分：
    s = 'done run going'
    p = re.compile(r'\b\w+(?!ing\b)')
    print(re.findall(p, s)) # 可见，出问题了，这不是我们预期的结果（预期的结果是：done和run），这是因为负向断言不支持匹配不定长的表达式，

    # 将p改一下再匹配：
    s = 'done run going'
    p = re.compile(r'\b\w{2}(?!ing\b)')  # 这个其实也有问题，如下
    print(re.findall(p, s))

    s = 'doning run gone'
    p = re.compile(r'\b\w{2}(?!ing\b)')  # 这个其实也有问题，如果不是5个字符的ing的就匹配不了
    print(re.findall(p, s))


    # 看下面例子
    import re

    address = re.compile(
        '''
        ^

        # An address: username@domain.tld

        # Ignore noreply addresses
        (?!noreply@.*$)
        [\w\d.+-]+       # username
        @
        ([\w\d.]+\.)+    # domain name prefix
        (com|org|edu)    # limit the allowed top-level domains

        $
        ''',
        re.VERBOSE)

    candidates = [
        'first.last@example.com',
        'noreply@example.com',
    ]

    for candidate in candidates:
        print('Candidate:', candidate)
        match = address.search(candidate)
        if match:
            print('  Match:', candidate[match.start():match.end()])
        else:
            print('  No match')

    # -----------------------负回顾后发断言：(?<!exp) 后向搜索否定模式-----------------------------------------------------
    # 匹配一个位置（但结果不包含此位置）之后的文本，这个位置不能满足正则exp，举例：匹配字符串s中不以do开头的单词：
    s = 'done run going'
    p = re.compile(r'(?<!\bdo)\w+\b')
    print(re.findall(p, s))  # 同上，出问题，

    s = 'done run going'
    p = re.compile(r'(?<!\bdo)\w{2}\b')
    print(re.findall(p, s))

    # 看下面例子
    pattern = r'^[\w\d\.+-]+(?<!noreply)@([\w\d.]+\.)+(com|org|edu)$'
    ls = ['first.last@example.com', 'noreply@example.com', 'noreplydar@example.com']

    for txt in ls:
        print('Candidate:', txt)
        match = re.search(pattern, txt)
        if match:
            print(u'    Match:', match.group(0))
        else:
            print(u'    No match')

