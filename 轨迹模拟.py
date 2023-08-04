import matplotlib.pyplot as plt
import random

# 定义四边形区域的边界坐标
bounds = [(39.9, 116.3), (39.9, 116.5), (39.7, 116.5), (39.7, 116.3)]

# 定义起始点
start_point = (random.uniform(bounds[0][0], bounds[1][0]), random.uniform(bounds[0][1], bounds[3][1]))

# 创建点列表
points = [start_point]

# 生成随机偏移的点
for i in range(1, 100):
    # 计算偏移量
    offset = (random.uniform(-0.01, 0.01), random.uniform(-0.01, 0.01))
    
    # 计算新的点
    new_point = (points[-1][0] + offset[0], points[-1][1] + offset[1])
    
    # 添加新的点到列表中
    points.append(new_point)

# 绘制点
x = [p[0] for p in points]
y = [p[1] for p in points]
plt.plot(x, y, 'ro')

# 绘制箭头
for i in range(len(points) - 1):
    plt.arrow(points[i][0], points[i][1], points[i+1][0] - points[i][0], points[i+1][1] - points[i][1], head_width=0.001, head_length=0.002, length_includes_head=True)

# 显示图形
plt.show()