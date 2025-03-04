import cv2
import time

ptime = 0
ctime = 0
cap = cv2.VideoCapture(0)  # argumento é o indice da camera utilizada
while True:
    sucess, img = cap.read()
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    reverse_gray = cv2.bitwise_not(gray_img)
    blur = cv2.GaussianBlur(reverse_gray,(21,21),0)
    rev_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(gray_img,rev_blur,scale=256.0)
    ctime = time.time()
    fps = 1 / (ctime - ptime)  # o calculo do fps vai resultar em um real
    ptime = ctime  # modifica os valores para próxima iteração
    nfps = int(fps)  # simplifica o numero a ser exibido
    txtfps = str(nfps)  # converte n para texto
    cv2.putText(
        sketch, txtfps, (10, 50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (20, 80, 255)
    )  # coloca o texto na imagem
    cv2.imshow("Live Sketch", sketch)
    if cv2.waitKey(10) & 0xFF == 27:  # Close camera with ESC
        break
