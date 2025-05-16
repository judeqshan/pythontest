import seaborn as sns
import matplotlib.pyplot as plt

# 加载示例数据集
tips = sns.load_dataset("tips")

# 创建FacetGrid实例
g = sns.FacetGrid(tips, col="time", row="smoker")  # 按"time"和"smoker"字段分面

# 映射到每个子图上的绘图函数
g.map(sns.scatterplot, "total_bill", "tip", "size")  # 在每个子图上绘制散点图

# 设置标题
g.set_titles(row_template='{row_name}', col_template='{col_name}')



# 展示图表
plt.show()