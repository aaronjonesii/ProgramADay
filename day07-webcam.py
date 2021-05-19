'''
Function:       Display contents of webcam, exit w/ESC
Date:           02.08.2019
Created By:     Anonymous Systems
Dependencies:   opencv-python
Idea:           Bypass LED when enabling camera(custom code camera internal firmware)
'''
import cv2


def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        return_value, frame = cam.read()
        cv2.imshow('WebcamTest', frame)
        if cv2.waitKey(1) == 27:
            break


if __name__ == '__main__':
    show_webcam()