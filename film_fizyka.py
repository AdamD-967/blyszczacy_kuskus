import cv2
cap = cv2.VideoCapture('C:/Users/adamd/yyy/video-1580892011.mp4')
if cap.isOpened() == False:
    print('error during opening')
i = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imwrite('klatka'+str(i)+'.jpg', frame)
    i += 1
cap.release()
cv2.destroyAllWindows()
