import mplleaflet
import matplotlib.pyplot as plt

# 创建一个Matplotlib图形
fig, ax = plt.subplots()

# 绘制一些数据点
x = [116.404, 116.418, 116.432]
y = [39.915, 39.925, 39.935]
ax.scatter(x, y)

# 将百度地图作为背景
mplleaflet.show(fig=fig, tiles='baidu')