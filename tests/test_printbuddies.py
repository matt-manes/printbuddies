import time

import pytest

import printbuddies


def test_printbuddies_display():
    print()
    total = 100
    bar = printbuddies.ProgBar(total - 1)
    for _ in range(total):
        bar.display()
        time.sleep(0.01)
    bar.reset()
    bar.update_frequency = 10
    for _ in range(total):
        bar.display()
        time.sleep(0.01)
