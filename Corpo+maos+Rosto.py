import mediapipe as mp
import cv2

mp_drawing=mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
#simples exibição de cÂmera
# cap=cv2.VideoCapture(0)
# while cap.isOpened():
#     ret, frame = cap.read()
#     cv2.imshow("Visao webcam", frame)
#     if cv2.waitKey(10)&0xFF == ord ('q'):  #a aplicação não fecha pelo icone de X, mas apertando o q no teclado
#         break
# cap.release()
# cv2.destroyWindow()

cap=cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame=cap.read()

        #mudar padrão de cores da captura para processamento
        image=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #leitura das posições
        results=holistic.process(image)
        #retorna para cor original para exibição
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        #marca as posições do corpo
        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.POSE_CONNECTIONS)
        #marcar posições das mãos
        #direita
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        #esquerda
        #mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp.holistic.HAND_CONNECTIONS)