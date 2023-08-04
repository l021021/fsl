import cv2
import numpy as np
# 加载 COCO 数据集的类别标签
LABELS = open("coco.names").read().strip().split("\n")

# 加载 YOLOv4 模型
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")

# 获取 YOLOv4 未连接的输出层名称
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# 打开 RTSP 视频流
cap = cv2.VideoCapture("rtsp://192.168.1.228:8554/t0")

# 循环读取视频帧并进行检测
while True:
    # 读取视频帧
    ret, frame = cap.read()
    if not ret:
        break

    # 对视频帧进行预处理
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)

    # 将预处理后的帧输入到 YOLOv4 模型中进行检测
    net.setInput(blob)
    layer_outputs = net.forward(output_layers)

    # 解析检测结果并计算人数
    class_ids = []
    confidences = []
    boxes = []
    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.8 and class_id == 0:  # 只检测人类
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                w = int(detection[2] * frame.shape[1])
                h = int(detection[3] * frame.shape[0])
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])
                #label each box with the confidence level
                cv2.putText(frame, str(round(confidence,2)), (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1) 


    # 显示检测结果
    num_people = len(boxes)
    for i in range(num_people):
        x, y, w, h = boxes[i]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #delete the overlapping boxes   
    for i in range(num_people):
        for j in range(i+1,num_people):
            if boxes[i][0] < boxes[j][0] + boxes[j][2] and boxes[i][0] + boxes[i][2] > boxes[j][0] and boxes[i][1] < boxes[j][1] + boxes[j][3] and boxes[i][1] + boxes[i][3] > boxes[j][1]:
                if confidences[i] > confidences[j]:
                    boxes[j][0] = 0
                    boxes[j][1] = 0
                    boxes[j][2] = 0
                    boxes[j][3] = 0
                else:
                    boxes[i][0] = 0
                    boxes[i][1] = 0
                    boxes[i][2] = 0
                    boxes[i][3] = 0
    
    cv2.putText(frame, f"Number of people: {num_people}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # 显示视频帧
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()