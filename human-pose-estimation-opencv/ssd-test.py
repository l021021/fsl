import cv2 as cv
import urllib.request

# 下载deploy.prototxt文件
urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/weiliu89/caffe/master/models/VGGNet/VOC0712/SSD_300x300/deploy.prototxt", "deploy.prototxt")

# 下载model.caffemodel文件
urllib.request.urlretrieve(
    "http://dl.caffe.berkeleyvision.org/SSD_300x300.caffemodel", "model.caffemodel")

# 加载SSD模型
model = cv.dnn.readNetFromCaffe("deploy.prototxt", "model.caffemodel")

# 打开RTSP流
cap = cv.VideoCapture("rtsp://example.com/stream")

while True:
    # 读取一帧图像
    ret, frame = cap.read()

    if not ret:
        break

    # 对图像进行预处理
    blob = cv.dnn.blobFromImage(
        frame, 1.0 / 255, (300, 300), (0, 0, 0), swapRB=True, crop=False)

    # 将预处理后的图像输入到神经网络中进行推理
    model.setInput(blob)
    detections = model.forward()

    # 解析输出结果
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            # 提取检测框的坐标
            box = detections[0, 0, i, 3:7] * np.array(
                [frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            (startX, startY, endX, endY) = box.astype("int")

            # 绘制检测结果
            cv.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

    # 显示检测结果
    cv.imshow("SSD result", frame)

    if cv.waitKey(1) == ord('q'):
        break

# 释放资源
cap.release()
cv.destroyAllWindows()
