import cv2
from predict import predict_image

def analyze_video(path):

    cap=cv2.VideoCapture(path)

    fake=0
    real=0

    frame_id=0

    while True:

        ret,frame=cap.read()

        if not ret:
            break

        if frame_id%30==0:

            temp="temp.jpg"

            cv2.imwrite(temp,frame)

            result,_=predict_image(temp)

            if result=="Fake":
                fake+=1
            else:
                real+=1

        frame_id+=1

    cap.release()

    if fake>real:
        return "Fake Video"

    return "Real Video"