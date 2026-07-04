from .settings import *


def pixel_to_horizontal_div(pixel, width):

    return pixel / (width / HORIZONTAL_DIV)


def pixel_to_vertical_div(pixel, height):

    return pixel / (height / VERTICAL_DIV)


def div_to_time(div):

    return div * TIME_PER_DIV


def div_to_voltage(div):

    return div * VOLT_PER_DIV