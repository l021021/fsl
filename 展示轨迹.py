import json
import matplotlib.pyplot as plt
import datetime
from matplotlib.font_manager import FontProperties

# 设置中文字体
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
# 从JSON文件加载数据


def load_location_data(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

# 绘制地图上的点和箭头


def plot_location_data(data):
    longitude_values = [item['longitude'] for item in data]
    latitude_values = [item['latitude'] for item in data]
    timestamps = [item['timestamp'] for item in data]

    plt.figure(figsize=(10, 6))
    plt.scatter(longitude_values, latitude_values, s=10, alpha=0.6)
    plt.xlabel('经度', fontproperties=font)
    plt.ylabel('纬度', fontproperties=font)
    plt.title('轨迹', fontproperties=font)

    for i in range(len(data)):
        datetimestr = datetime.datetime.fromtimestamp(
            timestamps[i]).strftime('%H:%M:%S')
        plt.annotate(
            str(i)+"_"+str(datetimestr),
            xy=(longitude_values[i], latitude_values[i]),
            xytext=(longitude_values[i] + 0.00001,
                    latitude_values[i] + 0.00001),  # 标签的偏移位置
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3'),
            fontsize=10,
            alpha=0.8,
        )

    for i in range(len(data) - 1):
        # 绘制箭头，连接相邻的点
        dx = longitude_values[i + 1] - longitude_values[i]
        dy = latitude_values[i + 1] - latitude_values[i]
        plt.arrow(
            longitude_values[i], latitude_values[i],
            dx, dy,
            head_width=0.0000001, head_length=0.00001,
            width=0.000000,
            fc='r', ec='blue', alpha=0.5
        )

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    data = load_location_data('test.json')
    plot_location_data(data)
