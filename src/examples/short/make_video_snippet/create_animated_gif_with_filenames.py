"""
This is an attempt to create an animated gif snippet from a video
using the 'cv2' and 'imageio' python modules.

References:
- https://theailearner.com/2021/05/29/creating-gif-from-video-using-opencv-and-imageio/
"""


import os
import sys

import cv2
import imageio


def create_animated_gif_from_video(
    video_path: str,
    output_path: str,
    start_time: int,  # in mili-seconds
    duration_between_frames: int,  # in mili-seconds
    number_of_frames: int,
) -> None:
    cap = cv2.VideoCapture(video_path)
    # frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # fps = cap.get(cv2.CAP_PROP_FPS)
    image_list = []
    for pos in range(start_time, start_time + duration_between_frames * number_of_frames, duration_between_frames):
        print(pos)
        cap.set(cv2.CAP_PROP_POS_MSEC, pos)
        p = cap.get(cv2.CAP_PROP_POS_MSEC)
        print(p)
        _ret, frame = cap.read()
        image_list.append(frame)
    cap.release()
    # imageio.mimsave(output_path, image_list, duration=2)
    print(len(image_list))
    with imageio.get_writer(output_path, mode="I") as writer:
        for img in image_list:
            writer.append_data(img)  # type: ignore


if __name__ == "__main__":
    if len(sys.argv) == 3:
        video = sys.argv[1]
        snippet = sys.argv[2]
    else:
        video = "data/make_video_snippet/hitler_uses_git.mp4"
        snippet = "data/make_video_snippet/hitler_uses_git_snippet_gif.gif"
    if os.path.isfile(snippet):
        os.unlink(snippet)
    create_animated_gif_from_video(video, snippet, 10000, 5000, 5)
