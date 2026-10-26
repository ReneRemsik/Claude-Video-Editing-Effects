#!/usr/bin/env python3
"""Save a frame every few seconds so Claude can see the setting, the speaker and the colours before designing an effect.

usage: python frames.py input.mp4 out_folder [--every 2]   -> out_folder/frame_000.0s.jpg, ...
"""
import argparse, os, subprocess, json

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('out'); ap.add_argument('--every', type=float, default=2.0)
a = ap.parse_args()
os.makedirs(a.out, exist_ok=True)
info = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=width,height', '-of', 'json', a.src]))
dur = float(info['format']['duration'])
t = 0.0
while t < dur:
    p = os.path.join(a.out, f'frame_{t:05.1f}s.jpg')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', a.src, '-frames:v', '1', '-vf', 'scale=540:-2', '-q:v', '4', p], check=True)
    print(p); t += a.every
print(f'duration {dur:.2f}s')
