try:
    from .detector import DetectorFactory
except (SystemError, ImportError):
    from detector import DetectorFactory

try:
    from .matcher import MatcherFactory
except (SystemError, ImportError):
    from matcher import MatcherFactory

class TrackerBuilder:

    def __init__(self):
        self.mfactory = MatcherFactory()
        self.dfactory = DetectorFactory()

    def get_tracker(self, tracker):

        dname, mname = tracker.split('_')
        detector = self.dfactory.get_detector(dname)
        matcher = self.mfactory.get_matcher(mname)

        if detector is not None and matcher is not None:
            return Tracker(detector, matcher)

        return None

class Tracker:
    
    def __init__(self, detector, matcher):
        self.detector = detector
        self.matcher = matcher

    def detect_and_compute(self, img):
        kp, des = self.detector.detect_and_compute(img)
        return kp, des
    
    def match(self, qdes, tdes):
        matches = self.matcher.match(qdes, tdes)
        return matches
