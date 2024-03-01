import uiautomator2 as u2
import time


class Explore:

    def __init__(self):
        self.d = u2.connect()
        self.first_video_x_y = (0.16, 0.505)