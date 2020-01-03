''' Interactive image pixel value finder '''
import sys

import cv2


def on_mouse_cb(event, x, y, flags, img):
    ''' On mouse event callback '''
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'x: {x}')
        print(f'y: {y}')
        print(f'v: {img[y,x]}')


def main():
    '''Main function of the script'''
    img = cv2.imread(sys.argv[1])
    cv2.imshow('', img)
    cv2.setMouseCallback('', on_mouse_cb, param=img)
    cv2.waitKey()


if __name__ == "__main__":
    main()
