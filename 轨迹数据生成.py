import random
import time
import json
from shapely.geometry import Point, Polygon

# 模拟地图边界范围（经度和纬度）
MAP_BOUNDARY = {
    'min_longitude': 121.49603350430783,
    'max_longitude': 121.50580830487178,
    'min_latitude':  31.339034933154934,
    'max_latitude': 31.346297650051994
}

polygon_coords = [(121.49603350430783, 31.339034933154934), (121.50580830487178, 31.339034933154934), (121.50580830487178, 31.346297650051994), (121.49603350430783, 31.346297650051994)]
                      
# 生成模拟数据的数量
NUM_DATA_POINTS = 300

# 生成模拟数据



polygon = Polygon(polygon_coords)

# 生成模拟数据
def generate_location_data():
    location_data = []
    last_longitude, last_latitude = None, None
    while len(location_data) < NUM_DATA_POINTS:
        longitude = round(random.uniform(
            MAP_BOUNDARY['min_longitude'], MAP_BOUNDARY['max_longitude']), 6)
        latitude = round(random.uniform(
            MAP_BOUNDARY['min_latitude'], MAP_BOUNDARY['max_latitude']), 6)
        point = Point(longitude, latitude)
        if polygon.contains(point):
            location_data.append((longitude, latitude))
            last_longitude, last_latitude = longitude, latitude
    return location_data
    timestamp = time.time()

    for _ in range(NUM_DATA_POINTS):
        # while True:
        # 生成随机的偏移量
        longitude_offset = random.uniform(-1, 1) / 1500  # 半分钟左右的行走距离
        latitude_offset = random.uniform(-1, 1) / 1500
        # print(longitude_offset, latitude_offset)
        if last_longitude is not None and last_latitude is not None:
            # 计算上一个点和当前点之间的距离
            # 假设移动速度在1m/s到10m/s之间，根据距离计算合理的时间间隔
            longitude = last_longitude + longitude_offset
            latitude = last_latitude + latitude_offset
            distance = haversine_distance(
                last_longitude, last_latitude, longitude, latitude)
            print(distance, end='   ')
            time_interval = distance*200  # 一分钟60米的速度
        else:
            # 对于第一个点，时间间隔设置为1秒
            time_interval = 30
        print(time_interval)
        # longitude = last_longitude + longitude_offset
        # latitude = last_latitude + latitude_offset

        timestamp = int(timestamp+time_interval)
        location_data.append(
            {'longitude': longitude, 'latitude': latitude, 'timestamp': timestamp})

        # 更新上一个点的经纬度
        last_longitude, last_latitude = longitude, latitude
        # 等待一段时间，模拟定位设备的发送间隔
        # time.sleep(time_interval)

    return location_data

# 计算两个经纬度点之间的距离（使用Haversine公式）


def haversine_distance(lon1, lat1, lon2, lat2):
    from math import radians, sin, cos, sqrt, atan2
    # 地球半径（单位：千米）
    R = 6371.0

    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

# 将模拟数据写入JSON文件


def write_to_json_file(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    location_data = generate_location_data()
    write_to_json_file(location_data, 'test.json')
