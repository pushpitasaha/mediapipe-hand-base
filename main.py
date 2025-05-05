import cv2
from hand_detector import HandDetector
from game_manager import GameManager, GameBase

class CountFingers(GameBase):
    def update(self, frame, lm_list):
        # count fingers based on landmarks
        if lm_list:
            tips = [4, 8, 12, 16, 20]
            count = 0
            for tip in tips:
                tip_y = next((y for i, x, y in lm_list if i == tip), None)
                base_y = next((y for i, x, y in lm_list if i == tip-2), None)
                if tip_y and base_y and tip_y < base_y:
                    count += 1
            cv2.putText(frame, f'fingers: {count}', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        return frame
    
def main():
    # start camera and setup modules
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    manager = GameManager(detector)
    manager.register(CountFingers)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # process frame through game manager
        out = manager.process(frame)
        cv2.imshow('hand base', out)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        # switch games with number keys
        if 49 <= key < 49 + len(manager.games):
            manager.switch(key - 49)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()