# coding=utf-8

MT_16_last = pd.pivot_table(
    MT_16,
    index=["省份"],
    columns=['订单状态'],
    values=['订单编号'],
    aggfunc=[len],
    margins=True)
