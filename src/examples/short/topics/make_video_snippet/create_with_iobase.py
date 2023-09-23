"""
This is an example of how to create a video snippet from a video file using
the python 'cv2' module.

The code was originally created by chatGPT
"""


import sys
import io
import os.path

import cv2

TEMP_FILE_IN = "/tmp/temp_in"
# the file MUST be called *.mp4 because otherwise opencv will not be able to open it
# as it will assume that it is a device or something.
TEMP_FILE_OUT = "/tmp/temp_out.mp4"


def write_stream_to_disk(stream, filename):
    assert isinstance(stream, io.IOBase)
    assert isinstance(filename, str)
    with open(TEMP_FILE_IN, "wb") as out:
        while b := stream.read(io.DEFAULT_BUFFER_SIZE):
            out.write(b)


def read_file_to_stream(filename, stream):
    assert isinstance(filename, str)
    assert isinstance(stream, io.IOBase)
    with open(filename, "rb") as in_stream:
        while b := in_stream.read(io.DEFAULT_BUFFER_SIZE):
            stream.write(b)


def create_video_snippet_streams(video_stream, snippet_stream, start_time, duration):
    assert isinstance(video_stream, io.IOBase)
    assert isinstance(snippet_stream, io.IOBase)
    if os.path.isfile(TEMP_FILE_IN):
        os.unlink(TEMP_FILE_IN)
    if os.path.isfile(TEMP_FILE_OUT):
        os.unlink(TEMP_FILE_OUT)
    write_stream_to_disk(video_stream, TEMP_FILE_IN)
    create_video_snippet(TEMP_FILE_IN, TEMP_FILE_OUT, start_time, duration)
    assert os.path.isfile(TEMP_FILE_OUT)
    read_file_to_stream(TEMP_FILE_OUT, snippet_stream)
    os.unlink(TEMP_FILE_IN)
    os.unlink(TEMP_FILE_OUT)


def create_video_snippet(video_path, output_path, start_time, duration):
    assert isinstance(video_path, str)
    assert isinstance(output_path, str)
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
    if len(sys.argv) == 3:
        video = sys.argv[1]
        snippet = sys.argv[2]
    else:
        video = "data/make_video_snippet/hitler_uses_git.mp4"
        snippet = "data/make_video_snippet/hitler_uses_git_snippet.mp4"
    if os.path.isfile(snippet):
        os.unlink(snippet)
    # create_video_snippet(video, snippet, 10, 5)
    with open(video, "rb") as s1, open(snippet, "wb") as s2:
        create_video_snippet_streams(s1, s2, 10, 5)
