import cv2

def calculate_length(contour):
    perimeter = cv2.arcLength(contour, True)
    return perimeter