import cv2
from deep_sort import DeepSort

# 初始化深度学习模型
deepsort = DeepSort(model_path="deepsort.t7") 

# 打开RTSP流
cap = cv2.VideoCapture(
    "rtsp://admin:Bjxy+2023ZYH@192.168.100.48:554/Streaming/Channels/1201")

while True:
    ret, frame = cap.read()
    
    if ret:
        # 检测人体
        bbox_xywh, cls_conf, cls_ids = yolo_model(frame)  
        
        # 目标跟踪
        outputs = deepsort.update(bbox_xywh, cls_conf, cls_ids, frame)
        
        # 画框并标识ID
        if len(outputs) > 0:
            for j, output in enumerate(outputs):
                bbox = output[0:4]
                id = output[4]
                cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])),(0, 255, 0), 2) 
                cv2.putText(frame, str(id), (int(bbox[0]), int(bbox[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
cap.release()
cv2.destroyAllWindows()
