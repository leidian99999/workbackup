#定义函数，每个月都要跟后面一个月对比下，本月有消费且下月也有消费，则本月记为1，下月没有消费则为0，本月没有消费则为NaN，由于最后个月没有下月数据，规定全为NaN
def purchase_return(data):
    status = []
    for i in range(17): # 月数-1
        if data[i] == 1:
            if data[i+1] == 1:
                status.append(1)
            if data[i+1] == 0:
                status.append(0)
        else:
            status.append(np.NaN)
    status.append(np.NaN)       
    return pd.Series(status)

# 可用于计算回购率