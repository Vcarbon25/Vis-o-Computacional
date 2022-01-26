

import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands=mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime=0
cTime=0
#file = open("posicoes da mao", "w")
#file.write("posições da mao \n")
while cap.isOpened():
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    #print(results.multi_hand_landmark)
    if  results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
               # file.write(id,",",cx,",",cy,"\n")
                if id==12:
                    cv2.circle(img, (cx,cy), 15, (255, 0, 255),cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    #cv2.putText(img, str(int(fps)), (10, 70),cv2.FONT_HERSHEY_PLAIN,3(255, 0, 255),3 )

    cv2.imshow("image",img)
    cv2.waitKey(1)
    #as tres linhas acima são o básico para  exibir a imagem de uma câmera
    if cv2.waitKey(10)&0xFF==ord('q'):
        break

#file.close()
print("até aqqui funciona")