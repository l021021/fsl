import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlabel('经度')
    ax.set_ylabel('纬度')
    ax.set_title('定位数据分布')

    scatter = ax.scatter([], [], s=10, alpha=0.6)
    annotation = ax.annotate(
        '', xy=(0, 0), xytext=(0.5, 0.5),
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3'),
        fontsize=8, alpha=0.8,
    )

    def update(frame):
        x = longitude_values[:frame+1]
        y = latitude_values[:frame+1]
        scatter.set_offsets(list(zip(x, y)))
        scatter.marker = '&'
        annotation.set_text(str(timestamps[frame]))
        annotation.set_position = (x, y)

        return scatter, annotation

    ani = animation.FuncAnimation(
        fig, update, frames=len(data), interval=100,
        repeat=False, blit=True
    )

    plt.grid(True)
    plt.show()

    # ani.save('sin_test2.gif', writer='imagemagick', fps=10)


if __name__ == "__main__":
    data = load_location_data('test.json')
    ani = plot_location_data(data)
