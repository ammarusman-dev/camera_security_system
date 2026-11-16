import time
import datetime
import random
import tkinter as tk
from tkinter import filedialog

WIDTH, HEIGHT = 28, 12
PIXEL_THRESHOLD = 30
MIN_MOTION_PIXELS = 4
TOTAL_FRAMES = 10

def generate_background():
    return [[50 for _ in range(WIDTH)] for _ in range(HEIGHT)]

def capture_simulated_frame(frame_idx):
    frame = [[50 + random.randint(-3, 3) for _ in range(WIDTH)] for _ in range(HEIGHT)]
    if 2 <= frame_idx <= 7:
        intruder_x = 3 + (frame_idx * 3)
        intruder_y = 4
        for r in range(intruder_y, min(intruder_y + 4, HEIGHT)):
            for c in range(intruder_x, min(intruder_x + 4, WIDTH)):
                frame[r][c] = 200
    return frame

def analyze_frame(background, current_frame):
    motion_coords = []
    for r in range(HEIGHT):
        for c in range(WIDTH):
            if abs(current_frame[r][c] - background[r][c]) > PIXEL_THRESHOLD:
                motion_coords.append((c, r))
    if len(motion_coords) >= MIN_MOTION_PIXELS:
        xs = [c[0] for c in motion_coords]
        ys = [c[1] for c in motion_coords]
        return True, (min(xs), min(ys), max(xs), max(ys))
    return False, None

def format_security_hud(frame_idx, motion_detected, bbox):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "ALERT: MOTION DETECTED!" if motion_detected else "Status: Clear"
    lines = ["=" * 56, f"Frame #{frame_idx:02d} | {timestamp} | {status}"]
    if bbox:
        lines.append(f"Target Locked -> Bounding Box: X({bbox[0]}..{bbox[2]}), Y({bbox[1]}..{bbox[3]})")
    lines.append("-" * 56)
    
    for r in range(HEIGHT):
        row_str = "  "
        for c in range(WIDTH):
            if bbox and (bbox[0] <= c <= bbox[2]) and (bbox[1] <= r <= bbox[3]):
                row_str += "+ " if (c in (bbox[0], bbox[2]) or r in (bbox[1], bbox[3])) else "# "
            else:
                row_str += ". "
        lines.append(row_str)
    lines.append("")
    return " ".join(lines)

def run_simulation():
    print("Initializing Pure-Python Computer Vision Security System...")
    background_model = generate_background()
    full_report = []
    
    for frame_idx in range(1, TOTAL_FRAMES + 1):
        frame = capture_simulated_frame(frame_idx)
        motion_detected, bbox = analyze_frame(background_model, frame)
        hud_output = format_security_hud(frame_idx, motion_detected, bbox)
        print(hud_output)
        full_report.append(hud_output)
        time.sleep(0.2)
        
    print(" *Security Monitoring Log Complete* ")
    
    # Trigger native "Save As" dialog window
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)  # Bring save window to the front on macOS
    
    save_path = filedialog.asksaveasfilename(
        title="Save Security Log",
        defaultextension=".txt",
        initialfile="security_report.txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    if save_path:
        with open(save_path, "w") as f:
            f.write(" ".join(full_report))
        print(f" [SUCCESS] Security report saved to: {save_path}")
    else:
        print(" [INFO] File save cancelled.")

if __name__ == "__main__":
    run_simulation()