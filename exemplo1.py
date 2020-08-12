# importa o opencv
import cv2

# Recebe o arquivo de harrcascade
classificador = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

# Carrega a imagem em uma variável com a função imread do opencv
imagem = cv2.imread('pessoas\\faceolho.jpg')

# Converte a imagem para cinza para facilitar na detecção
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

''' 
- Identifica as faces com a função detectMultiScale
- 
'''
facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.1, minNeighbors=9, minSize=(25, 25))

# Pega a quantidade de faces
qntFaces = len(facesDetectadas)

# Imprime a matriz das faces
print(facesDetectadas)

'''
- Percorre a imagem para destacar as faces com base na posiçao x e y, com largura e altura
- Adiciona a cor vermelho (em RGB)
- Adiciona uma borda de tamanho 2
'''

for (x, y, l, a) in facesDetectadas:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

# Abre a imagem original em uma janela com title de qnt de faces
cv2.imshow(str(qntFaces) + " Faces detectadas", imagem)

# Função para fechar janela ao click de qualquer tecla
cv2.waitKey()
