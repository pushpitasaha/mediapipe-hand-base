class GameBase:
    def __init__(self, detector):
        # store detector for game
        self.detector = detector

    def update(self, frame, lm_list):
        # override to add game logic
        return frame

class GameManager:
    def __init__(self, detector):
        self.detector = detector
        self.games = [] # init detector and game list
        self.active = None

    # add game to manager
    def register(self, game_cls):
        game = game_cls(self.detector)
        self.games.append(game)
        if not self.active:
            self.active = game
            
    # change active game by index
    def switch(self, idx):
        if 0 <= idx < len(self.games):
            self.active = self.games[idx]
            
    # run detection and game update
    def process(self, frame):
        frame = self.detector.detect(frame)
        lm_list = self.detector.get_landmarks(frame)
        return self.active.update(frame, lm_list)
