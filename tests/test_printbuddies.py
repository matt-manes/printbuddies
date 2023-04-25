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
    with printbuddies.ProgBar(total) as bar:
        for i in range(total):
            bar.display()
            time.sleep(0.01)
    with printbuddies.ProgBar(total) as bar:
        for i in range(total):
            bar.display(total_override=total * 0.5)
            time.sleep(0.01)


def test_spinner():
    print()
    spinner = printbuddies.Spinner()

    def spin():
        for _ in range(30):
            spinner.display()
            time.sleep(0.1)

    spin()
    print()
    spinner = printbuddies.Spinner(sequence=["~_~_~_~_~_~_", "_~_~_~_~_~_~"])
    spin()
    with printbuddies.Spinner() as spinner:
        spin()
