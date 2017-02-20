import cv2
from crop_text import process_image_without_save as pi


def detect(img):
    card = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # card = cv2.GaussianBlur(card, (3, 3), -1)
    card = cv2.bilateralFilter(card, 9, 25, 175)
    card = cv2.Canny(card, 50, 150)

    contours, _ = cv2.findContours(card, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print len(contours)

    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

    return img


def crop_text_region(img):
    return pi(img, 1)

if __name__ == '__main__':
    SIZE = 750
    path = 'samples/bc_ref/r_1.jpg'
    img = cv2.imread(path)

    img = cv2.resize(img, (SIZE, SIZE), None)
    cropped = crop_text_region(img)
    cv2.rectangle(img, (cropped[0], cropped[1]), (cropped[2], cropped[3]), (0, 255, 0), 1)
    cv2.imshow('Orig', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()