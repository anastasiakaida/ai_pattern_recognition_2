from agent import TestAgent
from matcher import _MATCHER
from detector import _DETECTOR

from item import Item
from image import ImagePath, ImageCV2
from enviroment import ImageEnviroment, CameraEnviroment

import cv2

def main():
    
    item = Item(
            'BOOK Lord of The Flies',
            ImagePath('../../img/lord_of_the_flies/lotf_item.JPG'),
            None,
            None
            )
    env = ImageEnviroment(ImageCV2(None))

    agents = []
    for detector in _DETECTOR:
        for matcher in _MATCHER:
            tracker = '{}_{}'.format(detector, matcher)
            agents.append(
                    TestAgent(tracker, env, item)
                    )

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    camera = CameraEnviroment(cap)
    frame = camera.get_state()
    cv2.imwrite('./img_t/frame.jpg', frame)
    for a in agents:
        try:
            print()
            a.env.sensor.data = frame[:]
            result = a.run()
            if result['state_img'] is not None:
                cv2.imwrite('./img_t/{}.jpg'.format(a.name), result['state_img'])
            print()
        except Exception as e:
            print(e)
            print('{} doesn\'t work'.format(a.name))

if __name__ == '__main__':
    main()
