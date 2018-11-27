import cv2

#_DETECTOR = [ 'SIFT', 'SURF', 'KAZE', 'AKAZE', 'BRISK', 'ORB' ]
_DETECTOR = [ 'SIFT', 'SURF', 'AKAZE', 'BRISK', 'ORB' ]

class DetectorNotFound(Exception):
    pass

class DetectorFactory:

    def get_detector(self, name):
        n = name.upper()

        if n == 'SIFT':
            return SiftDetector()
        elif n == 'SURF':
            return SurfDetector()
        elif n == 'KAZE':
            return KazeDetector()
        elif n == 'AKAZE':
            return AkazeDetector()
        elif n == 'BRISK':
            return BriskDetector()
        elif n == 'ORB':
            return OrbDetector()

        raise DetectorNotFound('{} detector wasn\'t found'.format(name))

class Detector:
    '''Base class for detector wrappers'''

    def __init__(self, detector):
        self.detector = detector

    def detect_and_compute(self, img):
        kp, des = self.detector.detectAndCompute(img, None)
        return kp, des

class SiftDetector(Detector):
    '''Wrapper for non-free SIFT detector'''

    def __init__(self):
        self.detector = cv2.xfeatures2d.SIFT_create()

class SurfDetector(Detector):
    '''Wrapper for non-free SURF detector'''

    def __init__(self):
        self.detector = cv2.xfeatures2d.SURF_create()

class KazeDetector(Detector):
    '''Wrapper for free KAZE detector'''

    def __init__(self):
        self.detector = cv2.KAZE_create()

class AkazeDetector(Detector):
    '''Wrapper for free AKAZE detector'''

    def __init__(self):
        self.detector = cv2.AKAZE_create()

class BriskDetector(Detector):
    '''Wrapper for free BRISK detector'''

    def __init__(self):
        self.detector = cv2.BRISK_create()

class OrbDetector(Detector):
    '''Wrapper for free ORB detector'''

    def __init__(self):
        self.detector = cv2.ORB_create()
