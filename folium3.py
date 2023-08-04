import folium
import matplotlib.pyplot as plt

# 创建一个Matplotlib图形
fig, ax = plt.subplots()

# 绘制一些数据点
x = [116.404, 116.418, 116.432]
y = [39.915, 39.925, 39.935]
ax.scatter(x, y)

# 创建一个folium地图对象
m = folium.Map(location=[39.915, 116.404], zoom_start=1, tiles='OpenStreetMap')

# 将folium地图转换为Matplotlib图形
fig = folium.Figure()
fig.add_child(m)
plt.axis('off')
plt.tight_layout()
plt.show()