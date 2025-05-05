import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, max_hands=2, det_conf=0.7, track_conf=0.6):
        # setup mediapipe hands model
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=det_conf,
            min_tracking_confidence=track_conf
        )
        self.draw = mp.solutions.drawing_utils

    def detect(self, frame, draw_landmarks=True):
        # convert to rgb and process frame
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.res = self.hands.process(rgb)
        # draw landmarks if found
        if draw_landmarks and self.res.multi_hand_landmarks:
            for hand in self.res.multi_hand_landmarks:
                self.draw.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
        return frame

    def get_landmarks(self, frame, hand_idx=0):
        # return landmarks list as (id, x, y)
        lm_list = []
        if self.res.multi_hand_landmarks and len(self.res.multi_hand_landmarks) > hand_idx:
            hand = self.res.multi_hand_landmarks[hand_idx]
            h, w, _ = frame.shape
            for i, lm in enumerate(hand.landmark):
                lm_list.append((i, int(lm.x * w), int(lm.y * h)))
        return lm_list
