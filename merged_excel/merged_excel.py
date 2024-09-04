import pandas as pd

# Excel 文件路径
file1 = 'user001.xls'  # 第一个 Excel 文件路径
file2 = 'user002.xls'  # 第二个 Excel 文件路径
file3 = 'user003.xls'  # 第三个 Excel 文件路径

# 读取 Excel 文件
df1 = pd.read_excel(file1)  # 读取第一个文件
df2 = pd.read_excel(file2)  # 读取第二个文件
df3 = pd.read_excel(file3)  # 读取第三个文件

# 合并 DataFrame
merged_df = pd.concat([df1, df2, df3], ignore_index=True)  # 按行合并，并重置索引

# 保存合并后的数据到一个新的 Excel 文件
merged_df.to_excel('allUser.xls', index=False)  # 保存合并后的文件，不保存行索引

print("Excel 文件合并完成！")
