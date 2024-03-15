import cv2
import time
ptime=0
ctime=0
cap = cv2.VideoCapture(0) #argumento é o indice da camera utilizada
while True:
    sucess, img = cap.read()

    ctime = time.time()
    fps = 1/(ctime-ptime) #o calculo do fps vai resultar em um real
    ptime=ctime  #modifica os valores para próxima iteração
    nfps=int(fps)  #simplifica o numero a ser exibido
    txtfps=str(nfps) #converte n para texto
    cv2.putText(img, txtfps,(10,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(20,80,255)) #coloca o texto na imagem
    cv2.imshow('Camera',img)
    if cv2.waitKey(10)&0xFF ==27: #Close camera with ESC
        break