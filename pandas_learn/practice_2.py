import pandas as pd

# 设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.width', 1000)
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 读取csv文件
path1 = "exercise_data/Euro2012_stats.csv"
data = pd.read_csv(path1)
# 打印Goals这一列
print(data.Goals)
# 打印行数
print(data.shape[0])
# 打印info
print(data.info())
# 打印整个表格
print(data.info)
# 选中表格中的三列组成新的表格
discipline = data[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)
# 主红牌次黄牌排序
print(discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False))
# 黄牌平均值
print(round(discipline['Yellow Cards'].mean()))
# 获得奖牌超过6个的队伍信息
print(data[data['Goals'] > 6])
print(data[data['Team'].str.startswith('G')])
print(data.iloc[:, 0:5])
print(data.iloc[:, :-3])
print(data.head(7))
print(data.loc[data['Team'].isin(['England', 'Italy', 'Russia']), ['Team', 'Goals']])
