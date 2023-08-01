"""
This is an attempt to create an animated gif snippet from a video
using the 'cv2' and 'imageio' python modules.

References:
- https://theailearner.com/2021/05/29/creating-gif-from-video-using-opencv-and-imageio/
- https://note.nkmk.me/en/python-opencv-video-to-still-image/
"""


import os
import sys

import cv2
import imageio


def create_animated_gif_from_video(
    video_path: str,
    output_path: str,
    start_time: float,  # in seconds
    skip_time: float,  # in seconds
    number_of_frames: int,
) -> None:
    cap = cv2.VideoCapture(video_path)
    # frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    start_frame = int(start_time * fps)
    skip_frames = int(skip_time * fps)
    end_frame = start_frame + skip_frames * number_of_frames
    image_list = []
    for pos in range(start_frame, end_frame, skip_frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos)
        ret, frame = cap.read()
        assert ret is not None
        # we need this conversin to RGB for the animated gif to look right
        resized_frame = cv2.resize(frame, (200,100))
        rgb_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
        image_list.append(rgb_frame)
    cap.release()
    # loop = 0 will loop indefinitely
    # duration is in miliseconds for each frame
    imageio.mimsave(output_path, image_list, loop=0, duration=1000)
    # with imageio.get_writer(output_path, mode="I") as writer:
    #     for img in image_list:
    #         writer.append_data(img)  # type: ignore


if __name__ == "__main__":
    if len(sys.argv) == 3:
        video = sys.argv[1]
        snippet = sys.argv[2]
    else:
        video = "data/make_video_snippet/hitler_uses_git.mp4"
        snippet = "data/make_video_snippet/hitler_uses_git_snippet_gif.gif"
    if os.path.isfile(snippet):
        os.unlink(snippet)
    create_animated_gif_from_video(video, snippet, 10.0, 5.0, 5)
