''' Main mmodle of the script '''
import cv2

from analytics import Analytics
from logger import CliLogger

from detect import detect


def main():
    '''Main function of the script'''
    logger = CliLogger('%H:%M:%S')
    analytics = Analytics(logger)
    img = cv2.imread('screenshots/Screen01.png')
    objects = detect(analytics, img, start=(186, 0, 185), end=(255, 2, 255))
    for obj in objects:
        img = cv2.putText(img, obj['name'], obj['coor'], 1, 1, (0, 255, 0))
    cv2.imshow('', img)
    cv2.waitKey()


if __name__ == "__main__":
    main()
