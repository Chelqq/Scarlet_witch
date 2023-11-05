import cv2
import numpy as np

# Inicializar el detector de cuerpo
net = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'graph.pbtxt')

# Leer la imagen de configuración y cargar el modelo
frame = cv2.imread('image.jpg')
frameWidth = frame.shape[1]
frameHeight = frame.shape[0]

# Definir las clases (en este caso, solo estamos interesados en personas)
classes = ["person"]

# Establecer la confianza mínima para la detección
confThreshold = 0.5

# Establecer el umbral de confianza para filtrar las detecciones
net.setInput(cv2.dnn.blobFromImage(frame, 0.007843, (frameWidth, frameHeight), 127.5))

# Obtener las detecciones
detections = net.forward()

# Iterar sobre las detecciones
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > confThreshold:
        class_id = int(detections[0, 0, i, 1])

        # Verificar si la clase detectada es una persona
        if classes[class_id] == "person":
            # Obtener las coordenadas del cuadro delimitador
            box = detections[0, 0, i, 3:7] * np.array([frameWidth, frameHeight, frameWidth, frameHeight])
            (startX, startY, endX, endY) = box.astype("int")

            # Dibujar el cuadro delimitador y mostrarlo
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

# Mostrar el frame con las detecciones
cv2.imshow('Body Detection', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
