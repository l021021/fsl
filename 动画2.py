import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

with open('test.json') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# # 读取轨迹数据
# df = pd.read_json('test.json', orient ='records',lines=True,dtype={'longitude': float, 'latitude': float, 'timestamp': 'datetime64[ms]'})
print(df.dtypes)
# #查看df各个列的数据类型

# 创建绘图窗口
fig, ax = plt.subplots()

# # 绘制初始图形
# ax.set_xlim(df['longitude'].min(), df['longitude'].max())
# ax.set_ylim(df['latitude'].min(), df['latitude'].max())
# ax.set_xlabel('Longitude')
# ax.set_ylabel('Latitude')
# line, = ax.plot([], [], 'bo', markersize=3)
# timestamp_text = ax.text(0.02, 0.98, '', transform=ax.transAxes, ha='left', va='top')

# # 定义更新函数
# def update(frame):
#     # 获取当前帧的数据
#     data = df.iloc[frame]

#     # 更新图形
#     line.set_data(data['longitude'], data['latitude'])
#     timestamp_text.set_text(f'Timestamp: {data["timestamp"]}')

# # 创建动画
# ani = FuncAnimation(fig, update, frames=len(df), interval=100)

# # 显示动画
# plt.show()
# 绘制初始图形
ax.set_xlim(df['longitude'].min(), df['longitude'].max())
ax.set_ylim(df['latitude'].min(), df['latitude'].max())
scat = ax.scatter(df['longitude'], df['latitude'])
line, = ax.plot([], [], color='blue')

# 更新函数
def update(frame):
    scat.set_offsets(df[['longitude', 'latitude']].iloc[:frame])
    line.set_data(df['longitude'].iloc[:frame], df['latitude'].iloc[:frame])
    return scat, line,

# 创建动画
ani = FuncAnimation(fig, update, frames=len(df), interval=100, blit=True)

# 显示动画
plt.show()