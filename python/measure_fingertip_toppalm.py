import cv2
import mediapipe as mp
import math
from os import system

# Inicializar el detector de manos
system("cls")
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Obtener el número total de cámaras disponibles
num_cameras = 2 

# Pedir al usuario que elija una cámara
print("Selecciona una cámara (0 - {}):".format(num_cameras - 1))
camera_idx = int(input())

# Inicializar la cámara seleccionada
cap = cv2.VideoCapture(camera_idx)

# Obtener medidas de la pantalla
screen_height = 1280
screen_width = screen_height

# Establecer la ventana en modo de pantalla completa
#cv2.namedWindow('Hand Detection', cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty('Hand Detection', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

     # Voltear el frame horizontalmente (espejo)
    frame = cv2.flip(frame, 1)

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar manos
    results = hands.process(frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for idx, landmark in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)
    # Obtener coordenadas de los puntos 8 y 5
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_base = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]

            # Calcular la distancia euclidiana
            distance = math.sqrt((index_tip.x - index_base.x)**2 + (index_tip.y - index_base.y)**2)
            #si es la webcam, divido para contrarrestar medidas
            if camera_idx == 1: distance = distance / 1.5714
            cv2.putText(frame, f'Distancia 5 a 8: {distance:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar el frame con las detecciones
    cv2.imshow('Hand Detection', frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
