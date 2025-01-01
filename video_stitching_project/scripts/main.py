import os
import cv2
import numpy as np

base_path = "D:/Work/AIO/video_stitching_project"

video1_path = os.path.join(base_path, "input_videos", "z.mp4")
video2_path = os.path.join(base_path, "input_videos", "n.mp4")
output_path = os.path.join(base_path, "output_videos", "stitched_video.mp4")

cap1 = cv2.VideoCapture(video1_path)
cap2 = cv2.VideoCapture(video2_path)

fps1 = int(cap1.get(cv2.CAP_PROP_FPS))
width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_width = width1 + width2
output_height = max(height1, height2)
out = cv2.VideoWriter(output_path, fourcc, fps1, (output_width, output_height))

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break

    stitched_frame = np.hstack((frame1, frame2))
    out.write(stitched_frame)

    cv2.imshow('Stitched Video', stitched_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()

print("video saved successfully.")