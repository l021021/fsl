import geopandas as gpd
import matplotlib.pyplot as plt

# 替换为您的轨迹点的实际纬度和经度数据
latitude_list = [1,2,3]
longitude_list = [1,2,3]

def plot_trajectory_on_map(latitude_list, longitude_list):
    # 创建一个geopandas的GeoDataFrame
    gdf = gpd.GeoDataFrame({'geometry': gpd.points_from_xy(longitude_list, latitude_list)})

    # 绘制地图
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    ax = world.plot(figsize=(10, 6), color='white', edgecolor='black')

    # 绘制轨迹
    gdf.plot(ax=ax, color='blue', markersize=50)

    plt.show()

if __name__ == "__main__":
    plot_trajectory_on_map(latitude_list, longitude_list)
