import cv2
import mediapipe as mp
import numpy as np

# Setup Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=2)
mp_drawing = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process with Mediapipe
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Get necessary landmarks
            h, w, _ = frame.shape
            nose = face_landmarks.landmark[1]
            left_eye = face_landmarks.landmark[33]
            right_eye = face_landmarks.landmark[263]

            # Convert to pixel coords
            nose_x = nose.x * w
            nose_y = nose.y * h
            left_x = left_eye.x * w
            right_x = right_eye.x * w
            avg_eye_y = (left_eye.y + right_eye.y) / 2 * h

            # Determine direction
            direction = "Center"
            if nose_x < left_x:
                direction = "Right"
            elif nose_x > right_x:
                direction = "Left"
            elif nose_y < avg_eye_y - 20:
                direction = "Up"
            elif nose_y > avg_eye_y + 20:
                direction = "Down"

            # Show direction
            cv2.putText(frame, f"Direction: {direction}", (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Draw landmarks (optional)
            mp_drawing.draw_landmarks(
                frame, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1))

    # Show frame
    cv2.imshow("Head Direction Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
