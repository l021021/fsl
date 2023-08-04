import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 替换为您的轨迹点的实际纬度和经度数据
latitude_list = [1,2,3]
longitude_list = [1,2,3]

def create_map_with_trajectory_animation(latitude_list, longitude_list):
    # 创建一个geopandas的GeoDataFrame
    gdf = gpd.GeoDataFrame({'geometry': gpd.points_from_xy(longitude_list, latitude_list)})

    # 计算轨迹的边界框（bounding box）
    min_x, min_y, max_x, max_y = gdf.geometry.total_bounds

    # 创建地图
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    fig, ax = plt.subplots(figsize=(10, 6))
    world.plot(ax=ax, color='white', edgecolor='black')

    # 初始化绘制轨迹点的图像对象
    point_plot, = ax.plot([], [], 'bo', markersize=10)

    def update(frame):
        # 在动画中逐步绘制轨迹点
        x = gdf.geometry.x[:frame+1]
        y = gdf.geometry.y[:frame+1]
        point_plot.set_data(x, y)

        # 动态调整地图显示范围以适应轨迹点的位置
        ax.set_xlim(min(x) - 0.1, max(x) + 0.1)
        ax.set_ylim(min(y) - 0.1, max(y) + 0.1)

        return point_plot,

    # 创建动画
    num_frames = len(gdf)
    animation = FuncAnimation(fig, func=update, frames=num_frames, interval=200, blit=True)

    plt.show()

if __name__ == "__main__":
    create_map_with_trajectory_animation(latitude_list, longitude_list)