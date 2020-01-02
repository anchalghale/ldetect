''' Module for screenshoting '''
import logging
import time

import mss
import mss.tools
import numpy
import win32gui


def screenshot(rect, margin=0, margin_top=0):
    ''' Captures window '''
    with mss.mss() as sct:
        left, top, right, bot = rect
        left = left + margin
        top = top + margin_top
        width = right - left - margin
        height = bot - top - margin

        monitor = {'top': top, 'left': left, 'width': width, 'height': height}

        sct_img = numpy.array(sct.grab(monitor))
        sct_img = sct_img[:, :, :3]
        return sct_img
