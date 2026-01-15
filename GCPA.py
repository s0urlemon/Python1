import cv2
import mediapipe as mp
import time
import numpy as np
mp_hands=mp.solutions.hands
hands=mp_hands.Hands(min_detection_confidence=0.7,min_tracking_confidence=0.7)
mp_draw=mp.solutions.drawing_utils

filters=[
    None,
    'GRAYSCALE',
    'SEPIA',
    'NEGATIVE',
    'BLUR'
]
current_filter=0

cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error:Couldn't access the webcam.")
    exit()

last_action_time=0
debounce_time=1

def apply_filter(frame,filter_type):
    if filter_type=='GRAYSCALE':
        return cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    elif filter_type=='SEPIA':
        sepia_filter=np.array([[0.272,0.534,0.131],
                               [0.349,0.686,0.168],
                               [0.393,0.769,0.189]])
        sepia_frame=cv2.transform(frame,sepia_filter)
        sepia_frame=np.clip(sepia_frame,0,255)
        return sepia_frame.astype(np.uint8)
    elif filter_type=='NEGATIVE':
        return cv2.bitwise_not(frame)
    elif filter_type=='BLUR':
        return cv2.GaussianBlur(frame,(15,15),0)
    return frame

while True:
    success,img=cap.read()
    if not success:
        print("Failed to read frame from webcam.")
        break
    img=cv2.filp(img,1)
    img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_draw_landmarks(img,hand_landmarks,mp_hands.HAND_CONNECTIONS)

            thumb_tip=hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip=hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_TIP]
            middle_tip=hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_TIP]
            ring_tip=hand_landmarks.landmark[mp_hands.HandLandmark.RING_TIP]
            pinky_tip=hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]