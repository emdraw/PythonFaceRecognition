import cv2

face_carcase = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

def facial():
    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_carcase.detectMultiScale(gray, 1.1, 4)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.imshow('img', img)
        k = cv2.waitKey(1)
        if k == 27:
            break
    cap.release()
