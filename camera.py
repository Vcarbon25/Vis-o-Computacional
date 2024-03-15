import cv2
import PySimpleGUI as sg

row1 = [[sg.Image(filename="",key="camera")]]
layout=[row1]
cap = cv2.VideoCapture(0)       # Setup the camera as a capture device
janela=sg.Window('V8DoTCC Mediapipe ',layout).finalize()

while True:                     # The PSG “Event Loop”

    event, values = janela.Read(timeout=20, timeout_key='timeout')      # get events for the window with 20ms max wait
    sucess, frame = cap.read()
        
    janela['camera'].Update(data=cv2.imencode('.png', frame)[1].tobytes()) # Update image in window
    if event==sg.WINDOW_CLOSED:
        break

