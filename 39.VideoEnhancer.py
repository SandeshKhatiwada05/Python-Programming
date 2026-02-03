import subprocess

input_video = 'Final.mp4'    # Replace with your input video path
output_video = 'output_video.mp4'  # Output file with better quality

# FFmpeg command to re-encode video with better quality (CRF=18), keep original audio
cmd = [
    'ffmpeg',
    '-i', input_video,
    '-c:v', 'libx264',
    '-crf', '18',          # Quality level: lower is better (18-23 is good range)
    '-preset', 'slow',     # Encoding speed/quality tradeoff
    '-c:a', 'copy',        # Copy audio as is (no quality loss)
    output_video,
]

subprocess.run(cmd)

print(f"Finished processing. Saved improved quality video as '{output_video}'")
