import cv2
import numpy as np

# Load YOLOv3 model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Load classes
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Set input and output layers
layer_names = net.getLayerNames()
output_layers = [layer_names[i- 1] for i in net.getUnconnectedOutLayers()]

# Open video stream
# cap = cv2.VideoCapture("rtsp://admin:bjxy2021@192.168.1.51:554/Streaming/Channels/101")
# cap = cv2.VideoCapture("rtsp://127.0.0.1:8554/test")
# cap = cv2.VideoCapture("rtsp://192.168.100.123:8554/test")
# cap = cv2.VideoCapture("rtsp://10.0.0.26:554/222")
# cap = cv2.VideoCapture("rtsp://10.0.0.22:554/1")
cap = cv2.VideoCapture("rtsp://192.168.1.228:8554/t0")


# cap = cv2.VideoCapture("rtsp://10.0.0.243:8554/czc")



# Initialize variables
count = 0
frame_count=0

while True:
    # Read frame from video stream
    ret, frame = cap.read()
    frame_count+=1
    
    if frame_count % 30 == 0:

        if ret:
            # Resize frame
            frame = cv2.resize(frame, None, fx=0.4, fy=0.4)

            # Convert frame to blob
            blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

            # Set input to network
            net.setInput(blob)

            # Forward pass through network
            outs = net.forward(output_layers)

            # Initialize variables
            class_ids = []
            confidences = []
            boxes = []

            # Loop over all detections
            for out in outs:
                for detection in out:
                    # Extract class ID and confidence
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]

                    # Check if detection confidence is high enough
                    if confidence > 0.5:
                        # Extract bounding box coordinates
                        center_x = int(detection[0] * frame.shape[1])
                        center_y = int(detection[1] * frame.shape[0])
                        width = int(detection[2] * frame.shape[1])
                        height = int(detection[3] * frame.shape[0])
                        left = int(center_x - width / 2)
                        top = int(center_y - height / 2)

                        # Add bounding box coordinates to list
                        boxes.append([left, top, width, height])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            # Draw bounding boxes and labels on frame
            indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
            for i in indices:
                # i = i[0]
                box = boxes[i]
                left = box[0]
                top = box[1]
                width = box[2]
                height = box[3]
                cv2.rectangle(frame, (left, top), (left + width, top + height), (0, 255, 0), 2)
                label = f"{classes[class_ids[i]]}: {confidences[i]:.2f}"
                cv2.putText(frame, label, (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            # Display frame
            cv2.imshow("Object detection", frame)

            # Check for key press
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

        else:
            break

# Release video stream and close all windows
cap.release()
cv2.destroyAllWindows()