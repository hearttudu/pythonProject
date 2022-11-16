import pandas as pd

# 设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.width', 1000)
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 读取csv文件
path1 = "exercise_data/chipotle.csv"
data = pd.read_csv(path1)
# 打印前五条
print(data.head())
# 打印行和列数量
print('行：' + str(data.shape[0]) + '; ' + '列：' + str(data.shape[1]))
# 打印出全部的列名称
print(data.columns)
# 打印数据集的索引
print(data.index)
# 按照quantity求和并且按照item_name分组
c = data[['item_name', 'quantity']].groupby(['item_name'], as_index=False).agg({'quantity': sum})
# 按照quantity从大到小排序
c1 = c.sort_values(['quantity'], ascending=False)
print(c1.head())
# 打印去重后item_name列的数量
print(data['item_name'].nunique())
# quantity求和
print(data['quantity'].sum())
# 将item_price转换为浮点数
dollarizer = lambda x: float(x[1:-1])
data['item_price'] = data['item_price'].apply(dollarizer)
print(data.head())
# 计算收入，保留整数
data['sub_total'] = round(data['item_price'] * data['quantity'])
print(data['sub_total'].sum())
# 订单数量
print(data['order_id'].nunique())
# 计算每单平均价格
c2 = data[['order_id', 'sub_total']].groupby(by=['order_id']
                                             ).agg({'sub_total': 'sum'})['sub_total'].mean()
print(round(c2))
