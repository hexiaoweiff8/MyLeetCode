# 主持人调度

def minmunNumberOfHost(list):
    # 排序列表
    # 如果开始时间相同则按照结束时间从小到大
    # 否则按照开始时间从小到大
    print(list)
    list = sorted(list, key=lambda x: (x[0], x[1]))
    print(list)
    busy_list = []
    # 计算最大并行区间
    max_parallel = 0
    index = 1
    pre_index = 0
    # 计算区间覆盖列表并行最大值
    for i in range(len(list)):
        if pre_index < list[i][0]:
            # 所有值-1并且弹出所有为0的值
            busy_list = [x - 1 for x in busy_list if x - 1 > 0]
            pre_index = list[i][0]

        if index < list[i][1]:
            busy_list.append(list[i][1] - 1)

        if max_parallel < len(busy_list):
            max_parallel = len(busy_list)

    return max_parallel


print("总共需要", minmunNumberOfHost([[1, 2], [2, 3], [1, 3]]), "位")
