import cv2
def cleanup(image):
    # grayscale
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # threshhold
    noise = cv2.fastNlMeansDenoising(gray)
    return noise

