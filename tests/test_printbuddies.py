import time

import pytest

import printbuddies


def test_printbuddies_display():
    print()
    total = 200
    bar = printbuddies.ProgBar(total)
    for _ in range(total):
        bar.display(prefix=bar.runtime)
        time.sleep(0.01)
    bar.reset()
    bar.update_frequency = 10
    for _ in range(total):
        bar.display(suffix=bar.runtime)
        time.sleep(0.01)
    bar.reset()
    bar.update_frequency = 1
    for i in range(total):
        bar.display(counter_override=i + 1)
        time.sleep(0.01)
    bar.reset()
    [bar.display(return_object=time.sleep(0.01)) for _ in range(total)]
