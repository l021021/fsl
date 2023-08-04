#读取data目录下的所有json文件,把里面的轨迹用不同的颜色画出来
import os
import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 读取JSON文件并创建DataFrame对象的函数
def read_json_file(filename):
    with open(filename) as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    return df

# 读取目录中的所有JSON文件
dfs = []
colors = []
for filename in os.listdir('data'):
    if filename.endswith('.json'):
        df = read_json_file(os.path.join('data', filename))
        dfs.append(df)
        colors.append(hash(filename) % 16777216)  # 生成唯一的颜色

# #打印dfs的第10到20个记录的经纬度
# print(dfs[0].loc[10:20,['longitude','latitude']])


# 创建绘图窗口

fig, ax = plt.subplots()

# 绘制初始图形
xmin = min(df['longitude'].min() for df in dfs)
xmax = max(df['longitude'].max() for df in dfs)
ymin = min(df['latitude'].min() for df in dfs)
ymax = max(df['latitude'].max() for df in dfs)
Nmax=   max(len(df) for df in dfs)
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
scats = []
lines=[]
for i, color in enumerate(colors):
    scat = ax.scatter([], [], color='#%06x' % color)
    scats.append(scat)
    line, = ax.plot([], [], color='#%06x' % color)
    lines.append(line)

# 更新函数
def update(frame):
    # print(frame)
    for i, scat in enumerate(scats):
        # start = i * len(dfs[0]) // len(scats)
        # end = (i + 1) * len(dfs[0]) // len(scats)
        data = (dfs[i].loc[frame,'longitude'], dfs[i].loc[frame,'latitude'])
        scat.set_offsets(data)
        #读取lines的值
        # print(lines[i].get_xdata()) 
        # print(frame,i,dfs[i].loc[frame,'longitude'])
        # xdata = list(lines[i].get_xdata())
        xdata=(dfs[i].loc[0:frame, 'longitude'])
        # ydata = list(lines[i].get_ydata())
        ydata=(dfs[i].loc[0:frame, 'latitude'])   
            # xdata = list(lines[i].get_xdata()).append(dfs[i].loc[frame,'longitude'])
        # ydata = list(lines[i].get_ydata()).append(dfs[i].loc[frame,'latitude'])
        # ydata = list(lines[i].get_ydata(),dfs[i].loc[frame,'latitude'])
        lines[i].set_data(xdata, ydata)
        # lines.set_data(dfs[i].loc[1:frame+1,'longitude'], dfs[i].loc[1:frame+1,'latitude'])
    #打赢lines的值
    # print(lines) 
    # return lines[0][0],lines[1][0],scats[0],scats[1]
    return tuple(lines + scats)

 # wrap lines and scats in a list

# 创建动画
ani = FuncAnimation(fig, update, frames=Nmax, interval=80, blit= False)

# 显示动画
plt.show()