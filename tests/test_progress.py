import time

import printbuddies


def test__progress_track():
    for _ in printbuddies.track(range(10)):
        time.sleep(0.25)


def test__progress_Progress():
    text = printbuddies.Gradient().apply("<>ProggyWoggy<>")
    with printbuddies.Progress() as progress:
        task = progress.add_task(text, total=500)
        while not progress.finished:
            time.sleep(0.01)
            progress.update(task, advance=1)
    with printbuddies.Progress() as progress:
        task = progress.add_task(suffix=text, total=500)
        while not progress.finished:
            time.sleep(0.01)
            progress.update(task, advance=1)
