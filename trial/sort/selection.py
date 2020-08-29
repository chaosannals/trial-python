def selection_sort(source):
    '''
    选择排序
    【不稳定排序】
    平均时间复杂度：O(n^2)
    '''
    target = source[:]
    count = len(target)
    for i in range(0, count - 1):
        minIndex = i
        for j in range(i + 1, count):
            minIndex = minIndex if target[minIndex] < target[j] else j
        tmp = target[i]
        target[i] = target[minIndex]
        target[minIndex] = tmp
    return target

