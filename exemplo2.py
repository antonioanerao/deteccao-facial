# Importa o opencv
import cv2

# Carrega os arquivos haarcascades treinados para face e olhos
classificadorFace = cv2.CascadeClassifier('cascades\\haarcascade_frontalface_default.xml')
classificadorOlhos = cv2.CascadeClassifier('cascades\\haarcascade_eye.xml')

# Carrega a imagem da Face e converte para cinza
imagem = cv2.imread('pessoas\\eu2.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Faz a detecção da face (ou faces)
facesDetectadas = classificadorFace.detectMultiScale(imagemCinza)

# Laço para percorrer a imagem e detectar face e olhos
for (x, y, l, a) in facesDetectadas:
    # Desenha o retangulo na face
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

    '''
    - Carrega a região da face detectada
    - Converte a região dos olhos para cinza
    - Detecta os olhos na imagem da face
    '''
    regiao = imagem[y:y + a, x:x + l]
    regiaoCinzaOlhos = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
    olhosDetectados = classificadorOlhos.detectMultiScale(regiaoCinzaOlhos, scaleFactor=1.1, minNeighbors=5)

    # Laço para percorrer a região dos olhos e desenhar o retangulo
    for (ox, oy, oa, ol) in olhosDetectados:
        cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (255, 0, 255), 2)

cv2.imshow("Olhos", imagem)
cv2.waitKey()
