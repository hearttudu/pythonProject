import pandas as pd

# 设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.width', 1000)
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 读取csv文件
path1 = "exercise_data/drinks.csv"
data = pd.read_csv(path1)
print(data.head())
# 每个大陆的啤酒消费平均数
print(data.groupby('continent')['beer_servings'].mean())
# 所有国家平均啤酒消费数
print(round(data['beer_servings'].mean()))
# 每个大陆的啤酒消费的描述性统计值
print(data.fillna({'continent': 'NA'}).groupby('continent')['beer_servings'].describe())
# 每个大陆各种饮料消费平均值
print(data.fillna({'continent': 'NA'}).groupby('continent').mean(numeric_only=True))
# 每个大陆各种饮料消费中位数
print(data.fillna({'continent': 'NA'}).groupby('continent').median(numeric_only=True))
# 每个大陆spirit饮品消耗的平均值，最大值和最小值
print(data.fillna({'continent': 'NA'}).groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max']))
