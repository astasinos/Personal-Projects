"""
    @Author : Alkis Stasinos 2020

    This is a simple lane detector script based on OpenCV
    It works by cropping a specific polygon on the given video,
    after it performs grayscaling and gaussian blur.

    Then, Hough Transform is used to detect the lines.



"""


import cv2
import numpy as np 


def make_coords(image, line_params):
    
    try:
        slope, intercept = line_params
    except TypeError:
        slope, intercept = 0.001, 0
    y1 = image.shape[0]
    y2 = int(y1 * (4/5))
    x1 = int((y1 - intercept)/slope)
    x2= int((y2 - intercept)/slope)
    return np.array([x1,y1,x2,y2])



def average(image, lines):

    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        params = np.polyfit((x1,x2), (y1,y2), 1)
        slope = params[0]
        intercept = params[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    
    left_fit_average = np.average(left_fit, axis = 0)
    right_fit_average = np.average(right_fit, axis = 0)
    left_line = make_coords(image, left_fit_average)
    right_line = make_coords(image, right_fit_average)
    return np.array([left_line, right_line])

def select_region(image):

    mask = np.zeros_like(image)
    height = image.shape[0]
    pts = np.array([[29,588], [518,491], [649,498], [1079,700], [65,700]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillConvexPoly(mask, pts, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def display_lines(image, lines):
    
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1,y1), (x2,y2), (0,255,0), 10)
    return line_image

capture  = cv2.VideoCapture("test3.mp4")

while(capture.isOpened()):
    _, frame = capture.read()

    lane_image = np.copy(frame)
    grayscale = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur  = cv2.GaussianBlur(grayscale, (5,5), 0)
    canny_img = cv2.Canny(blur, 50, 150)
    cropped = select_region(canny_img)
    lines = cv2.HoughLinesP(cropped, 2, np.pi/180, 70, np.array([]), 40, 10)
    averaged_lines = average(lane_image, lines)
    line_image = display_lines(lane_image, averaged_lines)

    
    combo_image = cv2.addWeighted(lane_image, 0.65, line_image, 1, 1)

    cv2.imshow("OpenCV Simple Lane Detection Demo   -   Alkis Stasinos", combo_image[150:, ])
    cv2.waitKey(10)


