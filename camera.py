import cv2

cap = cv2.VideoCapture(0) #argumento é o indice da camera utilizada
while True:
    sucess, img = cap.read()

    cv2.imshow('Camera',img)
    if cv2.waitKey(10)&0xFF ==27: #Close camera with ESC
        break