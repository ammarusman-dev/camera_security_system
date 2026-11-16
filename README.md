

A pure-Python automated camera security and motion detection system. 

Built as a capstone project after completing the **Learnify IT Python Programming for Beginners** and **Google IT Automation with Python** courses. This project bridges the gap between theoretical Python concepts and practical, real-world automation.

# Overview

This application tracks continuous video frames and identifies movement using pixel-delta thresholding. Rather than relying on heavy external computer vision libraries, this project implements the core logic from scratch to deeply understand data structures, continuous loops, and automation scripts.

# Features

Custom Motion Detection Engine: Compares incoming frames against a static background model to detect anomalies.
Bounding Box Tracking: Calculates X and Y coordinates to dynamically draw a bounding box around detected movement.
ASCII Heads-Up Display (HUD): Renders a live, real-time terminal visualizer showing the target lock.
Automated Event Logging: Triggers a native `tkinter` GUI dialog to export the security events to a `.txt` log file upon completion.

# Tech Stack
Language: Python 3.x
Libraries: `time`, `datetime`, `random`, `tkinter` (Standard Library - no external dependencies required!)

# 💻 Usage

Clone the repository and run the script from your terminal:

```bash
git clone [https://github.com/your-username/camera_security_system.git](https://github.com/ammarusman-dev/camera_security_system.git)
cd camera_security_system
python camera_security.py
