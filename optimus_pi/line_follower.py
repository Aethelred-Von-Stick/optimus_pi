#!/usr/bin/env python3

"""Mode for camera based line following."""

import logging

import cv2
import numpy as np
from gpiozero import Motor

from optimus_pi.mode import Mode

try:
    import picamera
except ImportError as exc:
    picamera = None  # pylint: disable=invalid-name
    logging.warning("picamera is not installed, line following is disabled.")

DTYPE = np.uint8
MAX_FOR_DTYPE = np.iinfo(DTYPE).max


class LineFollower(Mode):
    """Uses motors to follow a line based on picamera stream."""
    def __init__(  # pylint: disable=too-many-arguments
        self,
        lmot: Motor,
        rmot: Motor,
        resolution: tuple[int, int] = (640, 480),
        framerate: int = 12,
        threshold: float = 60.0,
    ):
        """Uses motors to follow a line based on picamera stream.

        Args:
            lmot (Motor): Left motor controller.
            rmot (Motor): Right motor controller.
            resolution (tuple[int, int], optional): Image pixel shape.
            framerate (int, optional): Number of frames per second to use for video stream.
            threshold (float, optional): Brightness threshold for finding the line.

        """
        super().__init__()
        self.running = False
        self.lmot = lmot
        self.rmot = rmot
        self.resolution = resolution
        self.shape = (*self.resolution, 3)
        self.framerate = framerate
        self.threshold = threshold

    def start(self):
        self.running = True

    def finish(self):
        self.running = False

    def follow_line(self):
        if picamera:
            with picamera.PiCamera(
                resolution=self.resolution, framerate=self.framerate
            ) as camera:
                buffer = np.empty(np.product(self.shape), dtype=DTYPE)
                for _ in camera.capture_continuous(buffer, "bgr", use_video_port=True):
                    if self.running:
                        contours = self.find_contours(buffer)
                        if len(contours) > 0:
                            biggest_contour = max(contours, key=cv2.contourArea)
                            centre = self.find_contour_centre(biggest_contour)
                            self.move_toward_centre(centre)
                        else:
                            logging.warning("Can't see the line!")
                            self.lmot.stop()
                            self.rmot.stop()
                    else:
                        break
        else:
            raise ModuleNotFoundError("No module named picamera.")

    def find_contours(self, buffer: np.ndarray) -> np.ndarray:
        bgr_image = buffer.reshape(self.shape)
        gray_image = cv2.cvtColor(bgr_image, cv2.BGR2GRAY)
        _, binary_image = cv2.threshold(
            gray_image, self.threshold, MAX_FOR_DTYPE, cv2.THRESH_BINARY_INV
        )
        contours, _ = cv2.findContours(binary_image.copy(), 1, cv2.CHAIN_APPROX_NONE)
        return contours

    def find_contour_centre(self, contour: np.ndarray) -> tuple[int, int]:
        moments = cv2.moments(contour)
        # https://docs.opencv.org/3.4/d8/d23/classcv_1_1Moments.html
        x_centre = moments["m10"] // moments["m00"]
        y_centre = moments["m01"] // moments["m00"]
        return x_centre, y_centre

    def move_toward_centre(self, centre: tuple[int, int]):
        if centre[0] < 60:
            self.lmot.forward(1)
            self.rmot.backward(1)
        elif centre[0] > 120:
            self.lmot.backward(1)
            self.rmot.forward(1)
        else:
            self.lmot.forward(1)
            self.rmot.forward(1)
