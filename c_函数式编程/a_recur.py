

# 阶乘
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


# fib，输入n，输出list
if __name__ == '__main__':
    def fib_list(n):
        # 初值
        if n ==1:
            return [1]  # 初值凑成输出的形式
        elif n == 2:
            return [1,1]  # 初值凑成输出的形式
        else:
            #
            rst = fib_list(n-1)  # 前一层递归的结果
            rst.append(rst[-1] + rst[-2])  # 用前一层递归的结果凑成输出的形式
            return rst
    fib_list(10)


# 递归,构造所有可能路径
if __name__ == '__main__':
    def perm(l):  # 构造路径（城市列表）
        if (len(l)) <= 1:  # 只有一个城市，选择这个城市
            return [l]
        r = []  # 空列表
        for i in range(len(l)):  # 对每个城市，构建不包括这个城市的所有可能序列
            s = l[:i] + l[i + 1:]  # 去除当前城市的列表
            p = perm(s)  # 调用自身，构造不包含这个城市的序列
            for x in p:
                r.append(l[i:i + 1] + x)  # 将序列和该城市合并，得到完整的序列
        return r

    city = [1, 2, 3, 4, 5]
    perm(city)


# 要在函数里面使用for
if __name__ == '__main__':
    def flattern(sample):
        if isinstance(sample, list):
            result = []
            for item in sample:
                result += flattern(item)
        else:
            return [sample]

        return result

    inputList = [1, [2, [3, [8888,666], [4, 6, [45, 78, [99]], [45,67,89,[999,[4543,90]]]]], 45]]
    flattern(inputList)

    # 另外一个
    def main(input_list):
        output = []
        for i in range(len(input_list)):
            if isinstance(input_list[i], list):
                new = main(input_list[i])
                output.extend(new)
            else:
                output.append(input_list[i])
        return output


    main(inputList)


'''
递归函数的凑的步骤
1、一定要有初值分支
2、考虑输入和输出的形式，特别是输出的形式，初值要凑成输出的形式，
3、从初值到非初值的那一步，注意使用前一层递归结果的形式
'''

