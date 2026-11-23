"""
Writes a Mandelbrot set picture to M.bmp.

This is a readable rewrite of a well known obfuscated one-liner Mandelbrot generator.
"""

import struct

MAX_ITERATIONS = 255
WIDTH = 1500
HEIGHT = 1000


def escape_value(z, c, iterations_left):
    """Iterate z -> z*z + c and return a value in [0, 1) saying how fast z escapes."""
    if abs(z) < 6:
        if iterations_left == 0:
            return 0
        return escape_value(z * z + c, c, iterations_left - 1)
    return (2 + iterations_left - 4 * abs(z) ** -0.4) / MAX_ITERATIONS


def color(value):
    """Map an escape value to a (blue, green, red) tuple of bytes."""
    values = (
        value * 80 + value**9 * MAX_ITERATIONS - 950 * value**99,
        value * 70 - 880 * value**18 + 701 * value**9,
        value * MAX_ITERATIONS ** (1 - value**45 * 2),
    )
    return tuple(max(0, min(255, int(v))) for v in values)


def main():
    with open("M.bmp", "wb") as bmp:
        bmp.write(b"BM" + struct.pack("<QIIHHHH", WIDTH * HEIGHT * 3 + 26, 26, 12, WIDTH, HEIGHT, 1, 24))
        for pixel in range(WIDTH * HEIGHT):
            # average 9 sub pixel samples (3x3 anti aliasing)
            total = 0
            for sample in range(9):
                point = (sample % 3 / 3.0 + pixel % WIDTH + (pixel / WIDTH + sample / 3 / 3.0 - HEIGHT / 2) * 1j) * 2.5 / HEIGHT - 2.7
                total += escape_value(0, point, MAX_ITERATIONS) ** 2
            bmp.write(struct.pack("BBB", *color(total / 9)))


main()
