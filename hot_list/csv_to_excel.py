import pandas as pd


def pandas_head():
    # 输入path和输出path
    input_path = "origin.csv"
    output_path = "result.xlsx"
    # 读取csv文件并根据"count"列按照数值大小递减排序
    data = pd.read_csv(input_path).sort_values(by="total", ignore_index=True, ascending=False)
    # 新增"percent"列，计算百分比
    data['percent'] = data['total'] / data['total'].sum(axis=0)
    data['percent'] = data['percent'].apply(lambda x: format(x, '.2%'))
    # 新增"cum_percent"列，计算累计百分比
    data['cum_percent'] = data['total'].cumsum() / data['total'].sum(axis=0)
    data['cum_percent'] = data['cum_percent'].apply(lambda x: format(x, '.2%'))
    print(data.head(40))
    # 保存到excel
    data.to_excel(output_path, index=False)


pandas_head()
