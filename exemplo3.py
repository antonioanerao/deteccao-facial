#Exemplo de uso com webcam

# Importa o opencv
import cv2

# Define a webcam que será usada. 0 para webcam padrão ou o número ID do dispositivo
video = cv2.VideoCapture(1)

# Carrega o arquivo haarcascade treinado
classificadorFace = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

# O while será verdadeiro e vai capturar até a tecla "Q" ser apertada
while True:
    # Frame recebe o vídeo. Conectado retorna true enquanto estiver dentro do while
    conectado, frame = video.read()

    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificadorFace.detectMultiScale(frameCinza, minSize=(70, 70), minNeighbors=10)

    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 0, 255), 2)

    # Mostra a webcam original com o retangulo
    cv2.imshow('Vídeo', frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
