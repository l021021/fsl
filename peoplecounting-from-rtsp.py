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
# cap = cv2.VideoCapture("rtsp://admin:Bjxy+2023ZYH@192.168.100.48:554/Streaming/Channels/1201")
# cap = cv2.VideoCapture("rtsp://127.0.0.1:8554/test1")
cap = cv2.VideoCapture("rtsp://192.168.1.228:8554/t0")


# Initialize variables
count = 0
prev_count = 0
frame_count = 0

while True:
    # Read frame from video stream
    ret, frame = cap.read()

    frame_count += 1

     # Check if it's time to detect people
    if frame_count % 30 == 0:

        if ret:
            # Resize frame
            frame = cv2.resize(frame, None, fx=0.7, fy=0.7)

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
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]

                    # Check if detection is a person
                    if classes[class_id] == "person": #and confidence > 0:
                        # Get bounding box coordinates
                        center_x = int(detection[0] * frame.shape[1])
                        center_y = int(detection[1] * frame.shape[0])
                        w = int(detection[2] * frame.shape[1])
                        h = int(detection[3] * frame.shape[0])
                        x = center_x - w // 2
                        y = center_y - h // 2

                        # Add detection to lists
                        class_ids.append(class_id)
                        confidences.append(float(confidence))
                        boxes.append([x, y, w, h])

            # Apply non-maximum suppression
            indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

            # Count people
            count = len(indices)
            if count >= 30:
            #退出循环
                print("人数超过3人")
                break

            # Draw bounding boxes and count on frame
            for i in indices:
                # i = i[0]
                box = boxes[i]
                x = box[0]
                y = box[1]
                w = box[2]
                h = box[3]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"People count: {count}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Show frame
        cv2.imshow("People counting", frame)

            # Check if count has changed
        if count != prev_count:
            print(f"People count: {count}")

            # Update previous count
        prev_count = count
        frame_count = 0

        # Wait for key press
        if cv2.waitKey(1) == ord("q"):
            break

# Release video stream and close window
cap.release()
cv2.destroyAllWindows()
