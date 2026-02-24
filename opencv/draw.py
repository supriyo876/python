import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

""" 
Color	Value
Blue	(255,0,0)
Green	(0,255,0)
Red	(0,0,255)
"""
blank[:] = 0,0,255
cv.imshow('red', blank)

cv.waitKey(0)