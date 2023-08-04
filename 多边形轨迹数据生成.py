import random
import time
import json
from shapely.geometry import Point, Polygon
import os

# 模拟地图边界范围（经度和纬度）
# MAP_BOUNDARY = {
#     'min_longitude': 121.49603350430783,
#     'max_longitude': 121.50580830487178,
#     'min_latitude':  31.339034933154934,
#     'max_latitude': 31.346297650051994
# }

# polygon_coords = [(121.49603350430783, 31.339034933154934), (121.50580830487178, 31.339034933154934), (121.50580830487178, 31.346297650051994), (121.49603350430783, 31.346297650051994)]

polygon_coords = [(121.49975987362944, 31.34611931891598), (121.49454252343583, 31.339521255235624), (121.49719814127178,
                                                                                                      31.338467354984033), (121.50195947628328, 31.344985309654533), (121.49975987362944, 31.34611931891598)]
# 生成模拟数据的数量
NUM_DATA_POINTS = 1000

# 生成模拟数据

polygon = Polygon(polygon_coords)

# get the max latitude and longitude of polygon
minx, miny, maxx, maxy = polygon.bounds
widx = maxx-minx
widy = maxy-miny
print(minx, miny, maxx, maxy)
print(polygon)

# 生成模拟数据


def generate_location_data():
    timestamp = time.time()
    location_data = []
    longitude = round(random.uniform(minx+0.3*widx, maxx-0.3*widx), 6)
    latitude = round(random.uniform(miny+0.3*widy, maxy-0.3*widy), 6)
    print(longitude, latitude)
    last_longitude, last_latitude = None, None
    while len(location_data) <= NUM_DATA_POINTS:
        print('g', end='')
        longitude_offset = random.uniform(-1, 1) / 1500  # 半分钟左右的行走距离
        latitude_offset = random.uniform(-1, 1) / 1500
        if last_longitude is not None and last_latitude is not None:
            # 计算上一个点和当前点之间的距离
            # 假设移动速度在1m/s到10m/s之间，根据距离计算合理的时间间隔
            longitude = last_longitude + longitude_offset
            latitude = last_latitude + latitude_offset
            point = Point(longitude, latitude)
            if polygon.contains(point):
                distance = haversine_distance(
                    last_longitude, last_latitude, longitude, latitude)
                print(distance, end='   ')
                time_interval = distance*200
                timestamp = int(timestamp+time_interval)
                print("bingo", len(location_data), end='   ')
                location_data.append(
                    {'longitude': longitude, 'latitude': latitude, 'timestamp': timestamp})
                last_longitude, last_latitude = longitude, latitude
                # 一分钟60米的速度
        else:
            # 对于第一个点，时间间隔设置为1秒
            time_interval = 30
            point = Point(longitude, latitude)

            if polygon.contains(point):
                #    location_data.append((longitude, latitude))
                #    print(time_interval)
                timestamp = int(timestamp+time_interval)
                location_data.append(
                    {'longitude': longitude, 'latitude': latitude, 'timestamp': timestamp})
                last_longitude, last_latitude = longitude, latitude

        # longitude = last_longitude + longitude_offset
        # latitude = last_latitude + latitude_offset
    return location_data

    # 更新上一个点的经纬度
    # 等待一段时间，模拟定位设备的发送间隔
    # time.sleep(time_interval)


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
    if os.path.exists(filename):
        i = 1
        while True:
            new_filename = f"{os.path.splitext(filename)[0]}_{i}{os.path.splitext(filename)[1]}"
            if not os.path.exists(new_filename):
                filename = new_filename
                break
            i += 1
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    location_data = generate_location_data()
    write_to_json_file(location_data, 'test.json')
