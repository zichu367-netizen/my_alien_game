# Alien Invasion Game (Project 14)

This project is based on the Alien Invasion game from *Python Crash Course (PCC)*.  
The goal is to improve the game by fixing the high score reset issue (14-4)  
and adding an extended gameplay feature (14-6).

---

## 📌 1. Environment Setup

### Python Version
- Python **3.13.9**

### Required Package
Install pygame:



pip install pygame


(If `pip` maps to another Python version, you can use:)


python -m pip install pygame


---

## 📌 2. Project File Structure



my_alien_game/
│
├── alien_invasion.py
├── settings.py
├── game_stats.py
├── ship.py
├── bullet.py
├── alien.py
├── alien_bullet.py
│
└── images/
├── ship.png
├── alien.png
└── laser.png


`high_score.txt` will be automatically created after you run the game.

---

## 📌 3. How to Run the Game

Open Terminal / PowerShell:



cd my_alien_game
python alien_invasion.py


If using Windows double-click:



run_game.bat


---

## 📌 4. Features Implemented

### ✔ 14-4 Fix: High Score Persistence
The high score is now saved into `high_score.txt` when quitting the game  
and loaded again when the game starts.

### ✔ 14-6 Expansion: Alien Shooting
Aliens now shoot bullets downward, creating a more challenging gameplay experience.

### ✔ Class-based structure
Game objects are implemented using:
- `Ship` class  
- `Bullet` class  
- `Alien` class  
- `AlienBullet` class  

---

## 📌 6. GitHub Link
https://github.com/zichu367-netizen/my_alien_game
