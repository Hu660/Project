import cv2
import os

# 打开摄像头
cap = cv2.VideoCapture(0)

# 读取一帧
ret, frame = cap.read()

# 释放摄像头
cap.release()

# 保存照片到桌面
file_path = os.path.expanduser("~/Desktop/photo.jpg")
cv2.imwrite(file_path, frame)

print("照片已保存到桌面")