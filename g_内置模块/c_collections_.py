
# Counter
if __name__ == '__main__':
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]

    from collections import Counter

    # Counter的作用的计算每个序列的元素的出现次数，相当于词频统计
    word_counts = Counter(words)  # 返回Counter对象
    dir(word_counts)
    top_three = word_counts.most_common(3)  # 返回一个list

    # 加入更多的词
    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    word_counts.update(morewords)
    print(word_counts.most_common(3))

    dir(word_counts)
    # 其他很多都是dict的方法
    word_counts.values()  # 返回词频values
    word_counts.keys()  # 返回keys

# Chainmap
if __name__ == '__main__':
    # ChainMap是将多个dict组合在一起的一个对象，保存了相应dict的链接，修改是直接修改对应的dict
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}

    from collections import ChainMap

    c = ChainMap(a, b)
    print(c['x'])  # Outputs 1  (from a)
    print(c['y'])  # Outputs 2  (from b)
    print(c['z'])  # Outputs 3  (from a)  返回在前面的value

    # 一些dict的方法可以用
    print('len(c):', len(c))
    print('c.keys():', list(c.keys()))
    print('c.values():', list(c.values()))

    # 修改ChainMap的值，就是修改底层的值，c只是一个连接
    c['z'] = 10
    c['w'] = 40
    del c['x']
    print("a:", a)

    # 可以在啊ChainMap中添加新的child
    values = ChainMap()
    values['x'] = 1

    # Add a new mapping
    values = values.new_child()
    values['x'] = 2

    # Add a new mapping
    values = values.new_child()
    values['x'] = 3

    print(values)
    print(values['x'])

    # 丢弃child
    values = values.parents
    print(values)
    print(values['x'])

    # Discard last mapping
    values = values.parents
    print(values)
    print(values['x'])

