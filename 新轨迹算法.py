
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay


def generate_points_in_polygon(polygon_points, time_interval=0.1):
    # 将多边形点转换为NumPy数组以便更方便地进行计算
    polygon_points = np.array(polygon_points)

    # 生成Delaunay三角剖分
    tri = Delaunay(polygon_points)

    # 获取多边形区域的对角线长度
    diag_length = np.linalg.norm(
        np.max(polygon_points, axis=0) - np.min(polygon_points, axis=0))

    # 计算相邻轨迹点之间的最大允许距离
    max_distance = diag_length * 0.1

    # 生成随机点
    random_points = np.random.rand(200, 2)  # 200个随机点，可以根据需要调整数量

    # 保留在多边形区域内的点
    points_in_polygon = []
    for point in random_points:
        if tri.find_simplex(point) >= 0:
            points_in_polygon.append(point)

    # 连接相邻点以形成连续轨迹
    trajectory_points = []
    timestamp = 0.0
    for i in range(len(points_in_polygon)):
        start_point = points_in_polygon[i]
        end_point = points_in_polygon[(i+1) % len(points_in_polygon)]
        vector = end_point - start_point
        distance = np.linalg.norm(vector)
        num_points = int(np.ceil(distance / max_distance))
        if num_points == 0:
            num_points = 1
        step = vector / num_points
        for j in range(num_points + 1):
            point = start_point + j * step
            trajectory_points.append(
                {'position': point, 'timestamp': timestamp})
            timestamp += time_interval

    return trajectory_points


# 示例使用一个复杂的多边形作为多边形区域
polygon_points = [(0, 0), (1, 0.5), (0.5, 1), (0, 0.5), (0.5, 0)]

# 生成轨迹点
trajectory_points = generate_points_in_polygon(polygon_points)

# 绘制多边形区域和轨迹点
plt.plot(polygon_points + [polygon_points[0]], 'bo-')
plt.plot([p['position'][0] for p in trajectory_points], [
         p['position'][1] for p in trajectory_points], 'r-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polygon and Trajectory Points')
plt.axis('equal')
plt.show()
