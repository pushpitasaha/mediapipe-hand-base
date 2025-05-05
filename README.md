# mediapipe hand base

simple modular setup for real-time hand landmarks using opencv + mediapipe.

## requirements
- python 3.7–3.11 (mediapipe not yet supported on python ≥3.12)
- pip

## setup
```bash
# create virtual env with compatible python version
py -3.11 -m venv venv
# activate venv
venv\Scripts\activate   # windows
source venv/bin/activate  # mac/linux
# update pip and install deps
pip install --upgrade pip
pip install -r requirements.txt
```

## run
```bash
python main.py
```

## add new game
1. create class inheriting from `GameBase` in `game_manager.py` or a new file
2. implement `update(self, frame, lm_list)` for landmark logic
   draw feedback on frame
3. register in `main()` via `manager.register(YourGameClass)`

## structure
- `hand_detector.py`: wraps mediapipe model + landmarks
- `game_manager.py`: handles module registration & switch
- `main.py`: camera loop + example game
- `requirements.txt`
