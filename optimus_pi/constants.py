#!/usr/bin/env python3

"""Constants for use in the optimus_pi package."""

from pathlib import Path

DEFAULT_CONFIG_FILE = Path(__file__).parent / "config.yml"

# Events
X_PRESS = "X_PRESS"
X_RELEASE = "X_RELEASE"
TRIANGLE_PRESS = "TRIANGLE_PRESS"
TRIANGLE_RELEASE = "TRIANGLE_RELEASE"
CIRCLE_PRESS = "CIRCLE_PRESS"
CIRCLE_RELEASE = "CIRCLE_RELEASE"
SQUARE_PRESS = "SQUARE_PRESS"
SQUARE_RELEASE = "SQUARE_RELEASE"
L1_PRESS = "L1_PRESS"
L1_RELEASE = "L1_RELEASE"
L2_PRESS = "L2_PRESS"
L2_RELEASE = "L2_RELEASE"
R1_PRESS = "R1_PRESS"
R1_RELEASE = "R1_RELEASE"
R2_PRESS = "R2_PRESS"
R2_RELEASE = "R2_RELEASE"
UP_ARROW_PRESS = "UP_ARROW_PRESS"
UP_DOWN_ARROW_RELEASE = "UP_DOWN_ARROW_RELEASE"
DOWN_ARROW_PRESS = "DOWN_ARROW_PRESS"
LEFT_ARROW_PRESS = "LEFT_ARROW_PRESS"
LEFT_RIGHT_ARROW_RELEASE = "LEFT_RIGHT_ARROW_RELEASE"
RIGHT_ARROW_PRESS = "RIGHT_ARROW_PRESS"
L3_UP = "L3_UP"
L3_DOWN = "L3_DOWN"
L3_LEFT = "L3_LEFT"
L3_RIGHT = "L3_RIGHT"
L3_Y_AT_REST = "L3_Y_AT_REST"
L3_X_AT_REST = "L3_X_AT_REST"
L3_PRESS = "L3_PRESS"
L3_RELEASE = "L3_RELEASE"
R3_UP = "R3_UP"
R3_DOWN = "R3_DOWN"
R3_LEFT = "R3_LEFT"
R3_RIGHT = "R3_RIGHT"
R3_Y_AT_REST = "R3_Y_AT_REST"
R3_X_AT_REST = "R3_X_AT_REST"
R3_PRESS = "R3_PRESS"
R3_RELEASE = "R3_RELEASE"
OPTIONS_PRESS = "OPTIONS_PRESS"
OPTIONS_RELEASE = "OPTIONS_RELEASE"
SHARE_PRESS = "SHARE_PRESS"
SHARE_RELEASE = "SHARE_RELEASE"
PLAYSTATION_BUTTON_PRESS = "PLAYSTATION_BUTTON_PRESS"
PLAYSTATION_BUTTON_RELEASE = "PLAYSTATION_BUTTON_RELEASE"

EVENT_MAP = {
    X_PRESS: "on_x_press",
    X_RELEASE: "on_x_release",
    TRIANGLE_PRESS: "on_triangle_press",
    TRIANGLE_RELEASE: "on_triangle_release",
    CIRCLE_PRESS: "on_circle_press",
    CIRCLE_RELEASE: "on_circle_release",
    SQUARE_PRESS: "on_square_press",
    SQUARE_RELEASE: "on_square_release",
    L1_PRESS: "on_L1_press",
    L1_RELEASE: "on_L1_release",
    L2_PRESS: "on_L2_press",
    L2_RELEASE: "on_L2_release",
    R1_PRESS: "on_R1_press",
    R1_RELEASE: "on_R1_release",
    R2_PRESS: "on_R2_press",
    R2_RELEASE: "on_R2_release",
    UP_ARROW_PRESS: "on_up_arrow_press",
    UP_DOWN_ARROW_RELEASE: "on_up_down_arrow_release",
    DOWN_ARROW_PRESS: "on_down_arrow_press",
    LEFT_ARROW_PRESS: "on_left_arrow_press",
    LEFT_RIGHT_ARROW_RELEASE: "on_left_right_arrow_release",
    RIGHT_ARROW_PRESS: "on_right_arrow_press",
    L3_UP: "on_L3_up",
    L3_DOWN: "on_L3_down",
    L3_LEFT: "on_L3_left",
    L3_RIGHT: "on_L3_right",
    L3_Y_AT_REST: "on_L3_y_at_rest",
    L3_X_AT_REST: "on_L3_x_at_rest",
    L3_PRESS: "on_L3_press",
    L3_RELEASE: "on_L3_release",
    R3_UP: "on_R3_up",
    R3_DOWN: "on_R3_down",
    R3_LEFT: "on_R3_left",
    R3_RIGHT: "on_R3_right",
    R3_Y_AT_REST: "on_R3_y_at_rest",
    R3_X_AT_REST: "on_R3_x_at_rest",
    R3_PRESS: "on_R3_press",
    R3_RELEASE: "on_R3_release",
    OPTIONS_PRESS: "on_options_press",
    OPTIONS_RELEASE: "on_options_release",
    SHARE_PRESS: "on_share_press",
    SHARE_RELEASE: "on_share_release",
    PLAYSTATION_BUTTON_PRESS: "on_playstation_button_press",
    PLAYSTATION_BUTTON_RELEASE: "on_playstation_button_release",
}
INVERSE_EVENT_MAP = {v: k for k, v in EVENT_MAP.items()}
