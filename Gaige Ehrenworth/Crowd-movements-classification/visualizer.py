import cv2
import numpy as np
import os

# Path to your video file
video_path = 'Data/Crowd-11/rgb/4_1740_21_NYPD_Crowd_Behavior_Training_Video.mp4'

# Load the saved optical flows and display them
saved_flow_file = "Data/Crowd-11/flow/4_1740_21_NYPD_Crowd_Behavior_Training_Video.npy"
if not os.path.exists(saved_flow_file):
    print("Error: Optical flow file does not exist.")
    exit()

video_flows = np.load(saved_flow_file)

def draw_flow(image, flow):
    h, w = image.shape[:2]
    step_size = 16  # You can adjust this value to increase/decrease the density of vectors

    for y in range(0, h - step_size, step_size):
        for x in range(0, w - step_size, step_size):
            flow_x, flow_y = flow[y, x]
            cv2.line(image, (x, y), (int(x + flow_x), int(y + flow_y)), (0, 255, 0), 1)
            cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

    return image

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video_path = 'flow_animation.avi'
out = cv2.VideoWriter(output_video_path, fourcc, 30.0, (476, 360), True)

# Iterate through the optical flows and display them
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_index = 0

while frame_index < len(video_flows):
    ret, frame = cap.read()
    if not ret:
        break
    
    flow_image = draw_flow(frame.copy(), video_flows[frame_index])

    out.write(flow_image)
    
    cv2.imshow('Optical Flow', flow_image)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
    frame_index += 1

cap.release()
out.release()
cv2.destroyAllWindows()
