import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Crea una instancia de cv2.VideoCapture para acceder a la cámara web.
cap = cv2.VideoCapture(0)

# Crea una instancia de mp.solutions.hands.Hands y configura los parámetros de detección y seguimiento.
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        # Lee un fotograma de la cámara web.
        success, image = cap.read()
        if not success:
            print("No se pudo leer el fotograma de la cámara web.")
            break

        # Usa el método process() para detectar las manos en el fotograma.
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Accede a los puntos clave de la mano detectada usando el atributo landmark.
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Dibuja los puntos clave en el fotograma.
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Accede a la posición del punto clave 0 (muñeca) para determinar si es la mano izquierda o derecha.
                if hand_landmarks.landmark[0].x < hand_landmarks.landmark[17].x:
                    print('Mano izquierda detectada.')
                else:
                    print('Mano derecha detectada.')

        # Muestra el fotograma con los puntos clave dibujados.
        cv2.imshow('MediaPipe Hands', image)

        # Espera a que el usuario presione la tecla 'q' para salir del bucle.
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# Libera los recursos.
cap.release()
cv2.destroyAllWindows()
