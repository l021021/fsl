import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mplleaflet

# 替换为您的轨迹点的实际纬度和经度数据
latitude_list = [1,2,3,4]
longitude_list = [1,2,3,6]

def plot_trajectory_on_map(latitude_list, longitude_list):
    # 创建一个geopandas的GeoDataFrame
    gdf = gpd.GeoDataFrame({'geometry': gpd.points_from_xy(longitude_list, latitude_list)})

    # 计算轨迹的边界框（bounding box）
    min_x, min_y, max_x, max_y = gdf.geometry.total_bounds

    # 创建地图
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    ax = world.plot(figsize=(10, 6), color='white', edgecolor='black')

    # 初始化绘制轨迹点的图像对象
    point_plot, = ax.plot([], [], 'bo', markersize=10)

    def update(frame):
        # 在动画中逐步绘制轨迹点
        x = gdf.geometry.x[:frame+1]
        y = gdf.geometry.y[:frame+1]
        point_plot.set_data(x, y)

        # 动态调整地图显示范围以适应轨迹点的位置
        ax.set_xlim(min_x, max_x)
        ax.set_ylim(min_y, max_y)

        return point_plot,

    # 创建动画
    num_frames = len(gdf)
    animation = FuncAnimation(fig=ax.get_figure(), func=update, frames=num_frames, interval=200, blit=True)

    # 使用mplleaflet将matplotlib图形转换为交互式地图并在Jupyter Notebook或浏览器中显示
    mplleaflet.show(fig=ax.get_figure())

if __name__ == "__main__":
    plot_trajectory_on_map(latitude_list, longitude_list)
