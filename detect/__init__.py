''' Object detection module '''
import cv2

from utils import coor_offset


def detect(analytics, img, start, end):
    ''' Finds the league objects '''
    analytics.start_timer('in_range', 'Filtering using in range')
    output = cv2.inRange(img, start, end)
    contours, _ = cv2.findContours(
        output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    objects = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area == 0:
            coor = tuple(contour[0][0])
            blue, green, red = img[coor_offset(coor, (27, 16), img.shape[:2])]
            if blue < 25 and green > 230 and red < 25:
                name = 'ally_champion'
            else:
                name = 'minion'
            objects.append({
                'name': name,
                'coor': coor,
            })
    analytics.end_timer('in_range')
    return objects
