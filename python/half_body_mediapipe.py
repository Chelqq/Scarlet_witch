import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Obtener el número total de cámaras disponibles
num_cameras = 2  # Puedes cambiar esto según el número de cámaras que tengas.

# Pedir al usuario que elija una cámara
print("Selecciona una cámara (0 - {}):".format(num_cameras - 1))
camera_idx = int(input())

# Inicializar la cámara seleccionada
cap = cv2.VideoCapture(camera_idx)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Voltear el frame horizontalmente (espejo)
        frame = cv2.flip(frame, 1)
        # Convertir el frame a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Invertir colores para que sea compatible con mediapipe
        image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        results = pose.process(image=image)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Obtener coordenadas de puntos de referencia específicos
            nose_coords = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE]
            left_shoulder_coords = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
            right_shoulder_coords = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]

            if nose_coords and left_shoulder_coords and right_shoulder_coords:
                h, w, _ = frame.shape
                x_nose, y_nose = int(nose_coords.x * w), int(nose_coords.y * h)
                x_l_shoulder, y_l_shoulder = int(
                    left_shoulder_coords.x * w), int(left_shoulder_coords.y * h)
                x_r_shoulder, y_r_shoulder = int(
                    right_shoulder_coords.x * w), int(right_shoulder_coords.y * h)

                cv2.circle(frame, (x_nose, y_nose), 5, (0, 255, 0), -1)
                cv2.circle(frame, (x_l_shoulder, y_l_shoulder),
                           5, (0, 255, 0), -1)
                cv2.circle(frame, (x_r_shoulder, y_r_shoulder),
                           5, (0, 255, 0), -1)

        cv2.imshow('Pose Landmark Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
