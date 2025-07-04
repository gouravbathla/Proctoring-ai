import cv2
import numpy as np

# Load Haar cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes[:2]:  # Only consider first two eyes detected
            eye = roi_gray[ey:ey+eh, ex:ex+ew]
            _, threshold_eye = cv2.threshold(eye, 70, 255, cv2.THRESH_BINARY)
            h_e, w_e = threshold_eye.shape
            left_side = threshold_eye[:, 0:int(w_e/2)]
            right_side = threshold_eye[:, int(w_e/2):]
            left_white = cv2.countNonZero(left_side)
            right_white = cv2.countNonZero(right_side)
            if left_white + right_white == 0:
                gaze_ratio = 0.5
            else:
                gaze_ratio = left_white / (left_white + right_white)
            if gaze_ratio < 0.4:
                gaze_direction = "RIGHT"
            elif gaze_ratio > 0.6:
                gaze_direction = "LEFT"
            else:
                gaze_direction = "CENTER"
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
            cv2.putText(frame, f'Gaze: {gaze_direction}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 3)
            break  # Only process one eye for simplicity

    cv2.imshow("Eye Gaze Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
