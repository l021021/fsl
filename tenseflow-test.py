import cv2
import tensorflow as tf
from keras.applications import MobileNetV2
model = MobileNetV2()

# 加载SSD模型
# model = tf.keras.applications.SSDMobileNetV2()

# 加载物体类别标签
labels = ['person', 'car', 'cat', 'dog', ...]

# 打开视频流
# cap = cv2.VideoCapture('rtsp://admin:Bjxy+2023ZYH@192.168.100.48:554/Streaming/Channels/501')
cap = cv2.VideoCapture("rtsp://192.168.1.228:8554/t0")

while True:
    # 读取视频帧
    ret, frame = cap.read()

    # 对帧进行物体检测
    detections = model.predict(frame)

    # 根据检测结果进行分类
    for detection in detections:
        class_id = detection['class_id']
        class_label = labels[class_id]
        confidence = detection['confidence']
        # 进行分类操作

    # 显示帧
    cv2.imshow('Video', frame)

    # 按下q键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放视频流和窗口
cap.release()
cv2.destroyAllWindows()
