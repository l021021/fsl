import cv2
import numpy as np
import os
import sys
import random
import math
import time
import tensorflow as tf
import keras
import mrcnn.config
import mrcnn.utils
import mrcnn.model

# Define the classes you want to detect
class_names = ['BG', 'class1', 'class2', 'class3']

# Load the Mask R-CNN model
model = mrcnn.model.MaskRCNN(mode="inference",
                             config=mrcnn.config.Config(),
                             model_dir=os.getcwd())

# Load the weights for the model
model.load_weights('mask_rcnn_coco.h5', by_name=True)

# Set up the RTSP stream
cap = cv2.VideoCapture('rtsp://your_rtsp_stream_url')

while True:
    # Read a frame from the stream
    ret, frame = cap.read()

    # Preprocess the frame
    frame = cv2.resize(frame, (1024, 1024))
    frame = np.array(frame)

    # Use the Mask R-CNN model to detect objects in the frame
    results = model.detect([frame], verbose=0)

    # Draw the detected objects on the frame
    r = results[0]
    for i in range(len(r['class_ids'])):
        if class_names[r['class_ids'][i]] == 'class1':
            color = (255, 0, 0)
        elif class_names[r['class_ids'][i]] == 'class2':
            color = (0, 255, 0)
        elif class_names[r['class_ids'][i]] == 'class3':
            color = (0, 0, 255)
        else:
            color = (0, 0, 0)
        cv2.rectangle(frame, (r['rois'][i][1], r['rois'][i][0]),
                      (r['rois'][i][3], r['rois'][i][2]), color, 2)
        cv2.putText(frame, class_names[r['class_ids'][i]], (
            r['rois'][i][1], r['rois'][i][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy the window
cap.release()
cv2.destroyAllWindows()
