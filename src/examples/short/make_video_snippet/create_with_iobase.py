"""
This is an example of how to create a video snippet from a video file using
the python 'cv2' module.

The code was originally created by chatGPT
"""


import sys
import cv2


def create_video_snippet(video_path, output_path, start_time, duration):
    print(type(video_path))
    print(type(output_path))
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_MSEC, start_time * 1000)  # Set the start time in milliseconds

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define the codec for the output video
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Capture frames until the desired duration is reached
    elapsed_time = 0
    while elapsed_time < duration * 1000:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)
        elapsed_time += 1000 / fps

    cap.release()
    out.release()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"{sys.argv[0]}: usage: {sys.argv[0]} [VIDEO] [SNIPPET]")
        sys.exit(1)
    video = sys.argv[1]
    snippet = sys.argv[2]
    with open(video, "rb") as s1, open(snippet, "wb") as s2:
        create_video_snippet(s1, s2, 10, 5)
