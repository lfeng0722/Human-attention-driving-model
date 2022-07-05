import cv2
import numpy as np


def overlay(gaze, img):
    img1 = cv2.imread("BDDA/training/camera_images/"+img+'.jpg')
    gaze = np.array(gaze)
    gaze = cv2.resize(gaze,(1280,720),interpolation=cv2.INTER_AREA)

    ret, mask = cv2.threshold(gaze, 175, 255, cv2.THRESH_BINARY)
    maskInv = cv2.bitwise_not(mask)


    img1Bg = cv2.bitwise_and(img1, img1, mask=maskInv)


    return img1Bg
