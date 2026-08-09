# Projectile Motion Simulator

An interactive 2D projectile motion simulator built with Python and Pygame. 
Adjust launch angle, speed, and gravity in real time and watch the trajectory 
update — includes live position tracking and post-landing stats (range, max 
height, time of flight).

## Features
- Real-time sliders for launch angle, speed, and gravity (converted to real-world units)
- Ground collision detection
- Live X/Y position display (ground-relative)
- Range, max height, and flight time shown after landing
- Menu screen with Start/Quit, and a way to return to the menu mid-session

## Demo
![demo gif](demo.gif)

## Installation
```bash
git clone https://github.com/entropy-117/Projectile-motion-sim
cd projectile-motion-sim
pip install -r requirements.txt
python Main.py
```

## What I learned
- Converting between pixel-space and real-world units (meters, m/s, m/s²)
- Frame-by-frame physics integration (velocity/acceleration updates per `dt`)
- Building a simple game-state machine (menu vs. simulation)
- Working with `pygame_widgets` for sliders, buttons, and labels
- Debugging silent UI bugs (indentation errors, invisible text due to box sizing)

## Controls
- **SPACE** — launch the projectile
- **Mouse** — drag sliders to adjust angle, speed, gravity