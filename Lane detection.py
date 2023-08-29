import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img

def draw_lines(img, lines, color=(0, 255, 0), thickness=2):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

cap = cv2.VideoCapture("C:\\Users\\krish\\Desktop\\Lane Detection files\\Sample.mp4")  # 0 for webcam, or replace with video file path

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_img, 100, 200)
    
    height, width = edges.shape[:2]
    vertices = np.array([[(0, height), (width / 2, height / 2), (width, height)]], dtype=np.int32)
    roi_img = region_of_interest(edges, vertices)
    
    lines = cv2.HoughLinesP(roi_img, rho=1, theta=np.pi / 180, threshold=40, minLineLength=20, maxLineGap=20)
    
    line_img = np.zeros((height, width, 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    
    result_img = cv2.addWeighted(frame, 0.8, line_img, 1, 0.0)
    
    cv2.imshow('Lane Detection', result_img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

