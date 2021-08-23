import cv2
import datetime
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
smile_cascade =  cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')
while True:
    i, frame = capture.read()
    original_frame = frame.copy()
    if not i:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray_scale,1.3,5)
    for x, y, w, h in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        face_roi=frame[y:y+h, x:x+w]
        gray_roi=gray_scale[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(gray_roi, 1.3,25)
        for x1, y1, w1, h1 in smile:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            photo_name = f'photo-{time_stamp}.png'
            cv2.imwrite(photo_name,original_frame)
    cv2.imshow('camera star', frame)
    if cv2.waitKey(20) == ord('Q' or 'q'):
        break