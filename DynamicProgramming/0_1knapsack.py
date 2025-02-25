
def knapsack(capacity, weights): 
    '''
    expects knapsack's capacity and a weights dict 
    mapping item value to weight;
    returns dict that maps item value to {0,1} (0 is exclude, 1 is include)
    '''
    values = list(weights.keys()) #array of item values (not necessarily ordered)
    m = len(weights) #number of items
    table = [[0]*(capacity+1) for _ in range(m+1)] #matrix of maximum values for a range of knapsack items and capacities
    for row in range(1, len(table)):
        value = values[row-1]
        weight = weights[value]
        for cap in range(1, capacity+1):
            if not weight <= cap:
                table[row][cap] = table[row-1][cap]
                continue
            if_include = value + table[row-1][cap-weight]
            if_exclude = table[row-1][cap]
            table[row][cap] = max(if_include, if_exclude)
    result = {}

    def build_result(row, cap):
        '''recursively traverses the dynamic programming table'''
        if len(result) == m:
            return
        value = values[row-1]
        if table[row][cap] != table[row-1][cap]:
            result[value] = 1 #include in knapsack
            build_result(row-1, cap-weights[value])
        else:
            result[value] = 0
            build_result(row-1, cap)

    build_result(m, capacity) #m is greatest row index, capacity is greatest column index
    return result
    






